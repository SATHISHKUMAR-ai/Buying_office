from myapp1 import views
from django.urls import path

urlpatterns = [
    #index
    path('',views.index),
    path('index',views.index),
    path('prelr',views.prelr),
    path('reg',views.reg),
    path('login',views.login),
    path('login_act',views.login_act),
    path('regcom',views.regcom),
    path('viewcom',views.viewcom),
    path('proview',views.proview),
    path('logout',views.logout),

    #admin
    path('admin1',views.admin1),
    path('admin2',views.admin2),
    path('addproduct',views.addproduct),

    #product
    path('prodetails',views.prodetails),
    path('viewprod',views.viewprod),
    path('selprod1/<int:id>',views.selprod1),
    path('prodelete/<int:id>',views.prodelete),
    path('proupdate',views.proupdate),
    path('orderdetails',views.orderdetails),

    #quatation
    path('quat/<int:id>',views.quat),
    path('quat1',views.quat1),
    path('quatviewadmin',views.quatviewadmin),
    path('activeorder/<int:id>',views.activeorder),
    path('updatestatus',views.updatestatus),
    path('activeorderstatus/<int:id>',views.activeorderstatus),
    path('orderstatus',views.orderstatus),    
    path('orderstatusview',views.orderstatusview),
]
