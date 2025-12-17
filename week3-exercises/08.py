import json

python_dict = { "username": "Sara", "email": "saratuemayh@gmail.com", "active_status": True}

json_data = json.dumps(python_dict)

print(json_data)