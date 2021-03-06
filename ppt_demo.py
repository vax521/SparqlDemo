from SPARQLWrapper import SPARQLWrapper, JSON


#查询所有的可用的RDF图
Query_all_usable_g = """
SELECT DISTINCT ?g WHERE {
GRAPH ?g {?s ?p ?o}
} LIMIT 1000
"""

# 查询
Query_book_author = """
PREFIX : <http://dbpedia.org/resource/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dbo: <http://dbpedia.org/ontology/>

SELECT ?author_name ?title

WHERE {
    ?author rdf:type dbo:Writer.
    ?author rdfs:label ?author_name.
    ?author dbo:notableWork ?work.
    ?work rdfs:label ?title .
}
"""
# 查询所有作家和他们的著名作品
query_author_notableWork = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX dbo: <http://dbpedia.org/ontology/>
SELECT ?author ?work
WHERE {
?author rdf:type dbo:Writer ;
dbo:notableWork ?work .
} LIMIT 100
"""
# 是否存在一个有著名作品的作家
ask_author_notableWrok = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX dbo: <http://dbpedia.org/ontology/>
ASK
WHERE {
?author rdf:type dbo:Writer .
?author dbo:notableWork ?work .
}
"""
# 查询所有没有著名作品的作家
query_no_authorwithbook = """
PREFIX : <http://dbpedia.org/resource/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dbo: <http://dbpedia.org/ontology/>
SELECT ?author
WHERE {
    ?author rdf:type dbo:Writer
    FILTER NOT EXISTS {?author dbo:notableWork ?work.}
} LIMIT 100
"""
# describe
query_deacribe = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX dbo: <http://dbpedia.org/ontology/>
DESCRIBE ?author ?work
WHERE {
    ?author rdf:type dbo:Writer.
    ?author dbo:notableWork ?work.
} LIMIT 10
"""
# 逻辑合取
query_union = """
PREFIX : <http://dbpedia.org/resource/>
PREFIX dbo: <http://dbpedia.org/ontology/>
SELECT ?influencer ?influenced
WHERE{
    { :Jules_Verne dbo:influenced ?influenced.}
    UNION
    { :Jules_Verne dbo:influencedBy ?influencer.}
}
"""
query_regex = """
PREFIX : <http://dbpedia.org/resource/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dbo: <http://dbpedia.org/ontology/>
SELECT ?author_name ?title
WHERE {
    ?author rdf:type dbo:Writer .
    ?author rdfs:label ?author_name .
    FILTER (LANG(?author_name)="en").
    ?author dbo:notableWork ?work .
    ?work rdfs:label ?title .
    FILTER (LANG(?title)="en").
    FILTER REGEX (?title, "love", "i").
} LIMIT 100
"""
query_graph_usable = """
SELECT DISTINCT ?g
WHERE {
GRAPH ?g { ?s ?p ?o . }
}
"""
# 选择所有所有作者及其著名著作和出版年份
query_author_date = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dbo: <http://dbpedia.org/ontology/>
PREFIX dbp: <http://dbpedia.org/property/>
SELECT ?author ?work ?date
WHERE {
    ?author rdf:type dbo:Writer.
    ?author dbo:notableWork ?work.
    ?work dbp:releaseDate ?date.
} 
GROUP BY ?author
ORDER BY ?date
LIMIT 100
"""
query ="""
SELECT ?author ?work ?date
WHERE {
    ?author rdf:type dbo:Writer.
    ?author dbo:notableWork ?work.
    ?work dbp:releaseDate ?date.
} 
GROUP BY ?author
LIMIT 100
"""

# ppt上的例子 dian
temp = """
     SELECT COUNT(?movie) SAMPLE(?movie) ?label
     WHERE {
         dbr:A_Trip_to_the_Moon dct:subject ?o.
         ?movie dct:subject ?o.
         ?movie rdfs:label ?label.
         FILTER(?movie != dbr:A_Trip_to_the_Moon).
    }
    GROUP BY ?movie ?label
    ORDER BY DESC(COUNT(?movie))
    LIMIT 3
"""


sparql = SPARQLWrapper("http://dbpedia.org/sparql/")
sparql.setQuery("""
     SELECT ?label
     WHERE {
         dbr:A_Trip_to_the_Moon dct:subject ?o.
         ?movie dct:subject ?o.
         ?movie rdfs:label ?label.
         FILTER(?movie != dbr:A_Trip_to_the_Moon).
    }
    GROUP BY ?movie ?label
    ORDER BY DESC(COUNT(?movie))
    LIMIT 3
""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()
# print(results)
print(type(results))
print(results)
for result in results["results"]["bindings"]:
    print(result)