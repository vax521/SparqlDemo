from SPARQLWrapper import SPARQLWrapper, JSON

# 查询所有可用的p
query_p = """
SELECT DISTINCT ?p WHERE {?s ?p ?o}
"""

# 查询由 Sofia Coppola 执导的电影
query_movie_dirBySofia = """
PREFIX m: <http://data.linkedmdb.org/resource/movie/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?filmTitle WHERE {
  ?film rdfs:label ?filmTitle.
  ?film m:director ?dir.
  ?dir  m:director_name "Sofia Coppola".
}
"""
# 查询在 Sofia Coppola 执导的电影中出现的所有演员：
query_movie_dirBySofia_actorname = """
PREFIX m: <http://data.linkedmdb.org/resource/movie/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?actorName ?filmTitle WHERE {
  ?film rdfs:label ?filmTitle;
        m:director ?dir;
        m:actor ?actor.
  ?dir  m:director_name "Sofia Coppola".
  ?actor m:actor_name ?actorName.
}
"""
# 查询列出 Sofia 和 Francis Ford Coppola 电影中共用的演员
query_actor = """
PREFIX m: <http://data.linkedmdb.org/resource/movie/>

SELECT DISTINCT ?actorName WHERE {
 
  ?dir1     m:director_name "Sofia Coppola".
 
  ?dir2     m:director_name "Francis Ford Coppola".
 
  ?dir1film m:director ?dir1;
            m:actor ?actor.
 
  ?dir2film m:director ?dir2;
            m:actor ?actor.
 
  ?actor    m:actor_name ?actorName.
}
"""
sparql = SPARQLWrapper("http://data.linkedmdb.org/sparql")
sparql.setQuery(query_actor)
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

for result in results["results"]["bindings"]:
    print(result)