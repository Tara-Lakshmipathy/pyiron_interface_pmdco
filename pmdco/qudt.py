from pmdco.root_classes import *
from rdflib import URIRef

class QUDT(Thing):
    @property
    def IRI(self):
        return URIRef("https://qudt.org/3.0.0/schema/qudt")

class Unit(QUDT):
    @property
    def IRI(self):
        return URIRef("http://qudt.org/schema/qudt/Unit")

class Sec(Unit):
    @property
    def IRI(self):
        return URIRef("hhttp://qudt.org/vocab/unit/SEC")
