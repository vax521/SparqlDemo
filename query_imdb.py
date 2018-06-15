from SPARQLWrapper import SPARQLWrapper, JSON
# publication retrieval recommend system
# 查询所有可用的p
query_p = """
SELECT DISTINCT ?p WHERE {?s ?p ?o}
"""
# 查询所有可用的s
query_s = """
SELECT DISTINCT ?s WHERE {?s ?p ?o} limit(10000)
"""
query_o = """
SELECT DISTINCT ?o WHERE {?s ?p ?o}
"""
query_movie_allinfo = """
PREFIX m: <http://data.linkedmdb.org/resource/movie/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?filmTitle ?dir ?prod ?writer WHERE {
  ?film rdfs:label ?filmTitle.
  ?film m:director ?dir.
  ?film m:producer_name ?prod.
  ?file m:writer_name   ?writer .
  
  ?dir  m:director_name "Sofia Coppola".
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

test_query = """
PREFIX m: <http://data.linkedmdb.org/resource/movie/>
PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    SELECT ?director ?dir_name
    WHERE {
     ?director rdf:type m:director.
     ?director m:director_name ?dir_name.
    } LIMIT 50
"""
query = """
     PREFIX m: <http://data.linkedmdb.org/resource/movie/>
     PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
     PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    SELECT ?film ?film_name
    WHERE {
         ?film rdf:type m:film.
         ?film rdfs:label ?film_name.
    }
"""
query_movie_by_movie = """
        PREFIX m: <http://data.linkedmdb.org/resource/movie/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX foaf:  <http://xmlns.com/foaf/0.1/>
        SELECT ?filmTitle WHERE {
            ?film rdfs:label 'The Shining'.
            ?film m:director ?director.
            ?director foaf:made ?other_movie.
            ?other_movie rdfs:label ?filmTitle.
            FILTER(?filmTitle != 'The Shining') 
        }
        LIMIT 3
"""
sparql = SPARQLWrapper("http://data.linkedmdb.org/sparql")
sparql.setQuery("""
        PREFIX m: <http://data.linkedmdb.org/resource/movie/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX dc: <http://purl.org/dc/terms/>
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
        SELECT ?dir_name ?actor_name ?writer_name ?date ?country_name ?runtime ?page WHERE {
          ?film rdfs:label 'Buffy the Vampire Slayer';
                m:director ?dir;
                m:actor    ?actor;
                m:writer   ?writer;
                dc:date    ?date;
                m:country  ?country;
                m:runtime  ?runtime;
                foaf:page   ?page.
                
               ?dir  m:director_name ?dir_name.
               ?actor m:actor_name   ?actor_name.
               ?writer m:writer_name ?writer_name.           
        }
""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()
print(results)
finished_product = {}

for item in results['head']['vars']:
    a = set()
    for row in results['results']['bindings']:
        a.add(row[item]['value'])
    finished_product[item] = a
print(finished_product)

