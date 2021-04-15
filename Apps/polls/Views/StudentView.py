from django.shortcuts import render, get_object_or_404, redirect
from .. import models
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
from django.http import HttpResponse
import time
import json

# Create your views here.


# 创建验证码


def captcha():
    hashkey = CaptchaStore.generate_key()  # 验证码答案
    image_url = captcha_image_url(hashkey)  # 验证码地址
    captcha = {'hashkey': hashkey, 'image_url': image_url}
    return captcha
# 刷新验证码


def refresh_captcha(request):
    return HttpResponse(json.dumps(captcha()), content_type='application/json')
# 验证验证码


def jarge_captcha(captchaStr, captchaHashkey):
    if captchaStr and captchaHashkey:
        try:
            # 获取根据hashkey获取数据库中的response值
            get_captcha = CaptchaStore.objects.get(hashkey=captchaHashkey)
            if get_captcha.response == captchaStr.lower():     # 如果验证码匹配
                return True
        except:
            return False
    else:
        return False


def student_login(request):
    request.session.clear()
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        capt = request.POST.get("captcha", None)  # 用户提交的验证码
        key = request.POST.get("hashkey", None)
        if username and password:
            username = username.strip()
            tmp = list(models.TCyuser.objects.filter(nouser=username))
            try:
                user = models.TCyuser.objects.get(nouser=username)
            except:
                return render(request, 'error/usernotexist.html')
            res_data = models.TCyuser.objects.filter(
                nouser=username, psw=password).first()
            if res_data:
                if jarge_captcha(capt, key):
                    request.session["is_login"] = True
                    request.session["username"] = res_data.nouser
                    request.session["personname"] = res_data.name
                    request.session["user_id"] = res_data.id
                    request.session["attr"] = res_data.attr
                    request.session.set_expiry(180)
                    if request.session['attr'] == 4:
                        res = redirect('polls:student_index')
                    else:
                        res = render(request, 'error/wrongattr.html')
                    return res
                else:
                    return render(request, 'error/wrongcaptcha.html')
            else:
                return render(request, 'error/wrongpassword.html')
    else:
        hashkey = CaptchaStore.generate_key()  # 验证码答案
        image_url = captcha_image_url(hashkey)  # 验证码地址
        captcha = {'hashkey': hashkey, 'image_url': image_url}
    return render(request, 'studentweb/login.html', locals())


def student_changepsw(request):
    is_login = request.session.get("is_login", False)
    if is_login:
        username = request.session.get("username", "")
        personname = request.session.get("personname", "")
        user_id = request.session.get("user_id")
        result = {}
        dbData = models.TCyuser.objects.filter(id=user_id)
        result['data'] = dbData
        if request.method == 'POST' and request.POST:
            username = username
            nameIndb = models.TCyuser.objects.filter(id=user_id).first()
            if request.POST.get('new_password') == request.POST.get('new_password_copy'):
                if request.POST.get('old_password') == nameIndb.psw:
                    nameIndb.psw = request.POST.get('new_password')
                    nameIndb.save()
                    result['statu'] = 'success'
                else:
                    result['statu'] = 'error'
            else:
                result['statu'] = 'error2'
        context = {}
        context['personname'] = personname
        context['result'] = result
        context['username'] = username
        return render(request, 'studentweb/changepsw.html', context)
    else:
        return student_login(request)


def student_changepswsuccess(request):
    return render(request, 'studentweb/changepswsuccess.html')


def get_course_information(request, location):
    is_login = request.session.get("is_login", False)
    if not(is_login):
        return student_login(request)
    else:
        username = request.session.get("username", "")
        personname = request.session.get("personname", "")
        user_id = request.session.get("user_id")
        tmp = models.TCyRunningaccount.objects.filter(id_user=user_id).values(
            'param2__id_curricula__name', 'param2__id_curricula').distinct()
        lessons = [i for i in tmp]  # 存放该学生选的所有课程
        context2 = {}
        context2['username'] = username
        context2['lessons'] = lessons
        context2['personname'] = personname
        return render(request, location, context2)


def student_index(request):
    location = 'studentweb/index.html'
    return get_course_information(request, location)


def student_lessons(request):
    location = 'studentweb/index.html'
    return get_course_information(request, location)


def student_statistics(request):
    location = 'studentweb/statistics.html'
    return get_course_information(request, location)


def student_lessoninfo(request, id):
    is_login = request.session.get("is_login", False)
    if is_login:
        username = request.session.get("username", "")
        personname = request.session.get("personname", "")
        user_id = request.session.get("user_id")
        tmp = models.TCycurricula.objects.filter(
            id=id)
        lesson = tmp[0].name
        tmp_course_arrangement = models.TCyplan.objects.filter(id_curricula=id)
        # for object in models.TCyplan.objects.all():
        #    if username in object.rangeusers:
        #        if object.id_curricula == id:
        #            lesson = object
        #            lesson = models.TCycurricula.objects.get#(id=lesson.id).name
        lessons = []
        for object in tmp_course_arrangement:
            object.timebegin = time.strftime(
                "%Y-%m-%d %H:%M:%S", time.localtime(object.timebegin+946656000))
            object.timeend = time.strftime(
                "%Y-%m-%d %H:%M:%S", time.localtime(object.timeend+946656000))
            lessons.append(object)
        context = {}
        context['lesson_obj'] = lesson
        context['lessons'] = lessons
        context['username'] = username
        context['personname'] = personname
        return render(request, "studentweb/lessoninfo.html", context)
    else:
        return student_login(request)


def student_attendtime(request, id):
    is_login = request.session.get("is_login", False)
    if is_login:
        username = request.session.get("username", "")
        personname = request.session.get("personname", "")
        user_id = request.session.get("user_id")
        tmp = models.TCycurricula.objects.filter(
            id=id)
        lesson = tmp[0].name
        # for object in models.TCyplan.objects.all():
        #    if username in object.rangeusers:
        #        if object.id_curricula == id:
        #            lesson = object
        #lesson = models.TCycurricula.objects.get(id=lesson.id).name
        # lessons2 = []  # 存放所有课程id
        # for object in models.TCyplan.objects.all():
        #    if username in object.rangeusers:
        #        if object.id_curricula == id:
        #            lessons2.append(object.id)
        #lessons = []
        # for object in lessons2:
        #    object = models.TCyRunningaccount.objects.get(id=object)
        #    object.time = time.strftime(
        #        "%Y-%m-%d %H:%M:%S", time.localtime(object.time))
        #    lessons.append(object)
        tmp = models.TCyRunningaccount.objects.filter(
            param2__id_curricula=id, id_user=user_id)
        for object in tmp:
            if object.time == None:
                object.time = 0
            else:
                object.time = time.strftime(
                    "%Y-%m-%d %H:%M:%S", time.localtime(object.time+946656000))
        lessons = [i for i in tmp]
        context = {}
        context['personname'] = personname
        context['lesson_obj'] = lesson
        context['lessons'] = lessons
        context['username'] = username
        return render(request, "studentweb/attendtime.html", context)
    else:
        return student_login(request)
