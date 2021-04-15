from django.http import HttpResponse
from drf_yasg.utils import swagger_auto_schema
from drf_yasg.openapi import Schema, Response, TYPE_FILE, TYPE_INTEGER, TYPE_OBJECT, TYPE_STRING
from rest_framework.views import APIView
from json import dumps
from time import time
from .. import models
from .Public import responses_success, responses_fail, get_request_args, content_type_tmp,  patch_error, patch_success, data_base_error
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.conf import settings
import os
class Picture(APIView):
    def post(self, request):
        is_login = request.COOKIES.get('is_login')
        if not request.session.get(is_login, None):
            return HttpResponse(dumps({'code': 0}),  content_type=content_type_tmp, charset='utf-8')
        user_id = request.COOKIES.get('user_id')
        user_id = request.session.get(user_id)
        file = request.FILES.get('pic')
        file =file.read()
        if file == None:
            return HttpResponse(dumps({'error_code': 1, 'message': '请插入图片'}))
        file_back = request.POST.get('file')
        #path = default_storage.save(
            #'E:\Programming\Engineering\Python\Django\WebInSQLServer\WebEn#gine#ering/static/'+file.name, ContentFile(file.read()))
        #tmp_file = os.path.join(settings.STATIC_ROOT,path)
        try:
            models.TCyuserex.objects.filter(id = user_id).update(photo = file)
            return HttpResponse(dumps({'error_code': 0, 'message': '添加数据成功'}),
                         content_type=content_type_tmp, charset='utf-8')
        except:
            return HttpResponse(dumps({'error_code': 1, 'message': data_base_error}), content_type=content_type_tmp, charset='utf-8')
