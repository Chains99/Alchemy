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
        self.name = "moreElemUsed"

    def get_instance(self, data):
        return MoreElementsUsed(int(data["n_elements_basic"]), data["subject_name"])

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
        return SubjectStudentsCredits(data["subject_name"])

class SubjectStudentsCreditsNFactory(QueryFactory):
    def __init__(self):
        self.name = 'subjStudentsCreditsN'

    def get_instance(self, data):
        return SubjectStudentsCreditsN(int(data['n_students_subCredits']), data["subject_name"])

class RankingByDatesTotalCreditsFactory(QueryFactory):
    def __init__(self):
        self.name = "rankingDatesTotalCredits"
    
    def get_instance(self, data):
        return RankingByDatesTotalCredits(data["initial_date"], data["final_date"])

class RankingByDatesSubjectCreditsFactory(QueryFactory):
    def __init__(self):
        self.name = "rankingDatesSubjectCredits"
    
    def get_instance(self, data):
        return RankingByDatesSubjectCredits(data["initial_date"], data["final_date"], data["subject_name"])