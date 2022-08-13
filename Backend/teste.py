import json
# dados em json
data_JSON = """
                {
  "name": "bulbasaur",
  "attributes": {
    "hp": 45,
    "attack": 49,
    "defense": 49,
    "special_attack": 65,
    "special_defense": 65,
    "speed": 45
  }
}
"""
#transformando json em dicionario
data_dict = json.loads(data_JSON)
print (data_dict)
print(data_dict["name"])
#imprimindo item de cada chave do dicionario
print(data_dict["attributes"])
 
#dados em dicionario python
jsonStr =  '{"name":"Tesla", "age":2, "city":"New York"}'

# parse json file
pythonObj = json.loads(jsonStr)
#print type of object
print(pythonObj)
#access elements in the object
name = pythonObj['name']
print(name)
teste = teste
