from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://dbpedia.org/sparql/")
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
sparql.setQuery(Query_movie_temp)
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

for result in results["results"]["bindings"]:
    print(result)