from django.http import HttpResponse
from django.db.models import Q
from drf_yasg.utils import swagger_auto_schema
from drf_yasg.openapi import Parameter, Schema, Response,  TYPE_INTEGER, TYPE_OBJECT, TYPE_STRING, IN_QUERY
from .. import models
from json import dumps
from .Public import responses_success, responses_fail, get_request_args, data_page_response, content_type_tmp,  patch_error, patch_success, post_search, post_error, put_error, put_success, id_error, data_base_error_specific, delete_schema
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt


class UserInformation(APIView):
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
        'id__nocard': Schema(
            title='ID of card ',
            description='用户的卡号',
            type=TYPE_STRING,
            format='string',
        ),
        'id__nouser': Schema(
            title='ID of user ',
            description='用户的身份id（比如学生的id就是他自己的学号）',
            type=TYPE_STRING,
            format='string',
        ),
        'id__name': Schema(
            title='用户的姓名',
            description='用户的姓名',
            type=TYPE_STRING,
            format='string'
        ),
        'id__psw': Schema(
            title='用户的密码',
            description='用户的密码',
            type=TYPE_STRING,
            format='string'
        ),
        'id__deptid__name': Schema(
            title='部门',
            description='用户所属的部门名称',
            type=TYPE_STRING,
            format='string'
        ),
        'id__sex': Schema(
            title='性别',
            description='用户的性别，0代表女性，1代表男性',
            enum=[0, 1],
            type=TYPE_INTEGER,
            format='int32',
        ),
        'id__attr': Schema(
            title='权限',
            description='用户管理权限，0代表超级管理员，1代表教务处管理员，2代表辅导员，3代表教师，4代表学生',
            enum=[0, 1, 2, 3, 4],
            type=TYPE_INTEGER,
            format='int32',
        ),
        'id__timeupdate': Schema(
            title='信息更新时间',
            description='用户表的更新时间',
            type=TYPE_INTEGER,
            format='int32',
        ),
        'id__localid': Schema(
            title='管理员地点',
            description=' 管理员所在的地点',
            type=TYPE_STRING,
            format='string'
        ),
        'timeupdate': Schema(
            title='timeupdate',
            description='用户附件表的更新时间',
            type=TYPE_INTEGER,
            format='int32',
        ),
        'idmanager__name': Schema(
            title='管理员姓名',
            description='修改账户的管理员姓名',
            type=TYPE_STRING,
            format='string'
        ),
        'rem': Schema(
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
        properties=data_schema
    )
    get_responses_success = Schema(
        title='成功获取查询数据',
        description='这个接口用于展示成功获取全部数据的格式',
        type=TYPE_OBJECT,
        properties={'page': Schema(
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
    StudentsInformation_get_responses_success = Response(
        description='个人信息查询成功的响应',
        schema=get_responses_success,
        examples=None
    )
    StudentsInformation_get_responses_fail = Response(
        description='个人信息查询失败的响应',
        schema=responses_fail,
        examples={'error_code': 1, 'message': patch_error})
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
        operation_description='所有学生信息查询',
        operation_summary=None,
        security=None,
        responses={
            200: StudentsInformation_get_responses_success,
            401: StudentsInformation_get_responses_fail
        },
        tags=None)
    @get_request_args
    @csrf_exempt
    def get(self, request, args, session):
        is_login = request.COOKIES.get('is_login')
        if not request.session.get(is_login, None):
            return HttpResponse(dumps({'code': 0}),  content_type=content_type_tmp, charset='utf-8')
        user_group_id = request.COOKIES.get('user_group_id')
        user_group_id = request.session.get(user_group_id)
        pages = int(args.get('page', 1))
        limits = int(args.get('limits', 20))
        data_user = models.TCyuser.objects.filter(attr=user_group_id).values(
            'id', 'nocard', 'nouser', 'name', 'psw', 'deptid__name', 'sex', 'attr', 'timeupdate').distinct().order_by('id')
        return data_page_response(data_user, pages, limits)

    '''
    list
    list all information about Equipment
    '''
    StudentsInformation_post_request_body = Schema(
        title='查询所有信息所需要的数据 ',  # 标题
        description=' 这是用查询信息数据所需要的基础信息 ',  # 接口描述
        type=TYPE_OBJECT,  # 类型 "object" ,"string" ,"number" ,"integer" ,"boolean" ,"array" ,"file"
        format=None,  # 格式    date,date-time,password,binary,bytes,float,double,int32,int64,email,ipv4, ipv6, uri, uuid, slug, decimal
        enum=None,  # [列表]列举参数的请求值
        pattern=None,  # 当 format为 string是才填此项
        # 当 type为object时，为dict对象 {'str1': Schema对象, 'str2': SchemaRef对象}
        properties=post_search,
        required=['input_string', 'page', 'limits'],  # [必须的属性列表]
        items=None,  # 当type是array时，填此项
    )
    StudentsInformation_post_responses_success = Response(
        description='查询所有信息成功的响应',
        schema=get_responses_success,
        examples=None,
    )
    StudentsInformation_post_responses_fail = Response(
        description='查询所有信息失败的响应',
        schema=responses_fail,
        examples={
            'error_code': 1,
            'message': post_error
        }
    )

    @swagger_auto_schema(
        request_body=StudentsInformation_post_request_body,
        manual_parameters=None,
        operation_id=None,
        operation_description='这个端口用于查询所有的信息',
        operation_summary=None,
        security=None,
        responses={
            201: StudentsInformation_post_responses_success,
            400: StudentsInformation_post_responses_fail
        },
        tags=None)
    @get_request_args
    @csrf_exempt
    def post(self, request, args, session):
        is_login = request.COOKIES.get('is_login')
        if not request.session.get(is_login, None):
            return HttpResponse(dumps({'code': 0}),  content_type=content_type_tmp, charset='utf-8')
        user_group_id = request.COOKIES.get('user_group_id')
        user_group_id = request.session.get(user_group_id)
        input_string = args.get('input_string', None)
        pages = int(args.get('page', 1))
        limits = int(args.get('limits', 20))
        if input_string == None:
            data_user = models.TCyuser.objects.filter(attr=user_group_id).values(
                'id', 'nocard', 'nouser', 'name', 'psw', 'deptid__name', 'sex', 'attr', 'timeupdate')
            return data_page_response(data_user, pages, limits)
        else:
            input_string = input_string.strip()
            try:
                test_input = eval(input_string)
            except:
                test_input = input_string
            if isinstance(test_input, int):
                data_user_information = models.TCyuserex.objects.filter(
                    Q(id=test_input) |
                    Q(id__nocard__icontains=str(test_input)) |
                    Q(id__nouser__icontains=str(test_input)) |
                    Q(id__deptid=test_input) |
                    Q(id__sex=test_input) |
                    Q(id__attr=test_input) |
                    Q(id__timeupdate=test_input) |
                    Q(timeupdate=test_input), attr=user_group_id
                ).values('id', 'id__nocard', 'id__nouser', 'id__name', 'id__psw', 'id__deptid__name', 'id__sex', 'id__attr', 'id__timeupdate', 'timeupdate', 'idmanager__name', 'rem', 'id__localid').distinct().order_by('id')
            else:
                data_user_information = models.TCyuserex.objects.filter(
                    Q(id__name__icontains=test_input) |
                    Q(id__psw__icontains=test_input) |
                    Q(id__deptid__name=test_input) |
                    Q(idmanager__name=test_input) |
                    Q(rem=test_input), attr=user_group_id
                ).values('id', 'id__nocard', 'id__nouser', 'id__name', 'id__psw', 'id__deptid__name', 'id__sex', 'id__attr', 'id__timeupdate', 'timeupdate', 'idmanager__name', 'rem',  'id__localid').distinct().order_by('id')

        return data_page_response(data_user_information, pages, limits)

    '''
    list
    list all information about Equipment
    '''
    StudentsInformation_put_request_body = Schema(
        title=' 增加信息 ',  # 标题
        description=' 所需要的必要数据用于增添数据 ',  # 接口描述
        type=TYPE_OBJECT,  # 类型 "object" ,"string" ,"number" ,"integer" ,"boolean" ,"array" ,"file"
        format=None,  # 格式    date,date-time,password,binary,bytes,float,double,int32,int64,email,ipv4, ipv6, uri, uuid, slug, decimal
        enum=None,  # [列表]列举参数的请求值
        pattern=None,  # 当 format为 string是才填此项
        # 当 type为object时，为dict对象 {'str1': Schema对象, 'str2': SchemaRef对象}
        properties=data_schema,
        required=['id', 'id__nocard', 'id__nouser', 'id__name', 'id__psw', 'id__deptid__name', 'id__sex',
                  'id__attr', 'id__timeupdate', 'timeupdate', 'idmanager__name', 'rem', 'id__localid'],  # [必须的属性列表]
        items=None,  # 当type是array时，填此项
    )
    StudentsInformation_put_responses_success = Response(
        description='增加个人信息成功的响应',
        schema=responses_success,
        examples={
            'error_code': 0,
            'message': put_success
        }
    )
    StudentsInformation_put_responses_fail = Response(
        description='增加个人信息失败的响应',
        schema=responses_fail,
        examples={
            'error_code': 1,
            'message': put_error
        }
    )

    @swagger_auto_schema(
        request_body=StudentsInformation_put_request_body,
        manual_parameters=None,
        operation_id=None,
        operation_description='用于向数据库增加个人信息',
        operation_summary=None,
        security=None,
        responses={
            201: StudentsInformation_put_responses_success, 400: StudentsInformation_put_responses_fail
        },
        tags=None)
    @get_request_args
    @csrf_exempt
    def put(self, request, args, session):
        is_login = request.COOKIES.get('is_login')
        if not request.session.get(is_login, None):
            return HttpResponse(dumps({'code': 0}),  content_type=content_type_tmp, charset='utf-8')
        field_name = ['id', 'id__nocard', 'id__nouser', 'id__name', 'id__psw', 'id__deptid__name', 'id__sex',
                      'id__attr', 'id__timeupdate', 'timeupdate', 'idmanager__name', 'rem',  'id__localid']
        variable_name = locals()
        for i in field_name:
            variable_name[i] = args.get(i, 0)
        user_id = request.COOKIES.get('user_id')
        user_id = request.session.get(user_id)
        variable_name['idmanager'] = user_id
        variable_name['id__deptid'] = variable_name['id__deptid__name']
        if isinstance(variable_name['id__deptid'], int):
            variable_name['id__deptid'] = variable_name['id__deptid__name']
        else:
            return HttpResponse(dumps(
                {'error_code': 1, 'message': '请确保所填的id类数据是数字'}),

                content_type=content_type_tmp,
                charset='utf-8')
        try:
            use_tmp = models.TCyuser.objects.create(
                id=variable_name.get('id'),
                nocard=variable_name.get('id__nocard'),
                nouser=variable_name.get('id__nouser'),
                name=variable_name.get('id__name'),
                psw=variable_name.get('id__psw'),
                deptid=variable_name.get('id__deptid'),
                sex=variable_name.get('id__sex'),
                attr=variable_name.get('id__attr'),
                timeupdate=variable_name.get('timeupdate'),
                idmanager=variable_name.get('idmanager'),
                localid=variable_name.get('localid')
            )
            idmanager_object = models.TCyuser.objects.get(
                id=variable_name.get('idmanager'))
            use_tmp_1 = models.TCyuserex.objects.create(
                id=variable_name.get('id'),
                rem=variable_name.get('rem'),
                timeupdate=variable_name.get('timeupdate'),
                idmanager=idmanager_object,
            )
            return HttpResponse(dumps({'error_code': 0, 'message': put_success}), content_type=content_type_tmp, charset='utf-8')
        except Exception as error:
            return HttpResponse(dumps({'error_code': 1, 'message': data_base_error_specific+str(error)}),  content_type=content_type_tmp, charset='utf-8')
    '''
    list
    list all information about Equipment
    '''
    StudentsInformation_patch_request_body = Schema(
        title=' 修改个人信息',  # 标题
        description=' 需要被更新的个人信息数据',  # 接口描述
        type=TYPE_OBJECT,  # 类型 "object" ,"string" ,"number" ,"integer" ,"boolean" ,"array" ,"file"
        format=None,  # 格式    date,date-time,password,binary,bytes,float,double,int32,int64,email,ipv4, ipv6, uri, uuid, slug, decimal
        enum=None,  # [列表]列举参数的请求值
        pattern=None,  # 当 format为 string是才填此项
        # 当 type为object时，为dict对象 {'str1': Schema对象, 'str2': SchemaRef对象}
        properties=data_schema,
        required=['id'],  # [必须的属性列表]
        items=None,  # 当type是array时，填此项
    )
    StudentsInformation_patch_responses_success = Response(
        description=' 修改个人信息成功的响应',
        schema=responses_success,
        examples={
            'error_code': 1,
            'message': patch_success
        }
    )
    StudentsInformation_patch_responses_fail = Response(
        description=' 修改个人信息失败的响应',
        schema=responses_fail,
        examples={
            'error_code': 1,
            'message': patch_error
        }
    )

    @swagger_auto_schema(
        request_body=StudentsInformation_patch_request_body,
        manual_parameters=None,
        operation_id=None,
        operation_description='用于修改个人信息',
        operation_summary=None,
        security=None,
        responses={
            201: StudentsInformation_patch_responses_success,
            400: StudentsInformation_patch_responses_fail
        },
        tags=None)
    @get_request_args
    @csrf_exempt
    def patch(self, request, args, session):
        is_login = request.COOKIES.get('is_login')
        if not request.session.get(is_login, None):
            return HttpResponse(dumps({'code': 0}),  content_type=content_type_tmp, charset='utf-8')
        id_user_information = args.get('id')
        data_user_information_initial = list(models.TCyuser.objects.filter(id=id_user_information).values(
            'id', 'id__nocard', 'id__nouser', 'id__name', 'id__psw', 'id__deptid', 'id__sex',
                  'id__attr', 'id__timeupdate', 'timeupdate', 'idmanager__name', 'rem',  'id__localid'
        ))
        if data_user_information_initial == []:
            return HttpResponse(dumps({'error_code': 1, 'message': id_error}),  content_type=content_type_tmp, charset='utf-8')
        data_user_information = data_user_information_initial[0]
        field_name = ['id', 'id__nocard', 'id__nouser', 'id__name', 'id__psw', 'id__deptid__name', 'id__sex',
                      'id__attr', 'id__timeupdate', 'timeupdate', 'idmanager__name', 'rem',  'id__localid']
        variable_name = locals()
        args['id__deptid'] = args.get(
            'id__deptid__name', data_user_information['id__deptid'])
        args['idmanager'] = args.get(
            'idmanager__name', data_user_information['idmanager'])
        if isinstance(args['id__deptid__name'], int):
            args['id__deptid'] = args['id__deptid__name']
            args['idmanager'] = args['idmanager__name']
        else:
            return HttpResponse(dumps(
                {'error_code': 1, 'message': '请确保所填的id类数据是数字'}),

                content_type=content_type_tmp,
                charset='utf-8')
        for i in field_name:
            if args[i] == 0:
                variable_name[i] = data_user_information[i]
            else:
                variable_name[i] = args.get(i, data_user_information[i])
        user_id = request.COOKIES.get('user_id')
        user_id = request.session.get(user_id)
        variable_name['idmanager'] = user_id
        try:
            use_tmp = models.TCyuser.objects.filter(id=id_user_information).update(
                nocard=variable_name.get('id__nocard'),
                nouser=variable_name.get('id__nouser'),
                name=variable_name.get('id__name'),
                psw=variable_name.get('id__psw'),
                deptid=variable_name.get('id__deptid'),
                sex=variable_name.get('id__sex'),
                attr=variable_name.get('id__attr'),
                timeupdate=variable_name.get('id__timeupdate'),
                idmanager=variable_name.get('id__idmanager'),
                localid=variable_name.get('id__localid')
            )
            use_tmp_1 = models.TCyuserex.objects.filter(id=id_user_information).update(
                rem=variable_name.get('rem'),
                timeupdate=variable_name.get('timeupdate'),
                idmanager=variable_name.get('idmanager')
            )
            return HttpResponse(dumps({'error_code': 0, 'message': '修改学生信息成功'}),  content_type=content_type_tmp, charset='utf-8')
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
            'error_code': 1,
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
                models.TCyuserex.objects.filter(
                    id=variable_name.get('id_'+str(i), 'id_1')).delete()
                models.TCyuser.objects.filter(
                    id=variable_name.get('id_'+str(i), 'id_1')).delete()
                return HttpResponse(dumps({'error_code': 0, 'message': '数据删除成功'}),  content_type=content_type_tmp, charset='utf-8')
        except Exception as error:
            return HttpResponse(dumps({'error_code': 1, 'message': data_base_error_specific + str(error)}), content_type=content_type_tmp, charset='utf-8')
