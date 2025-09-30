
import xml.etree.ElementTree as ET
import owlready2 as owl
from indented_logger import setup_logging, increase_indent, decrease_indent
from indented_logger.decorator import log_indent
import logging
import logger
from ontologies import *
from mtconnect_to_particulars import MTConnectToParticulars
from device import Device

logger = logging.getLogger(__name__)

class MTConnectToOnto:
  """Convert MTConnect XML to IOF OWL format."""
  def __init__(self, xml):
    self.xml_content = xml
    self.root = ET.fromstring(self.xml_content)
    print(self.root.tag)
    ns = self.root.tag[1:].split('}')[0]
    self.ns = {'m': ns }

  @log_indent
  def convert(self):
    """Convert the MTConnect XML to IOF OWL format.""" 
    element = self.root.find(".//m:Device", self.ns)
    self.device = Device(self.ns, element)
    
    self.Data = owl.get_ontology("https://mtconnect.org/data/")
    self.Data.base_iri = "https://mtconnect.org/data/"
    self.Data.imported_ontologies.append(MTConnect)

    logger.info(f"Converting device: {self.device.name} ")
    partics = MTConnectToParticulars(self.device, self.Data)
    partics.convert()
            
  def write(self):
    """Write the ontology to a file."""
    logger.info(f"Writing ontology to {self.device.name}")
    self.Data.save(file = f"{self.device.name}-Data.rdf", format = "rdfxml")
