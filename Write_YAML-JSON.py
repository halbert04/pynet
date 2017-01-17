import yaml
import json

my_list = range (5)
my_list.append ('hello')
my_list.append ('blablabla')
my_list.append ({})
my_list [-1] ['ip_addr'] = '10.154.20.50'
my_list [-1] ['attribs'] = range(4)

with open("my_yaml.yml", "w") as f:
    f.write(yaml.dump(my_list, default_flow_style=False))

with open ("my_json.json", "w") as f:
    json.dump(my_list, f)

