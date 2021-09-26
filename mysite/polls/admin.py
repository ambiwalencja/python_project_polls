from django.contrib import admin

# Register your models here.
from .models import Course, Edition, MentorInEdition, Mentor, \
    Template, ParticularForm, Question, QuestionType


# admin.site.register(Question)  # to dodaje mi modele do panelu administracyjnego (rejestruje je)


@admin.register(Course)  # dekorator, który
class CourseAdmin(admin.ModelAdmin):  # klasa, która pozwala zarządzać
                                    # (m.in. które obiekty mogę edytowac, z jakich poziomów)
    pass


@admin.register(Edition)
class EditionAdmin(admin.ModelAdmin):
    pass


@admin.register(MentorInEdition)
class MentorInEditionAdmin(admin.ModelAdmin):
    pass


@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    pass


@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    pass


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass


@admin.register(QuestionType)
class QuestionTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(ParticularForm)
class ParticularFormAdmin(admin.ModelAdmin):
    pass

