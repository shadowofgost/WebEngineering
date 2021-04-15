from __future__ import absolute_import, unicode_literals
from celery import shared_task
import datetime
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mass_mail
from django.core.mail import send_mail
from django.db.models.deletion import SET_NULL
from .. import models
from ..Views.Public import data_attendance
from ..Views.Public import select_quit_warning_student

# 此定时任务目的在于检测不合格学生以及考勤不合格学生，并用邮件提醒老师。


def send_email_course(select_student, course_name, id_speaker__name, id_speaker__email):
    if id_speaker__email == None:
        id_speaker__email = 'shadowofgost@outlook.com'
    teacher_title = str(course_name)+'课程考勤多次缺勤记录'
    student_title = str(course_name)+'课程考勤警告'
    quit_message = []
    students_email = [i['id_user__email']
                      for i in select_student if i['id_user__email'] != None]
    for i in select_student:
        quit_message.append(str(i['id_user__nouser'])+'  ' +
                            str(i['id_user__name']) + '缺勤次数为'+str(i['id_user__quit']))
    quit_total_message = '以下是缺勤名单\n' + '\n'.join(quit_message)
    send_mail(teacher_title, quit_total_message,
              str(id_speaker__email), [id_speaker__email])
    send_mail(student_title, '您已多次缺勤，请保持上课出勤率，否则将会面临挂科',
              str(id_speaker__email), students_email)


@shared_task
def warning(limit_not_attendtimes=3, limit_not_attendrates=0.2):
    data_course = tuple(models.TCycurricula.objects.all().values(
        'id', 'name', 'id_speaker__name', 'id_speaker__email'
        'rangeusers', 'listdepts'
    ).distinct().order_by('id'))
    format_type = 1
    id_list = []
    user_id = 1910404051
    for i in data_course:
        course_plan_id = i['id']
        select_students = select_quit_warning_student(
            course_plan_id, id_list, format_type, user_id, limit_not_attendrates, limit_not_attendtimes)
        send_email_course(select_students, i['name'],
                          i['id_speaker__name'], i['id_speaker__emai'])
    print('success')
    return 'success'
