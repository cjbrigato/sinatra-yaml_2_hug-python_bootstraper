from falcon import HTTP_400


class BaseController(object):

    def __init__(self, ressource, collection):
        self.ressource = ressource
        self.collection = collection

    def get_collection(self):
        document = {
            'Type': 'Collection',
            'Ressource': self.ressource.capitalize()
        }
        objects = []
        for c in self.collection:
            objects.append(c.__dict__)
        document['Object'] = objects
        return document

    def get_by_id(self, id: int, response):
        if id < 1:
            response.status = HTTP_400
            return {"error": "ids start at 1", "is_this_a_joke": "nope just a very old legacy off by one"}
        else:
            try:
                o = self.collection[(id - 1)].__dict__
            except IndexError:
                response.status = HTTP_400
                return {'error': 'No such ressource'}
            return {
                'Type': self.ressource.capitalize(),
                'Object': o
            }
