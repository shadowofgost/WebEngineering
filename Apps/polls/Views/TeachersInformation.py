from django.http import HttpResponse
from django.db.models import Q
from drf_yasg.utils import swagger_auto_schema
from drf_yasg.openapi import Parameter, Schema, Response,  TYPE_INTEGER, TYPE_OBJECT, TYPE_STRING, IN_QUERY
from json import dumps
from .. import models
from .StudentsInformation import StudentsInformation
from .Public import responses_fail, get_request_args, content_type_tmp,  patch_error, data_page_response, post_search, post_error, delete_schema, data_base_error_specific, responses_success
from rest_framework.views import APIView


class TeachersInformation(StudentsInformation):
    '''
    list
    list all information about Equipment
    '''
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
    data_schema_present = Schema(
        title='查询成功的返回',
        description='查询成功返回的函数值',
        type=TYPE_OBJECT,  # 类型
        properties=data_schema)

    get_responses_success = Schema(
        title='成功获取查询数据',
        description='这个接口用于展示成功获取全部数据的格式',
        type=TYPE_OBJECT,
        properties={
            'page': Schema(
                title='页码',
                description='用于表示展示的页码数',
                type=TYPE_INTEGER,
                format='int32',
            ),
            'limits': Schema(
                title='页码',
                description='用于表示每页展示的行数',
                type=TYPE_INTEGER,
                format='int32',
            ),
            'error_code': Schema(
                title='是否有报错数据',
                description='用于传达是否有报错数据',
                type=TYPE_INTEGER,
                format='int32',
            ),
            'data': Schema(
                title='数据',
                description='用于传递查询到的全部数据',
                type=TYPE_OBJECT,
                properties=[data_schema_present, data_schema_present]
            ),
        }
    )
    TeachersInformation_get_responses_success = Response(
        description='成功获取信息的响应',
        schema=get_responses_success,
        examples=None
    )
    UsertInformation_get_responses_fail = Response(
        description='查询所有教师和管理员的个人信息失败的响应',
        schema=responses_fail,
        examples={
            'error_code': 1,
            'message': patch_error
        })
    page_get_parammeter = Parameter(
        name='page',
        in_=IN_QUERY,
        description='查询时设定的页码数',
        required=True,
        type=TYPE_INTEGER,
        format='int32',
    )
    limits_get_parammeter = Parameter(
        name='limits',
        in_=IN_QUERY,
        description='查询时设定的每页行数',
        required=True,
        type=TYPE_INTEGER,
        format='int32',
    )

    @swagger_auto_schema(
        request_body=None,
        manual_parameters=[
            page_get_parammeter, limits_get_parammeter],
        operation_id=None,
        operation_description='用于获取所有教师和管理员的个人信息',
        operation_summary=None,
        security=None,
        responses={
            200: TeachersInformation_get_responses_success,
            401: UsertInformation_get_responses_fail
        },
        tags=None)
    @get_request_args
    def get(self, request, args, session):
        is_login = request.COOKIES.get('is_login')
        if not request.session.get(is_login, None):
            return HttpResponse(dumps({'code': 0}),  content_type=content_type_tmp, charset='utf-8')
        pages = int(args.get('page', 1))
        limits = int(args.get('limits', 20))
        data_user = models.TCyuser.objects.filter().exclude(attr=4).values('id', 'nocard', 'nouser', 'name', 'psw', 'deptid__name', 'sex', 'attr', 'timeupdate','userex_related_to_user_information__rem', 'localid', 'userex_related_to_user_information__timeupdate', 'userex_related_to_user_information__idmanager__name').distinct().order_by('id')
        return data_page_response(data_user, pages, limits)

    '''
    list
    list all information about Equipment
    '''
    TeachersInformation_post_request_body = Schema(
        title=' 查询个人数据所需要的查询数据',  # 标题
        description=' 这个端口用于查询所有老师和管理员的个人信息 ',  # 接口描述
        type=TYPE_OBJECT,  # 类型 "object" ,"string" ,"number" ,"integer" ,"boolean" ,"array" ,"file"
        format=None,  # 格式    date,date-time,password,binary,bytes,float,double,int32,int64,email,ipv4, ipv6, uri, uuid, slug, decimal
        enum=None,  # [列表]列举参数的请求值
        pattern=None,  # 当 format为 string是才填此项
        # 当 type为object时，为dict对象 {'str1': Schema对象, 'str2': SchemaRef对象}
        properties=post_search,
        required=['input_string', 'page', 'limits'],  # [必须的属性列表]
        items=None,  # 当type是array时，填此项
    )
    TeachersInformation_post_responses_success = Response(
        description='查询所有教师和管理员的个人信息成功的响应',
        schema=Schema(
            title='成功数据',
            description='成功数据',
            type=TYPE_OBJECT,
            properties=data_schema
        ), examples=None
    )
    TeachersInformation_post_responses_fail = Response(
        description='查询所有教师和管理员的个人信息失败的响应',
        schema=responses_fail,
        examples={
            'error_code': 1,
            'message': post_error
        })

    @swagger_auto_schema(
        request_body=TeachersInformation_post_request_body,
        manual_parameters=None,
        operation_id=None,
        operation_description='这个端口用于获取所有老师和管理员个人信息',
        operation_summary=None,
        security=None,
        responses={
            201: TeachersInformation_post_responses_success,
            400: TeachersInformation_post_responses_fail
        },
        tags=None)
    @get_request_args
    def post(self, request, args, session):
        is_login = request.COOKIES.get('is_login')
        if not request.session.get(is_login, None):
            return HttpResponse(dumps({'code': 0}),  content_type=content_type_tmp, charset='utf-8')
        input_string = args.get('input_string', None)
        pages = int(args.get('page', 1))
        limits = int(args.get('limits', 20))
        if input_string == None:
            data_user_information = models.TCyuser.objects.filter().exclude(attr=4).values('id', 'nocard', 'nouser', 'name', 'psw', 'deptid__name', 'sex', 'attr', 'timeupdate','userex_related_to_user_information__rem', 'localid', 'userex_related_to_user_information__timeupdate', 'userex_related_to_user_information__idmanager__name').distinct().order_by('id')
        else:
            input_string = input_string.strip()
            try:
                test_input = eval(input_string)
            except:
                test_input = input_string
            if isinstance(test_input, int):
                data_user_information = models.TCyuser.objects.filter(
                    Q(id=test_input) |
                    Q(nocard__icontains=str(test_input)) |
                    Q(nouser__icontains=str(test_input)) |
                    Q(deptid=test_input) |
                    Q(sex=test_input) |
                    Q(attr=test_input) |
                    Q(timeupdate=test_input)
                ).exclude(attr=4).values('id', 'nocard', 'nouser', 'name', 'psw', 'deptid__name', 'sex', 'attr', 'timeupdate', 'userex_related_to_user_information__rem', 'localid', 'userex_related_to_user_information__timeupdate', 'userex_related_to_user_information__idmanager__name').distinct().order_by('id')
            else:
                data_user_information = models.TCyuser.objects.filter(
                    Q(name__icontains=test_input) |
                    Q(psw__icontains=test_input) |
                    Q(deptid__name__icontains=test_input) |
                    Q(userex_related_to_user_information__rem=test_input)
                ).exclude(attr=4).values('id', 'nocard', 'nouser', 'name', 'psw', 'deptid__name', 'sex', 'attr', 'timeupdate', 'userex_related_to_user_information__rem', 'localid', 'userex_related_to_user_information__timeupdate', 'userex_related_to_user_information__idmanager__name').distinct().order_by('id')
        return data_page_response(data_user_information, pages, limits)
