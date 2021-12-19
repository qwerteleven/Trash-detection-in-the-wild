
import json



with open('./annotations.json') as f:
    data = json.load(f)

print(data['info'])

print(data['annotations'][0]['image_id'])
