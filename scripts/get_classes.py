import json



f = open("annotations.json",)
training_data = json.load(f)

check_set = set()
name = []

for i in range(len(training_data['categories'])):
    # print(training_data['categories'][0]['name'])
    name.append(str(training_data['categories'][i]['name']))

f.close()


f = open("classes_TACO", "a")

name = list(dict.fromkeys(name))

for classs in name:
    f.write(classs)
    f.write("\n")


f.close()














