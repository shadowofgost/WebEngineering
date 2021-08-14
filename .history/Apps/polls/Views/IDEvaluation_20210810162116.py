from django.shortcuts import render, redirect
from django.http import HttpResponse
from drf_yasg.utils import swagger_auto_schema
from drf_yasg.openapi import Schema, Response, TYPE_INTEGER, TYPE_OBJECT
from rest_framework.views import APIView
from json import dumps
from ..Models.CurriculaModel.Database import CurriculaModel
from ..Models.DepartmentModel.Database import DepartmentModel
from ..Models.EquipmentModel.Database import EquipmentModel
from ..Models.LocationModel.Database import LocationModel, LocationModelex
from ..Models.MmxModel.Database import MmxModel, MmxDataModel
from ..Models.CoursePlanModel.Database import CoursePlanModel
from ..Models.RunningAccountModel.Database import RunningAccountModel
from ..Models.TableInformationModel.Database import TableInformationModel
from ..Models.TyperaModel.Database import TyperaModel
from ..Models.UserModel.Database import UserModel, UserExtensionModel
from .Public import (
    responses_success,
    responses_fail,
    get_request_args,
    post_success,
    content_type_tmp,
    post_error,
)


class IDEvaluation(APIView):
    """
    List:
    Check the id information about user,equipment,course,login user
    """

    IDEvaluation_post_request_body = Schema(
        title="验证id的请求响应",  # 标题
        description="用于验证id是否存在于对应的的数据库中",  # 接口描述
        type=TYPE_OBJECT,  # 类型 "object" ,"string" ,"number" ,"integer" ,"boolean" ,"array" ,"file"
        format=None,  # 格式    date,date-time,password,binary,bytes,float,double,int32,int64,email,ipv4, ipv6, uri, uuid, slug, decimal
        enum=None,  # [列表]列举参数的请求值
        pattern=None,  # 当 format为 string是才填此项
        # 当 type为object时，为dict对象 {'str1': Schema对象, 'str2': SchemaRef对象}
        properties={
            "kind": Schema(
                title=" 选择想要验证的数据库",
                description=" 1 表示验证所有用户是否存在，扩展信息是否存在；2 表示验证验证设备是否存在；3表示验证课程是否存在；4 表示验证考勤记录的id是否存在；5表示验证部门id是否存在；6表示验证地点id是否存在；7表示课程安排id是否存在；8表示媒体信息的id是否存在，9表示搜索typera表中的数据是否存在",
                type=TYPE_INTEGER,
                format="int32",
                enum=[1, 2, 3, 4, 5, 6, 7, 8, 9],
            ),
            "id": Schema(
                title=" id数据",
                description="表示想要验证的id数据",
                type=TYPE_INTEGER,
                format="int32",
            ),
        },
        required=["kind", "id"],  # [必须的属性列表]
        items=None,  # 当type是array时，填此项
    )
    IDEvaluation_post_responses_success = Response(
        description="post请求成功的时候",
        schema=responses_success,
        examples={"error_code": 0, "message": post_success},
    )
    IDEvaluation_post_responses_fail = Response(
        description="post请求失败的时候",
        schema=responses_fail,
        examples={"error_code": 1, "message": post_error},
    )

    @swagger_auto_schema(
        request_body=IDEvaluation_post_request_body,
        manual_parameters=None,
        operation_id=None,
        operation_description="用于验证规定数据库内是否存在需要验证的id",
        operation_summary="Evaluation",
        security=None,
        responses={
            201: IDEvaluation_post_responses_success,
            401: IDEvaluation_post_responses_fail,
        },
        tags=None,
    )
    @get_request_args
    def post(self, request, args, session):
        """
        This method is to varify id information about user,equipment,course,login user.
        """
        id_evaluation = args.get("id", None)
        kind_evaluation = args.get("kind", None)
        data = []
        if not (id_evaluation or kind_evaluation):
            return HttpResponse(
                dumps({"error_code": 1, "message": "请勿空提交"}),
                content_type=content_type_tmp,
                charset="utf-8",
            )
        if kind_evaluation == 1:
            data = list(UserModel.objects.filter(id=id_evaluation).values())
        elif kind_evaluation == 2:
            data = list(EquipmentModel.objects.filter(id=id_evaluation).values())
        elif kind_evaluation == 3:
            data = list(CurriculaModel.objects.filter(id=id_evaluation).values())
        elif kind_evaluation == 4:
            data = list(RunningAccountModel.objects.filter(id=id_evaluation).values())
        elif kind_evaluation == 5:
            data = list(DepartmentModel.objects.filter(id=id_evaluation).values())
        elif kind_evaluation == 6:
            data = list(LocationModel.objects.filter(id=id_evaluation).values())
        elif kind_evaluation == 7:
            data = list(CoursePlanModel.objects.filter(id=id_evaluation).values())
        elif kind_evaluation == 8:
            data = list(MmxModel.objects.filter(id=id_evaluation).values())
        elif kind_evaluation == 9:
            data = list(TyperaModel.objects.filter(id=id_evaluation).values())
        if data == []:
            return HttpResponse(
                dumps({"error_code": 1, "message": "id不存在"}),
                content_type=content_type_tmp,
                charset="utf-8",
            )
        else:
            return HttpResponse(
                dumps({"error_code": 0, "message": "id存在"}),
                content_type=content_type_tmp,
                charset="utf-8",
            )
