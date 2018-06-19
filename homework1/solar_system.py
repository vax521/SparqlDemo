import rdflib
from rdflib import URIRef, BNode, Literal
from rdflib import Namespace
from rdflib.namespace import RDF, FOAF

g = rdflib.Graph()

entity_namespace = Namespace('http://example.org/entity/')
relation_namespace = Namespace('http://example.org/relation/')


planet = relation_namespace.planet
# 恒星
stellar = relation_namespace.stellar
# 矮行星
Dwarf_planet = relation_namespace.Dwarf_planet
satellite = relation_namespace.satellite

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
# 土星
Saturn = entity_namespace.Saturn
# 天王星
Uranus = entity_namespace.Uranus
# 海王星
Neptune = entity_namespace.Neptune
# 冥王星
Pluto = entity_namespace.Pluto
# 月球
Moon = entity_namespace.Moon

g.add((sun, RDF.type, stellar))

# 添加水星数据
g.add((Mercury, distance_to_the_sun, Literal(0.38709893)))
g.add((Mercury, radius, Literal(2440)))
g.add((Mercury, quality, Literal(0.05)))
g.add((Mercury, rotation_period, Literal("58.646d")))
g.add((Mercury, revolution_period, Literal("87.9d")))
g.add((Mercury, RDF.type, planet))
g.add((Mercury, planet, sun))

# 添加金星数据
g.add((Venus, distance_to_the_sun, Literal(0.725)))
g.add((Venus, radius, Literal(2440)))
g.add((Venus, quality, Literal(0.82)))
g.add((Venus, rotation_period, Literal(243)))
g.add((Venus, revolution_period, Literal(224.7)))
g.add((Venus, RDF.type, planet))
g.add((Venus, planet, sun))

# 添加地球数据
g.add((Earth, distance_to_the_sun, Literal(1)))
g.add((Earth, radius, Literal(6371)))
g.add((Earth, quality, Literal(1)))
g.add((Earth, rotation_period, Literal("24h")))
g.add((Earth, revolution_period, Literal("365d")))
g.add((Earth, RDF.type, planet))
g.add((Earth, planet, sun))

# 添加火星数据
g.add((Mars, distance_to_the_sun, Literal(1.524)))
g.add((Mars, radius, Literal(3397)))
g.add((Mars, quality, Literal(0.11)))
g.add((Mars, rotation_period, Literal("24.5h")))
g.add((Mars, revolution_period, Literal("1.9a")))
g.add((Mars, RDF.type, planet))
g.add((Mars, planet, sun))

# 添加木星数据
g.add((Jupiter, distance_to_the_sun, Literal(5.2)))
g.add((Jupiter, radius, Literal(7194)))
g.add((Jupiter, quality, Literal(317.94)))
g.add((Jupiter, rotation_period, Literal("9.5h")))
g.add((Jupiter, revolution_period, Literal("11.8a")))
g.add((Jupiter, RDF.type, planet))
g.add((Jupiter, planet, sun))

# 添加土星数据
g.add((Saturn, distance_to_the_sun, Literal(9.54)))
g.add((Saturn, radius, Literal(60330)))
g.add((Saturn, quality, Literal(95.18)))
g.add((Saturn, rotation_period, Literal("10h")))
g.add((Saturn, revolution_period, Literal("29.5a")))
g.add((Saturn, RDF.type, planet))
g.add((Saturn, planet, sun))

# 添加天王星数据
g.add((Uranus, distance_to_the_sun, Literal(19.18)))
g.add((Uranus, radius, Literal(51118)))
g.add((Uranus, quality, Literal(14.63)))
g.add((Uranus, rotation_period, Literal("16h")))
g.add((Uranus, revolution_period, Literal("84.0a")))
g.add((Uranus, RDF.type, planet))
g.add((Uranus, planet, sun))


# 添加海王星数据
g.add((Neptune, distance_to_the_sun, Literal(30.13)))
g.add((Neptune, radius, Literal(49532)))
g.add((Neptune, quality, Literal(17.22)))
g.add((Neptune, rotation_period, Literal("18h")))
g.add((Neptune, revolution_period, Literal("164.8a")))
g.add((Neptune, RDF.type, planet))
g.add((Neptune, planet, sun))

# 添加冥王星数据
g.add((Pluto, distance_to_the_sun, Literal(40)))
g.add((Pluto, radius, Literal(1150)))
g.add((Pluto, quality, Literal(0.8)))
g.add((Pluto, rotation_period, Literal("6.3d")))
g.add((Pluto, revolution_period, Literal("248a")))
g.add((Pluto, RDF.type, Dwarf_planet))
g.add((Pluto, Dwarf_planet, sun))


# 月球数据
g.add((Moon, distance_to_the_sun, Literal(1)))
g.add((Moon, radius, Literal(1738)))
g.add((Moon, quality, Literal(0.0125)))
g.add((Moon, rotation_period, Literal("27.32d")))
g.add((Moon, revolution_period, Literal("27.32d")))
g.add((Moon, RDF.type, satellite))
g.add((Moon, satellite, Earth))


# q = "select ?distance where { " \
#     "<http://example.org/entity/Moon> " \
#     "<http://example.org/relation/distance_to_the_sun> " \
#     " ?distance}"
# x = g.query(q)
#
# print(x.bindings[0])
#  write graph to file, re-read it and query the newly created graph
g.serialize("solar_system.rdf", format="turtle")
# g1 = rdflib.Graph()
# g1.parse("graph.rdf", format="xml")
# x1 = g1.query(q)
# print(list(x1))