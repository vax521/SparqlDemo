from rdflib import Graph
import pprint

g = Graph()
g.parse("./data/demo.nt", format="nt")
print("len(g)=", len(g))

for ssmt in g:
    pprint.pprint(ssmt)

# read remote graphs
g.parse("http://bigasterisk.com/foaf.rdf")
print("***", len(g))
# prints 42
