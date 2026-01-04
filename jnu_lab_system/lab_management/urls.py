from django.urls import path
from . import views

urlpatterns = [
    # 首页/登录页
    path('', views.login_view, name='login'),
    # 普通用户首页
    path('user/home/', views.user_home, name='user_home'),
    # 设备查询页
    path('user/device/list/', views.device_list, name='device_list'),
    # 预约申请页
    path('user/booking/apply/', views.booking_apply, name='booking_apply'),
    # 我的预约页
    path('user/booking/my/', views.my_booking, name='my_booking'),
    # 个人信息页
    path('user/profile/', views.user_profile, name='user_profile'),
    
    # 管理员首页
    path('labadmin/home/', views.admin_home, name='admin_home'),
    # 预约审批页
    path('labadmin/booking/approve/', views.booking_approve, name='booking_approve'),
    # 设备管理页
    path('labadmin/device/manage/', views.device_manage, name='device_manage'),
    # 报表统计页
    path('labadmin/report/', views.report_stat, name='report_stat'),
    
    # 负责人首页
    path('manager/home/', views.manager_home, name='manager_home'),
    # 校外人员审批页
    path('manager/booking/approve/', views.manager_booking_approve, name='manager_booking_approve'),
    # 用户管理页
    path('manager/user/manage/', views.user_manage, name='user_manage'),
    # 设备采购/报废页
    path('manager/device/purchase/', views.device_purchase, name='device_purchase'),
    path('manager/report/', views.manager_report_stat, name='manager_report_stat'),
    
    # 通用跳转：退出登录
    path('logout/', views.logout_view, name='logout'),
]