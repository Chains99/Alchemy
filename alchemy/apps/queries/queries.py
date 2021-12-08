from django.http import response
from django.urls.base import reverse
from apps.elements.models import Element
from apps.imparts.models import Imparts
from apps.basic_elements.models import BasicElement
from apps.students.models import Student
from apps.study.models import Study
from apps.subjects.models import Subject
from apps.professors.models import Professor
from django.db.models import Count
from apps.non_basic_elements.models import NonBasicElement
from abc import ABCMeta, abstractmethod
from datetime import *

class Query(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, context):
        pass

class MoreCredits(Query): #OK
    def __init__(self, n) -> None:
        self.n = n

    def execute(self, context):
        moreCredits = Student.objects.all().order_by('credits').reverse()[:self.n]
        context["moreCredits"] = moreCredits
        return context

class MoreElementsCreated(Query): #OK
    def __init__(self, n) -> None:
        self.n = n

    def execute(self, context):
        moreElemCreated = NonBasicElement.objects.all().select_related().values('study__student').annotate(count_elem=Count('id'))[:self.n]
        length = len(list(moreElemCreated))
        for i in range(length):
            id_stud = int(moreElemCreated[i]['study__student'])
            student = Student.objects.get(id = id_stud)
            moreElemCreated[i]['firstname'] = student.first_name
            moreElemCreated[i]['lastname'] = student.last_name
            moreElemCreated[i]['credits'] = student.credits

        context["moreElemCreated"] = moreElemCreated
        return context

class MoreBasicElementsUsed(Query): #OK
    def __init__(self, n, subject_name):
        self.n = n
        self.subject_name = subject_name
    
    def execute(self, context):
        moreBasicElemUsed = NonBasicElement.objects.all().select_related().filter(study__subject__name=self.subject_name).values('element1_id').annotate(cant_elem1=Count('element1_id'))[:self.n]
        moreBasicElemUsed2 = NonBasicElement.objects.all().select_related().filter(study__subject__name=self.subject_name).values('element2_id').annotate(cant_elem2=Count('element2_id'))[:self.n]
        list1 = list(moreBasicElemUsed)
        list2 = list(moreBasicElemUsed2)
        print(list1)
        print(list2)

        for i in range(len(list1)):
            id_elem1 = int(list1[i]['element1_id'])
            j = 0
            while len(list2) > 0 and j >= 0 and j < len(list2):
                id_elem2 = int(list2[j]['element2_id'])

                if id_elem1 == id_elem2:
                    cant = list2[j]['cant_elem2']
                    list1[i]['cant_elem1'] += cant
                    list2.pop(j)
                    j -= 1
                j += 1
        
        while len(list2) > 0:
            elem = list2.pop(0)
            new_elem = {'element1_id': elem['element2_id'], 'cant_elem1' : elem['cant_elem2']}
            list1.append(new_elem)

        moreBasicElemUsed = list1

        for i in range(len(moreBasicElemUsed)):
            id_elem = int(moreBasicElemUsed[i]['element1_id'])
            elem = Element.objects.get(id = id_elem)
            moreBasicElemUsed[i]['name'] = elem.name
            moreBasicElemUsed[i]['value'] = elem.value

        print(moreBasicElemUsed)
        context["moreBasicElemUsed"] = moreBasicElemUsed
        return context


class MoreValuableNoBasicElements(Query): #OK
    def __init__(self, n, subject_name) -> None:
        self.n = n
        self.subject_name = subject_name

    def execute(self, context):
        moreValNoBasicElem = NonBasicElement.objects.all().filter(study__subject__name= self.subject_name).order_by('value').reverse()[:self.n]
        context["moreValNoBasicElem"] = moreValNoBasicElem
        return context


class MoreValuableBasicElements(Query): #OK
    def __init__(self, n, subject_name) -> None:
        self.n = n
        self.subject_name = subject_name

    def execute(self, context):
        moreValBasicElem = BasicElement.objects.all().filter(imparts__subject__name= self.subject_name).order_by('value').reverse()[:self.n]
        context["moreValNoBasicElem"] = moreValBasicElem
        return context


class ElementsCreatedByDay(Query): #OK
    def __init__(self, day) -> None:
        self.day = day

    def execute(self, context):
        elemCreatedDay = NonBasicElement.objects.filter(date_time_creation__day=str(self.day))
        context["elemCreatedDay"] = elemCreatedDay
        return context


class ElementsCreatedByMonth(Query): #OK
    def __init__(self, month) -> None:
        self.month = month

    def execute(self, context):
        elemCreatedMonth = NonBasicElement.objects.filter(date_time_creation__month=str(self.month))
        context["elemCreatedDay"] = elemCreatedMonth
        return context

class ElementsCreatedByYear(Query): #OK
    def __init__(self, year) -> None:
        self.year = year

    def execute(self, context):
        elemCreatedYear = NonBasicElement.objects.filter(date_time_creation__year=str(self.year))
        context["elemCreatedDay"] = elemCreatedYear
        return context

class ElementsCreatedDates(Query): #OK
    def __init__(self, initial_date, final_date) -> None:
        self.initial_date = initial_date
        self.final_date = final_date

    def execute(self, context):
        elemCreatedDates = NonBasicElement.objects.filter(date_time_creation__range=[self.initial_date, self.final_date])
        context["elemCreatedDates"] = elemCreatedDates
        return context

class SubjectStudentsCredits(Query): #OK
    def __init__(self, n, subject_name) -> None:
        self.n = n
        self.subject_name = subject_name

    def execute(self, context):
        query1 = Study.objects.all().filter(subject__name=self.subject_name).order_by('credits').reverse()[:self.n]
        subjStudentsCredits = []

        for elem in query1:
            student = Student.objects.get(username = elem.student)
            subjStudentsCredits.append({'firstname':student.first_name, 'lastname':student.last_name, 'credits': elem.credits})
        
        context["subjStudentsCredits"] = subjStudentsCredits
        return context

class BestStudentBySubject(Query): #OK
    def execute(self, context):
        subjects = list(Subject.objects.all())
        bestStudentBySubj = []
        
        for subject in subjects:
            subject_name = subject.name
            student = SubjectStudentsCredits(1, subject_name).execute({})["subjStudentsCredits"][0]
            student["subject"] = subject_name
            bestStudentBySubj.append(student)
        
        print(bestStudentBySubj)
        context["bestStudentBySubj"] = bestStudentBySubj
        return context

class NoAcceptedNonBasicElem(Query): #OK
    def __init__(self, subject_name) -> None:
        self.subject_name = subject_name
    
    def execute(self, context):
        query1 = NonBasicElement.objects.all().filter(study__subject__name=self.subject_name, accepted=False)
        noAcceptedElem = []

        for elem in query1:
            student = Student.objects.get(username = elem.study.student)
            noAcceptedElem.append({'name': elem.name, 'student': (student.first_name + " " + student.last_name)})
        
        print(noAcceptedElem)
        context["noAcceptedElem"] = noAcceptedElem
        return context