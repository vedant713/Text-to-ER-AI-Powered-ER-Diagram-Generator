from dataclasses import dataclass
from typing import List

@dataclass
class Attribute:
    name: str
    is_primary: bool = False
    is_foreign: bool = False

@dataclass
class Entity:
    name: str
    attributes: List[Attribute]

@dataclass
class Relationship:
    entity1: str
    entity2: str
    relation: str
    cardinality: str = "1:1"