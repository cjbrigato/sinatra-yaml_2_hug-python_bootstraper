import yaml
import hug

from models import Relay, Sensor
from controllers import BaseController

# -*- coding: utf-8 -*-

banner = '''
/#######################################################################
                       AUTO HUG-API BOOTSTRAPER
                - We populate models so you don't have to -
/#######################################################################
'''

api_data = {}

def populate_model(model, db):
    global api_data
    print('     ->  Populating API with datas from', model)
    with open(db, 'r', errors='ignore') as stream:
        api_data[model] = yaml.load(stream)
    print('         Ok!')
    #print('>> DONE :', api_data[model])


def bootstrap(models,API):
    print(banner)
    print("[*] Looking for a hug")
    print("[*] Bootstrapping Models")
    # bootstrap
    #@hug.startup()
    for model in models:
        name = model[0]
        db = model[1]
        model_url = '/{0}'.format(name)
        unique_url = model_url + '/{id}'
        print('  -> Model :', name)
        print('     Database :', db)
        populate_model(name, db)
        print('     -> Bringing Up Controller')
        model_controller = BaseController(name, api_data[name])
        print('        Ok!')
        print('     -> Mapping controller to URLs:')
        hug.get(model_url, api=API)(model_controller.get_collection)
        print('        * Collection : GET', model_url)
        hug.get(unique_url, api=API)(model_controller.get_by_id)
        print('        * Ressource GET:', unique_url)
        print('     Ok!')
    print('[*] Our job is done here. Now hope for the best')
