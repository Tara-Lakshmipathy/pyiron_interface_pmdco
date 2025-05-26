from pmdco.root_classes import *
from rdflib import URIRef

class TextEditingAtomicNode(DigitalWorkflowAtomicNode):
    @property
    def IRI(self):
        return URIRef("https://w3id.org/pmd/co/TextEditingAtomicNodePending")

class TextEditingWorkflowNode(DigitalWorkflowMacroNode):
    @property
    def IRI(self):
        return URIRef("https://w3id.org/pmd/co/TextEditingWorkflowNodePending")

class SentenceSplittingNode(TextEditingAtomicNode):
    @property
    def IRI(self):
        return URIRef("https://w3id.org/pmd/co/SentenceSplittingNodePending")

class WordsCombiningNode(TextEditingAtomicNode):
    @property
    def IRI(self):
        return URIRef("https://w3id.org/pmd/co/WordsCombiningNodePending")

class WeirdTextEditingWorkflow(TextEditingWorkflowNode):
    @property
    def IRI(self):
        return URIRef("https://w3id.org/pmd/co/WeirdTextEditingWorkflowPending")

#--------------------------------------------------------------------------------------------------

class TextEditingAtomicProcess(DigitalWorkflowAtomicProcess):
    @property
    def IRI(self):
        return URIRef("https://w3id.org/pmd/co/TextEditingAtomicProcessPending")

class TextEditingWorkflowProcess(DigitalWorkflowMacroProcess):
    @property
    def IRI(self):
        return URIRef("https://w3id.org/pmd/co/TextEditingWorkflowProcessPending")

class SentenceSplittingProcess(TextEditingAtomicProcess):
    @property
    def IRI(self):
        return URIRef("https://w3id.org/pmd/co/SentenceSplittingProcessPending")

class WordsCombiningProcess(TextEditingAtomicProcess):
    @property
    def IRI(self):
        return URIRef("https://w3id.org/pmd/co/WordsCombiningProcessPending")

class WeirdTextEditingWorkflowProcess(TextEditingWorkflowProcess):
    @property
    def IRI(self):
        return URIRef("https://w3id.org/pmd/co/WeirdTextEditingWorkflowProcessPending")

#--------------------------------------------------------------------------------------------------

class TextEditingSoftware(Software):
    @property
    def IRI(self):
        return URIRef("https://w3id.org/pmd/co/TextEditingSoftwarePending")

class FONDAPlan(ProjectPlan):
    @property
    def IRI(self):
        return URIRef("https://w3id.org/pmd/co/FONDAPlanPending")