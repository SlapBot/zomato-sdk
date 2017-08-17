import re
import os
import json
from zomato.zomato import Zomato


def do_init(instance="common"):
    z = Zomato(API_KEY="e74778cd3728858df3578092ecea02cf")
    # o = getattr(s, instance)
    if instance.lower() == "common":
        return z.common
    elif instance.lower() == "location":
        return z.location
    return z.restaurant


def get_test_data(filename="testingdata/categories.json"):
    # filename = os.path.abspath(filename)
    directory = os.path.dirname(__file__)
    filename = os.path.join(directory, filename)
    with open(filename) as jsonfile:
        data = json.load(jsonfile)
        jsonfile.close()
    return data


def convert_to_snake_case(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()