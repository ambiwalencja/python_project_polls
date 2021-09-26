from django.http import HttpResponse, HttpResponseRedirect
# from django.template import loader
# from django.shortcuts import render, get_object_or_404
# from django.http import Http404  #for raising an exception


from .models import Course, Edition, MentorInEdition, Mentor, Template, ParticularForm, Question, QuestionType


def index(request):
    temp = 'hello'
    return HttpResponse(temp)


