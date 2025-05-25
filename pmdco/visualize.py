import graphviz

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