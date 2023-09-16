from random import randint, choice

from datacenter.models import Schoolkid, Mark, Chastisement, Lesson, Commendation

COMMENDATIONS = [
    "Молодец!",
    "Отлично!",
    "Хорошо!",
    "Гораздо лучше, чем я ожидал!",
    "Ты меня приятно удивил!",
    "Великолепно!",
    "Прекрасно!",
    "Ты меня очень обрадовал!",
    "Именно этого я давно ждал от тебя!",
    "Сказано здорово – просто и ясно!",
    "Ты, как всегда, точен!",
    "Очень хороший ответ!",
    "Талантливо!",
    "Ты сегодня прыгнул выше головы!",
    "Я поражен!",
    "Уже существенно лучше!",
    "Потрясающе!",
    "Замечательно!",
    "Прекрасное начало!",
    "Так держать!",
    "Ты на верном пути!",
    "Здорово!",
    "Это как раз то, что нужно!",
    "Я тобой горжусь!",
    "С каждым разом у тебя получается всё лучше!",
    "Мы с тобой не зря поработали!",
    "Я вижу, как ты стараешься!",
    "Ты растешь над собой!",
    "Ты многое сделал, я это вижу!",
    "Теперь у тебя точно все получится!",
]


def fix_marks(schoolkid):
    marks = Mark.objects.filter(schoolkid=schoolkid, points__lt=4)
    for mark in marks:
        mark.points = randint(4, 5)
        mark.save()


def remove_chastisements(schoolkid):
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    for chastisement in chastisements:
        chastisement.delete()


def create_commendation(schoolkid, subject, year_of_study=6, group_letter="А"):
    lessons = Lesson.objects.filter(
        year_of_study=year_of_study,
        group_letter=group_letter,
        subject__title=subject
    )
    for lesson in lessons:
        query_params = dict(
            schoolkid=schoolkid,
            created=lesson.date,
            subject=lesson.subject,
            teacher=lesson.teacher,
        )
        commendations = Commendation.objects.filter(**query_params)
        if commendations:
            continue

        commendation = Commendation(
            text=choice(COMMENDATIONS),
            **query_params
        )
        commendation.save()


def get_child(full_name):
    return Schoolkid.objects.filter(full_name__contains=full_name).get()
