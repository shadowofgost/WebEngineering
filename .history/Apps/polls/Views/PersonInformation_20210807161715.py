from django.http import HttpResponse
from drf_yasg.utils import swagger_auto_schema
from drf_yasg.openapi import Schema, Response,  TYPE_INTEGER, TYPE_OBJECT, TYPE_STRING
from rest_framework.views import APIView
from json import dumps
from time import time
from ..Models.UserModel.Database import UserModel,UserExtensionModel
from .Public import responses_success, responses_fail, get_request_args, content_type_tmp,  patch_error, patch_success, data_base_error


class PersonInformation(APIView):
    data_schema = {
        'id': Schema(
            title='ID',
            description='使用者的id',
            type=TYPE_INTEGER,
            format='int32',
        ),
        'nocard': Schema(
            title='ID of card ',
            description='用户的卡号',
            type=TYPE_STRING,
            format='string',
        ),
        'nouser': Schema(
            title='ID of user ',
            description='用户的身份id（比如学生的id就是他自己的学号）',
            type=TYPE_STRING,
            format='string',
        ),
        'name': Schema(
            title='用户的姓名',
            description='用户的姓名',
            type=TYPE_STRING,
            format='string'
        ),
        'psw': Schema(
            title='用户的密码',
            description='用户的密码',
            type=TYPE_STRING,
            format='string'
        ),
        'deptid__name': Schema(
            title='部门',
            description='用户所属的部门名称',
            type=TYPE_STRING,
            format='string'
        ),
        'sex': Schema(
            title='性别',
            description='用户的性别，0代表女性，1代表男性',
            enum=[0, 1],
            type=TYPE_INTEGER,
            format='int32',
        ),
        'attr': Schema(
            title='权限',
            description='用户管理权限，0代表超级管理员，1代表教务处管理员，2代表辅导员，3代表教师，4代表学生',
            enum=[0, 1, 2, 3, 4],
            type=TYPE_INTEGER,
            format='int32',
        ),
        'timeupdate': Schema(
            title='信息更新时间',
            description='用户表的更新时间',
            type=TYPE_INTEGER,
            format='int32',
        ),
        'localid': Schema(
            title='管理员地点',
            description=' 管理员所在的地点',
            type=TYPE_STRING,
            format='string'
        ),
        'userex_related_to_user_information__timeupdate': Schema(
            title='timeupdate',
            description='用户附件表的更新时间',
            type=TYPE_INTEGER,
            format='int32',
        ),
        'userex_related_to_user_information__idmanager__name': Schema(
            title='管理员姓名',
            description='修改账户的管理员姓名',
            type=TYPE_STRING,
            format='string'
        ),
        'userex_related_to_user_information__rem': Schema(
            title='描述',
            description='照片的描述',
            type=TYPE_STRING,
            format='string'
        )
    }
    PersonInformation_get_responses_success = Response(
        description='成功获取信息的响应',
        schema=Schema(
            title='成功数据',
            description='成功数据',
            type=TYPE_OBJECT,
            properties=data_schema
        ),
        examples=None
    )
    PersonInformation_get_responses_fail = Response(
        description='获取失败的响应',
        schema=responses_fail,
        examples={
            'error_code': 1,
            'message': '运行报错'}
    )

    @swagger_auto_schema(
        request_body=None,
        manual_parameters=None,
        operation_id=None,
        operation_description='获取所有登录个人信息',
        operation_summary=None,
        security=None,
        responses={
            200: PersonInformation_get_responses_success,
            404: PersonInformation_get_responses_fail
        },
        tags=None)
    @get_request_args
    def get(self, request, args, session):
        is_login = request.COOKIES.get('is_login')
        if not request.session.get(is_login, None):
            return HttpResponse(dumps({'code': 0}),  content_type=content_type_tmp, charset='utf-8')
        user_id = request.COOKIES.get('user_id')
        user_id = request.session.get(user_id)
        data_user = list(UserModel.objects.filter(id=user_id).values('id', 'nocard', 'nouser', 'name', 'psw', 'deptid__name', 'sex', 'attr', 'timeupdate',
                         'userex_related_to_user_information__rem', 'localid', 'userex_related_to_user_information__timeupdate', 'userex_related_to_user_information__idmanager__name'))
        if data_user == []:
            return HttpResponse(dumps({'error_code': 1, 'message': "数据库出现错误，请联系管理员"}), content_type=content_type_tmp, charset='utf-8')
        return HttpResponse(dumps({'error_code': 0, 'data': data_user}),  content_type=content_type_tmp, charset='utf-8')

    PersonInformation_patch_request_body = Schema(
        title="为修改个人信息更改的请求",  # 标题
        description='向前端请求信息的具体内容',  # 接口描述
        type=TYPE_OBJECT,  # 类型 "object" ,"string" ,"number" ,"integer" ,"boolean" ,"array" ,"file"
        format=None,  # 格式    date,date-time,password,binary,bytes,float,double,int32,int64,email,ipv4, ipv6, uri, uuid, slug, decimal
        enum=None,  # [列表]列举参数的请求值
        pattern=None,  # 当 format为 string是才填此项
        # 当 type为object时，为dict对象 {'str1': Schema对象, 'str2': SchemaRef对象}
        properties=data_schema,
        required=None,  # [必须的属性列表]
        items=None,  # 当type是array时，填此项
    )
    PersonInformation_patch_responses_success = Response(
        description='修改信息成功',
        schema=responses_success,
        examples={
            'error_code': 0,
            'message': patch_success
        }
    )
    PersonInformation_patch_responses_fail = Response(
        description='修改信息失败',
        schema=responses_fail,
        examples={
            'error_code': 1,
            'message': patch_error
        }
    )

    @swagger_auto_schema(
        request_body=PersonInformation_patch_request_body,
        manual_parameters=None,
        operation_id=None,
        operation_description='这个端口被用来修改登录者本身的信息',
        operation_summary=None,
        security=None,
        responses={
            201: PersonInformation_patch_responses_success,
            401: PersonInformation_patch_responses_fail},
        tags=None)
    @get_request_args
    def patch(self, request, args, session):
        is_login = request.COOKIES.get('is_login')
        if not request.session.get(is_login, None):
            return HttpResponse(dumps({'code': 0}),  content_type=content_type_tmp, charset='utf-8')
        data_patch_name = args.get('name', None)
        data_patch_psw = args.get('psw', None)
        data_patch_sex = args.get('sex', None)
        data_patch_rem = args.get(
            'userex_related_to_user_information__rem', None)
        if not(data_patch_name or data_patch_sex or data_patch_rem or data_patch_psw):
            return HttpResponse(dumps({'error_code': 0, 'message': patch_success}), content_type=content_type_tmp, charset='utf-8')
        user_id = request.COOKIES.get('user_id')
        user_id = request.session.get(user_id)
        time_update = int(time())-946656000
        if data_patch_name or data_patch_sex or data_patch_psw:
            data_user = list(
                UserModel.objects.filter(id=user_id).values('id', 'nocard', 'nouser', 'name', 'psw', 'sex', 'idmanager', 'timeupdate'))
            if data_user == []:
                return HttpResponse(dumps({'error_code': 1, 'message': data_base_error}), content_type=content_type_tmp, charset='utf-8')
            else:
                data_user = data_user[0]
                data_user['name'] = args.get('name', data_user['name'])
                data_user['psw'] = args.get('psw', data_user['psw'])
                data_user['sex'] = args.get('sex', data_user['sex'])
                data_user['idmanager'] = user_id
                data_user['timeupdate'] = time_update
                sex_dic = {'男': 1, '女': 0}
                data_user['sex'] = sex_dic.get(data_user['sex'])
                UserModel.objects.filter(id=user_id).update(
                    name=data_user.get('name'),
                    psw=data_user.get('psw'),
                    sex=data_user.get('sex'),
                    idmanager=data_user.get('idmanager'),
                    timeupdate=data_user.get('timeupdate')
                )
            return HttpResponse(dumps({'error_code': 0, 'message': patch_success}),  content_type=content_type_tmp, charset='utf-8')
        if data_patch_rem:
            data_user_extend = list(
                UserExtensionModel.objects.filter(id=user_id).values('id', 'rem', 'idmanager', 'timeupdate'))
            if data_user_extend == []:
                id_object = UserModel.objects.get(id=user_id)
                UserExtensionModel.objects.create(
                    id=id_object,
                    rem='None',
                    timeupdate=time_update,
                    imark=1,
                    photo_dataf='None',
                    idmanager=user_id
                )
            else:
                data_user_extend = data_user_extend[0]
                data_user_extend['rem'] = args.get(
                    'rem', data_user_extend['rem'])
                data_user_extend['idmanager'] = user_id
                data_user_extend['timeupdate'] = time_update
                UserExtensionModel.objects.filter(id=user_id).update(
                    rem=data_user_extend.get('rem'),
                    idmanager=data_user_extend.get('idmanager'),
                    timeupdate=data_user_extend.get('timeupdate')
                )
            return HttpResponse(dumps({'error_code': 0, 'message': patch_success}), content_type=content_type_tmp, charset='utf-8')
        return HttpResponse(dumps({'error_code': 1, 'message': data_base_error}), content_type=content_type_tmp, charset='utf-8')
