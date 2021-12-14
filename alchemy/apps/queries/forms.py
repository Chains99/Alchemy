from django import forms
from django.forms import Form

#Mostrar los n estudiantes con mas creditos acumulados (ordena descendiente).
class MoreCreditsForm(Form):
    n_students_credits = forms.IntegerField(min_value=1, required=True, initial=10)

#Mostrar los n estudiantes con mas elementos creados.
class MoreElementsCreatedForm(Form):
    n_students_elemCreated = forms.IntegerField(min_value=1, required=True, initial=10)

#Mostrar los n elementos mas utilizados por los estudiantes para realizar mezclas.
class MoreBasicElementsUsedForm(Form):
    n_elements_basic = forms.IntegerField(min_value=1, required=True, initial=10)
    subject_name = forms.CharField(label="Nombre de la asignatura", required=True)

#Mostrar los n elmentos mas valiosos de los elementos no basicos.
class MoreValuableNoBasicElementsForm(Form):
    n_elements_noBasic = forms.IntegerField(min_value=1, required=True, initial=10)
    subject_name = forms.CharField(label="Nombre de la asignatura", required=True)

#Mostrar los n elementos mas valiosos de los elementos basicos.
class MoreValuableBasicElementsForm(Form):
    n_elements_valbasic = forms.IntegerField(min_value=1, required=True, initial=10)
    subject_name = forms.CharField(label="Nombre de la asignatura", required=True)

#Dado un mes, un año o un dia: mostrar los elementos creados
class ElementsCreatedByDayForm(Form):
    day = forms.IntegerField(min_value=1, required=True, initial=10)

class ElementsCreatedByMonthForm(Form):
    month = forms.IntegerField(min_value=1, required=True, initial=10)

class ElementsCreatedByYearForm(Form):
    year = forms.IntegerField(min_value=1, required=True, initial=10)

#Dado un intervalo de fechas: mostrar los elementos creados en ese intervalo.
class ElementsCreatedDates:
    initial_date = forms.DateField(required=True)
    final_date = forms.DateField(required=True)

#Dado una asignatura: mostrar el ranking de estudiantes
class SubjectStudentsCreditsForm(Form):
    subject_name = forms.CharField(label="Nombre de la asignatura", required=True)

#Dado un intervalo de fechas mostrar el ranking de los estudiantes (por creditos totales)
class RankingByDatesTotalCreditsForm(Form):
    initial_date = forms.DateField(required=True)
    final_date = forms.DateField(required=True)

#Dado un intervalo de fechas y una asignatura mostrar el ranking de los estudiantes (por creditos de la asignatura)
class RankingByDatesSubjectCredits(Form):
    initial_date = forms.DateField(required=True)
    final_date = forms.DateField(required=True)
    subject_name = forms.CharField(label="Nombre de la asignatura", required=True)