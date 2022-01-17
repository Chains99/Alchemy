from django import db
from django.shortcuts import render
from apps.queries.queries import MoreCredits
from apps.queries.forms import *
from apps.queries.queries_factory import *
from django.urls import reverse_lazy
from django.http import *
from apps.subjects.models import Subject

_subjects=Subject.objects.all()
subjects=[(s.name,s.name) for s in _subjects]

def queries_render(request):
    context = {
        'subjects': subjects}
    return render(request, "queries.html",context=context)


def queries_result_render(request):

    context = {
        "moreCredits" : MoreCreditsForm,
        "moreElemCreated" : MoreElementsCreatedForm,
        "moreElemUsed" : MoreElementsUsedForm,
        "moreValNoBasicElem" : MoreValuableNoBasicElementsForm,
        "moreValBasicElem" : MoreValuableBasicElementsForm,
        "elemCreatedYear" : ElementsCreatedByYearForm,
        "elemCreatedDates" : ElementsCreatedDatesForm,
        "subjStudentsCredits" : SubjectStudentsCreditsForm,
        "rankingDatesTotalCredits" : RankingByDatesTotalCreditsForm,
        "rankingDatesSubjectCredits" : RankingByDatesSubjectCreditsForm
    }

    if request.method == "POST":
        factory = get_factory()
        instance = factory[request.POST["form-type"]].get_instance(request.POST)
        if instance is not None:
            context = instance.execute(context)
            print("CONTEXT",context)
    else:
        context = BestStudentBySubject().execute(context)

    return render(request, "queries_result.html", context=context)

    # if request.method == 'POST':
        # cont_data = HandlerForm().handle(request.POST, cont_data)
    # return render(request, "consultas.html", context=cont_data)