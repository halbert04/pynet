import yaml
import json

with open ("my_yaml.yml") as f:
    new_list = yaml.load(f)

with open ("my_json.json") as f:
    new_list1 = json.load(f)

from pprint import pprint as pp
pp (new_list)
pp (new_list1) 
