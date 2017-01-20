# sinatra-yaml_2_hug-python_bootstraper

* Got sinatra or yaml'ed microframework ?
* just describe models, a little magic and boom

'''
#  python3 /usr/local/bin/gunicorn main:__hug_wsgi__
[2017-01-20 04:01:46 +0100] [1486] [INFO] Starting gunicorn 19.6.0
[2017-01-20 04:01:46 +0100] [1486] [INFO] Listening at: http://127.0.0.1:8000 (1486)
[2017-01-20 04:01:46 +0100] [1486] [INFO] Using worker: sync
[2017-01-20 04:01:46 +0100] [1489] [INFO] Booting worker with pid: 1489

/#######################################################################                       AUTO HUG-API BOOTSTRAPER
                - We populate models so you don't have to -
/#######################################################################
[*] Looking for a hug
[*] Bootstrapping Models
  -> Model : relays
     Database : ../control.maison.apoui.net/db/relays.yml
     ->  Populating API with datas from relays
         Ok!
     -> Bringing Up Controller
        Ok!
     -> Mapping controller to URLs:
        * Collection : GET /relays
        * Ressource GET: /relays/{id}
     Ok!
  -> Model : sensors
     Database : ../control.maison.apoui.net/db/sensors.yml
     ->  Populating API with datas from sensors
         Ok!
     -> Bringing Up Controller
        Ok!
     -> Mapping controller to URLs:
        * Collection : GET /sensors
        * Ressource GET: /sensors/{id}
     Ok!
[*] Our job is done here. Now hope for the best
^C[2017-01-20 04:02:26 +0100] [1486] [INFO] Handling signal: int
[2017-01-20 04:02:26 +0100] [1489] [INFO] Worker exiting (pid: 1489)
[2017-01-20 04:02:27 +0100] [1486] [INFO] Shutting down: Master
'''
