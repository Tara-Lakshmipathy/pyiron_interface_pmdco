from pmdco.root_classes import *
from rdflib import URIRef

class Executes(Relation):
    @property
    def IRI(self):
        return URIRef("https://w3id.org/pmd/co/id_pending")

class HasContinuantPart(Relation):
    @property
    def IRI(self):
        return URIRef("http://purl.obolibrary.org/obo/BFO_0000178")

class Realizes(Relation):
    @property
    def IRI(self):
        return URIRef("http://purl.obolibrary.org/obo/BFO_0000055")

class IsAbout(Relation):
    @property
    def IRI(self):
        return URIRef("http://purl.obolibrary.org/obo/IAO_0000136")

class HasParticipant(Relation):
    @property
    def IRI(self):
        return URIRef("http://purl.obolibrary.org/obo/BFO_0000057")

class HasSpecifiedInput(HasParticipant):
    @property
    def IRI(self):
        return URIRef("http://purl.obolibrary.org/obo/OBI_0000293")

class HasSpecifiedOutput(HasParticipant):
    @property
    def IRI(self):
        return URIRef("http://purl.obolibrary.org/obo/OBI_0000299")

class IsConcretizedBy(Relation):
    @property
    def IRI(self):
        return URIRef("http://purl.obolibrary.org/obo/BFO_0000058")