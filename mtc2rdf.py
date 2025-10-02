import sys
import owlready2 as owl
from ontologies import MTConnect
from mtconnect_to_onto import MTConnectToOnto
from generate_diagram import GenerateDiagram
from iof_render import dl_render_terminology, dl_render_class, Namespaces
from indented_logger import setup_logging, increase_indent, decrease_indent
from indented_logger.decorator import log_indent
import logging
import logger
from generate_html import render_vendor, render_terminology
from pyshacl import validate
from glob import glob
from rdflib import Graph

logger = logging.getLogger(__name__)

MTConnect.load(only_local=True)
render_terminology("MTConnect", MTConnect)

if len(sys.argv) < 2:
    print("Usage: python script.py <file>")
    sys.exit(1)

file_name = sys.argv[1]

trans = None
with open(file_name, 'r') as file:
    print("Gettig MTConnect XML from:", file_name)

    xml = file.read()
    trans = MTConnectToOnto(xml)
    trans.convert()
    trans.write()

all_data = list(owl.default_world.sparql(f"""select ?s ?p ?o {{ ?s ?p ?o . FILTER(LIKE(STR(?s), "{trans.Data.base_iri}%")) }}"""))
full = GenerateDiagram(f"MazakFull", all_data)
logger.info("Generating full diagram")
full.generate()

data_graph = "Mazak-Data.rdf"
ont_graph = "mtconnect.rdf"

print("\n-----------------------------------------------\n")

error_graph = Graph()

for shacl in glob("shacl/*.shacl"):
  print("\nValidating with SHACL file:{}\n".format(shacl))
  shacl_graph = shacl
  shacl_report, shacl_graph, shacl_text = validate(data_graph,
        shacl_graph=shacl_graph,
        ont_graph=ont_graph,
        inference='rdfs',
        abort_on_first=False,
        allow_infos=True,
        allow_warnings=True,
        meta_shacl=False,
        advanced=False,
        js=False,
        debug=False)

  print(shacl_report)
  print(shacl_text)
  error_graph += shacl_graph

  print("\n-----------------------------------------------\n")
  
with open("shacl_errors.ttl", "wb") as errors:
  errors.write(error_graph.serialize(format='turtle').encode("utf-8"))


  
