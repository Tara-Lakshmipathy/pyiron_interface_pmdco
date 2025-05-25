from pmdco.root_classes import *
from rdflib import URIRef

class TextEditingAtomicNode(DigitalWorkflowAtomicNode):
    @property
    def IRI(self):
        return URIRef("https://w3id.org/pmd/co/id_pending")

class TextEditingWorkflowNode(DigitalWorkflowMacroNode):
    @property
    def IRI(self):
        return URIRef("https://w3id.org/pmd/co/id_pending")

class SentenceSplittingNode(TextEditingAtomicNode):
    @property
    def IRI(self):
        return URIRef("https://w3id.org/pmd/co/id_pending")

class WordsCombiningNode(TextEditingAtomicNode):
    @property
    def IRI(self):
        return URIRef("https://w3id.org/pmd/co/id_pending")

class WeirdTextEditingWorkflow(TextEditingWorkflowNode):
    @property
    def IRI(self):
        return URIRef("https://w3id.org/pmd/co/id_pending")

#--------------------------------------------------------------------------------------------------

class TextEditingAtomicProcess(DigitalWorkflowAtomicProcess):
    @property
    def IRI(self):
        return URIRef("https://w3id.org/pmd/co/id_pending")

class TextEditingWorkflowProcess(DigitalWorkflowMacroProcess):
    @property
    def IRI(self):
        return URIRef("https://w3id.org/pmd/co/id_pending")

class SentenceSplittingProcess(TextEditingAtomicProcess):
    @property
    def IRI(self):
        return URIRef("https://w3id.org/pmd/co/id_pending")

class WordsCombiningProcess(TextEditingAtomicProcess):
    @property
    def IRI(self):
        return URIRef("https://w3id.org/pmd/co/id_pending")

class WeirdTextEditingWorkflowProcess(TextEditingWorkflowProcess):
    @property
    def IRI(self):
        return URIRef("https://w3id.org/pmd/co/id_pending")

#--------------------------------------------------------------------------------------------------