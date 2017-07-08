from django.conf.urls import url
from . import views, auth_views
from .customer import Search, Buy, CustomerRemittanceManager
from .seller import ShopManager, GoodsManager, ShopRemittanceManager
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #1.基本界面 ****************************************************************************

    url(r'^$', views.index, name='index'),
    url(r'^shop_list$', views.shop_list, name='shop_list'),
    url(r'^homepage$', views.homepage, name = 'homepage'),
    url(r'^shop/([1-9][0-9]*)$', views.shop, name='shop'),
    url(r'^shop/([1-9][0-9]*)/goods/([1-9][0-9]*)$', views.goods, name='goods'),
    url(r'^shop_homepage/([1-9][0-9]*)$', views.shop_homepage, name = 'shop_homepage'),
    url(r'^shop_homepage/([1-9][0-9]*)/shop_goods/([1-9][0-9]*)$', views.goods, name="goods"),

    #2.用户管理 ****************************************************************************

    url(r'^login$', auth_views.login, name='login'),
    url(r'^authenticate$', auth_views.authenticate, name='authenticate'),
    url(r'^signup$', auth_views.signup, name='signup'),
    url(r'^signup/submit$', auth_views.signup_submit, name='signup-submit'),
    url(r'^logout$', auth_views.logout, name='logout'),
    url(r'^homepage/user_info$', auth_views.user_info, name='user_info'),
    url(r'^homepage/user_info/change_user_info$', auth_views.change_user_info, name='change_user_info'),
    url(r'^homepage/user_info/save_user_info$', auth_views.save_user_info, name='save_user_info'),

    #3.消费者 ****************************************************************************

    #消费者-搜索相关
    url(r'^search$', Search.search,
        name='search'),

    #消费者-购物车相关
    #购物车界面
    url(r'^shoppingcart$', Buy.shoppingcart,
        name='shoppingcart'),
    #从购物车移除物品
    url(r'^shoppingcart/removefromcart/([1-9][0-9]*)$', Buy.removefromcart,
        name="removefromcart"),
    #清空购物车
    url(r'^shoppingcart/removeall/([1-9][0-9]*)$', Buy.removeall,
        name="removeall"),
    #购物车全部购买
    url(r'^shoppingcart/buyall/$', Buy.buyall,
        name="buyall"),
    #将商品添加到购物车
    url(r'^shop/([1-9][0-9]*)/goods/addtocart$', Buy.addtocart,
        name='addtocart'),

    #消费者－订单相关
    #所有订单
    url(r'^homepage/remittances$', CustomerRemittanceManager.remittances,
        name='remittances'),
    #已完成订单
    url(r'^homepage/finished_remittances$', CustomerRemittanceManager.finished_remittances,
        name='finished_remittances'),
    #待评价订单
    url(r'^homepage/to_evaluate_remittances$', CustomerRemittanceManager.to_evaluate_remittances,
        name='to_evaluate_remittances'),
    #待收货订单
    url(r'^homepage/to_receive_remittances$', CustomerRemittanceManager.to_receive_remittances,
        name='to_receive_remittances'),
    #订单详情
    url(r'^remittance/([1-9][0-9]*)$', CustomerRemittanceManager.remittance,
        name='remittance'),
    #店铺打包创建订单，通过购物车
    url(r'^create_remittance_shop/([1-9][0-9]*)$', CustomerRemittanceManager.create_remittance_shop,
        name='create_remittance_shop'),
    #通过商品创建订单，通过直接购买按钮
    url(r'^goods/([1-9][0-9]*)/create_remittance$', CustomerRemittanceManager.create_remittance_goods,
        name='create_remittance_goods'),
    #确认收货
    url(r'^remittance/([1-9][0-9]*)/customer_confirm_remittance$', CustomerRemittanceManager.customer_confirm_remittance,
        name='customer_confirm_remittance'),
    #评价订单
    url(r'^remittance/([1-9][0-9]*)/evaluate_remittance$', CustomerRemittanceManager.evaluate_remittance,
        name='evaluate_remittance'),
    #存储订单评价信息
    url(r'^remittance/([1-9][0-9]*)/customer_evaluate_remittance$', CustomerRemittanceManager.customer_evaluate_remittance,
        name='customer_evaluate_remittance'),

    #4.销售者 ****************************************************************************

    #店铺列表
    url(r'^homepage/my_shop$', ShopManager.my_shop,
        name='my_shop'),
    #创建店铺
    url(r'^create_shop$', ShopManager.create_shop,
        name='create_shop'),
    #店铺主页
    url(r'shop_homepage/([1-9][0-9]*)$', ShopManager.shop_homepage,
        name='shop_homepage'),
    #店铺信息
    url(r'^shop_homepage/([1-9][0-9]*)/shop_info$', ShopManager.shop_info,
        name='shop_info'),
    #修改店铺信息
    url(r'^shop_homepage/([1-9][0-9]*)/shop_info/change_shop_info$', ShopManager.change_shop_info,
        name='change_shop_info'),
    #存储店铺信息
    url(r'^shop_homepage/([1-9][0-9]*)/shop_info/save_shop_info$', ShopManager.save_shop_info,
        name='save_shop_info'),
    #店铺商品列表
    url(r'^shop_homepage/([1-9][0-9]*)/shop_goods$', ShopManager.shop_goods,
        name='shop_goods'),
    #创建商品
    url(r'^shop_homepage/([1-9][0-9]*)/create_goods$', GoodsManager.create_goods,
        name='create_goods'),
    #修改商品信息
    url(r'^shop_homepage/([1-9][0-9]*)/shop_goods/change_goods_info/([1-9][0-9]*)$', GoodsManager.change_goods_info,
        name='change_goods_info'),
    #保存商品信息
    url(r'^shop_homepage/([1-9][0-9]*)/shop_goods/save_goods_info/([1-9][0-9]*)$', GoodsManager.save_goods_info,
        name='save_goods_info'),
    #删除商品
    url(r'^shop_homepage/([1-9][0-9]*)/shop_goods/delete_goods/([1-9][0-9]*)$', GoodsManager.delete_goods,
        name='delete_goods'),
    #店铺订单列表
    url(r'^shop_homepage/([1-9][0-9]*)/shop_remittances$', ShopRemittanceManager.shop_remittances,
        name='shop_remittances'),
    #店铺订单详情页
    url(r'^shop_homepage/([1-9][0-9]*)/shop_remittance/([1-9][0-9]*)$', ShopRemittanceManager.shop_remittance,
        name='shop_remittance'),
    #
    url(r'^shop_homepage/([1-9][0-9]*)/shop_confirmed_remittances$', ShopRemittanceManager.shop_confirmed_remittances,
        name='shop_confirmed_remittance'),
    #订单发货
    url(r'^shop_homepage/([1-9][0-9]*)/shop_remittance/([1-9][0-9]*)/shop_confirm_remittance$', ShopRemittanceManager.shop_confirm_remittance,
        name='shop_confirm_remittance'),

    #5.管理者 ****************************************************************************

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

