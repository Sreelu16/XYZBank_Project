import json
import os
from dotenv import load_dotenv

load_dotenv()


def readJson(jsonFilePath):
    if os.getenv('local'):
        with open(os.path.abspath(jsonFilePath)) as f:
            jsonFile = json.load(f)
    else :
        with open(os.getcwd() + jsonFilePath) as f:
            jsonFile = json.load(f)

    return jsonFile
