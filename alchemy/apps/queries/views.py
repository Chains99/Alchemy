from django import db
from django.shortcuts import render
from apps.queries.queries import MoreCredits
from apps.queries.forms import *
from apps.queries.queries_factory import *
from django.urls import reverse_lazy
from django.http import *


def queries_render(request):
    return render(request, "queries.html")


def queries_result_render(request):

    context = {}

    if request.method == "POST":
        factory = get_factory()
        instance = factory[request.POST["form-type"]].get_instance(request.POST)
        context = instance.execute(context)
    else:
        context = BestStudentBySubject().execute(context)

    return render(request, "queries_result.html", context=context)
