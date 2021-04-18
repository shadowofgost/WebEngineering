import re
from django.http import HttpResponse
from drf_yasg.utils import swagger_auto_schema
from drf_yasg.openapi import Schema, Response, Parameter, TYPE_INTEGER, TYPE_OBJECT, TYPE_STRING, IN_QUERY
from rest_framework.views import APIView
from json import dumps
from time import time
from .. import models
from .Public import responses_success, responses_fail, get_request_args, content_type_tmp, select_quit_warning_student, data_page_response


class QuitWarning(APIView):
    data_personal = Schema(
        title='缺勤次数过多的学生信息',
        description='缺勤次数过多学生个人信息',
        type=TYPE_OBJECT,  # 类型
        properties={
            'id_user__nouser': Schema(
                title='学号',
                description='学生的个人学号',
                type=TYPE_STRING,
                format='string',
            ),
            'id_user__name': Schema(
                title='学生姓名',
                description='学生的姓名',
                type=TYPE_STRING,
                format='string'
            ),
            'id_user__quit': Schema(
                title='缺勤次数 ',
                description='缺勤次数过多的学生的缺勤次数',
                type=TYPE_INTEGER,
                format='int32',
            )
        }
    )
    data_schema = {
        'id': Schema(
            title='ID',
            description='课程的id',
            type=TYPE_INTEGER,
            format='int32',
        ),
        'name': Schema(
            title='课程名',
            description='课程名',
            type=TYPE_STRING,
            format='string'
        ),
        'id_speaker__name': Schema(
            title='ID of card ',
            description='用户的卡号',
            type=TYPE_STRING,
            format='string',
        ),
        'id_speaker__email': Schema(
            title='ID of user ',
            description='用户的身份id（比如学生的id就是他自己的学号）',
            type=TYPE_STRING,
            format='string',
        ),
        'select_students': Schema(
            title='学生信息 ',
            description='缺勤次数超过标准的学生信息',
            type=TYPE_OBJECT,
            properties=[data_personal, data_personal]
        )
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
                description='用于传达是否有报错数据，0表示没有报错数据，1表示有报错数据',
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
    Warning_get_responses_success = Response(
        description='获取信息成功的响应',
        schema=get_responses_success,
        examples={
            'error_code': 0,
            'message': '成功获取信息'
        },
    )
    get_responses_fail = Response(
        description='检测图片失败的响应',
        schema=responses_fail,
        examples={
            'error_code': 1,
            'message': '获取信息失败失败'
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
        operation_description='这个端口用于提醒老师和管理员多次缺勤的学生',
        manual_parameters=[page_get_parammeter, limits_get_parammeter],
        security=None,
        responses={
            200: Warning_get_responses_success,
            401: get_responses_fail
        },
        tags=None)
    @get_request_args
    def get(self, request, args, session):
        is_login = request.COOKIES.get('is_login')
        if not request.session.get(is_login, None):
            return HttpResponse(dumps({'code': 0}),  content_type=content_type_tmp, charset='utf-8')
        pages = int(args.get('page', 1))
        limits = int(args.get('limits', 20))
        limit_not_attendrates = 3
        limit_not_attendtimes = 0.2
        user_group_id = request.COOKIES.get('user_group_id')
        user_group_id = request.session.get(user_group_id)
        user_id = request.COOKIES.get('user_id')
        user_id = request.session.get(user_id)
        user_nouser = request.COOKIES.get('user_nouser')
        user_nouser = request.session.get(user_nouser)
        data_course = []
        format_type = 1
        id_list = []
        return_data = []
        if user_group_id == 1 or user_group_id == 2:
            data_course = tuple(models.TCycurricula.objects.all().values(
                'id', 'name', 'id_speaker__name', 'id_speaker__email'
                'rangeusers', 'listdepts'
            ).distinct().order_by('id'))
        elif user_group_id == 3:
            data_course = tuple(models.TCycurricula.objects.filter(id_speaker=user_id).values(
                'id', 'name', 'id_speaker__name', 'id_speaker__email'
                'rangeusers', 'listdepts'
            ).distinct().order_by('id'))
        if data_course == []:
            return HttpResponse(dumps({'error_code': 1, 'message': '数据库出错，请联系管理员'}), content_type=content_type_tmp, charset='utf-8')
        for i in data_course:
            course_quit_data = {}
            course_quit_data['id'] = i['id']
            course_quit_data['name'] = i['name']
            course_quit_data['id_speaker'] = i['id_speaker']
            course_quit_data['id_speaker__name'] = i['id_speaker__name']
            course_plan_id = i['id']
            select_students = select_quit_warning_student(
                course_plan_id, id_list, format_type, user_id, limit_not_attendrates, limit_not_attendtimes)
            course_quit_data['select_students'] = select_students
            return_data.append(course_quit_data)
        if return_data == []:
            return HttpResponse(dumps({'error_code': 1, 'message': '没有考勤不合格学生'}), content_type=content_type_tmp, charset='utf-8')
        else:
            return data_page_response(return_data, pages, limits)
