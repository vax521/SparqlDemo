from SPARQLWrapper import SPARQLWrapper, JSON


# 共247个国家
query_all_country = """
    PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX m:<http://data.linkedmdb.org/resource/movie/>
    
    SELECT COUNT(?country_name)
      WHERE {
       ?country rdf:type m:country.
       ?country m:country_name ?country_name.
      }
"""
# 共 2500 部电影
query_all_movies = """
    PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX m:<http://data.linkedmdb.org/resource/movie/>
    SELECT ?film ?country_name
      WHERE {
       ?film rdf:type m:film.
       ?film m:country ?country.
       ?country m:country_name ?country_name.
      }
"""


# 作家总数: 81427
# 简介：dbo:abstract ?abstract
# 姓名：foaf:name ?name;
# 性别：foaf:gender
# 国籍：dbp:nationality ?nationality
query_all_writers = """
     SELECT   ?name ?gender  ?nationality ?abstract
     WHERE {
     ?author rdf:type dbo:Writer;
             foaf:name ?name;
             foaf:gender ?gender;
             dbp:nationality ?nationality;
             dbo:abstract ?abstract.
     }  
"""

pic = """
SELECT ?author SAMPLE(?thumbnail)
    WHERE {
    ?author rdf:type dbo:Writer.
    OPTIONAL { ?scientist dbo:thumbnail ?thumbnail}
    }
    LIMIT 10
"""


#  游戏总数 1748
query_all_games = """
     SELECT DISTINCT ?game ?designer_name ?name ?date
     WHERE{
        ?game rdf:type dbo:Game; 
              foaf:name ?name;
              dbo:designer ?designer;
              dbp:date  ?date.
        ?designer foaf:name ?designer_name.
    } 
    
"""

# sparql = SPARQLWrapper("http://data.linkedmdb.org/sparql")
sparql = SPARQLWrapper("http://dbpedia.org/sparql/")
sparql.setQuery(query_all_games)
sparql.setReturnFormat(JSON)
results = sparql.query().convert()
print(results)
for result in results["results"]["bindings"]:
    print(result)
