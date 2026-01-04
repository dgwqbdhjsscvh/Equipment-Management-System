from django.shortcuts import render, redirect

# 登录页
def login_view(request):
    # 模拟登录跳转：根据选择的角色跳转到对应首页
    if request.method == 'POST':
        role = request.POST.get('role')
        if role == 'user':
            return redirect('user_home')
        elif role == 'admin':
            return redirect('admin_home')
        elif role == 'manager':
            return redirect('manager_home')
    return render(request, 'login.html')

# 退出登录
def logout_view(request):
    return redirect('login')

# ---------------------- 普通用户视图 ----------------------
def user_home(request):
    return render(request, 'user/home.html')

def device_list(request):
    return render(request, 'user/device_list.html')

def booking_apply(request):
    # 模拟提交预约申请后跳转
    if request.method == 'POST':
        return redirect('my_booking')
    return render(request, 'user/booking_apply.html')

def my_booking(request):
    return render(request, 'user/my_booking.html')

def user_profile(request):
    return render(request, 'user/user_profile.html')

# ---------------------- 管理员视图 ----------------------
def admin_home(request):
    return render(request, 'admin/home.html')

def booking_approve(request):
    # 模拟审批操作后刷新页面
    if request.method == 'POST':
        return redirect('booking_approve')
    return render(request, 'admin/booking_approve.html')

def device_manage(request):
    return render(request, 'admin/device_manage.html')

def report_stat(request):
    return render(request, 'admin/report_stat.html')

# ---------------------- 负责人视图 ----------------------
def manager_home(request):
    return render(request, 'manager/home.html')

def manager_booking_approve(request):
    if request.method == 'POST':
        return redirect('manager_booking_approve')
    return render(request, 'manager/booking_approve.html')

def user_manage(request):
    return render(request, 'manager/user_manage.html')

def device_purchase(request):
    return render(request, 'manager/device_purchase.html')

def manager_report_stat(request):
    return render(request, 'manager/report_stat.html')