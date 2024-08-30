from django.core.management.base import BaseCommand

from main.models import Photo, Question


class Command(BaseCommand):
    def handle(self, *args, **options):
        Photo.objects.all().delete(),
        Question.objects.all().delete(),

        Photo.objects.create(
            img='media/fight/training/img.webp')
        Photo.objects.create(
            img='media/fight/training/img_1.webp', )
        Photo.objects.create(
            img='media/fight/training/img_2.webp', )
        Photo.objects.create(
            img='media/fight/training/img_3.webp', )
        Photo.objects.create(
            img='media/fight/training/img_4.webp', )
        Photo.objects.create(
            img='media/fight/training/img_5.webp', )
        Photo.objects.create(
            img='media/fight/training/img_6.webp', )
        Photo.objects.create(
            img='media/fight/training/img_7.webp', )
        Photo.objects.create(
            img='media/fight/training/img_8.webp', )
        Photo.objects.create(
            img='media/fight/training/img_9.webp', )
        Photo.objects.create(
            img='media/fight/training/img_10.webp', )
        Photo.objects.create(
            img='media/fight/training/img_11.webp', )

        Question.objects.create(
            question='Со скольки лет можно посещать тренировки',
            answer="С 4-х полных лет")
        Question.objects.create(
            question='Что нужно для посещения тренировки',
            answer="Справка от врача, что можно заниматься муайтай (тайским боксом). Удобная одежда для тренировок, занимаемся босиком."
                   " В перспективе необходимо приобретать: бинты, боксерские перчатки, защиту ног,"
                   " налокотники, шлем, капа, защиту паха. Детям до 18 лет дополнительно к написанному выше жилет (защита корпуса).")
        Question.objects.create(
            question='Когда можно привести ребенка',
            answer="Ознакомьтесь с расписанием и/или обращайтесь по контактному номеру телефона")
