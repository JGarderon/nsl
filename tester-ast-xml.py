
import ast

import ast, re, sys
from xml.dom import minidom

from xml.etree import cElementTree as etree 
import xml.etree.ElementTree as ET

def prettify(xml_string):
    reparsed = minidom.parseString(xml_string)
    return reparsed.toprettyxml(indent="  ") 

class ast2xml(ast.NodeVisitor):
    def __init__(self):
        super(ast.NodeVisitor, self).__init__()
        self.path = []
        self.root = etree.Element('ast')
        self.celement = self.root
    def convert(self, tree):
        self.visit(tree)
        return etree.tostring(self.root)
    def generic_visit(self, node):
        node_name = type(node).__name__
        self.path.append(node_name)
        ocelement = self.celement
        self.celement = etree.SubElement(self.celement, node_name)
        for item in node.__dict__:
            if isinstance(getattr(node, item), ast.AST):
                self.generic_visit(getattr(node, item))
            elif isinstance(getattr(node, item), list):
                ocel2 = self.celement
                self.celement = etree.SubElement(self.celement, item)
                [self.generic_visit(childnode) for childnode in getattr(node, item) if isinstance(childnode, (ast.AST, list))]
                self.celement = ocel2
            else:
                self.celement.attrib.update({item: str(getattr(node, item))})
        self.path.pop()
        self.celement = ocelement

if __name__=="__main__":  

    # création 

    tree = ast.parse('''
def ok(m):
    return m+" !"
ok(1)
ok("coucou")
''') 
    print(ast.dump( tree )) 

    # transformation AST -> XML 
    
    res = ast2xml().convert(tree)
    #print(prettify(res)) 

    # transformation XML -> AST

    root = ET.fromstring( res ) 
    print(root) 

    for valeurConstante in root.iter('Constant'):
        print(valeurConstante.tag) 
        print(valeurConstante.attrib)
        valeurConstante.attrib['value'] = valeurConstante.attrib['value']+"**"

    print(prettify( ET.tostring(root, encoding="unicode", method="xml") )) 



