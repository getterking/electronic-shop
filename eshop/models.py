# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Webuser(models.Model):
    ori_user = models.OneToOneField('auth.User', related_name='real_user', related_query_name='real_users')
    is_owner = models.BooleanField()
    nickname = models.CharField(max_length=20)
    gender = models.BooleanField()
    age = models.IntegerField()
    photo = models.ImageField(blank = True, upload_to = 'userphoto')
    email = models.EmailField(blank = True)

class Shop(models.Model):
    owner = models.ForeignKey('Webuser',
            related_name = 'shops',
            related_query_name = 'shop')
    name = models.CharField(max_length=20)
    introduction = models.TextField()
    photo = models.ImageField(blank = True, upload_to = 'shopphoto')
    address = models.CharField(max_length = 255)
    created_at = models.DateTimeField(default = timezone.now)
    sales = models.PositiveIntegerField(default = 0)

class ShoppingCartItem(models.Model):
    owner = models.ForeignKey('Webuser',
        related_name = 'shoppingCart',
        related_query_name = 'shoppingCartItem')
    goods = models.ForeignKey('Goods',
            related_name = 'shoppingcart_items')
    number = models.PositiveIntegerField()

class Remittance(models.Model):
    owner = models.ForeignKey('Webuser',
            related_name = 'remittances',
            related_query_name = 'remittance')
    shop = models.ForeignKey('Shop',
            related_name = 'remittances',
            related_query_name = 'remittance')
    STATUS_CHOICE = (
            ('c', '已下单'),
            ('t', '运送中'),
            ('r', '已收货'),
            ('e', '已评价')
        )
    status = models.CharField(max_length = 1, choices=STATUS_CHOICE, default="c")
    address = models.CharField(max_length = 255)
    payment_choices = (
            (0, '在线支付'),
            (1, '货到付款'),
        )
    payment = models.IntegerField(choices = payment_choices)
    phone = models.CharField(max_length = 20)
    message = models.CharField(max_length = 255)
    price = models.DecimalField(max_digits = 7, decimal_places = 2)
    created_at = models.DateTimeField(default = timezone.now)

class RemittanceItem(models.Model):
    remittance = models.ForeignKey('Remittance',
            related_name = 'remittance_items',
            related_query_name = 'remittance_item')
    goods = models.ForeignKey('Goods',
            related_name = 'remittance_item')
    number = models.PositiveIntegerField()

class Goods(models.Model):
    shop = models.ForeignKey('Shop',
            related_name = 'goods',
            related_query_name = 'shop_goods')
    name = models.CharField(max_length = 20)
    price = models.DecimalField(max_digits = 7, decimal_places = 2)
    introduction = models.TextField()
    total_score = models.FloatField(default=0)
    score_num = models.IntegerField(default=0)
    score = models.DecimalField(max_digits = 2, decimal_places = 1, default = 0)
    GOODS_TYPE_CHOICE = (
            ("games", '游戏'),
            ("books", '书籍'),
            ("resources", '资源'),
            ("unknown", '我不知道')
        )
    goods_type = models.CharField(max_length = 20, choices=GOODS_TYPE_CHOICE, default="unknown")
    keywords = models.ManyToManyField('Keyword',
            related_name = 'keyword_goods',
            related_query_name = 'keyword_goods')
    sales = models.PositiveIntegerField(default = 0)

class Keyword(models.Model):
    name = models.CharField(max_length = 20)

class GoodsImage(models.Model):
    image = models.ImageField(upload_to = 'goodsphoto')
    goods = models.ForeignKey('Goods',
            related_name = 'goods_images',
            related_query_name = 'goods_image')

class Comment(models.Model):
    item = models.OneToOneField('RemittanceItem',
            related_name = 'comment',
            related_query_name = 'comments')
    author = models.ForeignKey('Webuser',
            related_name = 'comment',
            related_query_name = 'comments')
    content = models.TextField()
    score = models.IntegerField()
    created_at = models.DateTimeField(default = timezone.now)
