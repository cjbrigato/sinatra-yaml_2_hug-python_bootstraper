import yaml

##
# Ruby-Transitional Ressources + Hug Routers
##


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
