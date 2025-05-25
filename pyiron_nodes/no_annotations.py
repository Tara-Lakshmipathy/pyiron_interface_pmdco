from pyiron_workflow import Workflow, as_function_node, as_dataclass_node
from dataclasses import dataclass, field
from semantikon.typing import u
from semantikon.converter import semantikon_class
import typing

@dataclass
class Sentence:
    first_word: str = "Hello"
    last_word: str = "World"

@as_function_node("first_word", "second_word")
def SentenceSplitter(sentence: Sentence) -> typing.Tuple[str,str]:
    first = sentence.first_word
    last = sentence.last_word
    print("Sentence: " + first + " " + last)
    return first, last

@as_function_node("sentence")
def WordsCombiner(first_word: str, last_word: str) -> Sentence:
    sentence_dc = Sentence()
    sentence_dc.first_word = first_word
    sentence_dc.last_word = last_word
    print("Sentence: " + sentence_dc.first_word + " " + sentence_dc.last_word)
    return sentence_dc





