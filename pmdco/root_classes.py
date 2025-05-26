from rdflib import URIRef

class Thing():
    @property
    def IRI(self):
        return URIRef("https://pending")

class BasicFormalOntology(Thing):
    @property
    def IRI(self):
        return URIRef("http://purl.obolibrary.org/obo/bfo.owl")

class Entity(BasicFormalOntology):
    @property
    def IRI(self):
        return URIRef("http://purl.obolibrary.org/obo/BFO_0000001")

class Relation(BasicFormalOntology):
    @property
    def IRI(self):
        return URIRef("https://w3id.org/pmd/co/RelationPending")

class Continuant(Entity):
    @property
    def IRI(self):
        return URIRef("http://purl.obolibrary.org/obo/BFO_0000002")

class Occurent(Entity):
    @property
    def IRI(self):
        return URIRef("http://purl.obolibrary.org/obo/BFO_0000003")

#--------------------------------------------------------------------------------------------------

class GenericallyDependentContinuant(Continuant):
    @property
    def IRI(self):
        return URIRef("http://purl.obolibrary.org/obo/BFO_0000031")

class InformationContentEntity(GenericallyDependentContinuant):
    @property
    def IRI(self):
        return URIRef("http://purl.obolibrary.org/obo/IAO_0000030")

class DirectiveInformationEntity(InformationContentEntity):
    @property
    def IRI(self):
        return URIRef("http://purl.obolibrary.org/obo/IAO_0000033")

class PlanSpecification(DirectiveInformationEntity):
    @property
    def IRI(self):
        return URIRef("https://w3id.org/pmd/co/PMD_0000003")

class ValueSpecification(DirectiveInformationEntity):
    @property
    def IRI(self):
        return URIRef("http://purl.obolibrary.org/obo/OBI_0001933")

class DataItem(InformationContentEntity):
    @property
    def IRI(self):
        return URIRef("http://purl.obolibrary.org/obo/IAO_0000027")

class Software(PlanSpecification):
    @property
    def IRI(self):
        return URIRef("http://purl.obolibrary.org/obo/IAO_0000010")

class SoftwareEnv(PlanSpecification):
    @property
    def IRI(self):
        return URIRef("https://w3id.org/pmd/co/SoftwareEnvPending")

#--------------------------------------------------------------------------------------------------

class IndependentContinuant(Continuant):
    @property
    def IRI(self):
        return URIRef("http://purl.obolibrary.org/obo/BFO_0000004")

class MaterialEntity(IndependentContinuant):
    @property
    def IRI(self):
        return URIRef("http://purl.obolibrary.org/obo/BFO_0000040")

class Object(MaterialEntity):
    @property
    def IRI(self):
        return URIRef("http://purl.obolibrary.org/obo/BFO_0000030")

class Device(Object):
    @property
    def IRI(self):
        return URIRef("https://w3id.org/pmd/co/PMD_0000602")

#--------------------------------------------------------------------------------------------------

class SpecificallyDependentContinuant(Continuant):
    @property
    def IRI(self):
        return URIRef("http://purl.obolibrary.org/obo/BFO_0000020")

class RealizableEntity(SpecificallyDependentContinuant):
    @property
    def IRI(self):
        return URIRef("http://purl.obolibrary.org/obo/BFO_0000017")

class Role(RealizableEntity):
    @property
    def IRI(self):
        return URIRef("http://purl.obolibrary.org/obo/BFO_0000023")

class Plan(RealizableEntity):
    @property
    def IRI(self):
        return URIRef("https://w3id.org/pmd/co/PMD_0000014")

class ProjectPlan(Plan):
    @property
    def IRI(self):
        return URIRef("https://w3id.org/pmd/co/ProjectPlanPending")

#--------------------------------------------------------------------------------------------------

class Process(Occurent):
    @property
    def IRI(self):
        return URIRef("http://purl.obolibrary.org/obo/BFO_0000015")

class PlannedProcess(Process):
    @property
    def IRI(self):
        return URIRef("http://purl.obolibrary.org/obo/OBI_0000011")

#--------------------------------------------------------------------------------------------------

class DigitalWorkflowNode(PlanSpecification):
    @property
    def IRI(self):
        return URIRef("https://w3id.org/pmd/co/DigitalWorkflowNodePending")

class DigitalWorkflowAtomicNode(DigitalWorkflowNode):
    @property
    def IRI(self):
        return URIRef("https://w3id.org/pmd/co/DigitalWorkflowAtomicNodePending")

class DigitalWorkflowMacroNode(DigitalWorkflowNode):
    @property
    def IRI(self):
        return URIRef("https://w3id.org/pmd/co/DigitalWorkflowMacroNodePending")

class DigitalWorkflowProcess(PlannedProcess):
    @property
    def IRI(self):
        return URIRef("https://w3id.org/pmd/co/DigitalWorkflowProcessPending")

class DigitalWorkflowAtomicProcess(DigitalWorkflowProcess):
    @property
    def IRI(self):
        return URIRef("https://w3id.org/pmd/co/DigitalWorkflowAtomicProcessPending")

class DigitalWorkflowMacroProcess(DigitalWorkflowProcess):
    @property
    def IRI(self):
        return URIRef("https://w3id.org/pmd/co/DigitalWorkflowMacroProcessPending")

#--------------------------------------------------------------------------------------------------

class NodePortRole(Role):
    @property
    def IRI(self):
        return URIRef("https://w3id.org/pmd/co/NodePortRolePending")

class NodeInputPortRole(NodePortRole):
    @property
    def IRI(self):
        return URIRef("https://w3id.org/pmd/co/NodeInputPortRolePending")

class NodeOutputPortRole(NodePortRole):
    @property
    def IRI(self):
        return URIRef("https://w3id.org/pmd/co/NodeOutputPortRolePending")

#--------------------------------------------------------------------------------------------------

class DigitalWorkflowPlan(Plan):
    @property
    def IRI(self):
        return URIRef("https://w3id.org/pmd/co/DigitalWorkflowPlanPending")

class DigitalWorkflowAtomicPlan(DigitalWorkflowPlan):
    @property
    def IRI(self):
        return URIRef("https://w3id.org/pmd/co/DigitalWorkflowAtomicPlanPending")

class DigitalWorkflowMacroPlan(DigitalWorkflowPlan):
    @property
    def IRI(self):
        return URIRef("https://w3id.org/pmd/co/DigitalWorkflowMacroPlanPending")

#--------------------------------------------------------------------------------------------------

class StringValueSpecification(ValueSpecification):
    @property
    def IRI(self):
        return URIRef("https://w3id.org/pmd/co/StringValueSpecificationPending")


        




        