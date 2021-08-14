from django.http import HttpResponse
from drf_yasg.utils import swagger_auto_schema
from drf_yasg.openapi import IN_FORM, Parameter, Response, TYPE_FILE, IN_QUERY
from rest_framework.views import APIView
from json import dumps
from ..Models.UserModel.Database import UserExtensionModel
from .Public import responses_success, responses_fail, get_request_args, content_type_tmp,  patch_error, patch_success, data_base_error
from django.core.files.storage import default_storage
from django.conf import settings


class Picture(APIView):
    post_parammeter = Parameter(
        name='图片',
        in_=IN_QUERY,
        description='传输每个人的图片',
        required=True,
        type=TYPE_FILE,
    )
    post_responses_success = Response(
        description='上传信息成功的响应',
        schema=responses_success,
        examples={
            'error_code': 0,
            'message': '上传图片成功'
        },
    )
    post_responses_fail = Response(
        description='上传图片失败的响应',
        schema=responses_fail,
        examples={
            'error_code': 1,
            'message': '上传图片失败'
        }
    )

    @swagger_auto_schema(
        request_body=None,
        manual_parameters=[post_parammeter],
        operation_id=None,
        operation_description='这个端口用于上传用户照片',
        operation_summary=None,
        security=None,
        responses={
            200: post_responses_success,
            401: post_responses_fail
        },
        tags=None)
    @get_request_args
    def post(self, request):
        is_login = request.COOKIES.get('is_login')
        if not request.session.get(is_login, None):
            return HttpResponse(dumps({'code': 0}),  content_type=content_type_tmp, charset='utf-8')
        user_id = request.COOKIES.get('user_id')
        user_id = request.session.get(user_id)
        file = request.FILES.get('pic')
        file = file.read()
        if file == None:
            return HttpResponse(dumps({'error_code': 1, 'message': '请插入图片'}))
        file_back = request.POST.get('file')
        # path = default_storage.save(
        # 'E:\Programming\Engineering\Python\Django\WebInSQLServer\WebEn#gine#ering/static/'+file.name, ContentFile(file.read()))
        #tmp_file = os.path.join(settings.STATIC_ROOT,path)
        try:
            UserExtensionModel.objects.filter(id=user_id).update(photo=file)
            return HttpResponse(dumps({'error_code': 0, 'message': '添加数据成功'}),
                                content_type=content_type_tmp, charset='utf-8')
        except:
            return HttpResponse(dumps({'error_code': 1, 'message': data_base_error}), content_type=content_type_tmp, charset='utf-8')
