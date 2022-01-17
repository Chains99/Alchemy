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
        n = data["n_students_credits"]
        if n != "":
            return MoreCredits(int(n))
        return None

class MoreElementsCreatedFactory(QueryFactory):
    def __init__(self):
        self.name = "moreElemCreated"
    
    def get_instance(self, data):
        n = data["n_students_elemCreated"]
        if n != "":
            return MoreElementsCreated(int(n))
        return None


class MoreBasicElementsUsedFactory(QueryFactory):
    def __init__(self):
        self.name = "moreElemUsed"

    def get_instance(self, data):
        n = data["n_elements_basic"]
        s = data["subject_name"]
        if n != "" and s != "":
            return MoreElementsUsed(int(n), s)
        return None

class MoreValuableNoBasicElementsFactory(QueryFactory):
    def __init__(self):
        self.name = 'moreValNoBasicElem'
    
    def get_instance(self, data):
        return MoreValuableNoBasicElements(int(data['n_elements_noBasic']), data["subject_name"])

class MoreValuableBasicElementsFactory(QueryFactory):
    def __init__(self):
        self.name = 'moreValBasicElem'
    
    def get_instance(self, data):
        n = data['n_elements_valbasic']
        s = data["subject_name"]
        if n != "" and s != "":
            return MoreValuableBasicElements(int(n), s)
        return None

class ElementsCreatedByYearFactory(QueryFactory):
    def __init__(self):
        self.name = "elemCreatedYear"
    
    def get_instance(self, data):
        n = data["year"]
        if n != "":
            return ElementsCreatedByYear(int(n))
        return None


class ElementsCreatedDatesFactory(QueryFactory):
    def __init__(self):
        self.name = "elemCreatedDates"

    def get_instance(self, data):
        i = data["initial_date"]
        f = data["final_date"]
        if i != "" and f != "":
            return ElementsCreatedDates(i, f)
        return None

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