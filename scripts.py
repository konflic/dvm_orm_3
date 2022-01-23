import random


def fix_marks(schoolkid):
    bad_marks =  Mark.objects.filter(schoolkid=child, points__in=[2, 3])
    for mark in marks:
        mark.points = 5
        mark.save()


def remove_chastisements(schoolkid):
    Chastisement.objects.filter(schoolkid=schoolkid).delete()
 
 
def create_commendation(name, subject_title):
    child = Schoolkid.objects.get(full_name__contains=name)
    subject = Subject.objects.filter(title=subject_title, year_of_study=child.year_of_study)[0]
    lesson = Lesson.objects.filter(group_letter=child.group_letter, year_of_study=child.year_of_study, subject=subject).order_by("-date")[0]
    commendation_text = random.choice(["Молодец!", "Отлично!", "Хорошо!", "Ты меня приятно удивил!","Великолепно!", "Прекрасно!", "Талантливо!", "Потрясающе!"])
    Commendation.objects.create(text=commendation_text, created=lesson.date, schoolkid=child, subject=lesson.subject, teacher=lesson.teacher)
