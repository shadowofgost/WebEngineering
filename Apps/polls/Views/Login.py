from django.shortcuts import render
from django.http import HttpResponse
from drf_yasg.utils import swagger_auto_schema
from drf_yasg.openapi import Schema, Response,  TYPE_INTEGER, TYPE_OBJECT, TYPE_STRING
from rest_framework.views import APIView
from json import dumps
from .. import models
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
from uuid import uuid4
from .Public import content_type_tmp,  get_request_args


class Login(APIView):
    '''
    Retrive:
    Return the login page
    '''
    # TODO:把登录的html更改为李乐晗的html

    def get(self, request):
        hashkey = CaptchaStore.generate_key()  # 验证码答案
        image_url = captcha_image_url(hashkey)  # 验证码地址
        captcha = {'hashkey': hashkey, 'image_url': image_url}
        return render(request, "login.html", locals())
    '''
    List:
    Check the Login and redirect to the Front page
    '''
    login_post_request_body = Schema(
        title='后端需要的登录字段数据',  # 标题
        description=None,  # 接口描述
        type=TYPE_OBJECT,  # 类型 "object" ,"string" ,"number" ,"integer" ,"boolean" ,"array" ,"file"
        format=None,  # 格式    date,date-time,password,binary,bytes,float,double,int32,int64,email,ipv4, ipv6, uri, uuid, slug, decimal
        enum=None,  # [列表]列举参数的请求值
        pattern=None,  # 当 format为 string是才填此项
        # 当 type为object时，为dict对象 {'str1': Schema对象, 'str2': SchemaRef对象}
        properties={
            'user_id': Schema(
                title='登录者的账号名',
                description='登录者的账号名，对应的是nouser字段相当于账号的唯一标识（相当于学生学号）',
                type=TYPE_INTEGER,
                format='int32',
            ),
            'password': Schema(
                title='密码 ',
                description='登录者账号的密码 ',
                type=TYPE_STRING,
                format='string',
            )
        },
        required=['userid', 'psw'],  # [必须的属性列表]
        items=None,  # 当type是array时，填此项
    )
    login_post_responses_success = Response(
        description='The Response data if login is success',
        schema=Schema(
            title='登录成功的响应值',
            type=TYPE_OBJECT,
            properties={
                'error_code': Schema(
                    title='是否有报错数据',
                    description='用于传达是否有报错数据',
                    type=TYPE_INTEGER,
                    format='int32',
                ),
                'userid': Schema(
                    title='登录者的账号名',
                    description='登录者的账号名，对应的是nouser字段相当于账号的唯一标识（相当于学生学号）',
                    type=TYPE_INTEGER,
                    format='int32',
                ),
                'psw': Schema(
                    title='密码 ',
                    description='登录者账号的密码 ',
                    type=TYPE_STRING,
                    format='string',
                ),
                'status': Schema(
                    title='状态',
                    description='1代表登录成功，2代表登录不成功',
                    type=TYPE_STRING,
                    format='string',
                )
            }
        ),
        examples={
            'uerid': 1910404051,
            'psw': '123456',
            'status': '0'
        }
    )
    login_post_responses_fail = Response(
        description='登录失败的响应值',
        schema=Schema(
            title='The Response is fail',
            description='test',
            type=TYPE_STRING,
            format='string',
        ),
        examples={'error_code': 1, 'message': 'fail'}
    )

    @swagger_auto_schema(
        request_body=login_post_request_body,
        manual_parameters=None,
        operation_id=None,
        operation_description='登录成功的端口',
        operation_summary=None,
        security=None,
        responses={
            200: login_post_responses_success,
            401: login_post_responses_fail
        },
        tags=None)
    @get_request_args
    def post(self, request, args, session):
        if request.session.get('is_login', False):
            # 如果本来就未登录，也就没有登出一说
            data_attr = request.session['user_group_id']
            return HttpResponse(dumps({'code': 1}),  content_type=content_type_tmp, charset='utf-8')
        # Get the user_id and password from the front page
        user_id = args.get("user_id")
        password = args.get("password")
        if len(str(user_id)) == 0 or len(password) == 0:
            return HttpResponse(dumps({'error_code': 1, 'message': '请输入用户名和密码'}),  content_type=content_type_tmp, charset='utf-8')
        # select data from database based on the id of the user.
        data = tuple(models.TCyuser.objects.filter(
            nouser=str(user_id)).values())
        if data == ():
            return HttpResponse(dumps({'error_code': 1, 'message': "用户名不存在，重新输入用户名或者进行注册"}),  content_type=content_type_tmp, charset='utf-8')
        else:
            data = data[0]
            data_password = data.get('psw', None)
            data_attr = data.get('attr', None)
            user_id = data.get('id', None)
            user_nouser = data.get('nouser', None)
            if data_password != password:
                return HttpResponse(dumps({'error_code': 1, 'message': '登录失败,密码不正确'}), content_type=content_type_tmp, charset='utf-8')
            # 若用户名或密码失败,则将提示语与跳转链接继续传递到前端
            else:
                http_response = HttpResponse(
                    dumps({'code': 1, 'attr': data_attr}),  content_type=content_type_tmp, charset='utf-8')
                is_login = str(uuid4())
                user_id_session = str(uuid4())
                user_group_id = str(uuid4())
                user_nouser_session = str(uuid4())
                http_response.set_cookie("is_login", is_login)
                http_response.set_cookie('user_id', user_id_session)
                http_response.set_cookie('user_group_id', user_group_id)
                http_response.set_cookie('user_nouser', user_nouser_session)
                # 2.设置session的值
                request.session[is_login] = True
                request.session[user_id_session] = user_id
                request.session[user_group_id] = data_attr
                request.session[user_nouser_session] = user_nouser
                return http_response
