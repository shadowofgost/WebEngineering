from django.http import HttpResponse
from django.db.models import Q
from drf_yasg.utils import swagger_auto_schema
from drf_yasg.openapi import Schema, Response,  TYPE_INTEGER, TYPE_OBJECT, TYPE_STRING
from json import dumps
from .. import models
from .Public import responses_success, responses_fail, get_request_args, data_page_response, content_type_tmp, post_search, put_success, put_error, post_error, data_base_error_specific, patch_success, patch_error, id_error, delete_schema
from rest_framework.views import APIView


class StudentCourse(APIView):
    pass
