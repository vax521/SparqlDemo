from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://data.linkedmdb.org/sparql")
# sparql = SPARQLWrapper("http://data.linkedmdb.org/")

query_recommend ="""
  PREFIX m: <http://data.linkedmdb.org/resource/movie/>
  PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
  PREFIX foaf:  <http://xmlns.com/foaf/0.1/>
SELECT ?filmTitle ?director_name WHERE {
   { SELECT ?director   WHERE {
         ?film rdfs:label "Lost in Translation";
               m:director ?director.
     }
  ?director  m:director_name ?director_name
  ?film rdfs:label ?filmTitle.
}
"""
query_recommend_also ="""
  PREFIX m: <http://data.linkedmdb.org/resource/movie/>
  PREFIX owl: <http://www.w3.org/2002/07/owl#>
  PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?movie WHERE {
         ?film rdfs:label "Lost in Translation";
               owl:sameAs ?movie.
     }
}
"""

Query_movies = """
   PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
SELECT * WHERE { 
    GRAPH ?g { 
       ?film rdf:type <http://dbpedia.org/ontology/Film>.
    } 
}
"""
Query_books = """
   PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
SELECT * WHERE { 
    GRAPH ?g { 
       ?book rdf:type <http://dbpedia.org/ontology/Book>.
    } 
}
"""

Query_games = """
   PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    SELECT * WHERE { 
     GRAPH ?g { 
       ?book rdf:type <http://dbpedia.org/ontology/Game>.
    } 
}
"""

Query_book_author = """
   PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
     SELECT ?book ?author WHERE { 
       ?book rdf:type <http://dbpedia.org/ontology/Book>;
       ?author rdf:type <http://dbpedia.org/ontology/Author>.
    }
"""
Query_one_book = """
      PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
         SELECT * WHERE {
      ?book rdf:type <http://dbpedia.org/resource/Citizens:_A_Chronicle_of_the_French_Revolution>.
}
"""
Query_movie_temp = """
   PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
SELECT * WHERE { 
    GRAPH ?g { 
        ?book rdf:type <http://dbpedia.org/resource/Citizens:_A_Chronicle_of_the_French_Revolution>.
    } 
}
"""
query = """
PREFIX m:<http://data.linkedmdb.org/resource/movie/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?filmTitle WHERE {
  ?film rdfs:label ?filmTitle.
  ?film m:director ?dir.
  ?dir  m:director_name "Sofia Coppola".
} LIMIT 3
"""
sparql.setQuery(query)
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

for result in results["results"]["bindings"]:
    print(result)