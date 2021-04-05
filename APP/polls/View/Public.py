from django.http import HttpResponse
from drf_yasg.openapi import Parameter, Schema, Response,  TYPE_INTEGER, TYPE_OBJECT, TYPE_STRING
from json import dumps, loads
from .. import models
from django.core.paginator import Paginator, EmptyPage
tmp = 'polls/Login/'
content_type_tmp = 'application/json'
data_base_error = '数据库出现错误，请联系管理员'
data_base_error_specific = "数据库出现错误，请联系管理员，错误原因是"
no_idea = ' No idea what is this used for  '
name_user = '使用者的姓名'
psw_word = '使用者的密码'
time_update_database = '记录最后更新时间；（2000-1-1 0:0:0 经过的秒），必须有值'
id_in_use = '是关键字，每个位置的唯一标识，一旦添加不能更改，必须有值；'
introduction_course = ' 课程介绍 '
id_error = 'id号码不存在，请重新输入'
post_success = '获取数据成功'
post_error = '查询失败，请重新尝试'
put_success = '数据添加完成'
put_error = '添加失败，请重新尝试'
patch_success = '数据修改已经完成'
patch_error = '修改失败，重新尝试'

responses_success = Schema(
    title='成功消息',
    description='将会返回的成功消息 ',
    type=TYPE_OBJECT,
    properties={
        'message': Schema(
            title='成功消息',
            description='传达的当响应成功的时候的消息',
            type=TYPE_STRING,
            format='string'
        )
    }
)

responses_fail = Schema(
    title='失败消息',
    description='将会返回的失败消息 ',
    type=TYPE_OBJECT,
    properties={
        'message': Schema(
            title='失败消息',
            description='传达的当响应失败的时候的消息',
            type=TYPE_STRING,
            format='string'
        )
    }
)

post_search = {
    'input_string': Schema(
        title='输入的查询字符串',
        type=TYPE_STRING,
        format='string',
    )
}

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


def get_request_args(func):
    def _get_request_args(self, request):
        if request.method == 'GET':
            args = request.GET
            session = request.session
        else:
            body = request.body
            session = request.session
            if body:
                try:
                    args = loads(body)
                except Exception as e:
                    print(e)
                    args = request.POST
            else:
                args = request.POST
        return func(self, request, args, session)
    return _get_request_args


def data_page_response(data, pages, limits):
    if list(data) == []:
        return HttpResponse(dumps({'message': data_base_error}), content_type=content_type_tmp, charset='utf-8')
    object_page = Paginator(data, limits)
    total_number = object_page.num_pages
    try:
        data_response = object_page.page(pages)
    except EmptyPage:
        data_response = object_page.page(total_number)
    return HttpResponse(dumps({'data': list(data)}), content_type=content_type_tmp, charset='utf-8')


def data_total_response(data, pages, limits):
    data_response = list(data)
    total_number = len(data_response)
    if data_response == []:
        return HttpResponse(dumps({'message': "内容不存在"}), content_type=content_type_tmp, charset='utf-8')
    else:
        total_number = len(data_response)
        return HttpResponse(dumps({'data': data_response}), content_type=content_type_tmp, charset='utf-8')


def data_attendance_format(data_equipment, data_plan, id_list):
    id_user_initial = data_equipment[0]['id_user']
    data_equipment_return = []
    person_data = []
    attend_times = 0
    attend_total = 0
    for i in data_equipment:
        data_id_user = i['id_user']
        if id_user_initial == data_id_user:
            person_data_one = {}
            for j in data_plan:
                if i['param2'] == j['id']:
                    person_data_one['param2'] = i['param2']
                    person_data_one['param2__id_curricula__name'] = j['id_curricula__name']
                    person_data_one['param2__timebegin'] = j['timebegin']
                    person_data_one['param2__timeend'] = j['timeend']
                    person_data_one['timeupdate'] = i['timeupdate']
                    person_data_one['idmanager__name'] = i['idmanager__name']
                    person_data_one['time'] = i['time']
                    if j['timebegincheckbegin'] == None:
                        j['timebegincheckbegin'] = 0
                    if j['timebegincheckend'] == None:
                        j['timebegincheckend'] = 0
                    if j['timeendcheckend'] == None:
                        j['timeendcheckend'] = 0
                    if j['timeendcheckbegin'] == None:
                        j['timeendcheckbegin'] = 0
                    if j['timebegin'] <= i['time'] <= j['timeend']:
                        person_data_one['status'] = 1
                        attend_times = attend_times + 1
                        if j['timebegin']+j['timebegincheckend'] * 60 < i['time']:
                            person_data_one['status'] = 2
                    elif j['timeend']+j['timeendcheckend'] < i['time']:
                        person_data_one['status'] = 3
                    attend_total = attend_total + 1
                    person_data.append(person_data_one)
                    break
        else:
            person_total_data = {}
            person_total_data['id'] = id_user_initial
            person_total_data['id_user__name'] = i['id_user__name']
            person_total_data['attendtimes'] = attend_times
            person_total_data['attendtotal'] = attend_total
            person_total_data['attendrates'] = attend_times/attend_total
            person_total_data['person_data'] = person_data
            id_user_initial = data_id_user
            data_equipment_return.append(person_total_data)
            person_data = []
            attend_times = 0
            attend_total = 0
            person_data_one = {}
            for j in data_plan:
                if i['param2'] == j['id']:
                    person_data_one['param2'] = i['param2']
                    person_data_one['param2__id_curricula__name'] = j['id_curricula__name']
                    person_data_one['param2__timebegin'] = j['timebegin']
                    person_data_one['param2__timeend'] = j['timeend']
                    person_data_one['timeupdate'] = i['timeupdate']
                    person_data_one['idmanager__name'] = i['idmanager__name']
                    person_data_one['time'] = i['time']
                    if j['timebegincheckbegin'] == None:
                        j['timebegincheckbegin'] = 0
                    if j['timebegincheckend'] == None:
                        j['timebegincheckend'] = 0
                    if j['timeendcheckend'] == None:
                        j['timeendcheckend'] = 0
                    if j['timeendcheckbegin'] == None:
                        j['timeendcheckbegin'] = 0
                    if j['timebegin'] <= i['time'] <= j['timeend']:
                        person_data_one['status'] = 1
                        attend_times = attend_times + 1
                        if j['timebegin']+j['timebegincheckend'] * 60 < i['time']:
                            person_data_one['status'] = 2
                    elif j['timeend']+j['timeendcheckend'] < i['time']:
                        person_data_one['status'] = 3
                    attend_total = attend_total + 1
                    person_data.append(person_data_one)
                    break
    else:
        person_total_data = {}
        person_total_data['id'] = id_user_initial
        person_total_data['id_user__name'] = data_equipment[-1]['id_user__name']
        person_total_data['attendtimes'] = attend_times
        person_total_data['attendtotal'] = attend_total
        person_total_data['attendrates'] = attend_times/attend_total
        person_total_data['person_data'] = person_data
        data_equipment_return.append(person_total_data)
    return data_equipment_return


def data_attendance_class_format(data_equipment, data_plan, id_list):
    id_user_initial = data_equipment[0]['param2']
    data_equipment_return = []
    person_data = []
    attend_times = 0
    attend_total = 0
    param2 = 0
    param2__id_curricula__name = 0
    param2__timebegin = 0
    param2__timeend = 0
    for i in data_equipment:
        data_id_user = i['param2']
        if id_user_initial == data_id_user:
            person_data_one = {}
            for j in data_plan:
                if i['param2'] == j['id']:
                    param2 = i['param2']
                    param2__id_curricula__name = j['id_curricula__name']
                    param2__timebegin = j['timebegin']
                    param2__timeend = j['timeend']
                    person_data_one['id'] = i['id']
                    person_data_one['id_user__name'] = i['id_user__name']
                    person_data_one['timeupdate'] = i['timeupdate']
                    person_data_one['idmanager__name'] = i['idmanager__name']
                    person_data_one['time'] = i['time']
                    if j['timebegincheckbegin'] == None:
                        j['timebegincheckbegin'] = 0
                    if j['timebegincheckend'] == None:
                        j['timebegincheckend'] = 0
                    if j['timeendcheckend'] == None:
                        j['timeendcheckend'] = 0
                    if j['timeendcheckbegin'] == None:
                        j['timeendcheckbegin'] = 0
                    if j['timebegin'] <= i['time'] <= j['timeend']:
                        person_data_one['status'] = 1
                        attend_times = attend_times + 1
                        if j['timebegin']+j['timebegincheckend'] * 60 < i['time']:
                            person_data_one['status'] = 2
                    elif j['timeend']+j['timeendcheckend'] < i['time']:
                        person_data_one['status'] = 3
                    attend_total = attend_total + 1
                    person_data.append(person_data_one)
                    break
        else:
            person_total_data = {}
            person_total_data['param2'] = param2
            person_total_data['param2__id_curricula__name'] = param2__id_curricula__name
            person_total_data['param2__timebegin'] = param2__timebegin
            person_total_data['param2__timeend'] = param2__timeend
            person_total_data['id_user__name'] = i['id_user__name']
            person_total_data['attendnumbers'] = attend_times
            person_total_data['totalnumbers'] = attend_total
            person_total_data['attendrates'] = attend_times/attend_total
            person_total_data['person_data'] = person_data
            id_user_initial = data_id_user
            data_equipment_return.append(person_total_data)
            person_data = []
            attend_times = 0
            attend_total = 0
            person_data_one = {}
            for j in data_plan:
                if i['param2'] == j['id']:
                    param2 = i['param2']
                    param2__id_curricula__name = j['id_curricula__name']
                    param2__timebegin = j['timebegin']
                    param2__timeend = j['timeend']
                    person_data_one['id'] = i['id']
                    person_data_one['id_user__name'] = i['id_user__name']
                    person_data_one['timeupdate'] = i['timeupdate']
                    person_data_one['idmanager__name'] = i['idmanager__name']
                    person_data_one['time'] = i['time']
                    if j['timebegincheckbegin'] == None:
                        j['timebegincheckbegin'] = 0
                    if j['timebegincheckend'] == None:
                        j['timebegincheckend'] = 0
                    if j['timeendcheckend'] == None:
                        j['timeendcheckend'] = 0
                    if j['timeendcheckbegin'] == None:
                        j['timeendcheckbegin'] = 0
                    if j['timebegin'] <= i['time'] <= j['timeend']:
                        person_data_one['status'] = 1
                        attend_times = attend_times + 1
                        if j['timebegin']+j['timebegincheckend'] * 60 < i['time']:
                            person_data_one['status'] = 2
                    elif j['timeend']+j['timeendcheckend'] < i['time']:
                        person_data_one['status'] = 3
                    attend_total = attend_total + 1
                    person_data.append(person_data_one)
                    break
    else:
        person_total_data = {}
        person_total_data['id'] = id_user_initial
        person_total_data['id_user__name'] = data_equipment[-1]['id_user__name']
        person_total_data['attendtimes'] = attend_times
        person_total_data['attendtotal'] = attend_total
        person_total_data['attendrates'] = attend_times/attend_total
        person_total_data['person_data'] = person_data
        data_equipment_return.append(person_total_data)
    return data_equipment_return


def data_students_attendance_format(data_equipment, data_plan, id_list):
    data_equipment_return = []
    for i in data_equipment:
        data_person = {}
        for j in data_plan:
            if i['param2'] == j['id']:
                data_person['param2'] = i['param2']
                data_person['param2__id_curricula__name'] = j['id_curricula__name']
                data_person['param2__timebegin'] = j['timebegin']
                data_person['param2__timeend'] = j['timeend']
                data_person['timeupdate'] = i['timeupdate']
                data_person['idmanager__name'] = i['idmanager__name']
                data_person['time'] = i['time']
                if j['timebegincheckbegin'] == None:
                    j['timebegincheckbegin'] = 0
                if j['timebegincheckend'] == None:
                    j['timebegincheckend'] = 0
                if j['timeendcheckend'] == None:
                    j['timeendcheckend'] = 0
                if j['timeendcheckbegin'] == None:
                    j['timeendcheckbegin'] = 0
                if j['timebegin'] <= i['time'] <= j['timeend']:
                    data_person['status'] = 1
                    if j['timebegin']+j['timebegincheckend'] * 60 < i['time']:
                        data_person['status'] = 2
                elif j['timeend']+j['timeendcheckend'] < i['time']:
                    data_person['status'] = 3
                    break
        data_equipment_return.append(data_person)
        return data_equipment_return


def data_attendance(course_plan_id, id_list, format_type, user_id):
    '''
    format_type is used to decide the type of the selection,1 represents for data attendance in personal format, 2 represents for data attendance in class format,3 represents for personal data
    '''
    data_equipment = [{'id': 'test'}]
    data_plan = [1, 2, 3, 4, 5]
    if format_type == 3:
        data_equipment = list(models.TCyRunningaccount.objects.filter(id_user=user_id, param2__id_curricula=course_plan_id).values(
            'id', 'id_user__name', 'time', 'type_field', 'param2', 'timeupdate', 'idmanager__name').order_by('param2'))
        data_plan = list(models.TCyplan.objects.filter(id_curricula=course_plan_id).values(
            'id', 'timebegin', 'timeend', 'timebegincheckbegin', 'timebegincheckend', 'timeendcheckend', 'timeendcheckbegin', 'id_curricula__name').order_by('id'))
    elif format_type == 1:
        data_equipment = list(models.TCyRunningaccount.objects.filter(param2__id_curricula=course_plan_id).values(
            'id', 'id_user__name', 'id_user', 'time', 'type_field', 'param2', 'timeupdate', 'idmanager__name').order_by('id_user'))
        data_plan = list(models.TCyplan.objects.filter(id_curricula=course_plan_id).values(
            'id', 'timebegin', 'timeend', 'timebegincheckbegin', 'timebegincheckend', 'timeendcheckend', 'timeendcheckbegin', 'id_curricula__name').order_by('id'))
    elif format_type == 2:
        data_equipment = list(models.TCyRunningaccount.objects.filter(param2__id_curricula=course_plan_id).values(
            'id', 'id_user__name', 'id_user', 'time', 'type_field', 'param2', 'timeupdate', 'idmanager__name').order_by('param2'))
        data_plan = list(models.TCyplan.objects.filter(id_curricula=course_plan_id).values(
            'id', 'timebegin', 'timeend', 'timebegincheckbegin', 'timebegincheckend', 'timeendcheckend', 'timeendcheckbegin', 'id_curricula__name'))
    if data_plan == [] or data_equipment == []:
        return False
    if id_list == []:
        for j in data_equipment:
            id_list.append(j['id'])
    if format_type == 1:
        data_equipment = data_attendance_format(
            data_equipment, data_plan, id_list)
    elif format_type == 2:
        data_equipment = data_attendance_class_format(
            data_equipment, data_plan, id_list)
    elif format_type == 3:
        data_equipment = data_students_attendance_format(
            data_equipment, data_plan, id_list)
    return data_equipment
