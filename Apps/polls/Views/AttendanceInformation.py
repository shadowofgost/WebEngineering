from django.http import HttpResponse
from django.db.models import Q
from drf_yasg.utils import swagger_auto_schema
from drf_yasg.openapi import Parameter, Schema, Response,  TYPE_INTEGER, TYPE_OBJECT, TYPE_STRING, IN_QUERY
from json import dumps
from .. import models
from copy import deepcopy
from .Public import responses_success, responses_fail, get_request_args, post_search, content_type_tmp, data_page_response, post_success, post_error, patch_success, patch_error, put_success, put_error, data_base_error_specific, id_error, data_attendance, delete_schema
from .APIViewDelete import APIViewDelete
from rest_framework.views import APIView


class AttendanceInformation(APIView):
    '''
    list
    list all information about Equipment
    '''
    data_schema_personal_data = {
        'status':
        Schema(
            title='签到',
            description=' 1 代表 已在课程中签到，2 代表已经在课程中签退3 代表在课程中迟到，4 代表旷课',
            type=TYPE_INTEGER,
            format='int32',
            enum=[1, 2, 3, 4],
        ),
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

    data_schema_personal = Schema(
        title='学生个人数据',
        description=' 学生个人数据',
        type=TYPE_OBJECT,
        properties=data_schema_personal_data
    )
    data_schema = {
        'id':
        Schema(
            title='考勤记录的关键字',
            description=' 关键字，每个记录的唯一标识，一旦添加不能能更改，顺序增加',
            type=TYPE_INTEGER,
            format='int32',
            enum=None,
        ),
        'id_user__name':
        Schema(
            title='考勤者的姓名',
            description='考勤记录者的姓名',
            type=TYPE_STRING,
            format='string',
            enum=None,
        ),
        'attendtimes':
        Schema(
            title='考勤记录者出勤的次数',
            description='考勤者打卡签到的次数',
            type=TYPE_INTEGER,
            format='int32',
            enum=None,
        ),
        'attendtotal':
        Schema(
            title='应该出勤的次数',
            description=' 应该出勤的次数 ',
            type=TYPE_INTEGER,
            format='int32',
            enum=None,
        ),
        'attendrates':
        Schema(
            title='出勤率',
            description=' 这门课或者学生的出勤率 ',
            type=TYPE_INTEGER,
            format='int32',
            enum=None,
        ),
        'person_data':
        Schema(
            title='签到者的个人数据',
            description='签到人员的个人数据，这门课每次签到的具体数据',
            type=TYPE_OBJECT,
            properties=[data_schema_personal, data_schema_personal],
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
            'error_code': Schema(
                title='是否有报错数据',
                description='用于传达是否有报错数据',
                type=TYPE_INTEGER,
                format='int32',
            ),
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
            'data': Schema(
                title='数据',
                description='用于传递查询到的全部数据',
                type=TYPE_OBJECT,
                properties=[data_schema_present, data_schema_present]
            ),
        }
    )
    AttendanceInformation_get_parammeter = Parameter(
        name='course_plan_id',
        in_=IN_QUERY,
        description='传递给后端的需要查询的课程的id（是课程id而不是课程安排表的id）',
        required=True,
        type=TYPE_INTEGER,
        format='int32',
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
    AttendanceInformation_get_responses_success = Response(
        description='获取签到记录成功的响应',
        schema=get_responses_success,
        examples={
            'error_code': 0,
            'message': '获取成功'
        }
    )
    AttendanceInformation_get_responses_fail = Response(
        description='获取签到记录失败的响应',
        schema=responses_fail,
        examples={
            'error_code': 1,
            'message': '获取失败'
        }
    )

    @swagger_auto_schema(
        request_body=None,
        manual_parameters=[AttendanceInformation_get_parammeter,
                           page_get_parammeter, limits_get_parammeter],
        operation_id=None,
        operation_description='获取学生签到记录',
        operation_summary=None,
        security=None,
        responses={
            200: AttendanceInformation_get_responses_success,
            401: AttendanceInformation_get_responses_fail
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
        course_plan_id = args.get('course_plan_id')
        format_type = 1
        id_list = []
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
    AttendanceInformation_post_request_body = Schema(
        title=' 查询学生签到情况 ',  # 标题
        description='这个接口用于检测学生签到情况',  # 接口描述
        type=TYPE_OBJECT,  # 类型 "object" ,"string" ,"number" ,"integer" ,"boolean" ,"array" ,"file"
        format=None,  # 格式    date,date-time,password,binary,bytes,float,double,int32,int64,email,ipv4, ipv6, uri, uuid, slug, decimal
        enum=None,  # [列表]列举参数的请求值
        pattern=None,  # 当 format为 string是才填此项
        # 当 type为object时，为dict对象 {'str1': Schema对象, 'str2': SchemaRef对象}
        properties=post_search,
        required=['input_string', 'page', 'limits'],  # [必须的属性列表]
        items=None,  # 当type是array时，填此项
    )
    AttendanceInformation_post_responses_success = Response(
        description='查询学生签到记录成功的响应',
        schema=get_responses_success,
        examples={
            'message': post_success
        }
    )
    AttendanceInformation_post_responses_fail = Response(
        description='查询学生签到记录失败的响应',
        schema=responses_fail,
        examples={
            'error_code': 1,
            'message': post_error
        }
    )

    @swagger_auto_schema(
        request_body=AttendanceInformation_post_request_body,
        manual_parameters=None,
        operation_id=None,
        operation_description='这个接口用于查询学生签到情况',
        operation_summary=None,
        security=None,
        responses={
            201: AttendanceInformation_post_responses_success, 400: AttendanceInformation_post_responses_fail
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
        course_plan_id = args.get('course_plan_id')
        format_type = 1
        id_list = []
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
                    Q(timeupdate=str(test_input)), param2__id_curricula=course_plan_id)
                    .values('id').distinct().order_by('id'))
            else:
                data_equipment = list(models.TCyRunningaccount.objects.filter(
                    Q(id_user__name__icontains=test_input)
                    | Q(param2__id_curricula__name__icontains=test_input)
                    | Q(idmanager__name__icontains=test_input),
                    param2__id_curricula=course_plan_id).values(
                        'id').distinct().order_by('id'))
            data_equipment = data_attendance(
                course_plan_id, data_equipment, format_type, user_id)
        if data_equipment == []:
            return HttpResponse(dumps({'error_code': 1, 'message': '所要查询的记录不存在，请确认是否课程是否开课，其他意外情况请联系教务部'}),  content_type=content_type_tmp, charset='utf-8')
        else:
            return data_page_response(data_equipment, pages, limits)
    '''
    list
    list all information about Equipment
    '''
    AttendanceInformation_put_schema = deepcopy(data_schema)
    AttendanceInformation_put_schema['idmanager'] = Schema(
        title='管理者id',
        description='修改的管理者id',
        type=TYPE_INTEGER,
        format='int32',
        enum=None,
    )
    AttendanceInformation_put_schema['timeupdate'] = data_schema_personal_data['timeupdate']
    AttendanceInformation_put_schema['id_user'] = Schema(
        title='记录着id',
        description='参与打卡签到的学生的id',
        type=TYPE_INTEGER,
        format='int32',
        enum=None,
    )
    del AttendanceInformation_put_schema['id_user__name']
    del AttendanceInformation_put_schema['attendtimes']
    del AttendanceInformation_put_schema['attendtotal']
    del AttendanceInformation_put_schema['attendrates']
    del AttendanceInformation_put_schema['person_data']
    AttendanceInformation_put_schema['param2'] = Schema(
        title='课程安排表id',
        description='学生正在上课的课程安排表id，是课程安排表tcyplan的id',
        type=TYPE_INTEGER,
        format='int32',
        enum=None,
    )
    AttendanceInformation_put_schema['time'] = Schema(
        title='签到时间',
        description='记录最后更新时间；（2000-1-1 0:0:0 经过的秒），必须有值，如果是更改签到时间，签到时间按照上课时间来定',
        type=TYPE_INTEGER,
        format='int32',
        enum=None,
    )
    AttendanceInformation_put_schema['type_field'] = Schema(
        title='记录类型',
        description='记录的具体类型，具体使用参照T_CyTypeRA',
        type=TYPE_INTEGER,
        format='int32',
    )
    AttendanceInformation_put_schema['param1'] = Schema(
        title='特殊字段',
        description='特殊字段，使用不明',
        type=TYPE_INTEGER,
        format='int32',
        enum=None,
    )
    AttendanceInformation_put_schema['money'] = Schema(
        title='发生的费用',
        description='发生的费用',
        type=TYPE_INTEGER,
        format='int32',
        enum=None,
    )
    AttendanceInformation_put_request_body = Schema(
        title='增加签到记录',  # 标题
        description='用于增加学生签到记录',  # 接口描述
        type=TYPE_OBJECT,  # 类型 "object" ,"string" ,"number" ,"integer" ,"boolean" ,"array" ,"file"
        format=None,  # 格式    date,date-time,password,binary,bytes,float,double,int32,int64,email,ipv4, ipv6, uri, uuid, slug, decimal
        enum=None,  # [列表]列举参数的请求值
        pattern=None,  # 当 format为 string是才填此项
        # 当 type为object时，为dict对象 {'str1': Schema对象, 'str2': SchemaRef对象}
        properties=AttendanceInformation_put_schema,
        required=[
            'id', 'id_user', 'param2', 'idmanager', 'timeupdate', 'time'
        ],  # [必须的属性列表]
        items=None,  # 当type是array时，填此项
    )
    AttendanceInformation_put_responses_success = Response(
        description='添加学生签到记录成功的响应',
        schema=responses_success,
        examples={
            'error_code': 0,
            'message': put_success
        }
    )
    AttendanceInformation_put_responses_fail = Response(
        description='添加学生签到记录失败的响应',
        schema=responses_fail,
        examples={
            'error_code': 1,
            'message': put_error
        }
    )

    @swagger_auto_schema(
        request_body=AttendanceInformation_put_request_body,
        manual_parameters=None,
        operation_id=None,
        operation_description='增加学生的签到记录',
        operation_summary=None,
        security=None,
        responses={
            201: AttendanceInformation_put_responses_success,
            400: AttendanceInformation_put_responses_fail
        },
        tags=None)
    @get_request_args
    def put(self, request, args, session):
        is_login = request.COOKIES.get('is_login')
        if not request.session.get(is_login, None):
            return HttpResponse(dumps({'code': 0}),  content_type=content_type_tmp, charset='utf-8')
        field_name = ['id', 'id_user', 'param2', 'idmanager',
                      'timeupdate', 'param1', 'time', 'money', 'type_field']
        variable_name = locals()
        for i in field_name:
            variable_name[i] = args.get(i, 0)
        user_id = request.COOKIES.get('user_id')
        user_id = request.session.get(user_id)
        variable_name['idmanager'] = user_id
        # 批量命名变量
        try:
            user_object = models.TCyuser.objects.get(
                id=variable_name.get('id_user'))
            param2_object = models.TCyplan.objects.get(
                id=variable_name.get('param2'))
            idmanager_object = models.TCyuser.objects.get(
                id=variable_name.get('idmanager'))
            ueses_tmp = models.TCyRunningaccount.objects.create(
                id=variable_name.get('id'),
                id_user=user_object,
                time=variable_name.get('time'),
                type_field=variable_name.get('type_field'),
                money=variable_name.get('money'),
                param1=variable_name.get('param1'),
                param2=param2_object,
                timeupdate=variable_name.get('timeupdate'),
                idmanager=idmanager_object
            )
            return HttpResponse(dumps({'error_code': 0, 'message': put_success}), content_type=content_type_tmp, charset='utf-8')
        except Exception as error:
            return HttpResponse(dumps({'error_code': 1, 'message': data_base_error_specific+str(error)}),  content_type=content_type_tmp, charset='utf-8')
    '''
    list
    list all information about Equipment
    '''
    AttendanceInformation_patch_request_body = Schema(
        title='修改学生签到记录',  # 标题
        description='用于修改学生签到记录',  # 接口描述
        type=TYPE_OBJECT,  # 类型 "object" ,"string" ,"number" ,"integer" ,"boolean" ,"array" ,"file"
        format=None,  # 格式    date,date-time,password,binary,bytes,float,double,int32,int64,email,ipv4, ipv6, uri, uuid, slug, decimal
        enum=None,  # [列表]列举参数的请求值
        pattern=None,  # 当 format为 string是才填此项
        # 当 type为object时，为dict对象 {'str1': Schema对象, 'str2': SchemaRef对象}
        properties=AttendanceInformation_put_schema,
        required=['id'],  # [必须的属性列表]
        items=None,  # 当type是array时，填此项
    )
    AttendanceInformation_patch_responses_success = Response(
        description='修改学生签到记录成功的响应',
        schema=responses_success,
        examples={
            'error_code': 0,
            'message': patch_success
        }
    )
    AttendanceInformation_patch_responses_fail = Response(
        description='修改学生签到记录失败的响应',
        schema=responses_fail,
        examples={
            'error_code': 1,
            'message': patch_error
        }
    )

    @swagger_auto_schema(
        request_body=AttendanceInformation_patch_request_body,
        manual_parameters=None,
        operation_id=None,
        operation_description='用于修改学生签到记录',
        operation_summary=None,
        security=None,
        responses={
            201: AttendanceInformation_patch_responses_success, 400: AttendanceInformation_patch_responses_fail
        },
        tags=None)
    @get_request_args
    def patch(self, request, args, session):
        is_login = request.COOKIES.get('is_login')
        if not request.session.get(is_login, None):
            return HttpResponse(dumps({'code': 0}),  content_type=content_type_tmp, charset='utf-8')
        id_equipment = args.get('id')
        data_equipment_initial = list(
            models.TCyRunningaccount.objects.filter(id=id_equipment).values('id', 'id_user', 'param2', 'idmanager', 'timeupdate', 'param1', 'time', 'money', 'type_field'))
        if data_equipment_initial == []:
            return HttpResponse(dumps({'error_code': 1, 'message': id_error}), content_type=content_type_tmp, charset='utf-8')
        data_equipment = data_equipment_initial[0]
        field_name = ['id', 'id_user', 'param2', 'idmanager',
                      'timeupdate', 'param1', 'time', 'money', 'type_field']
        variable_name = locals()
        for i in field_name:
            if args[i] == 0:
                variable_name[i] = data_equipment[i]
            else:
                variable_name[i] = args.get(i, data_equipment[i])
        user_id = request.COOKIES.get('user_id')
        user_id = request.session.get(user_id)
        variable_name['idmanager'] = user_id
        try:
            models.TCyRunningaccount.objects.filter(id=id_equipment).update(
                id=variable_name.get('id'),
                id_user=variable_name.get('id_user'),
                time=variable_name.get('time'),
                type_field=variable_name.get('type_field'),
                money=variable_name.get('money'),
                param1=variable_name.get('param1'),
                param2=variable_name.get('param2'),
                timeupdate=variable_name.get('timeupdate'),
                idmanager=variable_name.get('idmanager'))
            return HttpResponse(dumps({'error_code': 0, 'message': '修改签到记录成功'}),  content_type=content_type_tmp, charset='utf-8')
        except Exception as error:
            return HttpResponse(dumps({'error_code': 1, 'message': data_base_error_specific+str(error)}),  content_type=content_type_tmp, charset='utf-8')

    APIView_delete_request_body = Schema(
        title=' 删除数据库中的信息 ',  # 标题
        description='删除数据库中具体的id名称',  # 接口描述
        type=TYPE_OBJECT,  # 类型 "object" ,"string" ,"number" ,"integer" ,"boolean" ,"array" ,"file"
        format=None,  # 格式    date,date-time,password,binary,bytes,float,double,int32,int64,email,ipv4, ipv6, uri, uuid, slug, decimal
        enum=None,  # [列表]列举参数的请求值
        pattern=None,  # 当 format为 string是才填此项
        # 当 type为object时，为dict对象 {'str1': Schema对象, 'str2': SchemaRef对象}
        properties=delete_schema,
        required=['ids'],  # [必须的属性列表]
        items=None,  # 当type是array时，填此项
    )
    APIView_delete_responses_success = Response(
        description='APIView_delete_responses is success',
        schema=responses_success,
        examples={
            'error_code': 0,
            'message': '删除成功'
        }
    )
    APIView_delete_responses_fail = Response(
        description='APIView_delete_responses is failure',
        schema=responses_fail,
        examples={
            'error_code': 1,
            'message': '删除失败，请输入正确的id'
        }
    )

    @ swagger_auto_schema(
        request_body=APIView_delete_request_body,
        manual_parameters=None,
        operation_id=None,
        operation_description='api是用来删除数据库中的给定字段',
        operation_summary=None,
        security=None,
        responses={
            204: APIView_delete_request_body,
            500: APIView_delete_request_body
        },
        tags=None)
    @ get_request_args
    def delete(self, request, args, session):
        is_login = request.COOKIES.get('is_login')
        if not request.session.get(is_login, None):
            return HttpResponse(dumps({'code': 0}),  content_type=content_type_tmp, charset='utf-8')
        variable_name = locals()
        delete_data = args.get('ids')
        numbers_id = len(delete_data)
        for i in range(numbers_id):
            variable_name['id_'+str(i)] = delete_data[str(i)].get('data_id')
        try:
            for i in range(numbers_id):
                models.TCyRunningaccount.objects.filter(
                    id=variable_name.get('id_'+str(i), 'id_1')).delete()
                return HttpResponse(dumps({'error_code': 0, 'message': '数据删除成功'}),  content_type=content_type_tmp, charset='utf-8')
        except Exception as error:
            return HttpResponse(dumps({'error_code': 1, 'message': data_base_error_specific + str(error)}), content_type=content_type_tmp, charset='utf-8')
