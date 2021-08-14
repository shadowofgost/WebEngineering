
from django.http import HttpResponse
from django.db.models import Q
from drf_yasg.utils import swagger_auto_schema
from drf_yasg.openapi import Parameter, Schema, Response,  TYPE_INTEGER, TYPE_OBJECT, TYPE_STRING, IN_QUERY
from json import dumps
from ..Models.CoursePlanModel.Database import CoursePlanModel
from ..Models.LocationModel.Database import LocationModel
from ..Models.UserModel.Database import UserModel
from ..Models.CurriculaModel.Database import CurriculaModel
from .Public import responses_success, responses_fail, get_request_args, data_page_response, content_type_tmp, post_search, put_success, put_error, post_error, data_base_error_specific, patch_success, patch_error, id_error, delete_schema
from rest_framework.views import APIView


class CourseArrangement(APIView):
    '''
    list
    list all information about Equipment
    '''
    data_schema = {
        'id':
        Schema(
            title='课程id',
            description='课程id,其中课程id是唯一的标识',
            type=TYPE_INTEGER,
            format='int32',
            enum=None,
        ),
        'id_curricula__name':
        Schema(
            title='课程名称',
            description='课程名称 是课程安排表对应的课程课程名称',
            type=TYPE_STRING,
            format='string',
            enum=None,
        ),
        'timebegin':
        Schema(
            title='课程开时间 ',
            description=' 项目开始时间记录最后更新时间；（2000-1-1 0:0:0 经过的秒），必须有值  ',
            type=TYPE_INTEGER,
            format='int32',
            enum=None,
        ),
        'timeend':
        Schema(
            title='课程结束时间',
            description='项目结束时间记录最后更新时间；（2000-1-1 0:0:0 经过的秒），必须有值 ',
            type=TYPE_INTEGER,
            format='int32',
            enum=None,
        ),
        'id_location__name':
        Schema(
            title=' 课程所在教室的地点的名称 ',
            description='课程所在教室的地点的名称 ',
            type=TYPE_STRING,
            format='string',
            enum=None,
        ),
        'id_speaker__name':
        Schema(
            title='主讲人',
            description='主讲人也就是课程老师的姓名',
            type=TYPE_STRING,
            format='string',
            enum=None,
        ),
        'attr':
        Schema(
            title='课程属性',
            description='1代表实验类型、2代表普通上课类型、3讲座考勤类型，必须有值',
            type=TYPE_INTEGER,
            format='int32',
            enum=[1, 2, 3],
        ),
        'charge':
        Schema(
            title=' 是否收费的字段 ',
            description=' 免费0、收费1、开放2，必须有值 ',
            type=TYPE_INTEGER,
            format='int32',
            enum=[0, 1, 2],
        ),
        'pwaccess':
        Schema(
            title='派位',
            description='不派位0、刷卡派位1（派位指用户刷卡时系统指定座位），必须有值',
            type=TYPE_INTEGER,
            format='int32',
            enum=[0, 1],
        ),
        'pwcontinuous':
        Schema(
            title='派位连续性',
            description='连续派位0、随机派位1，必须有值',
            type=TYPE_INTEGER,
            format='int32',
            enum=[0, 1],
        ),
        'pwdirection':
        Schema(
            title='排位顺序',
            description='顺序派位0、逆序派位1（当设置为随机派位时本功能无效），必须有值',
            type=TYPE_INTEGER,
            format='int32',
            enum=[0, 1],
        ),
        'dooropen':
        Schema(
            title='是否开门',
            description='匹配的用户刷卡是否开门，0开门，1不开门',
            type=TYPE_INTEGER,
            format='int32',
            enum=[0, 1],
        ),
        'timebegincheckbegin':
        Schema(
            title='最早开始考勤的最早时间',
            description=' 安排考勤开始的最早时间（单位为分钟，0代表无效），必须有值 ',
            type=TYPE_INTEGER,
            format='int32',
            enum=None,
        ),
        'timebegincheckend':
        Schema(
            title='最早签到结束时间 ',
            description=' 安排考勤开始的最迟时间（单位为分钟，0代表无效），必须有值 ',
            type=TYPE_INTEGER,
            format='int32',
            enum=None,
        ),
        'timeendcheckbegin':
        Schema(
            title='考勤结束的最早时间（签退） ',
            description=' 安排考勤结束的最早时间（单位为分钟，0代表无效），必须有值  ',
            type=TYPE_INTEGER,
            format='int32',
            enum=None,
        ),
        'timeendcheckend':
        Schema(
            title='考勤结束的最迟时间（签退）',
            description=' 安排考勤结束的最迟时间（单位为分钟，0代表无效），必须有值',
            type=TYPE_INTEGER,
            format='int32',
            enum=None,
        ),
        'listdepts':
        Schema(
            title=' 参加本安排的学生部门列表 ',
            description=' 参加本安排的学生部门列表 ',
            type=TYPE_STRING,
            format='string',
            enum=None,
        ),
        'rangeusers':
        Schema(
            title='参加本安排的学生学号列表（与RangeUser为相加的关系）',
            description='参加本安排的学生学号列表（与RangeUser为相加的关系）',
            type=TYPE_STRING,
            format='string',
            enum=None,
        ),
        'rangeequs':
        Schema(
            title=' 座位表 ',
            description=' 课程使用的座位范围列表 ',
            type=TYPE_STRING,
            format='string',
            enum=None,
        ),
        'listplaces':
        Schema(
            title=' 课程使用的地点 ',
            description=' 课程使用的地点列表（与课程使用的座位范围列表为相加的关系）',
            type=TYPE_STRING,
            format='string',
            enum=None,
        ),
        'mapuser2equ':
        Schema(
            title='学生和座位对应表',
            description='学生和座位对应表',
            type=TYPE_STRING,
            format='string',
            enum=None,
        ),
        'aboutspeaker':
        Schema(
            title='本课程主讲人介绍',
            description=' 本课程主讲人也就是上课老师的介绍',
            type=TYPE_STRING,
            format='string',
            enum=None,
        ),
        'rem':
        Schema(
            title='课程介绍',
            description='课程内容的介绍',
            type=TYPE_STRING,
            format='string',
            enum=None,
        ),
        'timeupdate':
        Schema(
            title='update time ',
            description=' 记录最后更新时间；（2000-1-1 0:0:0 经过的秒），必须有值 ',
            type=TYPE_INTEGER,
            format='int32',
            enum=None,
        ),
        'idmanager__name':
        Schema(
            title=' 更新信息的管理员的姓名 ',
            description=' 更新信息的管理员的姓名 ',
            type=TYPE_STRING,
            format='string',
            enum=None,
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
    CourseInformation_get_responses_success = Response(
        description='查询课程信息成功的响应',
        schema=get_responses_success,
        examples=None,
    )
    CourseInformation_get_responses_fail = Response(
        description='查询课程信息失败的响应',
        schema=responses_fail,
        examples={
            'error_code': 1,
            'message': '查询课程信息失败'
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
        manual_parameters=[
            page_get_parammeter, limits_get_parammeter],
        operation_id=None,
        operation_description='这个端口用于查询课程信息',
        operation_summary=None,
        security=None,
        responses={
            200: CourseInformation_get_responses_success, 401: CourseInformation_get_responses_fail
        },
        tags=None)
    @get_request_args
    def get(self, request, args, session):
        is_login = request.COOKIES.get('is_login')
        if not request.session.get(is_login, None):
            return HttpResponse(dumps({'code': 0}),  content_type=content_type_tmp, charset='utf-8')
        pages = int(args.get('page', 1))
        limits = int(args.get('limits', 20))
        data_equipment = CoursePlanModel.objects.all().values('id','id_curricula__name', 'timebegin', 'timeend', 'id_location__name', 'id_speaker__name', 'attr', 'charge', 'pwaccess', 'pwcontinuous', 'pwdirection', 'dooropen', 'timebegincheckbegin', 'timebegincheckend', 'timeendcheckbegin', 'timeendcheckend', 'rangeusers', 'listdepts', 'rangeequs', 'timeupdate', 'listplaces', 'idmanager__name', 'mapuser2equ', 'aboutspeaker', 'rem').distinct().order_by('id')
        return data_page_response(data_equipment, pages, limits)
    '''
    list
    list all information about Equipment
    '''
    CourseArrangement_post_request_body = Schema(
        title='查询课程安排所需要的信息',  # 标题
        description=' 输入查询字符串用于查询课程安排信息 ',  # 接口描述
        type=TYPE_OBJECT,  # 类型 "object" ,"string" ,"number" ,"integer" ,"boolean" ,"array"" ,"boolean" ,"array" ,"file"
        format=None,  # 格式    date,date-time,password,binary,bytes,float,double,int32,int64,email,ipv4, ipv6, uri, uuid, slug, decimal
        enum=None,  # [列表]列举参数的请求值
        pattern=None,  # 当 format为 string是才填此项
        # 当 type为object时，为dict对象 {'str1': Schema对象, 'str2': SchemaRef对象}
        properties=post_search,
        required=['input_string', 'page', 'limits'],  # [必须的属性列表]
        items=None,  # 当type是array时，填此项
    )
    CourseArrangement_post_responses_success = Response(
        description='查询课程安排表成功的响应',
        schema=get_responses_success,
        examples={
            'error_code': 0,
            'message': '查询成功'
        })
    CourseArrangement_post_responses_fail = Response(
        description='查询课程安排表失败的响应',
        schema=responses_fail,
        examples={
            'error_code': 1,
            'message': post_error
        })

    @swagger_auto_schema(
        request_body=CourseArrangement_post_request_body,
        manual_parameters=None,
        operation_id=None,
        operation_description='这个端口用于查询课程安排表（某些条件下的课程安排表）',
        operation_summary=None,
        security=None,
        responses={
            201: CourseArrangement_post_responses_success,
            400: CourseArrangement_post_responses_fail
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
            data_equipment = CoursePlanModel.objects.all().values(
                'id',
                'id_curricula__name',
                'timebegin',
                'timeend',
                'id_location__name',
                'id_speaker__name',
                'attr',
                'charge',
                'pwaccess',
                'pwcontinuous',
                'pwdirection',
                'dooropen',
                'timebegincheckbegin',
                'timebegincheckend',
                'timeendcheckbegin',
                'timeendcheckend',
                'rangeusers',
                'listdepts',
                'rangeequs',
                'timeupdate',
                'listplaces',
                'idmanager__name',
                'mapuser2equ',
                'aboutspeaker',
                'rem'
            ).distinct().order_by('id')
        else:
            input_string = input_string.strip()
            try:
                test_input = eval(input_string)
            except:
                test_input = input_string
            if isinstance(test_input, int):
                data_equipment = CoursePlanModel.objects.filter(
                    Q(id=test_input)
                    | Q(id_curricula=test_input)
                    | Q(timebegin=test_input)
                    | Q(timeend=test_input)
                    | Q(id_location=test_input)
                    | Q(id_speaker=test_input)
                    | Q(attr=test_input)
                    | Q(charge=test_input)
                    | Q(pwaccess=test_input)
                    | Q(pwcontinuous=test_input)
                    | Q(pwdirection=test_input)
                    | Q(dooropen=test_input)
                    | Q(timebegincheckbegin=test_input)
                    | Q(timebegincheckend=test_input)
                    | Q(timeendcheckbegin=test_input)
                    | Q(timeendcheckend=test_input)
                    | Q(timeupdate=test_input)
                    | Q(idmanager=test_input)).values(
                        'id',
                        'id_curricula',
                        'timebegin',
                        'timeend',
                        'id_location',
                        'id_speaker',
                        'attr',
                        'charge',
                        'pwaccess',
                        'pwcontinuous',
                        'pwdirection',
                        'dooropen',
                        'timebegincheckbegin',
                        'timebegincheckend',
                        'timeendcheckbegin',
                        'timeendcheckend',
                        'rangeusers',
                        'listdepts',
                        'rangeequs',
                        'timeupdate',
                        'listplaces',
                        'idmanager',
                        'mapuser2equ',
                        'aboutspeaker',
                        'rem'
                ).distinct().order_by('id')
            else:
                data_equipment = CoursePlanModel.objects.filter(
                    Q(rem__icontains=test_input)
                    | Q(rangeequs__icontains=test_input)
                    | Q(rangeequs__icontains=test_input)
                    | Q(listdepts__icontains=test_input)
                    | Q(listplaces__icontains=test_input)
                    | Q(mapuser2equ__icontains=test_input)
                    | Q(aboutspeaker__icontains=test_input)
                    | Q(idmanager__name__icontains=test_input)
                    | Q(id_location__name__icontains=test_input)
                    | Q(id_speaker__name__icontains=test_input)).values(
                        'id',
                        'id_curricula',
                        'timebegin',
                        'timeend',
                        'id_location__name',
                        'id_speaker__name',
                        'attr',
                        'charge',
                        'pwaccess',
                        'pwcontinuous',
                        'pwdirection',
                        'dooropen',
                        'timebegincheckbegin',
                        'timebegincheckend',
                        'timeendcheckbegin',
                        'timeendcheckend',
                        'rangeusers',
                        'listdepts',
                        'rangeequs',
                        'timeupdate',
                        'listplaces',
                        'idmanager__name',
                        'mapuser2equ',
                        'aboutspeaker',
                        'rem',
                ).distinct().order_by('id')
        return data_page_response(data_equipment, pages, limits)

    '''
    list
    list all information about Equipment
    '''
    CourseArrangement_put_request_body = Schema(
        title='  增加课程安排表需要的数据  ',  # 标题
        description='向数据库增加课程安排表需要的数据和字段',  # 接口描述
        type=TYPE_OBJECT,  # 类型 "object" ,"string" ,"number" ,"integer" ,"boolean" ,"array" ,"file"
        properties=data_schema,
        required=[
            'id', 'id_curricula__name', 'timebegin', 'timeend', 'id_location__name', 'id_speaker__name',
            'attr', 'charge', 'pwaccess', 'pwcontinuous',
            'pwdirection', 'dooropen', 'timebegincheckbegin',
            'timebegincheckend', 'timeendcheckbegin', 'timeendcheckend',
            'rangeusers', 'listdepts', 'rangeequs', 'timeupdate', 'listplaces',
            'idmanager__name', 'mapuser2equ', 'aboutspeaker', 'rem']
    )
    CourseArrangement_put_responses_success = Response(
        description='增加课程安排表数据成功的响应',
        schema=responses_success,
        examples={
            'error_code': 0,
            'message': put_success
        })
    CourseArrangement_put_responses_fail = Response(
        description='增加课程安排表数据失败的响应',
        schema=responses_fail,
        examples={
            'error_code': 1,
            'message': put_error
        })

    @swagger_auto_schema(
        request_body=CourseArrangement_put_request_body,
        manual_parameters=None,
        operation_id=None,
        operation_description='这个端口用于向数据库增加课程安排表的数据',
        operation_summary=None,
        security=None,
        responses={
            201: CourseArrangement_put_responses_success,
            400: CourseArrangement_put_responses_fail
        },
        tags=None)
    @get_request_args
    def put(self, request, args, session):
        field_name = [
            'id', 'id_curricula__name', 'timebegin', 'timeend', 'id_location__name', 'id_speaker__name', 'timeupdate',
            'idmanager__name',  'aboutspeaker', 'rem'
        ]
        is_login = request.COOKIES.get('is_login')
        if not request.session.get(is_login, None):
            return HttpResponse(dumps({'code': 0}),  content_type=content_type_tmp, charset='utf-8')
        variable_name = locals()
        for i in field_name:
            variable_name[i] = args.get(i, 0)
        user_id = request.COOKIES.get('user_id')
        user_id = request.session.get(user_id)
        variable_name['idmanager'] = user_id
        del variable_name['idmanager__name']
        if isinstance(variable_name['id_location__name'], int) and isinstance(variable_name['id_speaker__name'], int) and isinstance(variable_name['id_curricula__name'], int):
            variable_name['id_location'] = variable_name['id_location__name']
            variable_name['id_speaker'] = variable_name['id_speaker__name']
            variable_name['id_curricula'] = variable_name['id_curricula__name']
        else:
            return HttpResponse(dumps(
                {'error_code': 1, 'message': '请确保所填的id类数据是数字'}),
                content_type=content_type_tmp,
                charset='utf-8')
        # 批量命名变量
        try:
            curricula_object = CurriculaModel.objects.get(
                id=variable_name.get('id_curricula'))
            location_object = LocationModel.objects.get(
                id=variable_name.get('id_location'))
            speaker_object = UserModel.objects.get(
                id=variable_name.get('id_speaker'))
            idmanager_object = UserModel.objects.get(
                id=variable_name.get('idmanager'))
            ueses_tmp = CoursePlanModel.objects.create(
                id=variable_name.get('id'),
                id_curricula=curricula_object,
                id_location=location_object,
                id_speaker=speaker_object,
                timebegin=variable_name.get('timebegin'),
                timeend=variable_name.get('timeend'),
                attr=variable_name.get('attr'),
                charge=variable_name.get('charge'),
                pwaccess=variable_name.get('pwaccess'),
                pwcontinuous=variable_name.get('pwcontinuous'),
                pwdirection=variable_name.get('pwdirection'),
                dooropen=variable_name.get('dooropen'),
                timebegincheckbegin=variable_name.get('timebegincheckbegin'),
                timebegincheckend=variable_name.get('timebegincheckend'),
                timeendcheckbegin=variable_name.get('timeendcheckbegin'),
                timeendcheckend=variable_name.get('timeendcheckend'),
                rangeusers=variable_name.get('rangeusers'),
                listdepts=variable_name.get('listdepts'),
                rangeequs=variable_name.get('rangeequs'),
                timeupdate=variable_name.get('timeupdate'),
                listplaces=variable_name.get('listplaces'),
                idmanager=idmanager_object,
                mapuser2equ=variable_name.get('mapuser2equ'),
                aboutspeaker=variable_name.get('aboutspeaker'),
                rem=variable_name.get('rem'))
            return HttpResponse(dumps({'error_code': 0, 'message': put_success}),
                                content_type=content_type_tmp,
                                charset='utf-8')
        except Exception as error:
            return HttpResponse(dumps(
                {'error_code': 1, 'message': data_base_error_specific + str(error)}),
                content_type=content_type_tmp,
                charset='utf-8')

    '''
    list
    list all information about Equipment
    '''
    CourseArrangement_patch_request_body = Schema(
        title=' 修改课程安排表所需要的数据 ',  # 标题
        description=' 修改课程安排表 ',  # 接口描述
        type=TYPE_OBJECT,  # 类型 "object" ,"string" ,"number" ,"integer" ,"boolean" ,"array" ,"file"
        format=None,  # 格式    date,date-time,password,binary,bytes,float,double,int32,int64,email,ipv4, ipv6, uri, uuid, slug, decimal
        enum=None,  # [列表]列举参数的请求值
        pattern=None,  # 当 format为 string是才填此项
        # 当 type为object时，为dict对象 {'str1': Schema对象, 'str2': SchemaRef对象}
        properties=data_schema,
        required=['id'],  # [必须的属性列表]
        items=None,  # 当type是array时，填此项
    )
    CourseArrangement_patch_responses_success = Response(
        description='修改课程安排表成功的响应',
        schema=responses_success,
        examples={
            'error_code': 0,
            'message': patch_success
        })
    CourseArrangement_patch_responses_fail = Response(
        description='修改课程安排表失败的响应',
        schema=responses_fail,
        examples={
            'error_code': 1,
            'message': patch_error
        })

    @swagger_auto_schema(request_body=CourseArrangement_patch_request_body,
                         manual_parameters=None,
                         operation_id=None,
                         operation_description='这个端口用于修改课程安排表的数据',
                         operation_summary=None,
                         security=None,
                         responses={
                             201: CourseArrangement_patch_responses_success,
                             400: CourseArrangement_patch_responses_fail
                         },
                         tags=None)
    @get_request_args
    def patch(self, request, args, session):
        is_login = request.COOKIES.get('is_login')
        if not request.session.get(is_login, None):
            return HttpResponse(dumps({'code': 0}),  content_type=content_type_tmp, charset='utf-8')
        id_equipment = args.get('id')
        data_equipment_initial = list(
            CoursePlanModel.objects.filter(id=id_equipment).values(
                'id',
                'id_curricula',
                'timebegin',
                'timeend',
                'id_location',
                'id_speaker',
                'attr',
                'charge',
                'pwaccess',
                'pwcontinuous',
                'pwdirection',
                'dooropen',
                'timebegincheckbegin',
                'timebegincheckend',
                'timeendcheckbegin',
                'timeendcheckend',
                'rangeusers',
                'listdepts',
                'rangeequs',
                'timeupdate',
                'listplaces',
                'idmanager',
                'mapuser2equ',
                'aboutspeaker',
                'rem'))
        if data_equipment_initial == []:
            return HttpResponse(dumps({'error_code': 1, 'message': id_error}),

                                content_type=content_type_tmp,
                                charset='utf-8')
        data_equipment = data_equipment_initial[0]
        field_name = [
            'id', 'id_curricula__name', 'timebegin', 'timeend', 'id_location__name', 'id_speaker__name',
            'attr',  'charge', 'pwaccess', 'pwcontinuous',
            'pwdirection', 'dooropen', 'timebegincheckbegin',
            'timebegincheckend', 'timeendcheckbegin', 'timeendcheckend',
            'rangeusers', 'listdepts', 'rangeequs', 'timeupdate', 'listplaces',
            'idmanager__name', 'mapuser2equ', 'aboutspeaker', 'rem'
        ]
        args['id_curricula'] = args.get(
            'id_curricula__name', data_equipment['id_curricula'])
        args['id_location'] = args.get(
            'id_location__name', data_equipment['id_location'])
        args['id_speaker'] = args.get(
            'id_speaker__name', data_equipment['id_speaker'])
        args['idmanager'] = args.get(
            'idmanager__name', data_equipment['idmanager'])
        if isinstance(args['id_location__name'], int) and isinstance(args['id_speaker__name'], int) and isinstance(args['id_curricula__name'], int) and isinstance(args['idmanager__name'], int):
            args['id_location'] = args['id_location__name']
            args['id_speaker'] = args['id_speaker__name']
            args['id_curricula'] = args['id_curricula__name']
            args['idmanager'] = args['idmanager__name']
        else:
            return HttpResponse(dumps(
                {'error_code': 1, 'message': '请确保所填的id类数据是数字'}),

                content_type=content_type_tmp,
                charset='utf-8')
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
            CoursePlanModel.objects.filter(id=id_equipment).update(
                id=variable_name.get('id'),
                id_curricula=variable_name.get('id_curricula'),
                id_location=variable_name.get('id_location'),
                id_speaker=variable_name.get('id_speaker'),
                timebegin=variable_name.get('timebegin'),
                timeend=variable_name.get('timeend'),
                attr=variable_name.get('attr'),
                charge=variable_name.get('charge'),
                pwaccess=variable_name.get('pwaccess'),
                pwcontinuous=variable_name.get('pwcontinuous'),
                pwdirection=variable_name.get('pwdirection'),
                dooropen=variable_name.get('dooropen'),
                timebegincheckbegin=variable_name.get('timebegincheckbegin'),
                timebegincheckend=variable_name.get('timebegincheckend'),
                timeendcheckbegin=variable_name.get('timeendcheckbegin'),
                timeendcheckend=variable_name.get('timeendcheckend'),
                rangeusers=variable_name.get('rangeusers'),
                listdepts=variable_name.get('listdepts'),
                rangeequs=variable_name.get('rangeequs'),
                timeupdate=variable_name.get('timeupdate'),
                listplaces=variable_name.get('listplaces'),
                idmanager=variable_name.get('idmanager'),
                mapuser2equ=variable_name.get('mapuser2equ'),
                aboutspeaker=variable_name.get('aboutspeaker'),
                rem=variable_name.get('rem'))
            return HttpResponse(dumps({'message': '修改课程安排表成功'}),  content_type=content_type_tmp, charset='utf-8')
        except Exception as error:
            return HttpResponse(dumps(
                {'error_code': 1, 'message': data_base_error_specific + str(error)}),

                content_type=content_type_tmp,
                charset='utf-8')
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
            variable_name['id_'+str(i)] = delete_data[i].get('data_id')
        try:
            for i in range(numbers_id):
                CoursePlanModel.objects.filter(
                    id=variable_name.get('id_'+str(i), 'id_1')).delete()
                return HttpResponse(dumps({'error_code': 0, 'message': '数据删除成功'}),  content_type=content_type_tmp, charset='utf-8')
        except Exception as error:
            return HttpResponse(dumps({'error_code': 1, 'message': data_base_error_specific + str(error)}), content_type=content_type_tmp, charset='utf-8')
