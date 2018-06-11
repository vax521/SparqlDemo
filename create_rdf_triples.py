from rdflib import URIRef, BNode, Literal
from rdflib import Namespace
from rdflib.namespace import RDF, FOAF
from rdflib import Graph

bob = URIRef("http://example.org/people/Bob")
linda = BNode()  # a GUID is generated

name = Literal("bob")
age = Literal(29)
height = Literal(1.75)

n = Namespace('http://example.org/people/')
print('n.bob=', n.bob)
print('RDF.type=', RDF.type)
print('FOAF.knows=', FOAF.knows)

# add triples
from rdflib import Graph
g = Graph()

g.add((bob, RDF.type, FOAF.Person))
g.add((bob, FOAF.name, name))
g.add((bob, FOAF.knows, linda))
g.add((linda, RDF.type, FOAF.Person))
g.add((linda, FOAF.name, Literal('Linda')))

# 将rdf三元组存储为文件
print(g.serialize('./data/person.nt', format='turtle'))


# set方法
g.add((bob, FOAF.age, Literal(42)))
print("Bob is ", g.value( bob, FOAF.age ))
# prints: Bob is 42

g.set((bob, FOAF.age, Literal(43) ) ) # replaces 42 set above
print("Bob is now ", g.value( bob, FOAF.age ))
# prints: Bob is now 43

g.parse("http://danbri.livejournal.com/data/foaf")
for s, _, n in g.triples((None, FOAF['member_name'], None)):
    g.add((s, FOAF['name'], n))