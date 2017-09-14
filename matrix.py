from copy import deepcopy
from json import load, dumps
from random import choice
from time import sleep
from uuid import uuid4

GREEN='\033[0;32m'

with open("/Users/burkel/matrix.json") as matrix_json:
    JSON=load(matrix_json)

while True:
    temp_json=deepcopy(JSON)
    temp_json["data"][0]["data"]["@id"] = str(uuid4())
    temp_json["data"][0]["data"]["actor"]["extensions"]["orgId"] = str(uuid4())
    temp_json["data"][0]["data"]["actor"]["extensions"]["orgRefId"] = str(uuid4())
    delete = str(choice(list(temp_json["data"][0]["data"]["object"])))
    del temp_json["data"][0]["data"]["object"][delete]
    print("New event payload ==========================================>")
    print(GREEN + dumps(temp_json, indent=4, sort_keys=True))
    sleep(0.5)
