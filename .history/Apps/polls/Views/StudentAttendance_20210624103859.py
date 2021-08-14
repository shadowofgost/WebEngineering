from django.http import HttpResponse
from django.db.models import Q, Count
from django.db import connection
from drf_yasg.utils import swagger_auto_schema
from drf_yasg.openapi import Parameter, Schema, Response, TYPE_INTEGER, TYPE_OBJECT, TYPE_STRING, IN_QUERY
from rest_framework.views import APIView
from json import dumps, loads
from .. import models
from .Public import responses_fail, data_attendance, get_request_args, post_search, content_type_tmp, data_page_response, post_error
from rest_framework.views import APIView


class StudentAttendance(APIView):
    '''
    list
    list all information about Equipment
    '''
    data_schema = {
        'param2':
        Schema(
            title='签到课程',
            description='签到的课程安排表id ',
            type=TYPE_INTEGER,
            format='int32',
            enum=None,
        ),
        'param2__id_curricula__name':
        Schema(
            title='签到课程名称',
            description='签到课程名称',
            type=TYPE_STRING,
            format='string',
            enum=None,
        ),
        'param2__timebegin':
        Schema(
            title='签到课程开始时间',
            description='签到课程开始时间',
            type=TYPE_INTEGER,
            format='int32',
            enum=None,
        ),
        'param2__timeend':
        Schema(
            title='签到课程结束时间',
            description='签到课程结束时间',
            type=TYPE_INTEGER,
            format='int32',
            enum=None,
        ),
        'status':
        Schema(
            title='签到',
            description=' 1 代表 已在课程中签到，2 代表已经在课程中签退3 代表在课程中迟到，4 代表旷课',
            type=TYPE_INTEGER,
            format='int32',
            enum=[1, 2, 3, 4],
        ),
        'timeupdate':
        Schema(
            title='记录更新时间',
            description=' 记录最后更新时间；（2000-1-1 0:0:0 经过的秒），必须有值',
            type=TYPE_INTEGER,
            format='int32',
            enum=None,
        ),
        'idmanager__name':
        Schema(
            title='修改字段的操作员姓名',
            description=' 修改字段数据的操作员姓名',
            type=TYPE_STRING,
            format='string',
            enum=None,
        ),
        'time':
        Schema(
            title='上课时间',
            description=' 每一次课程的上课时间，从2001年一月一日的秒数',
            type=TYPE_INTEGER,
            format='int32',
            enum=None,
        ),
    }
    data_schema_present = Schema(
        title='查询成功的返回',
        description='查询成功返回的函数值',
        type=TYPE_OBJECT,  # 类型
        properties=data_schema
    )
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
                description='用于传达是否有报错数据，0表示没有报错数据，1表示有报错数据',
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
    StudentInformation_get_parammeter = Parameter(
        name='course_plan_id',
        in_=IN_QUERY,
        description='传递给后端的需要查询的课程的id（是课程id而不是课程安排表的id）',
        required=True,
        type=TYPE_INTEGER,
        format='int32',
    )
    StudentAttendanceInformation_get_responses_success = Response(
        description='学生获取考勤数据成功的响应',
        schema=get_responses_success,
        examples={
            'error_code': 0,
            'message': '获取成功'
        }
    )
    StudentAttendanceInformation_get_responses_fail = Response(
        description='学生获取考勤数据失败的响应',
        schema=responses_fail,
        examples={
            'error_code': 1,
            'message': '获取成功'
        }
    )
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
        manual_parameters=[StudentInformation_get_parammeter,
                           page_get_parammeter, limits_get_parammeter],
        operation_id=None,
        operation_description='学生端查看自己本人的考勤记录',
        operation_summary=None,
        security=None,
        responses={
            200: StudentAttendanceInformation_get_responses_success,
            401: StudentAttendanceInformation_get_responses_fail
        },
        tags=None)
    @get_request_args
    def get(self, request, args, session):
        is_login = request.COOKIES.get('is_login')
        if not request.session.get(is_login, None):
            return HttpResponse(dumps({'code': 0}),  content_type=content_type_tmp, charset='utf-8')
        user_id = request.COOKIES.get('user_id')
        user_id = request.session.get(user_id)
        pages = int(args.get('page', 1))
        limits = int(args.get('limits', 20))
        user_id = request.COOKIES.get('user_id')
        user_id = request.session.get(user_id)
        course_plan_id = args.get('course_plan_id')
        id_list = []
        format_type = 3
        data_equipment = data_attendance(
            course_plan_id, id_list, format_type, user_id)
        if data_equipment == []:
            return HttpResponse(dumps({'error_code': 1, 'message': '所要查询的记录不存在，请确认是否课程是否开课，其他意外情况请联系教务部'}),  content_type=content_type_tmp, charset='utf-8')
        else:
            return data_page_response(data_equipment, pages, limits)
    '''
    list
    list all information about Equipment
    '''
    post_search['course_plan_id'] = Schema(
        title='需要查询的课程id',
        description='需要查询的课程id，需要前端传递给后端',
        type=TYPE_INTEGER,
        format='int32',
        enum=None,
    )
    StudentAttendanceInformation_post_request_body = Schema(
        title='学生查询自己的签到情况',  # 标题
        description=None,  # 接口描述
        type=TYPE_OBJECT,  # 类型 "object" ,"string" ,"number" ,"integer" ,"boolean" ,"array" ,"file"
        format=None,  # 格式    date,date-time,password,binary,bytes,float,double,int32,int64,email,ipv4, ipv6, uri, uuid, slug, decimal
        enum=None,  # [列表]列举参数的请求值
        pattern=None,  # 当 format为 string是才填此项
        # 当 type为object时，为dict对象 {'str1': Schema对象, 'str2': SchemaRef对象}
        properties=post_search,
        required=['input_string', 'page', 'limits'],  # [必须的属性列表]
        items=None,  # 当type是array时，填此项
    )
    StudentAttendanceInformation_post_responses_success = Response(
        description='查询考勤成绩成功的响应',
        schema=get_responses_success,
        examples={
            'error_code': 0,
            'message': '查询成功'
        }
    )
    StudentAttendanceInformation_post_responses_fail = Response(
        description='查询考勤成绩失败的响应',
        schema=responses_fail,
        examples={
            'error_code': 1,
            'message': post_error
        }
    )

    @swagger_auto_schema(
        request_body=StudentAttendanceInformation_post_request_body,
        manual_parameters=None,
        operation_id=None,
        operation_description='学生查询自己的考勤成绩的端口',
        operation_summary=None,
        security=None,
        responses={
            201: StudentAttendanceInformation_post_responses_success, 400: StudentAttendanceInformation_post_responses_fail
        },
        tags=None)
    @get_request_args
    def post(self, request, args, session):
        is_login = request.COOKIES.get('is_login')
        if not request.session.get(is_login, None):
            return HttpResponse(dumps({'code': 0}),  content_type=content_type_tmp, charset='utf-8')
        user_id = request.COOKIES.get('user_id')
        user_id = request.session.get(user_id)
        input_string = args.get('input_string', None)
        pages = int(args.get('page', 1))
        limits = int(args.get('limits', 20))
        user_id = request.COOKIES.get('user_id')
        user_id = request.session.get(user_id)
        course_plan_id = args.get('course_plan_id')
        id_list = []
        format_type = 3
        if input_string == None:
            data_equipment = data_attendance(
                course_plan_id, id_list, format_type, user_id)
        else:
            input_string = input_string.strip()
            try:
                test_input = eval(input_string)
            except:
                test_input = input_string
            if isinstance(test_input, int):
                data_equipment = list(models.TCyRunningaccount.objects.filter(
                    Q(id=test_input) |
                    Q(id_user=test_input) |
                    Q(param2=test_input) |
                    Q(idmanager=test_input) |
                    Q(time=test_input) |
                    Q(timeupdate=str(test_input)), param2__id_curricula=course_plan_id, id_user=user_id
                ).values('id').distinct().order_by('id'))
            else:
                data_equipment = list(models.TCyRunningaccount.objects.filter(
                    Q(id_user__name__icontains=test_input)
                    | Q(param2__id_curricula__name__icontains=test_input)
                    | Q(idmanager__name__icontains=test_input),
                    param2__id_curricula=course_plan_id,
                    id_user=user_id).values(
                        'id').distinct().order_by('id'))
            data_equipment = data_attendance(
                course_plan_id, data_equipment, format_type, user_id)
        if data_equipment == []:
            return HttpResponse(dumps({'error_code': 1, 'message': '所要查询的记录不存在，请确认是否课程是否开课，其他意外情况请联系教务部'}),  content_type=content_type_tmp, charset='utf-8')
        else:
            return data_page_response(data_equipment, pages, limits)
