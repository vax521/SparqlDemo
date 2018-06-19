import rdflib

g = rdflib.Graph()
g.parse('solar_system.rdf', format="turtle")

# 查询太阳系的所有行星
query_all_planets = """
  prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
  SELECT ?planet 
  WHERE {
   ?planet rdf:type <http://example.org/relation/planet>.
  }
"""

# 查询太阳系的所有非矮行星
query_not_Dwarf_planet = """
prefix ns1: <http://example.org/relation/> 
SELECT ?star 
    WHERE {
       ?star  ns1:planet <http://example.org/entity/sun>.
       OPTIONAL{
        ?star ns1:satellite <http://example.org/entity/Earth>.}
      }
"""

# 查找离太阳最近的行星
query_least_sun = """
    prefix ns1: <http://example.org/relation/> 
    prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    SELECT ?star 
        WHERE {
           ?star ns1:distance_to_the_sun ?distance .
           ?star rdf:type ns1:planet .
        }
        ORDER BY ?distance
        LIMIT 1
"""

result = g.query(query_not_Dwarf_planet)
print(list(result))
