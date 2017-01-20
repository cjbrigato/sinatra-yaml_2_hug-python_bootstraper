# From Sinatra to Koala
**beware** : contains very early WiP idea spanked hard by namedroping and flashy graphic material
![N|Solid](http://www.brigato.fr/sinatrug.png)
Got sinatra or yaml'ed microframework ?
Want to move to python with magic and falcon speed ?
Keep your dirty legacy hidden and working with the other side of the force !
# The dirty domotic example
## From Sinatra + yaml
* Fast and bad Ruby Classes serialized as yaml :
```ruby
class Relay
  attr_accessor :id, :name, :localname, :fimage, :description, :place, :masterip
  #[...]
end
class Sensor
  attr_accessor :id, :name, :localname, :fimage, :type, :description, :place, :masterip
  #[...]
end

$relays = YAML.load_file('./db/relays.yml')
$sensors = YAML.load_file('./db/sensors.yml')
```
* Serialized : 
```sh
# cat relays.yml
---
- !ruby/object:Relay
  id: 1
  name: salon.canap.relay1
  localname: relay1
  fimage: fa-lightbulb-o
  description: Salon - GAUCHE Canap
  place: Salon - Canap
  masterip: 192.168.1.42
[...]
# cat sensors.yml
---
- !ruby/object:Sensor
  id: 1
  name: salon.temp.sensor1
  localname: temp.sensor1
  fimage: fa-empire
  type: temperature
  description: Temperature Salon
  place: Salon - Meuble Tv
  masterip: 192.168.1.18
```
## To yaml objects :
```python
class Relay(yaml.YAMLObject):
    """ Constructor for Yaml deserializing from ruby's Relay Model"""
    yaml_tag = '!ruby/object:Relay'

    def __init__(self, id, name, localname, fimage, description, place, masterip):
        self.id = id
        self.name = name
        self.localname = localname
        self.fimage = fimage
        self.description = description
        self.place = place
        self.masterip = masterip

    def __repr__(self):
        return "%s(id=%r, name=%r, localname=%r, fimage=%r, description=%r, place=%r, masterip=%r)" % (self.__class__.__name__, self.id, self.name, self.localname, self.fimage, self.description, self.place, self.masterip)


class Sensor(yaml.YAMLObject):
    """ Constructor for Yaml deserializing from ruby's Sensor Model"""
    yaml_tag = '!ruby/object:Sensor'

    def __init__(self, id, name, localname, fimage, type, description, place, masterip):
        self.id = id
        self.name = name
        self.localname = localname
        self.fimage = fimage
        self.type = type
        self.description = description
        self.place = place
        self.masterip = masterip

    def __repr__(self):
        return "%s(id=%r, name=%r, localname=%r, fimage=%r, type=%r, description=%r, place=%r, masterip=%r)" % (self.__class__.__name__, self.id, self.name, self.localname, self.fimage, self.type, self.description, self.place, self.masterip)
```
* Let's the koala know about our legash*t 
```python
relays_db = '../control.maison.apoui.net/db/relays.yml'
sensors_db = '../control.maison.apoui.net/db/sensors.yml'
models = [('relays', relays_db), ('sensors', sensors_db)]
```
## And that's how Frank goes to hug ..llywood
```sh
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
```
* That's a start.
```sh
# curl 127.0.0.1:8000/relays/1
{"Type": "Relays", "Object": {"masterip": "192.168.1.42", "place": "Salon - Canap", "localname": "relay1", "name": "salon.canap.relay1", "description": "Salon - GAUCHE Canap", "fimage": "fa-lightbulb-o", "id": 1}}
```
```sh
 # curl 127.0.0.1:8000/sensors
{"Type": "Collection", "Ressource": "Relays", "Object": [{"masterip": "192.168.1.42", "place": "Salon - Canap", "localname": "relay1", "name": "salon.canap.relay1", "description": "Salon - GAUCHE Canap", "fimage": "fa-lightbulb-o", "id": 1}, {"masterip": "192.168.1.42", "place": "Salon - Canap", "localname": "relay2", "name": "salon.canap.relay2", "description": "Salon - DROITE Canap", "fimage": "fa-lightbulb-o", "id": 2}, {"masterip": "192.168.1.28", "place": "Chambre - Fond gauche", "localname": "relay1", "name": "chambre.relay1", "description": "Chambre - Grande Lumiere", "fimage": "fa-lightbulb-o", "id": 3}, {"masterip": "192.168.1.28", "place": "Chambre - arriere-lit", "localname": "relay2", "name": "chambre.relay2", "description": "Chambre - Veilleuse Anas <3", "fimage": "fa-moon-o", "id": 4}, {"masterip": "192.168.1.6", "place": "Salon - Meuble TV", "localname": "relay1", "name": "salon.meubletv.relay1", "description": "TV / Wii / FREEBOX (Combo)", "fimage": "fa-television", "id": 5}, {"masterip": "192.168.1.25", "place": "Studio - Cote Gauche (Piano)", "localname": "relay1", "name": "studio.gauche.relay1", "description": "Studio lumire Gauche", "fimage": "fa-music", "id": 6}, {"masterip": "192.168.1.39", "place": "Chambre - arriere-lit", "localname": "relay1", "name": "chambre.relay3", "description": "Chambre - Veilleuse Colin <3", "fimage": "fa-moon-o", "id": 7}]}
```