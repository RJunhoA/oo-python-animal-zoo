from animal import Animal
import ipdb
class Zoo(Animal):

    all = []

    def __init__(self, name, location):
        self.name = name
        self.location = location
        Zoo.all.append(self)

    @property
    def animals(self):
        # list = []
        # for animal in Animal.all:
        #     if animal.zoo == self:
        #         list.append(animal)
        # return list
        return [a for a in Animal.all if a.zoo == self]
    
    @property
    def animal_species(self):
        # species = []
        # for animal in Animal.all:
        #     if animal.species not in species:
        #         species.append(animal.species)
        # return species
        return {a.species for a in self.animals}
    
    def find_by_species(self, species):
        # animal_list = []
        # for animal in Animal.all:
        #     if animal.species == species:
        #         animal_list.append(animal)
        # return animal_list
        return [a for a in Animal.all if a.species == species]
    
    @property
    def animal_nicknames(self):
        # nickname_list = []
        # for animal in Animal.all:
        #     nickname_list.append(animal.nickname)
        # return nickname_list
        return [a.nickname for a in self.animals if a.zoo == self]

    @classmethod
    def find_by_location(cls, location):
        # filtered = []
        # for zoo in cls.all:
        #     if zoo.location == location:
        #         filtered.append(zoo)
        # return filtered
        return [z for z in cls.all if z.location == location]


z1 = Zoo( 'Micke Grove Zoo', 'Lodi, CA' )
a1 = Animal( 'Lion', 75, 'Luke', z1 )
a2 = Animal( 'Dog', 50, 'Ammo', z1 )
a3 = Animal( 'Dog', 50, 'Cici', z1 )

z2 = Zoo('Bronx Zoo', 'The Bronx')
a1 = Animal( 'Lion', 75, 'Luke', z2 )
a2 = Animal( 'Dog', 50, 'Ammo', z2 )
a3 = Animal( 'Dog', 50, 'Cici', z2 )



ipdb.set_trace()