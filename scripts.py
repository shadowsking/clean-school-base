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
    marks.update(points=randint(4, 5))


def remove_chastisements(schoolkid):
    Chastisement.objects.filter(schoolkid=schoolkid).delete()


def create_commendation(schoolkid, subject, year_of_study=6, group_letter="А"):
    random_lesson = Lesson.objects.filter(
        year_of_study=year_of_study,
        group_letter=group_letter,
        subject__title=subject
    ).order_by("?").first()
    if not random_lesson:
        return

    query_params = dict(
        schoolkid=schoolkid,
        created=random_lesson.date,
        subject=random_lesson.subject,
        teacher=random_lesson.teacher,
    )
    commendations = Commendation.objects.filter(**query_params)
    if commendations:
        return

    commendations.create(
        text=choice(COMMENDATIONS),
        **query_params
    )


def get_child(full_name):
    try:
        return Schoolkid.objects.get(full_name__contains=full_name)
    except Schoolkid.DoesNotExist:
        print("Такого ученика нет в базе данных. Проверьте корректность ФИО.")
    except Schoolkid.MultipleObjectsReturned:
        print("Найдено более одного ученика. Уточните ФИО ученика.")
