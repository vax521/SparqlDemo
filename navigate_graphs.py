from rdflib import Graph, BNode, Literal
from rdflib import URIRef
from rdflib.namespace import RDF,FOAF

bob = URIRef("http://example.org/people/bob")
linda = BNode()  # a GUID is generated
name = Literal("bob")
age = Literal(29)
height = Literal(1.75)
g = Graph()

g.add((bob, RDF.type, FOAF.Person))
g.add((bob, FOAF.name, name))
g.add((bob, FOAF.knows, linda))
g.add((linda, RDF.type, FOAF.Person))
g.add((linda, FOAF.name, Literal('Linda')))
if (bob, RDF.type, FOAF.Person ) in g:
    print("This graph knows that Bob is a person!")