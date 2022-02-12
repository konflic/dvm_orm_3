import sys
import random

from datacenter.models import Schoolkid
from datacenter.models import Mark
from datacenter.models import Lesson
from datacenter.models import Subject
from datacenter.models import Commendation
from datacenter.models import Chastisement
from django.db.models import Model


def get_schoolkid(name):
    """Получение объекта ученика по имени в журнале.

    :param name: Строка с именем ученика, пример "Василий Пупкин"
    :return: Schoolkid
    """
    try:
        return Schoolkid.objects.get(full_name__contains=name)
    except Model.DoesNotExist:
        print(f"Не найдено учеников по запросу '{name}'.")
    except Model.MultipleObjectsReturned:
        print(f"Найдено несколько учеников по запросу '{name}'.")
    sys.exit(1)


def fix_marks(name):
    """Исправление плохих оценок ученику с именем name.

    :param name: Строка с именем ученика, пример "Василий Пупкин"
    :return: None
    """
    schoolkid = get_schoolkid(name)
    bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3])

    for mark in bad_marks:
        mark.points = 5
        mark.save()


def remove_chastisements(name):
    """Удалить замечания ученику с именем name.

    :param name: Строка с именем ученика, пример "Василий Пупкин"
    :return: None
    """
    schoolkid = get_schoolkid(name)

    Chastisement.objects.filter(schoolkid=schoolkid).delete()


def create_commendation(name, subject_title):
    """Функция для добавления похвалы.

    :param name: Строка с именем ученика, пример "Василий Пупкин"
    :param subject_title: Предмет по которому нужно добавить похвалу
    :return: None
    """

    schoolkid = get_schoolkid(name)

    commendation_text = random.choice(
        [
            "Молодец!",
            "Отлично!",
            "Хорошо!",
            "Ты меня приятно удивил!",
            "Великолепно!",
            "Прекрасно!",
            "Талантливо!",
            "Потрясающе!",
        ]
    )


    subject = Subject.objects.filter(
        title=subject_title, year_of_study=schoolkid.year_of_study
    ).first()

    lesson = Lesson.objects.filter(
        group_letter=schoolkid.group_letter,
        year_of_study=schoolkid.year_of_study,
        subject=subject,
    ).order_by("-date").first()

    Commendation.objects.create(
        text=commendation_text,
        created=lesson.date,
        schoolkid=schoolkid,
        subject=lesson.subject,
        teacher=lesson.teacher,
    )
