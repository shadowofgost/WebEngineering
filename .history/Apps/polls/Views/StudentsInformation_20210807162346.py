from django.http import HttpResponse
from django.db.models import Q
from drf_yasg.utils import swagger_auto_schema
from drf_yasg.openapi import Parameter, Schema, Response,  TYPE_INTEGER, TYPE_OBJECT, TYPE_STRING, IN_QUERY
from ..Models.UserModel.Database import UserModel,UserExtensionModel
from ..Models.DepartmentModel.Database import DepartmentModel
from json import dumps
from .Public import responses_success, responses_fail, get_request_args, data_page_response, content_type_tmp,  patch_error, patch_success, post_search, post_error, put_error, put_success, id_error, data_base_error_specific, delete_schema
from rest_framework.views import APIView


class StudentsInformation(APIView):
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
    StudentsInformation_get_responses_success = Response(
        description='学生个人信息查询成功的响应',
        schema=get_responses_success,
        examples=None
    )
    StudentsInformation_get_responses_fail = Response(
        description='学生个人信息查询失败的响应',
        schema=responses_fail,
        examples={
            'error_code': 1,
            'message': patch_error})
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
    def get(self, request, args, session):
        is_login = request.COOKIES.get('is_login')
        if not request.session.get(is_login, None):
            return HttpResponse(dumps({'code': 0}),  content_type=content_type_tmp, charset='utf-8')
        pages = int(args.get('page', 1))
        limits = int(args.get('limits', 20))
        data_user = UserModel.objects.filter(attr=4).values('id', 'nocard', 'nouser', 'name', 'psw', 'deptid__name', 'sex', 'attr', 'timeupdate', 'userex_related_to_user_information__rem',
                                                                 'localid', 'userex_related_to_user_information__timeupdate', 'userex_related_to_user_information__idmanager__name').distinct().order_by('id')
        return data_page_response(data_user, pages, limits)

    '''
    list
    list all information about Equipment
    '''
    StudentsInformation_post_request_body = Schema(
        title='查询所有学生信息所需要的数据 ',  # 标题
        description=' 这是用查询学生信息数据所需要的基础信息 ',  # 接口描述
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
        description='查询所有个人学生信息成功的响应',
        schema=get_responses_success,
        examples=None,
    )
    StudentsInformation_post_responses_fail = Response(
        description='查询所有学生个人信息失败的响应',
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
        operation_description='这个端口用于查询所有学生的信息',
        operation_summary=None,
        security=None,
        responses={
            201: StudentsInformation_post_responses_success,
            400: StudentsInformation_post_responses_fail
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
            data_user_information = UserModel.objects.filter(attr=4).values('id', 'nocard', 'nouser', 'name', 'psw', 'deptid__name', 'sex', 'attr', 'timeupdate', 'userex_related_to_user_information__rem',
                                                                                 'localid', 'userex_related_to_user_information__timeupdate', 'userex_related_to_user_information__idmanager__name').distinct().order_by('id')
            return data_page_response(data_user_information, pages, limits)
        else:
            input_string = input_string.strip()
            try:
                test_input = eval(input_string)
            except:
                test_input = input_string
            if isinstance(test_input, int):
                data_user_information = UserModel.objects.filter(
                    Q(id=test_input) |
                    Q(nocard__icontains=str(test_input)) |
                    Q(nouser__icontains=str(test_input)) |
                    Q(deptid=test_input) |
                    Q(sex=test_input) |
                    Q(attr=test_input) |
                    Q(timeupdate=test_input), attr=4
                ).values('id', 'nocard', 'nouser', 'name', 'psw', 'deptid__name', 'sex', 'attr', 'timeupdate', 'userex_related_to_user_information__rem', 'localid', 'userex_related_to_user_information__timeupdate', 'userex_related_to_user_information__idmanager__name').distinct().order_by('id')
            else:
                data_user_information = UserModel.objects.filter(
                    Q(name__icontains=test_input) |
                    Q(psw__icontains=test_input) |
                    Q(deptid__name__icontains=test_input) |
                    Q(userex_related_to_user_information__rem=test_input), attr=4
                ).values('id', 'nocard', 'nouser', 'name', 'psw', 'deptid__name', 'sex', 'attr', 'timeupdate', 'userex_related_to_user_information__rem', 'localid', 'userex_related_to_user_information__timeupdate', 'userex_related_to_user_information__idmanager__name').distinct().order_by('id')
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
    def put(self, request, args, session):
        is_login = request.COOKIES.get('is_login')
        if not request.session.get(is_login, None):
            return HttpResponse(dumps({'code': 0}),  content_type=content_type_tmp, charset='utf-8')
        field_name = ['id', 'nocard', 'nouser', 'name', 'psw', 'deptid__name', 'sex', 'attr', 'timeupdate',
                      'localid', 'userex_related_to_user_information__timeupdate', 'userex_related_to_user_information__idmanager__name']
        variable_name = locals()
        for i in field_name:
            variable_name[i] = args.get(i, 0)
        user_id = request.COOKIES.get('user_id')
        user_id = request.session.get(user_id)
        variable_name['timeupdate'] = int(variable_name['timeupdate'])
        variable_name['idmanager'] = user_id
        variable_name['deptid'] = variable_name['deptid__name']
        if isinstance(variable_name['deptid'], int):
            variable_name['deptid'] = variable_name['deptid__name']
        else:
            return HttpResponse(dumps(
                {'error_code': 1, 'message': '请确保所填的id类数据是数字'}),         content_type=content_type_tmp, charset='utf-8')
        try:
            deptid_object = DepartmentModel.objects.get(
                id=variable_name.get('deptid'))
            use_tmp = UserModel.objects.create(
                id=variable_name.get('id'),
                nocard=variable_name.get('nocard'),
                nouser=variable_name.get('nouser'),
                name=variable_name.get('name'),
                psw=variable_name.get('psw'),
                deptid=deptid_object,
                sex=variable_name.get('sex'),
                attr=variable_name.get('attr'),
                timeupdate=variable_name.get('timeupdate'),
                idmanager=variable_name.get('idmanager'),
                localid=variable_name.get('localid')
            )
            idmanager_object = UserModel.objects.get(
                id=variable_name.get('idmanager'))
            user_id_object = UserModel.objects.get(
                id=variable_name.get('id'))
            use_tmp_1 = UserExtensionModel.objects.create(
                id=user_id_object,
                rem=variable_name.get(
                    'userex_related_to_user_information__rem'),
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
            'error_code': 0,
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
    def patch(self, request, args, session):
        is_login = request.COOKIES.get('is_login')
        if not request.session.get(is_login, None):
            return HttpResponse(dumps({'code': 0}),  content_type=content_type_tmp, charset='utf-8')
        id_user_information = args.get('id')
        data_user_information_initial = list(UserModel.objects.filter(id=id_user_information).values(
            'id', 'nocard', 'nouser', 'name', 'psw', 'deptid', 'sex', 'attr', 'timeupdate', 'userex_related_to_user_information__rem',
            'localid', 'userex_related_to_user_information__timeupdate', 'userex_related_to_user_information__idmanager', 'idmanager'
        ))
        if data_user_information_initial == []:
            return HttpResponse(dumps({'error_code': 1, 'message': id_error}),  content_type=content_type_tmp, charset='utf-8')
        data_user_information = data_user_information_initial[0]
        field_name = ['id', 'nocard', 'nouser', 'name', 'psw', 'deptid__name', 'sex', 'attr', 'timeupdate', 'userex_related_to_user_information__rem',
                      'localid', 'idmanager__name', 'userex_related_to_user_information__timeupdate', 'userex_related_to_user_information__idmanager__name']
        variable_name = locals()
        args['deptid'] = args.get(
            'deptid__name', data_user_information['deptid'])
        args['idmanager'] = args.get(
            'idmanager__name', data_user_information['idmanager'])
        if isinstance(args['deptid__name'], int):
            args['deptid'] = args['deptid__name']
            args['userex_related_to_user_information__idmanager'] = args['userex_related_to_user_information__idmanager__name']
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
            use_tmp = UserModel.objects.get(id=variable_name["id"]).update(
                nocard=variable_name.get('nocard'),
                nouser=variable_name.get('nouser'),
                name=variable_name.get('name'),
                psw=variable_name.get('psw'),
                deptid=variable_name.get('deptid'),
                sex=variable_name.get('sex'),
                attr=variable_name.get('id'),
                timeupdate=variable_name.get('timeupdate'),
                idmanager=variable_name.get('idmanager'),
                localid=variable_name.get('localid')
            )
            tmp = list(UserExtensionModel.objects.filter(id=id).values())
            if tmp == []:
                try:
                    deptid_object = DepartmentModel.objects.get(
                        id=variable_name.get('deptid'))
                    use_tmp = UserModel.objects.create(
                        id=variable_name.get('id'),
                        nocard=variable_name.get('nocard'),
                        nouser=variable_name.get('nouser'),
                        name=variable_name.get('name'),
                        psw=variable_name.get('psw'),
                        deptid=deptid_object,
                        sex=variable_name.get('sex'),
                        attr=variable_name.get('attr'),
                        timeupdate=variable_name.get('timeupdate'),
                        idmanager=variable_name.get('idmanager'),
                        localid=variable_name.get('localid')
                    )
                    idmanager_object = UserModel.objects.get(
                        id=variable_name.get('idmanager'))
                    user_id_object = UserModel.objects.get(
                        id=variable_name.get('id'))
                    use_tmp_1 = UserExtensionModel.objects.create(
                        id=user_id_object,
                        rem=variable_name.get(
                            'userex_related_to_user_information__rem'),
                        timeupdate=variable_name.get('timeupdate'),
                        idmanager=idmanager_object
                    )
                    return HttpResponse(dumps({'error_code': 0, 'message': put_success}), content_type=content_type_tmp, charset='utf-8')
                except Exception as error:
                    return HttpResponse(dumps({'error_code': 1, 'message': data_base_error_specific+str(error)}),  content_type=content_type_tmp, charset='utf-8')
            use_tmp_1 = UserExtensionModel.objects.filter(id=variable_name["id"]).update(
                rem=variable_name.get(
                    'userex_related_to_user_information__rem'),
                timeupdate=variable_name.get(
                    'userex_related_to_user_information__timeupdate'),
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
                UserExtensionModel.objects.filter(
                    id=variable_name.get('id_'+str(i), 'id_1')).delete()
                UserModel.objects.filter(
                    id=variable_name.get('id_'+str(i), 'id_1')).delete()
                return HttpResponse(dumps({'error_code': 0, 'message': '数据删除成功'}),  content_type=content_type_tmp, charset='utf-8')
        except Exception as error:
            return HttpResponse(dumps({'error_code': 1, 'message': data_base_error_specific + str(error)}), content_type=content_type_tmp, charset='utf-8')
