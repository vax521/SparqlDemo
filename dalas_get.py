from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://dbpedia.org/sparql/")
Query_Texas_Citys = """PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
   SELECT * WHERE {
    ?city rdf:type <http://dbpedia.org/class/yago/WikicatCitiesInTexas>
  }
"""
# 查询德克萨斯州各个城市总人口
Query_Texas_Citys_popTotal = """
      PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
      PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#>
      PREFIX dbp:<http://dbpedia.org/ontology/>
      SELECT * WHERE {
      ?city rdf:type <http://dbpedia.org/class/yago/WikicatCitiesInTexas>;
      dbp:populationTotal ?popTotal.
      }
"""
# 查询德克萨斯州各个城市总人口以及地铁人口
Query_Texas_Citys_popTotal_popMetro = """
 PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
      PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#>
      PREFIX dbp:<http://dbpedia.org/ontology/>
      SELECT * WHERE {
      ?city rdf:type <http://dbpedia.org/class/yago/WikicatCitiesInTexas>;
      dbp:populationTotal ?popTotal;
      dbp:populationMetro ?popMetro.
      }
"""
# optionalaa选项 注意dbp:populationTotal ?popTotal后面要加.。
Query_Texas_Citys_popTotal_popMetro_ifexited = """
 PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
      PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#>
      PREFIX dbp:<http://dbpedia.org/ontology/>
      SELECT * WHERE {
      ?city rdf:type <http://dbpedia.org/class/yago/WikicatCitiesInTexas>;
      dbp:populationTotal ?popTotal. 
      optional { ?city dbp:populationMetro ?popMetro.}
      }
"""
# 查询德克萨斯州各个城市总人口,结果按照总人口降序返回。最多返回10个结果，从第5 个结果开始。
Query_Texas_Citys_popTotal_ORDER = """
      PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
      PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#>
      PREFIX dbp:<http://dbpedia.org/ontology/>
      SELECT * WHERE {
      ?city rdf:type <http://dbpedia.org/class/yago/WikicatCitiesInTexas>;
      dbp:populationTotal ?popTotal.
      }
      ORDER BY desc(?popTotal)
      LIMIT 10
      OFFSET 5
"""
# 使用filter过滤数据，仅返回总人数超过50,000的城市
Query_Texas_Citys_popTotal_popMetro_filter = """
 PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
      PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#>
      PREFIX dbp:<http://dbpedia.org/ontology/>
      SELECT * WHERE {
      ?city rdf:type <http://dbpedia.org/class/yago/WikicatCitiesInTexas>;
      dbp:populationTotal ?popTotal.
      optional { ?city dbp:populationMetro ?popMetro.}
      filter(?popTotal>50000)
      }
      order by desc(?popTotal)
"""
# rdfs：label是通常用于表示资源的人类可读名称的RDFS谓词。
# 返回具有结果的每个城市的可读的中文名称
Query_Texas_Citys_popTotal_popMetro_label = """
 PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
      PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#>
      PREFIX dbp:<http://dbpedia.org/ontology/>
      SELECT * WHERE {
      ?city rdf:type <http://dbpedia.org/class/yago/WikicatCitiesInTexas>;
      dbp:populationTotal ?popTotal;
      rdfs:label ?name.
      optional { ?city dbp:populationMetro ?popMetro.}
      filter(?popTotal>50000 && langmatches(lang(?name),"zh"))
      }
      order by desc(?popTotal)
"""
# 只匹配名称中具有“El”的城市
Query_Texas_Citys_popTotal_popMetro_regex = """
  PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
      PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#>
      PREFIX dbp:<http://dbpedia.org/ontology/>
      SELECT * WHERE {
      ?city rdf:type <http://dbpedia.org/class/yago/WikicatCitiesInTexas>;
      dbp:populationTotal ?popTotal;
      rdfs:label ?name.
      optional { ?city dbp:populationMetro ?popMetro.}
      filter(?popTotal>50000 && lang(?name)="en" &&
      regex(str(?name), "E"))
      }
      order by desc(?popTotal)
"""
sparql.setQuery(Query_Texas_Citys_popTotal_popMetro_regex)
sparql.setReturnFormat(JSON)
results = sparql.query().convert()
# for result in results["results"]["bindings"]:
#     print(result['city']['value'], '城市总人口：', result['popTotal']['value'], '地铁人口：', result['popMetro']['value'])
for result in results["results"]["bindings"]:
    print(result['city']['value'], '城市名称:', result['name']['value'])


