import json
json_data = '''{
                "product": "Laptop",
                "price": 75000,
                "available": true
                }
             '''

python_dict = json.loads(json_data)

print(python_dict["product"], python_dict["price"])