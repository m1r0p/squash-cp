###### classes for this project


#class SquashElement:
#    #kind = None
#    #parrent_id = None
#    #inner_objects = list()
#
#    def __init__(self, self_id, name, kind, parrent_id, sub_level):
#        self.self_id = self_id
#        self.name = name
#        self.kind = kind
#        self.parrent_id = parrent_id
#        self.inner_objects = list()
#        self.sub_level = sub_level
#       
#    def add_object(self, objid):
#        self.inner_objects.append(objid)

class SquashElement:
    def __init__(self, self_id, name, kind, sub_level):
        self.self_id = self_id
        self.name = name
        self.kind = kind
        self.sub_level = sub_level
       

class SquashProject(SquashElement):
    def __init__(self, self_id, name, kind, sub_level):
        SquashElement.__init__(self, self_id, name, kind, sub_level)
        self.inner_objects = list()
    
    def add_object(self, objid):
        self.inner_objects.append(objid)

class SquashFolder(SquashElement):
    def __init__(self, self_id, name, kind, sub_level, parrent_id):
        SquashElement.__init__(self, self_id, name, kind, sub_level)
        self.inner_objects = list()
        self.parrent_id = parrent_id
    
    def add_object(self, objid):
        self.inner_objects.append(objid)

class SquashFile(SquashElement):
    def __init__(self, self_id, name, kind, sub_level, parrent_id):
        SquashElement.__init__(self, self_id, name, kind, sub_level)
        self.parrent_id = parrent_id
   
class ReqFile(SquashFile):
    def __init__(
            self, 
            self_id, 
            name, 
            kind, 
            sub_level, 
            parrent_id,
            criticality,
            category,
            status,
            description,
            ):
        SquashFile.__init__(self, self_id, name, kind, sub_level, parrent_id)
        self.criticality = criticality 
        self.category = category
        self.status = status
        self.description = description


