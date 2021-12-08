from abc import ABCMeta, abstractmethod
from apps.queries.queries import *

#Esta clase se encarga de identificar el tipo de form que es, y crear la instancia de la clase
#de la consulta que se quiere ejecutar

def get_factory():
    _factory = {}

    for meta_item in QueryFactory.__subclasses__():
        item = meta_item()
        _factory[item.name] = item
    return _factory

class QueryFactory(metaclass=ABCMeta):
    def __init__(self):
        self.name = str()
    
    @abstractmethod
    def get_instance(self, data):
        pass

class MoreCreditsFactory(QueryFactory):
    def __init__(self):
        self.name = "moreCredits"
    
    def get_instance(self, data):
        return MoreCredits(int(data["n_students_credits"]))

class MoreElementsCreatedFactory(QueryFactory):
    def __init__(self):
        self.name = "moreElemCreated"
    
    def get_instance(self, data):
        return MoreElementsCreated(int(data["n_students_elemCreated"]))


class MoreBasicElementsUsedFactory(QueryFactory):
    def __init__(self):
        self.name = "moreBasicElemUsed"

    def get_instance(self, data):
        return MoreBasicElementsUsed(int(data["n_elements_basic"]), data["subject_name"])

class MoreValuableNoBasicElementsFactory(QueryFactory):
    def __init__(self):
        self.name = 'moreValNoBasicElem'
    
    def get_instance(self, data):
        return MoreValuableNoBasicElements(int(data['n_elements_noBasic']), data["subject_name"])

class MoreValuableBasicElementsFactory(QueryFactory):
    def __init__(self):
        self.name = 'moreValBasicElem'
    
    def get_instance(self, data):
        return MoreValuableBasicElements(int(data['n_elements_valbasic']), data["subject_name"])

class ElementsCreatedByDayFactory(QueryFactory):
    def __init__(self):
        self.name = "elemCreatedDay"
    
    def get_instance(self, data):
        return ElementsCreatedByDay(int(data["day"]))


class ElementsCreatedByMonthFactory(QueryFactory):
    def __init__(self):
        self.name = "elemCreatedMonth"
    
    def get_instance(self, data):
        return ElementsCreatedByMonth(int(data["month"]))

class ElementsCreatedByYearFactory(QueryFactory):
    def __init__(self):
        self.name = "elemCreatedYear"
    
    def get_instance(self, data):
        return ElementsCreatedByYear(int(data["year"]))


class ElementsCreatedDatesFactory(QueryFactory):
    def __init__(self):
        self.name = "elemCreatedDates"

    def get_instance(self, data):
        return ElementsCreatedDates(data["initial_date"], data["final_date"])

class SubjectStudentsCreditsFactory(QueryFactory):
    def __init__(self):
        self.name = 'subjStudentsCredits'

    def get_instance(self, data):
        return SubjectStudentsCredits(int(data['n_students_subCredits']), data["subject_name"])

class NoAcceptedNonBasicElemFactory(QueryFactory):
    def __init__(self):
        self.name = 'noAcceptedElem'

    def get_instance(self, data):
        return NoAcceptedNonBasicElem(data["subject_name"])