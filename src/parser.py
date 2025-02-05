import ollama
import re
from .model import Entity, Attribute, Relationship

class ERParser:
    def __init__(self):
        self.entities = {}
        self.relationships = []

    def parse(self, text: str):    
        try:
            print("DEBUG: Sending text to Ollama LLM...")
            response = ollama.chat(model="llama3", messages=[
                {"role": "system", "content": """
                    Extract entities and relationships from the given text.
                    Format the response as follows:

                    Entity: EntityName [attribute1, attribute2, ...]
                    Relationship: Entity1 -- relationship_name --> Entity2 (cardinality)

                    Example:
                    Entity: Hotel [id*, name, location]
                    Entity: Room [id*, hotel_id, room_number, price]
                    Entity: Customer [id*, name, email]
                    Entity: Booking [id*, customer_id, hotel_id, booking_date]
                    
                    Relationship: Hotel -- has --> Room (1:N)
                    Relationship: Customer -- makes --> Booking (1:N)
                    Relationship: Booking -- belongs_to --> Hotel (1:1)
                    
                    Do not include explanations, just return the structured output.
                """},
                {"role": "user", "content": text}
            ])
            print(f"DEBUG: LLM Response: {response}")

            llm_output = response["message"]["content"]
            print(f"DEBUG: Processed LLM Output: {llm_output}")

            self._process_llm_output(llm_output)
        except Exception as e:
            print(f"ERROR: Failed to communicate with Ollama: {e}")

    def _process_llm_output(self, output):
        try:
            # Ensure correct parsing of structured output
            lines = output.strip().split("\n")
            extracting_entities = False
            extracting_relationships = False

            for line in lines:
                line = line.strip()
                if line.startswith("Entity:"):
                    extracting_entities = True
                    extracting_relationships = False
                    match = re.match(r"Entity:\s*(\w+)\s*\[(.*)\]", line)
                    if match:
                        self._parse_entity(match)
                elif line.startswith("Relationship:"):
                    extracting_entities = False
                    extracting_relationships = True
                    match = re.match(r"Relationship:\s*(\w+)\s*--\s*(\w+)\s*-->\s*(\w+)\s*(?:\((.*)\))?", line)
                    if match:
                        self._parse_relationship(match)

        except Exception as e:
            print(f"ERROR: Failed to process LLM output: {e}")



    def _parse_entity(self, match):
        entity_name, attributes = match.groups()
        attrs = []
        for attr in attributes.split(','):
            attr = attr.strip()
            is_primary = '*' in attr
            name = attr.replace('*', '').strip()
            attrs.append(Attribute(name, is_primary))
        self.entities[entity_name] = Entity(entity_name, attrs)

    def _parse_relationship(self, match):
        entity1, relation, entity2, cardinality = match.groups()
        cardinality = cardinality if cardinality else "1:1"
        self.relationships.append(Relationship(entity1, entity2, relation, cardinality))
