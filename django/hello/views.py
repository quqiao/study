
from django.http import HttpResponse, Http404
from hello.models import User
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from rest_framework import serializers
from rest_framework import viewsets
from django.http import HttpResponse, JsonResponse
from django.http import QueryDict
from rest_framework.request import Request
from hello.models import *
from django.contrib.auth.hashers import make_password, check_password

@login_required()
def index(request):
    return HttpResponse(request, 'demo.html')

@login_required()
def demo(request):
    return render(request, "demo.html")
    # return HttpResponse("这是个人中心，只有登陆后才能看到！")

def home(request):
    return render(request, "home.html")

def page(request, num):
    try:
        num = int(num)
        return render(request, 'demo.html')
    except:
        raise Http404

@login_required
def home1(request, year='2020', month='03'):
    return HttpResponse("获取当前页面home时间标签：%s年/%s月" % (year, month))

@login_required
def home2(request, year='2020', month='04'):
    return HttpResponse("获取当前页面home1时间标签：%s年/%s月" % (year, month))

@login_required
def yoyo(request):
    context = {}
    context['name'] = '嘻嘻'
    return render(request, 'yoyo.html', context)


def page1(request):
    context = {"name": "test", "location": "成都"}
    return render(request, 'page1.html', context)

# @login_required
def sonpage(request):
    context = {"ads": ["selenium", "appium", "requests"]}
    return render(request, "sonpage.html", context)

def get_demo(request):
    return render(request, 'get_demo.html')

# 测试QQ号访问页面
def test_qq(request):
    return render(request, 'get_demo.html')

# 提交后返回页面
def result_qq(request):
    '''返回结果'''
    if request.method == 'GET':
        # 获取提交的数据
        r = request.GET["q"]  # key就是前面输入框里的name属性对应值name="q"
        res = ""
        try:
            if int(r) % 2:
                res = "大吉大利！"
            else:
                res = "恭喜发财！"
        except:
            res = "请输入正确QQ号！"

        return HttpResponse("测试结果：%s" % res)
    else:
        render(request, 'get_demo.html')

# @login_required(login_url='/login/')
def user(request):
    '''请求页面-返回结果'''
    res = ""
    if request.method == 'GET':
        # 获取提交的数据
        # r = request.GET["q"] # key就是前面输入框里的name属性对应值name="q"
        n = request.GET.get('name', None)  # key不存在时不会报错
        res = User.objects.filter(user_name="%s" % n)
        try:
            res = res[0].mail
        except:
            res = "未查询到数据"
        return render(request, 'name.html', {'email': res})
    else:
        return render(request, 'name.html', {'email': res})

def register(request):
    '''注册页面'''
    res = ""
    if request.method == "POST":
        username = request.POST.get('username')
        psw = request.POST.get('password')
        mail = request.POST.get('mail')

        # 先查询数据库是否有此用户名
        user_lst = User.objects.filter(user_name=username)
        if user_lst:
            # 如果已经注册过，就给个提示
            res = "%s用户已被注册" % username
            return render(request, 'register.html', {'rename': res})

        else:
            # 如果没被注册，插入数据库

            # 第一种写法 -- 推荐
            user = User()
            user.user_name = username
            user.psw = psw
            user.mail = mail
            user.save()

            # 第二种写法
            # user = User(user_name=username,
            #            psw = psw,
            #            mail = mail,
            #            )
            # user.save()
            return render(request, 'login.html', {'rename': res})
    return render(request, 'register.html')

def login(request):
    '''登录页面'''
    if request.method == "GET":
        return render(request, 'login.html')
        # request.session['login_from'] = request.META.get('HTTP_REFERER', '/')

    if request.method == "POST":
        # 先查询数据库是否有此用户名
        username = request.POST.get('username')
        psw = request.POST.get('password')
        # 查询用户名和密码
        user_obj = User.objects.filter(user_name=username, psw=psw).first()
        if user_obj:
            return render(request, "demo.html")
            # return redirect('/demo')
            # return HttpResponse('登陆成功')
            # return HttpResponseRedirect(request.session['login_from'])
        else:
            return HttpResponse('用户名或密码错误')


def reset_psw(request):
    '''修改密码'''
    res = ""
    if request.method == "GET":
        return render(request, 'reset_psw.html', {'msg': res})

    if request.method == "POST":
        username = request.POST.get('username')
        psw = request.POST.get('password')
        new_psw = request.POST.get('new')

        if psw == new_psw:
            res = "新密码和旧密码不能重复"
            return render(request, 'reset_psw.html', {'msg': res})
        else:
            # 先查询数据库是否有此用户名
            user_lst = User.objects.filter(user_name=username)
            if not user_lst:
                # 如果没这个用户
                res = "用户未注册：%s" % username
                return render(request, 'reset_psw.html', {'msg': res})

            else:
                # 如果注册过，判断密码对不对
                ret = User.objects.filter(user_name=username).first()
                # 校验密码
                is_psw_true = check_password(psw, ret.psw)
                print(psw)
                print(ret.psw)
                print(is_psw_true)
                if is_psw_true:
                    user = User()
                    user.psw = make_password(new_psw)
                    user.save()
                    res = "密码修改成功！"
                else:
                    res = "密码错误！"
                return render(request, 'reset_psw.html', {'msg': res})

def get_parameter_dic(request, *args, **kwargs):
    if isinstance(request, Request) == False:
        return {}
    query_params = request.query_params
    if isinstance(query_params, QueryDict):
        query_params = query_params.dict()
    result_data = request.data
    if isinstance(result_data, QueryDict):
        result_data = result_data.dict()

    if query_params != {}:
        return query_params
    else:
        return result_data


class CardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Card
        fields = "__all__"

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def get(self, request, *args, **kwargs):
        params = get_parameter_dic(request)
        return JsonResponse(data=params)

    def post(self, request, *args, **kwargs):
        params = get_parameter_dic(request)
        return JsonResponse(data=params)

    def put(self, request, *args, **kwargs):
        params = get_parameter_dic(request)
        return JsonResponse(data=params)
