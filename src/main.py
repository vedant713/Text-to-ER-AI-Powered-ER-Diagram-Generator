import argparse
from .parser import ERParser
from .diagram_generator import ERDiagramGenerator

def main():
    parser = argparse.ArgumentParser(description="Generate ER diagram from text")
    parser.add_argument("input_file", help="Text file with ER description")
    parser.add_argument("-o", "--output", default="er_diagram", 
                       help="Output file name")
    args = parser.parse_args()

    with open(args.input_file) as f:
        content = f.read()

    er_parser = ERParser()
    er_parser.parse(content)
    
    generator = ERDiagramGenerator(er_parser.entities, er_parser.relationships)
    generator.generate(args.output)

if __name__ == "__main__":
    main()