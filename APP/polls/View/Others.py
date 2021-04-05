from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import  Count
from django.db import connection
from rest_framework.views import APIView
from json import dumps
from .. import models
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url


tmp ='index.html'
def check_session_index(request):
    status = request.session.get('is_login')
    if not status:
        return render(request, "check_session_index.html")
    return render(request, "check_session_index.html")

# 用于将request转化的函数
def index(request):
    return HttpResponse('你好！这里是投票系统')


class Equipment(APIView):
    def get(self, request):
        with connection.cursor() as cursor:
            cursor.execute(
                "select ID,Name,State from T_CyEquipment")
            data = cursor.fetchall()
        data_name = ("ipc_id", "ipc_name", "active_status")
        data_result = []
        if data == []:
            return HttpResponse({
                "data": 0,
                "code": 5013,
                "msg": "Fail",
            })
        else:
            for i in data:
                tmp = dict(zip(data_name, i))
                data_result.append(tmp)
            total_count = len(data)
            t = {
                "data": {
                    "total_count": total_count,
                    "ipc_list": data_result,
                },
                "code": 0,
                "msg": "succeed",
            }
            return HttpResponse(t)  # ('%s'%t)

    def post(self, request):
        status = request.session.get('is_login')
        if not status:
            return redirect('/login/')
        with connection.cursor() as cursor:
            cursor.execute(
                "select ID,Name,State from T_CyEquipment")
            data = cursor.fetchall()
        data_name = ("ipc_id", "ipc_name", "active_status")
        data_result = []
        if data == []:
            return HttpResponse({
                "data": 0,
                "code": 5013,
                "msg": "Fail",
            })
        else:
            for i in data:
                tmp = dict(zip(data_name, i))
                data_result.append(tmp)
            total_count = len(data)
            return HttpResponse({
                "data": {
                    "total_count": total_count,
                    "ipc_list": data_result,
                },
                "code": 0,
                "msg": "succeed",
            })


class User(APIView):
    def get(self, request):
        data = models.TCyuser.objects.all().values('name')
        data_result = []
        for i in range(len(data)):
            data_result.append({"username": data[i]['name']})
        tmp = {
            "data": {
                "ipc_namelist": data_result
            },
        }
        return HttpResponse('%s' % tmp)

    def post(self, request):
        data = models.TCyuser.objects.all().values('name')
        data_result = []
        for i in range(len(data)):
            data_result.append({"username": data[i]['name']})
        tmp = {
            "data": {
                "ipc_namelist": data_result
            },
        }
        return HttpResponse(tmp)


class Academy(APIView):
    def get(self, request):
        user_id = '1910404051'
        data = models.TCyuser.objects.get(id=user_id)
        data_department = models.TCydept.objects.get(id=data.deptid)
        data_department = models.TCydept.objects.get(id=data_department.parent)
        tmp = {
            "department_list": [
                {
                    "academy": data_department.name
                }
            ],
            "code": 0,
            "msg": "succeed",
        }
        return HttpResponse(tmp)

    def post(self, request):
        user_id = request.POST.get('user_id')
        data = models.TCyuser.objects.get(id=user_id)
        data_department = models.TCydept.objects.get(id=data.deptid)
        data_department = models.TCydept.objects.get(id=data_department.parent)
        tmp = {
            "department_list": [
                {
                    "academy": data_department.name
                }
            ],
            "code": 0,
            "msg": "succeed",
        }
        return HttpResponse(tmp)


class Department(APIView):
    def get(self, request):
        user_id = '1910404051'
        data = models.TCyuser.objects.get(id=user_id)
        data_department = models.TCydept.objects.get(id=data.deptid)
        data_department = models.TCydept.objects.get(id=data_department.parent)
        tmp = {
            "department_list": [
                {
                    "academy": data_department.name
                }
            ],
            "code": 0,
            "msg": "succeed",
        }
        return HttpResponse(tmp)

    def post(self, request):
        user_id = request.POST.get('user_id')
        data = models.TCyuser.objects.get(id=user_id)
        data_department = models.TCydept.objects.get(id=data.deptid)
        data_department = models.TCydept.objects.get(id=data_department.parent)
        tmp = {
            "department_list": [
                {
                    "academy": data_department.name
                }
            ],
            "code": 0,
            "msg": "succeed",
        }
        return HttpResponse(tmp)

##废除的函数


def data_attendance_class_format(
    data_equipment, data_equipment_back, data_personal):
    return 0


##废除函数
def data_attendance_class(course_plan_id, id_list, format_type, user_id):
    data_equipment = list(
         models.TCyRunningaccount.objects.filter(
              id_plan=course_plan_id,
              status__gt=0).annotate(attendnumbers=Count('id_user')).values(
              'time', 'attendnumbers').order_by('time'))
    data_equipment_back = list(
          models.TCyRunningaccount.objects.filter(
               id_plan=course_plan_id, ).annotate(
                    totalnumbers=Count('id_user')).values(
                        'time', 'totalnumbers').order_by('time'))
    data_personal = list(
           models.TCyRunningaccount.objects.filter(
                id_plan=course_plan_id).values('id', 'id_user__name', 'status', 'time', 'idmanager__name', 'timeupdate').order_by('time'))
    if id_list == []:
        for j in data_equipment_back:
                id_list.append(j['time'])
    data_equipment = data_attendance_class_format(
            data_equipment, data_equipment_back, data_personal)
    return data_equipment
##废除的函数

def data_students_attendance_format(
        data_equipment, data_equipment_back, data_personal):
    return 0
##废除的函数
def data_students_attendance(user_id, id_list):
    data_equipment = list(models.TCyRunningaccount.objects.filter(
        id_user=user_id, status__gt= 0).annotate(attendtimes = Count('id')).values('id_plan', 'id_plan__id_curricula__name', 'id_plan__weekday', 'attendtimes').order_by('id_plan'))
    data_equipment_back = list(
        models.TCyRunningaccount.objects.filter(
            id_user=user_id).annotate(attendtotal=Count('id')).values(
                'id_plan', 'attendtotal').order_by('id_plan'))
    data_personal = list(models.TCyRunningaccount.objects.filter(
        id_user=user_id).values('id_plan', 'status', 'idmanager__name', 'timeupdate', 'time').order_by('id_plan'))
    if id_list == []:
        for j in data_equipment_back:
            id_list.append(j['id_plan'])
    data_equipment = data_students_attendance_format(
        data_equipment, data_equipment_back, data_personal)
    return data_equipment

## 创建验证码
def captcha():
    hashkey = CaptchaStore.generate_key()   #验证码答案
    image_url = captcha_image_url(hashkey)  #验证码地址
    captcha = {'hashkey': hashkey, 'image_url': image_url}
    return captcha
##刷新验证码
def refresh_captcha(request):
    return HttpResponse(dumps(captcha()), content_type='application/json')
## 验证验证码
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
class IndexView(APIView):
    def get(self, request):
        hashkey = CaptchaStore.generate_key()  # 验证码答案
        image_url = captcha_image_url(hashkey)  # 验证码地址
        captcha = {'hashkey': hashkey, 'image_url': image_url}
        return render(request, "login.html", locals())
    def post(self,request):
        capt=request.POST.get("captcha",None)         #用户提交的验证码
        key=request.POST.get("hashkey",None)          #验证码答案
        if jarge_captcha(capt,key):
            return  HttpResponse("验证码正确")
        else:
            return HttpResponse("验证码错误")


class SuperAdminstration(APIView):
    def get(self, request):
        if not request.session.get('is_login', None):
            # 如果本来就未登录，也就没有登出一说
            return render(request,tmp)
        status = request.session.get('is_login')
        userid = request.session.get('user_id')
        if not status:
            return redirect('/login/')
        with connection.cursor() as cursor:
            cursor.execute(
                "select Nocard,NoUser,Name,Psw,Deptid, sex,attr from T_CyUser where Id=%s" % userid)
            data = cursor.fetchall()
            cursor.execute(
                "select Photo from T_CyUserEx where Id=%s" % userid
            )
            data_photo = cursor.fetchall()
        error_msg = ''
        if data == []:
            error_msg = {'message': "用户不存在，请重新输入"}
        else:
            data_name = ('Nocard', 'NoUser', 'Name',
                         'Psw', 'Deptid', 'sex', 'attr')
            data_result = dict(zip(data_name, data))
            #t = {"data": {
            #        "user_id": userid,
            #        "user_name": data[0][2],
            #        "password": data[0][3],
            #        "user_groupid": data[0][-1],
            #        "user_photo": data_photo[0][0],
            #    }
            #}
            return render(request, tmp, data_result)

    def post(self, request):
        status = request.session.get('is_login')
        userid = request.session.get('userid')
        with connection.cursor() as cursor:
            cursor.execute(
                "select Nocard,NoUser,Name,Psw,Deptid, sex,attr from T_CyUser where Id=%s" % userid)
            data = cursor.fetchall()
            cursor.execute(
                "select Photo from T_CyUserEx where Id=%s" % userid
            )
            data_photo = cursor.fetchall()
        error_msg = ''
        if data == []:
            error_msg = {'message': "用户不存在，请重新输入"}
        elif data[0][-1] == 0 or data[0][-1] == 1:
            with connection.cursor() as cursor:
                cursor.execute(
                    "select * from T_CyUser ")
                data = cursor.fetchall()
            data_name = tuple(models.TCyuser._meta.fields)
            data_result = []
            for i in data:
                tmp = dict(zip(data_name, i))
                data_result.append(tmp)
            return HttpResponse(dumps(data_result))
        else:
            data_name = (
                'Nocard', 'NoUser', 'Name',
                'Psw', 'Deptid', 'sex', 'attr'
            )
            data_result = dict(zip(data_name, data))
            t = {
                "data": {
                    "user_id": userid,
                    "user_name": data[0][2],
                    "password": data[0][3],
                    "user_groupid": data[0][-1],
                    "user_photo": data_photo[0][1],
                }
            }
            # return HttpResponse(t)
            return render(request, 'index.html', t)


class AcademicAdminstration(APIView):
    def get(self, request):
        userid = request.session.get('userid')
        return HttpResponse(dumps({'result': userid}, ensure_ascii=False))


class Counsellor(APIView):
    pass


class Teacher(APIView):
    pass


class Student(APIView):
    def get(self, request, userid):
        with connection.cursor() as cursor:
            cursor.execute('select ')

    def post(self, request, userid):
        course_name = request.POST.get("CourseName")
        with connection.cursor() as cursor:
            cursor.execute('select ')
