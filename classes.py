###### classes for this project


class SquashElement:
    #kind = None
    #parrent_id = None
    #inner_objects = list()

    def __init__(self, self_id, name, kind, parrent_id, sub_level):
        self.self_id = self_id
        self.name = name
        self.kind = kind
        self.parrent_id = parrent_id
        self.inner_objects = list()
        self.sub_level = sub_level
       
    def add_object(self, objid):
        self.inner_objects.append(objid)

