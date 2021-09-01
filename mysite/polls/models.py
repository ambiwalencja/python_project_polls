from django.db import models
# import datetime
from django.utils import timezone
# import pytz


class PublicationTracker(models.Model):
    created_datetime = models.DateTimeField(auto_now_add=True)  # ustawia się przy tworzeniu
    updated_datetime = models.DateTimeField(auto_now=True)  # ustawia się przy każdej modyfikacji

    class Meta:
        abstract = True  # to sprawia, że klasa jest używana do dziedziczenia, ale nie tworzy tabeli w db

# model_name_id is a default attribute
class Course(PublicationTracker):
    name = models.CharField(max_length=128, verbose_name="Nazwa kursu")


    def __str__(self):
        return self.name


class Edition(PublicationTracker):
    course = models.ForeignKey('Course', on_delete=models.PROTECT)
    number = models.SmallIntegerField(verbose_name="Numer")
    start_date = models.DateField(verbose_name="Data startu")
    end_date = models.DateField(verbose_name="Data zakończenia", blank=True)

    def __str__(self):
        return f'{self.course} {self.number}'


class Mentor(PublicationTracker):
    contract_no = models.IntegerField(verbose_name="Numer umowy")
    name = models.CharField(max_length=64, verbose_name="Imię")
    surname = models.CharField(max_length=64, verbose_name="Nazwisko")
    gender = models.CharField(max_length=1, choices=(("M", "Male"), ("F", "Female")))

    def __str__(self):
        return f'{self.name} {self.surname}'


class MentorInEdition(PublicationTracker):
    edition = models.ForeignKey('Edition', on_delete=models.CASCADE)
    mentor = models.ForeignKey('Mentor', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.edition}: {self.mentor}'  # czy tutaj od razu wyświetlą się reprezentacje str mentora i edycji?


class Template(PublicationTracker):
    name = models.CharField(max_length=64, verbose_name="Rodzaj szablonu")

    def __str__(self):
        return self.name


class ParticularForm(PublicationTracker):
    template = models.ForeignKey('Template', on_delete=models.SET_NULL, null=True)  # po usunięciu template ta wartość się ustawi na None
    mentor_in_edition = models.ForeignKey('MentorInEdition', on_delete=models.SET_NULL)
    sent_at = models.DateTimeField(verbose_name="Data wysłania ankiety")

    def __str__(self):
        return f'Form {self.template} in {self.mentor_in_edition}'  # to samo pytanie co powyżej


class QuestionType(PublicationTracker):
    # name (radio button, checkbox, text field)
    pass


class Question(PublicationTracker):
    # question_type -> FK QuestionType
    question_text = models.CharField(max_length=500, verbose_name="Tekst pytania")
    answer_text = models.CharField(max_length=500, verbose_name="Tekst odpowiedzi", blank=True, default='')

    def __str__(self):
        return self.question_text
