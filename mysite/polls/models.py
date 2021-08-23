from django.db import models
# import datetime
from django.utils import timezone
# import pytz


# model_name_id is a default attribute
class Course(models.Model):
    name = models.CharField(max_length=64)
    created = models.DateTimeField
    updated = models.DateTimeField

    def __str__(self):
        return self.name


class Edition(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    number = models.SmallIntegerField
    start_date = models.DateField
    end_date = models.DateField
    created = models.DateTimeField
    updated = models.DateTimeField

    def __str__(self):
        return f'{self.course} {self.number}'


class Mentor(models.Model):
    contract_no = models.IntegerField
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    gender = models.CharField(max_length=1, choices=[("M", "Male"), ("F", "Female")])
    created = models.DateTimeField
    updated = models.DateTimeField

    def __str__(self):
        return f'{self.name} {self.surname}'


class MentorInEdition(models.Model):
    edition = models.ForeignKey(Edition, on_delete=models.CASCADE)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    created = models.DateTimeField
    updated = models.DateTimeField

    def __str__(self):
        return f'{self.edition}: {self.mentor}'  # czy tutaj od razu wyświetlą się reprezentacje str mentora i edycji?


class Template(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Form(models.Model):
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
    mentor_in_edition = models.ForeignKey(MentorInEdition, on_delete=models.CASCADE)
    sent_at = models.DateTimeField
    created = models.DateTimeField
    updated = models.DateTimeField

    def __str__(self):
        return f'Form {self.template} in {self.mentor_in_edition}'  # to samo pytanie co powyżej


class Question(models.Model):
    question_text = models.CharField(max_length=500)
    answer_type = models.CharField(max_length=64, default='')  # na razie tak, ale potem czyżby było konieczne
    #                                                       stworzenie modeli z wyborami? + default dodałam, bo
    #                                                       wyskakiwało mi ostrzeżenie
    created = models.DateTimeField
    updated = models.DateTimeField

    def __str__(self):
        return self.question_text
