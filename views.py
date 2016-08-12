from django.shortcuts import render
from block.models import Block
from django.contrib.auth.models import User




def index(request):
    block_infos= Block.objects.all().order_by("id")

    return  render(request,"index.html",{"blocks":block_infos})

def register(request):
    error = ""
    if request.method == "GET":
        return render(request, "register.html", {})
    else:
        username = request.POST['username'].strip()
        email = request.POST['email'].strip()
        password = request.POST['password'].strip()
        re_password = request.POST['re_password'].strip()
        if not username or not password or not email:
            error = "任何字段都不能为空"
        if password != re_password:
            error = "两次密码不一致"
        if User.objects.filter(username=username).count() > 0:
            error = "用户已存在"
        if not error:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
        else:
            return render(request, "register.html", {"error": error})
        return render(request, "regist_success.html", )


