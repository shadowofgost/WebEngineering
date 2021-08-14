from django.http import HttpResponse
from drf_yasg.utils import swagger_auto_schema
from drf_yasg.openapi import Schema, Response, TYPE_INTEGER, TYPE_OBJECT
from rest_framework.views import APIView
from json import dumps
from .. import models
from .Public import responses_success,responses_fail,get_request_args,content_type_tmp,data_base_error_specific
id_schema = Schema(
    title='信息查询的id号',
    description='数据库表中需要被删除的字段的id号',
    type=TYPE_OBJECT,
    properties={'data_id': Schema(
        title=' id',
        description=' 需要删除的每一个id号 ',
        type=TYPE_INTEGER,
        format='int32',)}
)

delete_schema = {
    'ids': Schema(
        title=' id号',
        description='整个需要被删除的信息的id号排列',
        type=TYPE_OBJECT,
        properties=[id_schema, id_schema]
    )
}
class APIViewDelete(APIView):
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

    @swagger_auto_schema(
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
    @get_request_args
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
            for i in range( numbers_id):
                models.EquipmentModel.objects.filter(
                    id=variable_name.get('id_'+str(i), 'id_1')).delete()
            return HttpResponse(dumps({'message': '数据删除成功'}),  content_type=content_type_tmp, charset='utf-8')
        except Exception as error:
            return HttpResponse(dumps({'message': data_base_error_specific + str(error)}), content_type=content_type_tmp, charset='utf-8')
