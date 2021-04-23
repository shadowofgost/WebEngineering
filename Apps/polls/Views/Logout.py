from django.http import HttpResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from json import dumps
from .Public import content_type_tmp


class Logout(APIView):
    @swagger_auto_schema(
        operation_description='The api for logout action',)
    def delete(self, request):
        is_login = request.COOKIES.get('is_login')
        if not request.session.get(is_login, None):
            return HttpResponse(dumps({'code': 0}),  content_type=content_type_tmp, charset='utf-8')
        request.session.flush()
        return HttpResponse(dumps({'code': 0}),  content_type=content_type_tmp, charset='utf-8')
