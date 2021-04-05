from django.http import HttpResponse
from django.db.models import Q
from drf_yasg.utils import swagger_auto_schema
from drf_yasg.openapi import Schema, Response,  TYPE_INTEGER, TYPE_OBJECT, TYPE_STRING
from json import dumps
from .. import models
from copy import deepcopy
from .Public import responses_success, responses_fail, get_request_args, data_total_response, content_type_tmp, post_search, put_success, put_error, post_error, data_base_error_specific, patch_error, id_error, no_idea, delete_schema
from .APIViewDelete import APIViewDelete
from rest_framework.views import APIView


class EquipmentInformation(APIView):
    '''
    list
    list all information about Equipment
    '''
    data_schema = {
        'id': Schema(
            title='设备的id',
            description='设备的id',
            type=TYPE_INTEGER,
            format='int32',
            enum=None,
        ),
        'name': Schema(
            title='设备名称',
            description='设备名称',
            type=TYPE_STRING,
            format='string',
            enum=None,
        ),
        'id_location__name': Schema(
            title='设备所在地点的名称',
            description='设备所在地点的名称',
            type=TYPE_STRING,
            format='string',
            enum=None,
        ),
        'id_location_sn': Schema(
            title='设备所在位置内部的编号',
            description='设备所在位置的内部编号',
            type=TYPE_INTEGER,
            format='int32',
            enum=None,
        ),
        'id_ip': Schema(
            title='设备的ip地址',
            description='设备所有的IP地址，例如192.168.0.222',
            type=TYPE_STRING,
            format='string',
            enum=None,
        ),
        'mac': Schema(
            title='设备的mac地址  ',
            description='设备的mac地址，例如xx-xx-xx-xx-xx-xx',
            type=TYPE_STRING,
            format='string',
            enum=None,
        ),
        'state': Schema(
            title=' 设备状态 ',
            description='设备状态，0：正常空闲、1：故障、2：其它、3：正常使用中、4开放，必须有值',
            type=TYPE_INTEGER,
            format='int32',
            enum=[0, 1, 2, 3, 4],
        ),
        'login': Schema(
            title='登录状态',
            description='登录状态，0：未登录、1：已经登录',
            type=TYPE_INTEGER,
            format='int32',
            enum=[0, 1],
        ),
        'link': Schema(
            title=' 设备网络连接状态 ',
            description=' 网络状态，0：脱机、1：在线，必须有值 ',
            type=TYPE_INTEGER,
            format='int32',
            enum=[0, 1],
        ),
        'class_field': Schema(
            title=' 设备种类 ',
            description=' 设备种类，0：PC设备、1：刷卡设备，必须有值',
            type=TYPE_STRING,
            format='string',
            enum=[0, 1],
        ),
        'dx': Schema(
            title='设备的像素x位置信息',
            description=' Layout显示坐标位置x（单位像素），必须有值 ',
            type=TYPE_INTEGER,
            format='int32',
            enum=None,
        ),
        'dy': Schema(
            title=' 设备的像素y位置信息 ',
            description=' Layout显示坐标位置y（单位像素），必须有值 ',
            type=TYPE_INTEGER,
            format='int32',
            enum=None,
        ),
        'id_user__name': Schema(
            title=' 使用者的姓名 ',
            description=' 使用者的姓名 ',
            type=TYPE_STRING,
            format='string',
            enum=None,
        ),
        'id_plan': Schema(
            title=' 设备所关联的课程安排表id',
            description=' 设备所关联的课程安排表id  ',
            type=TYPE_INTEGER,
            format='int32',
            enum=None,
        ),
        'itimebegin': Schema(
            title=no_idea,
            description=no_idea,
            type=TYPE_INTEGER,
            format='int32',
            enum=None,
        ),
        'itimelogin': Schema(
            title=no_idea,
            description=no_idea,
            type=TYPE_INTEGER,
            format='int32',
            enum=None,
        ),
        'whitelist': Schema(
            title=no_idea,
            description=no_idea,
            type=TYPE_STRING,
            format='string',
            enum=None,
        ),
        'rem': Schema(
            title=' 设备说明 ',
            description='设备说明',
            type=TYPE_STRING,
            format='string',
            enum=None,
        ),
        'timeupdate': Schema(
            title=' 更新时间 ',
            description=' 记录最后更新时间；（2000-1-1 0:0:0 经过的秒），必须有值 ',
            type=TYPE_INTEGER,
            format='int32',
            enum=None,
        ),
        'idmanager__name': Schema(
            title=' 最后修改信息的管理员 ',
            description=' 最后修改信息的管理员的姓名 ',
            type=TYPE_STRING,
            format='string',
            enum=None,
        ),
        'portlisten': Schema(
            title=' 数据端口 ',
            description=' 接收数据端口,默认:1234，必须有值',
            type=TYPE_INTEGER,
            format='int32',
            enum=None,
        ),
        'type_field': Schema(
            title=' 刷卡器类型,默认:31，必须有值 ',
            description=' 刷卡器类型,默认:31，必须有值 ',
            type=TYPE_INTEGER,
            format='int32',
            enum=None,
        ),
        'timedelay': Schema(
            title=' 开门延迟时间 ',
            description=' 门禁开门延时,默认:5秒，必须有值  ',
            type=TYPE_INTEGER,
            format='int32',
            enum=None,
        ),
        'keycancel': Schema(
            title=' 取消键键码,11，必须有值 ',
            description=' 取消键键码,11，必须有值',
            type=TYPE_INTEGER,
            format='int32',
            enum=None,
        ),
        'keyOk': Schema(
            title=' 确定键键码,14，必须有值 ',
            description=' 确定键键码,14，必须有值',
            type=TYPE_INTEGER,
            format='int32',
            enum=None,
        ),
        'keydel': Schema(
            title=' 删除键键码,13，必须有值 ',
            description=' 删除键键码,13，必须有值',
            type=TYPE_INTEGER,
            format='int32',
            enum=None,
        ),
        'keyf1': Schema(
            title=' 功能键键码,12，必须有值 ',
            description=' 功能键键码,12，必须有值',
            type=TYPE_INTEGER,
            format='int32',
            enum=None,
        ),
        'onall': Schema(
            title=' 门禁刷卡总是开门,默认:1总是开门、1校验成功后开门，必须有值 ',
            description=' 门禁刷卡总是开门,默认:1总是开门、1校验成功后开门，必须有值',
            type=TYPE_INTEGER,
            format='int32',
            enum=None,
        ),
        'rangeequs': Schema(
            title=' 管理设备范围，必须有值 ',
            description=' 管理设备范围，必须有值 ',
            type=TYPE_STRING,
            format='string',
            enum=None,
        ),
        'listplaces': Schema(
            title=' 管理地点范围，必须有值 ',
            description='管理地点范围，必须有值 ',
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
            'data': Schema(
                title='数据',
                description='用于传递查询到的全部数据',
                type=TYPE_OBJECT,
                properties=[data_schema_present, data_schema_present]
            ),
        }
    )
    EquipmentInformation_get_responses_success = Response(
        description='查询成功返回的响应',
        schema=get_responses_success,
        examples=None,
    )
    EquipmentInformation_get_responses_fail = Response(
        description='查询失败返回的响应',
        schema=responses_fail,
        examples={
            'message': patch_error
        }
    )

    @swagger_auto_schema(
        request_body=None,
        manual_parameters=None,
        operation_id=None,
        operation_description='获取设备的信息的端口',
        operation_summary=None,
        security=None,
        responses={
            200: EquipmentInformation_get_responses_success,
            401: EquipmentInformation_get_responses_fail
        },
        tags=None)
    @get_request_args
    def get(self, request, args, session):
        is_login = request.COOKIES.get('is_login')
        if not request.session.get(is_login, None):
            return HttpResponse(dumps({'code': 0}),  content_type=content_type_tmp, charset='utf-8')
        pages = args.get('page', 1)
        limits = args.get('limits', 20)
        data_equipment = models.TCyequipment.objects.all().values(
            'id', 'name', 'id_location__name', 'id_location_sn', 'id_ip', 'mac', 'state', 'login', 'link', 'class_field', 'dx', 'dy', 'id_user__name', 'id_plan', 'itimebegin', 'itimelogin', 'whitelist', 'rem', 'timeupdate', 'idmanager__name', 'portlisten', 'type_field', 'timedelay', 'keycancel', 'keyOk', 'keydel', 'keyf1', 'onall', 'rangeequs', 'listplaces'
        )
        return data_total_response(data_equipment, pages, limits)

    '''
    list
    list all information about Equipment
    '''
    EquipmentInformation_post_request_body = Schema(
        title=' 查询设备信息 ',  # 标题
        description=' 获取设备信息需要的数据 ',  # 接口描述
        type=TYPE_OBJECT,  # 类型 "object" ,"string" ,"number" ,"integer" ,"boolean" ,"array" ,"file"
        format=None,  # 格式    date,date-time,password,binary,bytes,float,double,int32,int64,email,ipv4, ipv6, uri, uuid, slug, decimal
        enum=None,  # [列表]列举参数的请求值
        pattern=None,  # 当 format为 string是才填此项
        # 当 type为object时，为dict对象 {'str1': Schema对象, 'str2': SchemaRef对象}
        properties=post_search,
        required=['input_string'],  # [必须的属性列表]
        items=None,  # 当type是array时，填此项
    )
    EquipmentInformation_post_responses_success = Response(
        description='查询设备信息查询成功',
        schema=get_responses_success,
    )
    EquipmentInformation_post_responses_fail = Response(
        description='查询设备信息查询失败',
        schema=responses_fail,
        examples={
            'message': post_error
        }
    )

    @swagger_auto_schema(
        request_body=EquipmentInformation_post_request_body,
        manual_parameters=None,
        operation_id=None,
        operation_description='这个端口用于查询设备信息数据',
        operation_summary=None,
        security=None,
        responses={
            201: EquipmentInformation_post_responses_success,
            400: EquipmentInformation_post_responses_fail
        },
        tags=None)
    @get_request_args
    def post(self, request, args, session):
        is_login = request.COOKIES.get('is_login')
        if not request.session.get(is_login, None):
            return HttpResponse(dumps({'code': 0}),  content_type=content_type_tmp, charset='utf-8')
        input_string = args.get('input_string', None)
        pages = args.get('page', 1)
        limits = args.get('limits', 20)
        if input_string == None:
            data_equipment = models.TCyequipment.objects.all().values(
                'id', 'name', 'id_location__name', 'id_location_sn', 'id_ip', 'mac', 'state', 'login', 'link', 'class_field', 'dx', 'dy', 'id_user__name', 'id_plan', 'itimebegin', 'itimelogin', 'whitelist', 'rem', 'timeupdate', 'idmanager__name', 'portlisten', 'type_field', 'timedelay', 'keycancel', 'keyOk', 'keydel', 'keyf1', 'onall', 'rangeequs', 'listplaces')
        else:
            input_string = input_string.strip()
            try:
                test_input = eval(input_string)
            except:
                test_input = input_string
            if isinstance(test_input, int):
                data_equipment = models.TCyequipment.objects.filter(
                    Q(id=test_input) |
                    Q(id_location_sn=test_input) |
                    Q(id_location=test_input) |
                    Q(id_user=test_input) |
                    Q(idmanager=test_input) |
                    Q(id_ip__icontains=str(test_input)) |
                    Q(mac__icontains=str(test_input)) |
                    Q(state=test_input) |
                    Q(login=test_input) |
                    Q(link=test_input) |
                    Q(class_field=test_input) |
                    Q(dx=test_input) |
                    Q(dy=test_input) |
                    Q(id_plan=test_input) |
                    Q(itimebegin=test_input) |
                    Q(itimelogin=test_input) |
                    Q(timeupdate=test_input) |
                    Q(portlisten=test_input) |
                    Q(type_field=test_input) |
                    Q(timedelay=test_input) |
                    Q(keycancel=test_input) |
                    Q(keyOk=test_input) |
                    Q(keydel=test_input) |
                    Q(keyf1=test_input) |
                    Q(onall=test_input)
                ).values('id', 'name', 'id_location__name', 'id_location_sn', 'id_ip', 'mac', 'state', 'login', 'link', 'class_field', 'dx', 'dy', 'id_user__name', 'id_plan', 'itimebegin', 'itimelogin', 'whitelist', 'rem', 'timeupdate', 'idmanager__name', 'portlisten', 'type_field', 'timedelay', 'keycancel', 'keyOk', 'keydel', 'keyf1', 'onall', 'rangeequs', 'listplaces').distinct()
            else:
                data_equipment = models.TCyequipment.objects.filter(
                    Q(name__icontains=input_string) |
                    Q(whitelist__icontains=input_string) |
                    Q(id_location__name__icontains=input_string) |
                    Q(id_user__name__icontains=input_string) |
                    Q(idmanager__name__icontains=input_string) |
                    Q(rem__icontains=input_string) |
                    Q(rangeequs__icontains=input_string) |
                    Q(listplaces__icontains=input_string)
                ).values('id', 'name', 'id_location__name', 'id_location_sn', 'id_ip', 'mac', 'state', 'login', 'link', 'class_field', 'dx', 'dy', 'id_user__name', 'id_plan', 'itimebegin', 'itimelogin', 'whitelist', 'rem', 'timeupdate', 'idmanager__name', 'portlisten', 'type_field', 'timedelay', 'keycancel', 'keyOk', 'keydel', 'keyf1', 'onall', 'rangeequs', 'listplaces').distinct()
        return data_total_response(data_equipment, pages, limits)

    '''
    list
    list all information about Equipment
    '''
    EquipmentInformation_put_request_body = Schema(
        title=' put请求向前端请求添加数据的数据 ',  # 标题
        description='向数据库内部添加数据',  # 接口描述
        type=TYPE_OBJECT,  # 类型 "object" ,"string" ,"number" ,"integer" ,"boolean" ,"array" ,"file"
        format=None,  # 格式    date,date-time,password,binary,bytes,float,double,int32,int64,email,ipv4, ipv6, uri, uuid, slug, decimal
        enum=None,  # [列表]列举参数的请求值
        pattern=None,  # 当 format为 string是才填此项
        # 当 type为object时，为dict对象 {'str1': Schema对象, 'str2': SchemaRef对象}
        properties=data_schema,
        required=['id', 'name', 'id_location__name', 'id_location_sn',
                  'id_ip', 'mac', 'dx', 'dy', 'id_user__name', 'id_plan',   'timeupdate', 'idmanager__name'],  # [必须的属性列表]
        items=None,  # 当type是array时，填此项
    )
    EquipmentInformation_put_responses_success = Response(
        description='向数据库内增加设备信息成功的响应',
        schema=responses_success,
        examples={
            'message': put_success
        }
    )
    EquipmentInformation_put_responses_fail = Response(
        description='向数据库内增加设备信息失败的响应',
        schema=responses_fail,
        examples={
            'message': put_error
        }
    )

    @swagger_auto_schema(
        request_body=EquipmentInformation_put_request_body,
        manual_parameters=None,
        operation_id=None,
        operation_description='向数据库内部添加设备信息',
        operation_summary=None,
        security=None,
        responses={
            201: EquipmentInformation_put_responses_success,
            400: EquipmentInformation_put_responses_fail
        },
        tags=None)
    @get_request_args
    def put(self, request, args, session):
        '''
        This method is to use to add equipment information
        '''
        field_name = ['id', 'name', 'id_location__name',                          'id_location_sn',
                      'id_ip', 'mac', 'state', 'login', 'link', 'class_field', 'dx', 'dy', 'id_user__name', 'id_plan', 'itimebegin', 'whitelist', 'rem', 'timeupdate', 'idmanager__name', 'portlisten', 'type_field', 'timedelay', 'keycancel', 'keyOk', 'keydel', 'keyf1', 'onall', 'rangeequs', 'listplaces']
        is_login = request.COOKIES.get('is_login')
        if not request.session.get(is_login, None):
            return HttpResponse(dumps({'code': 0}),  content_type=content_type_tmp, charset='utf-8')
        variable_name = locals()
        for i in field_name:
            variable_name[i] = args.get(i, 0)
        user_id = request.COOKIES.get('user_id')
        user_id = request.session.get(user_id)
        variable_name['idmanager'] = user_id
        variable_name['id_location'] = variable_name['id_location__name']
        variable_name['id_user'] = variable_name['id_user__name']
        if isinstance(variable_name['id_location__name'], int) and isinstance(variable_name['id_user__name'], int):
            variable_name['id_location'] = variable_name['id_location__name']
            variable_name['id_user'] = variable_name['id_user__name']
        else:
            return HttpResponse(dumps(
                {'message': '请确保所填的id类数据是数字'}),

                content_type=content_type_tmp,
                charset='utf-8')
        # 批量命名变量
        try:
            location_object = models.TCylocation.objects.get(
                id=variable_name.get('id_location'))
            user_object = models.TCyuser.objects.get(
                id=variable_name.get('id_user'))
            plan_object = models.TCyplan.objects.get(
                id=variable_name.get('id_plan'))
            idmanager_object = models.TCyuser.objects.get(
                id=variable_name.get('idmanager'))
            ueses_tmp = models.TCyequipment.objects.create(
                id=variable_name.get('id'),
                name=variable_name.get('name'),
                id_location=location_object,
                id_location_sn=variable_name.get('id_location_sn'),
                id_ip=variable_name.get('id_ip'),
                mac=variable_name.get('mac'),
                state=variable_name.get('state'),
                login=variable_name.get('login'),
                link=variable_name.get('link'),
                class_field=variable_name.get('class_field'),
                dx=variable_name.get('dx'),
                dy=variable_name.get('dy'),
                id_user=user_object,
                id_plan=plan_object,
                itimebegin=variable_name.get('itimebegin'),
                whitelist=variable_name.get('whitelist'),
                rem=variable_name.get('rem'),
                timeupdate=variable_name.get('timeupdate'),
                idmanager=idmanager_object,
                portlisten=variable_name.get('portlisten'),
                type_field=variable_name.get('type_field'),
                timedelay=variable_name.get('timedelay'),
                keycancel=variable_name.get('keycancel'),
                keyOk=variable_name.get('keyOk'),
                keydel=variable_name.get('keydel'),
                keyf1=variable_name.get('keyf1'),
                onall=variable_name.get('onall'),
                rangeequs=variable_name.get('rangeequs'),
                listplaces=variable_name.get('listplaces')
            )
            return HttpResponse(dumps({'message': put_success}), content_type=content_type_tmp, charset='utf-8')
        except Exception as error:
            return HttpResponse(dumps({'message': data_base_error_specific+str(error)}),  content_type=content_type_tmp, charset='utf-8')
    '''
    list
    list all information about Equipment
    '''
    EquipmentInformation_patch_request_body = Schema(
        title=' 请求修改设备信息 ',  # 标题
        description=' 修改数据库中的设备信息 ',  # 接口描述
        type=TYPE_OBJECT,  # 类型 "object" ,"string" ,"number" ,"integer" ,"boolean" ,"array" ,"file"
        format=None,  # 格式    date,date-time,password,binary,bytes,float,double,int32,int64,email,ipv4, ipv6, uri, uuid, slug, decimal
        enum=None,  # [列表]列举参数的请求值
        pattern=None,  # 当 format为 string是才填此项
        # 当 type为object时，为dict对象 {'str1': Schema对象, 'str2': SchemaRef对象}
        properties=data_schema,
        required=['id'],  # [必须的属性列表]
        items=None,  # 当type是array时，填此项
    )
    EquipmentInformation_patch_responses_success = Response(
        description='修改设备信息成功的响应',
        schema=responses_success,
        examples={
            'message': '修改成功'
        }
    )
    EquipmentInformation_patch_responses_fail = Response(
        description='修改设备信息成功的响应',
        schema=responses_fail,
        examples={
            'message': patch_error
        }
    )

    @swagger_auto_schema(
        request_body=EquipmentInformation_patch_request_body,
        manual_parameters=None,
        operation_id=None,
        operation_description='用于修改设备信息的api接口 ',
        operation_summary=None,
        security=None,
        responses={
            201: EquipmentInformation_patch_responses_success,
            400: EquipmentInformation_patch_responses_fail
        },
        tags=None)
    @get_request_args
    def patch(self, request, args, session):
        is_login = request.COOKIES.get('is_login')
        if not request.session.get(is_login, None):
            return HttpResponse(dumps({'code': 0}),  content_type=content_type_tmp, charset='utf-8')
        id_equipment = args.get('id')
        data_equipment_initial = list(
            models.TCyequipment.objects.filter(id=id_equipment).values('id', 'name', 'id_location', 'id_location_sn',    'id_ip', 'mac', 'state', 'login', 'link', 'class_field', 'dx', 'dy', 'id_user', 'id_plan', 'itimebegin', 'whitelist', 'rem', 'timeupdate', 'idmanager', 'portlisten', 'type_field', 'timedelay', 'keycancel', 'keyOk', 'keydel', 'keyf1', 'onall', 'rangeequs', 'listplaces'))
        if data_equipment_initial == []:
            return HttpResponse(dumps({'message': id_error}), content_type=content_type_tmp, charset='utf-8')
        data_equipment = data_equipment_initial[0]
        field_name = ['id', 'name', 'id_location', 'id_location_sn',
                      'id_ip', 'mac', 'state', 'login', 'link', 'class_field', 'dx', 'dy', 'id_user', 'id_plan', 'itimebegin', 'whitelist', 'rem', 'timeupdate', 'idmanager', 'portlisten', 'type_field', 'timedelay', 'keycancel', 'keyOk', 'keydel', 'keyf1', 'onall', 'rangeequs', 'listplaces']
        args['id_location'] = args.get(
            'id_location__name', data_equipment['id_location'])
        args['id_user'] = args.get(
            'id_user__name', data_equipment['id_user'])
        args['idmanager'] = args.get(
            'idmanager__name', data_equipment['idmanager'])
        if isinstance(args['id_location__name'], int) and isinstance(args['id_user__name'], int):
            args['id_location'] = args['id_location__name']
            args['id_user'] = args['id_user__name']
            args['idmanager'] = args['idmanager__name']
        else:
            return HttpResponse(dumps(
                {'message': '请确保所填的id类数据是数字'}),
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
            models.TCyequipment.objects.filter(id=id_equipment).update(
                name=variable_name.get('name'),
                id_location=variable_name.get('id_location'),
                id_location_sn=variable_name.get('id_location_sn'),
                id_ip=variable_name.get('id_ip'),
                mac=variable_name.get('mac'),
                state=variable_name.get('state'),
                login=variable_name.get('login'),
                link=variable_name.get('link'),
                class_field=variable_name.get('class_field'),
                dx=variable_name.get('dx'),
                dy=variable_name.get('dy'),
                id_user=variable_name.get('id_user'),
                id_plan=variable_name.get('id_plan'),
                itimebegin=variable_name.get('itimebegin'),
                whitelist=variable_name.get('whitelist'),
                rem=variable_name.get('rem'),
                timeupdate=variable_name.get('timeupdate'),
                idmanager=variable_name.get('idmanager'),
                portlisten=variable_name.get('portlisten'),
                type_field=variable_name.get('type_field'),
                timedelay=variable_name.get('timedelay'),
                keycancel=variable_name.get('keycancel'),
                keyOk=variable_name.get('keyOk'),
                keydel=variable_name.get('keydel'),
                keyf1=variable_name.get('keyf1'),
                onall=variable_name.get('onall'),
                rangeequs=variable_name.get('rangeequs'),
                listplaces=variable_name.get('listplaces')
            )
            return HttpResponse(dumps({'message': '修改设备信息成功'}),  content_type=content_type_tmp, charset='utf-8')
        except Exception as error:
            return HttpResponse(dumps({'message': data_base_error_specific+str(error)}),  content_type=content_type_tmp, charset='utf-8')
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
            'message': '删除成功'
        }
    )
    APIView_delete_responses_fail = Response(
        description='APIView_delete_responses is failure',
        schema=responses_fail,
        examples={
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
                models.TCyequipment.objects.filter(
                    id=variable_name.get('id_'+str(i), 'id_1')).delete()
                return HttpResponse(dumps({'message': '数据删除成功'}),  content_type=content_type_tmp, charset='utf-8')
        except Exception as error:
            return HttpResponse(dumps({'message': data_base_error_specific + str(error)}), content_type=content_type_tmp, charset='utf-8')
