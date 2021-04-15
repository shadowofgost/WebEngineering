from django.http import HttpResponse
from drf_yasg.utils import swagger_auto_schema
from drf_yasg.openapi import Schema, Response, TYPE_FILE, TYPE_INTEGER, TYPE_OBJECT, TYPE_STRING
from rest_framework.views import APIView
from json import dumps
from time import time
from .. import models
from .Public import responses_success, responses_fail, get_request_args, content_type_tmp,  patch_error, patch_success, data_base_error
