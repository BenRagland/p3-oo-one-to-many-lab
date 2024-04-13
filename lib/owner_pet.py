class Pet:
    all = []
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    
    def __init__(self,name,pet_type,owner=None):
        self.name = name
        self.owner = owner
        
        
        if (pet_type.lower() in Pet.PET_TYPES):
            self.pet_type = pet_type
        else:
            raise Exception("pet should be in approved list")
        
        if (owner):
            if( isinstance(owner,Owner) ):
                 Pet.all.append(pet_type)  
            else: 
                raise Exception("Owner must be of type Owner") 
 
            
            

        
class Owner:
    def __init__(self,name):
        self.name = name
        self.all_pets = []

    def pets(self):
        return [pet for pet in self.all_pets ]

    def add_pet(self,pet):
        if isinstance(pet,Pet):
            self.all_pets.append(pet)
        else:
            raise Exception("not of Type Pet")
        
    def get_sorted_pets(self,pet):
        if (isinstance(pet,Pet)):
            return [item for item in self.all_pets ]
        else:
            raise Exception("must be type Pet")


# import ipdb; ipdb.set_trace()