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
# optional选项 注意dbp:populationTotal ?popTotal后面要加.。
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
# rdfs:label是通常用于表示资源的人类可读名称的RDFS谓词。
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
      regex(str(?name), "El"))
      }
      order by desc(?popTotal)
"""
# 否定逻辑
# 返回不具备地铁的人口
Query_Texas_Citys_popTotal_popMetro_not = """
   PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
      PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#>
      PREFIX dbp:<http://dbpedia.org/ontology/>
      SELECT * WHERE {
      ?city rdf:type <http://dbpedia.org/class/yago/WikicatCitiesInTexas>;
      dbp:populationTotal ?popTotal.
      optional { ?city dbp:populationMetro ?popMetro.}
      filter(!bound(?popMetro))
      }
      order by desc(?popTotal)
      limit 10
"""
# Union操作符
# 只返回类型为“德克萨斯城市” 或 “加州城市”类型的城市。
Query_Texas_Citys_popTotal_popMetro_union = """
PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
      PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#>
      PREFIX dbp:<http://dbpedia.org/ontology/>
      SELECT * WHERE {
      ?city dbp:populationTotal ?popTotal;
      rdfs:label ?name.
      optional { ?city dbp:populationMetro ?popMetro.}
      filter(?popTotal>50000 && lang(?name)="en")
        {?city rdf:type <http://dbpedia.org/class/yago/WikicatCitiesInTexas>.} 
       UNION 
        {?city rdf:type <http://dbpedia.org/class/yago/CitiesInCalifornia>.}
      }
      order by desc(?popTotal)
      limit 10
"""

# 命名图和GRAPH条款, 每个命名图由URI标识。
# 此查询返回“德克萨斯州城市”类型的城市以及包含每个城市资源的图表。
Query_Texas_graph = """
PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
SELECT * WHERE { 
    GRAPH ?g { 
       ?city rdf:type <http://dbpedia.org/class/yago/WikicatCitiesInTexas>.
    } 
}
"""
# ask查询
# Bad Gateway
Query_ask = """
PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
ASK WHERE { 
    <http://dbpedia.org/resource/Austin,_Texas> rdf:type
    <http://dbpedia.org/class/yago/WikicatCitiesInTexas>.
}
"""
# ask rdf:type后面不加分号
# 询问德克萨斯州是否存在总人口超过60万的城市，而城市人口少于1,800,000
# 返回true
Query_ask_filter = """
    PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX dbp:<http://dbpedia.org/ontology/>
    ASK WHERE {
      ?city rdf:type
       <http://dbpedia.org/class/yago/WikicatCitiesInTexas>; 
       dbp:populationTotal?popTotal; 
       dbp:populationMetro?popMetro.
    FILTER(?popTotal>600000 &&?popMetro<1800000)
    }
"""

# DESCRIBE查询返回描述资源的RDF图。该返回表单的实现取决于每个查询引擎。
# 该查询语句返回奥斯丁的RDF图
Query_Austin_rdf = """
DESCRIBE <http://dbpedia.org/resource/Austin,_Texas>
"""

# 此查询返回一个RDF图，描述德克萨斯州总体人口超过60万，城市人口少于180000的所有城市
Query_desc_Austin = """
PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX dbp:<http://dbpedia.org/ontology/>
DESCRIBE ?city WHERE { 
    ?city rdf:type <http://dbpedia.org/class/yago/WikicatCitiesInTexas>;
    dbp:populationTotal ?popTotal; 
    dbp:populationMetro ?popMetro.
    FILTER(?popTotal > 600000 && ?popMetro < 1800000)
}
"""
# CONSTRUCT查询返回从CONSTRUCT查询中指定的图形模板创建的RDF图。
# 更具体地，通过获取查询模式的结果并填充在构造模板中出现的变量的值来创建结果RDF图。
# 使用CONSTRUCT，您可以将RDF数据转换为具有不同词汇表的不同图形结构。
# 如果您有自动生成的RDF数据，并希望使用众所周知的词汇表进行转换，或者合并来自多个词汇表的RDF数据，
# 这可能很有用。因此，CONSTRUCT是从各种来源消费RDF的强大工具。
# 查询为德克萨斯州的城市人口大于50万的城市构建了新的RDF图
construct_rdf_Austin = '''
    PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs:<http://www.w3.org/2000/01/rdf-schema#>
    PREFIX dbp:<http://dbpedia.org/ontology/>  
    CONSTRUCT {
        ?city rdf:type <http://myvocabulary.com/LargeMetroCitiesInTexas>; 
        <http://myvocabulary.com/cityName>?name; 
        <http://myvocabulary.com/totalPopulation>?popTotal; 
        <http://myvocabulary.com/metroPopulation>?popMetro.
    }
    WHERE { 
    ?city rdf:type <http://dbpedia.org/class/yago/WikicatCitiesInTexas>; 
    dbp:populationTotal ?popTotal; 
    rdfs:label ?name; 
    dbp:populationMetro ?popMetro.
    FILTER(?popTotal> 500000 && langmatches(lang(?name),"EN"))
}
'''
sparql.setQuery(construct_rdf_Austin)
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

# print('德克萨斯州是否存在总人口超过60万的城市，而城市人口少于1,800,000:', results['boolean'])

for result in results["results"]["bindings"]:
    print('S:', result['s'], ',P:', result['p'], ',O:', result['o'])

# for result in results["results"]["bindings"]:
#     print(result['city']['value'], '城市名称:', result['name']['value'])



