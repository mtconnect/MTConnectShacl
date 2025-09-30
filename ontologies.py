import owlready2 as owl
import os
import re
import logger

# owl.default_world.set_backend(filename = "./ontologies.sqlite3")
path = os.path.dirname(os.path.abspath(__file__))

# owl.set_log_level(10)
print("Loading ontologies")
owl.onto_path.append(f"file:///{path}")

if os.path.exists(f"{path}/mtconnect.rdf"):
  with open(f"{path}/mtconnect.rdf", "rb") as f:
    MTConnect = owl.get_ontology("https://purl.mtconnect.org/ontology/").load(only_local = True, fileobj=f)
  MTConnect.base_iri = "https://purl.mtconnect.org/ontology/"

