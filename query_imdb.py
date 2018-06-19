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
<<<<<<< HEAD
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
=======
>>>>>>> 720b330dcd7912e2ea6eb6667d1e0b292c05a9ba
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

<<<<<<< HEAD
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
=======
save = """
 PREFIX m: <http://data.linkedmdb.org/resource/movie/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX dc: <http://purl.org/dc/terms/>
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
        SELECT  ?dir_name ?actor_name ?writer_name ?date ?runtime ?page WHERE {
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
"""
temp = """
>>>>>>> 720b330dcd7912e2ea6eb6667d1e0b292c05a9ba
        PREFIX m: <http://data.linkedmdb.org/resource/movie/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX dc: <http://purl.org/dc/terms/>
        PREFIX foaf: <http://xmlns.com/foaf/0.1/>
<<<<<<< HEAD
        SELECT ?dir_name ?actor_name ?writer_name ?date ?country_name ?runtime ?page WHERE {
=======
        SELECT  ?dir_name ?actor_name ?writer_name ?date  ?page WHERE {
>>>>>>> 720b330dcd7912e2ea6eb6667d1e0b292c05a9ba
          ?film rdfs:label 'Buffy the Vampire Slayer';
                m:director ?dir;
                m:actor    ?actor;
                m:writer   ?writer;
                dc:date    ?date;
<<<<<<< HEAD
                m:country  ?country;
                m:runtime  ?runtime;
=======
                
        
>>>>>>> 720b330dcd7912e2ea6eb6667d1e0b292c05a9ba
                foaf:page   ?page.
                
               ?dir  m:director_name ?dir_name.
               ?actor m:actor_name   ?actor_name.
<<<<<<< HEAD
               ?writer m:writer_name ?writer_name.           
        }
=======
               ?writer m:writer_name ?writer_name.
        }
"""

# YES
temp_rec = """
     PREFIX dct: <http://purl.org/dc/terms/>
     PREFIX film: <http://data.linkedmdb.org/resource/film/>

     SELECT COUNT(?film) SAMPLE(?movie)
     WHERE {
         film:1 dct:subject ?o.
         ?film  dct:subject ?o.
         FILTER(?film != film:1)
    }
    GROUP BY ?film
    ORDER BY DESC(COUNT(?film))
"""

sparql = SPARQLWrapper("http://data.linkedmdb.org/sparql/")
sparql.setQuery("""
        PREFIX m: <http://data.linkedmdb.org/resource/movie/>
        PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        SELECT COUNT(?film) AS ?film_nums
        WHERE {
             ?film rdf:type m:film.
        }
        
>>>>>>> 720b330dcd7912e2ea6eb6667d1e0b292c05a9ba
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

<<<<<<< HEAD
=======
# with open("./data/movie_p.csv", mode="a+", encoding="utf-8") as f:
#     f.seek(0)
#     f.truncate()
#     for result in results["results"]["bindings"]:
#         print(result)
#         f.write(str(result)+"\n")
for result in results["results"]["bindings"]:
    print(result)
# print(results)
>>>>>>> 720b330dcd7912e2ea6eb6667d1e0b292c05a9ba
