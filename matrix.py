from copy import deepcopy
from datetime import datetime
from json import load, dumps
from random import choice
from time import sleep
from uuid import uuid4

GREEN='\033[0;32m'
RED='\033[0;31m'

with open("./matrix.json") as matrix_json:
    JSON=load(matrix_json)

while True:
    temp_json=deepcopy(JSON)
    temp_json["data"]["@id"] = str(uuid4())
    temp_json["data"]["actor"]["extensions"]["orgId"] = str(uuid4())
    temp_json["data"]["actor"]["extensions"]["orgRefId"] = str(uuid4())
    temp_json["data"]["eventTime"] = datetime.now().isoformat()
    temp_json["sendTime"] = datetime.now().isoformat()
    delete = str(choice(list(temp_json["data"]["object"])))
    del temp_json["data"]["object"][delete]

    print(RED + "New event payload ==========================================>")
    print(GREEN + dumps(temp_json, indent=4, sort_keys=True))
    sleep(0.25)
