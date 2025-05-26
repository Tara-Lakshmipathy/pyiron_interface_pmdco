import graphviz
from IPython.display import SVG
from rdflib import Graph, URIRef
from rdflib.namespace import RDF, RDFS

def gather_classes(cls, max_depth, current_depth=0, classes=None, seen=None):
    if classes is None:
        classes = set()
    if seen is None:
        seen = set()
    if current_depth > max_depth or cls in seen:
        return classes
    classes.add(cls)
    seen.add(cls)
    for subclass in cls.__subclasses__():
        gather_classes(subclass, max_depth, current_depth + 1, classes, seen)
    return classes

def plot_inheritance_from_class(root_cls, max_depth=10):
    classes = gather_classes(root_cls, max_depth)
    dot = graphviz.Digraph()
    for cls in classes:
        dot.node(cls.__name__, 
                 style='filled', 
                 fillcolor='lightblue', 
                 shape='rect', 
                 fontname='Arial',
                 fontsize="10"
                 )
        for base in cls.__bases__:
            if base in classes:
                dot.edge(base.__name__, cls.__name__)
    return dot

def build_node_labels(g, instance_nodes):
    node_info = {}
    # Only collect info for instance nodes
    for s in instance_nodes:
        entry = node_info.setdefault(s, {})
        for p, o in g.predicate_objects(s):
            if p == RDFS.label:
                entry['label'] = str(o)
            elif p == RDF.value:
                entry['value'] = str(o)
            elif p == RDF.type:
                entry['type'] = o  # keep as URIRef for now
    # Look up type_label for each node with a type
    for entry in node_info.values():
        if 'type' in entry and isinstance(entry['type'], URIRef):
            type_label = None
            for lbl in g.objects(entry['type'], RDFS.label):
                type_label = str(lbl)
                break
            if type_label:
                entry['type_label'] = type_label
            else:
                entry['type_label'] = str(entry['type']).split('/')[-1].split('#')[-1]
            entry['type'] = str(entry['type'])
    return node_info

    # Second pass: for each node with type, try to find the label of the type
    for entry in node_info.values():
        if 'type' in entry and isinstance(entry['type'], URIRef):
            type_label = None
            for lbl in g.objects(entry['type'], RDFS.label):
                type_label = str(lbl)
                break
            if type_label:
                entry['type_label'] = type_label
            else:
                # fallback: use local part of type URI
                entry['type_label'] = str(entry['type']).split('/')[-1].split('#')[-1]
            entry['type'] = str(entry['type'])  # Optionally, keep string as well
    return node_info

def make_html_label(info, raw_id):
    label = "<"
    label += '<table BORDER="1" CELLBORDER="0" CELLSPACING="0">'
    # Add all fields, always center
    if 'type_label' in info:
        label += f'<tr><td ALIGN="CENTER" BGCOLOR="lightblue"><font point-size="10" face="monospace">type: {info["type_label"]}</font></td></tr>'
    if 'label' in info:
        label += f'<tr><td ALIGN="CENTER" BGCOLOR="lightyellow"><font point-size="10" face="monospace">label: {info["label"]}</font></td></tr>'
    label += f'<tr><td ALIGN="CENTER" BGCOLOR="lightgray"><font point-size="10" face="monospace">id: </font><font point-size="8" face="monospace">{raw_id}</font></td></tr>'
    if 'value' in info:
        label += f'<tr><td ALIGN="CENTER" BGCOLOR="white"><font point-size="10" face="monospace">value: {info["value"]}</font></td></tr>'
    label += "</table>>"
    return label

def get_property_label(graph, property_uri):
    for label in graph.objects(property_uri, RDFS.label):
        return str(label)
    # Fallback to local name
    s = str(property_uri)
    if '#' in s:
        return s.split('#')[-1]
    else:
        return s.rstrip('/').split('/')[-1]

def visualize(g: Graph):
    dot = graphviz.Digraph('RDF_Graph', engine="dot")
    dot.attr(rankdir='TB')

    # Determine which nodes are instances:
    instance_nodes = set()
    for s, p, o in g:
        if not isinstance(s, URIRef):
            continue
        # If predicate is not rdfs:label and not rdf:type, it's "real" data
        if p != RDF.type and p != RDFS.label:
            instance_nodes.add(s)
    # Also include any node that's the subject of rdf:type (otherwise, type-only nodes vanish from labels)
    for s, p, o in g.triples((None, RDF.type, None)):
        instance_nodes.add(s)

    node_labels = build_node_labels(g, instance_nodes)
    node_ids = {n: str(n).split('/')[-1] for n in node_labels.keys()}

    for node, info in node_labels.items():
        raw_id = node_ids[node]
        label = make_html_label(info, raw_id)
        dot.node(raw_id, label=label, shape='plaintext')

    # Edges only between these instance nodes
    for subj, pred, obj in g:
        if pred == RDF.type:
            continue
        if not (isinstance(subj, URIRef) and isinstance(obj, URIRef)):
            continue
        if subj not in node_labels or obj not in node_labels:
            continue
        subj_id = node_ids[subj]
        obj_id = node_ids[obj]
        pred_label = get_property_label(g, pred)
        dot.edge(subj_id, obj_id, label=pred_label, fontsize='10', fontname="monospace")

    display(SVG(dot.pipe(format='svg')))