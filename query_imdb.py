from SPARQLWrapper import SPARQLWrapper, JSON
# publication retrieval recommend system
# 查询所有可用的p
query_p = """
SELECT DISTINCT ?p WHERE {?s ?p ?o}
"""

# 查询所有可用的s
query_s = """
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT DISTINCT ?s WHERE {
                ?s rdfs:label ?o
                } limit(10000)
"""
# 查询名为"Lost in Translation"的电影导演,演员，上映年份
query_movie_director_by_moviename ="""
PREFIX m: <http://data.linkedmdb.org/resource/movie/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT DISTINCT ?dir_name ?actor_name ?writer_name ?language WHERE {
  ?film rdfs:label "Lost in Translation";
        m:director ?dir;
        m:actor    ?actor;
        m:writer   ?writer;
        m:language ?language.
        
       ?dir  m:director_name ?dir_name.
       ?actor m:actor_name   ?actor_name.
       ?writer m:writer_name ?writer_name.
}
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
sparql.setQuery(query_movie_director_by_moviename)
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

# with open("./data/movie_p.csv", mode="a+", encoding="utf-8") as f:
#     f.seek(0)
#     f.truncate()
#     for result in results["results"]["bindings"]:
#         print(result)
#         f.write(str(result)+"\n")
for result in results["results"]["bindings"]:
    print(result)
# print(results)