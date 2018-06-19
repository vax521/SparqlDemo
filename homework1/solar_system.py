import rdflib
from rdflib import URIRef, BNode, Literal
from rdflib import Namespace
from rdflib.namespace import RDF, FOAF

g = rdflib.Graph()

entity_namespace = Namespace('http://example.org/entity/')
relation_namespace = Namespace('http://example.org/relation/')
# 到太阳的距离
distance_to_the_sun = relation_namespace.distance_to_the_sun
radius = relation_namespace.radius
quality = relation_namespace.quality
# 自转周期
rotation_period = relation_namespace.rotation_period
# 公转周期
revolution_period = relation_namespace.revolution_period

sun = entity_namespace.sun
# 水星
Mercury = entity_namespace.Mercury
# 金星
Venus = entity_namespace.Venus
Earth = entity_namespace.Earth
# 火星
Mars = entity_namespace.Mars
# 木星
Jupiter = entity_namespace.Jupiter
# 天王星
Uranus = entity_namespace.Uranus
# 海王星
Neptune = entity_namespace.Neptune
# 冥王星
Pluto = entity_namespace.Pluto
# 月球
Moon = entity_namespace.moon

# 添加水星数据
g.add((Mercury, distance_to_the_sun, Literal(0.38709893)))
g.add((Mercury, radius, Literal(2440)))
g.add((Mercury, quality, Literal("3.302×10²³")))
g.add((Mercury, rotation_period, Literal("58.646")))
g.add((Mercury, revolution_period, Literal("87.9")))
# 添加金星数据
g.add((Venus, distance_to_the_sun, Literal(0.725)))
g.add((Venus, radius, Literal(2440)))
g.add((Venus, quality, Literal("4.869×10²⁴")))
g.add((Venus, rotation_period, Literal("243")))
g.add((Venus, revolution_period, Literal("224.7")))


q = "select ?country where { ?country <http://www.example.org/located_in> <http://www.example.org/part1> }"
x = g.query(q)
print
list(x)
# write graph to file, re-read it and query the newly created graph
g.serialize("graph.rdf")
g1 = rdflib.Graph()
g1.parse("graph.rdf", format="xml")
x1 = g1.query(q)
print(list(x1))