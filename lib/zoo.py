from animal import Animal
import ipdb
class Zoo(Animal):

    all = []

    def __init__(self, name, location):
        self.name = name
        self.location = location
        Zoo.all.append(self)

    def animals(self):
        list = []
        for animal in Animal.all:
            if animal.zoo == self:
                list.append(animal)
        return list
    
    def animal_species(self):
        species = []
        for animal in Animal.all:
            if animal.species not in species:
                species.append(animal.species)
        return species
    
    def find_by_species(self, species):
        animal_list = []
        for animal in Animal.all:
            if animal.species == species:
                animal_list.append(animal)
        return animal_list
    
    def animal_nicknames(self):
        nickname_list = []
        for animal in Animal.all:
            nickname_list.append(animal.nickname)
        return nickname_list

    @classmethod
    def find_by_location(cls, location):
        filtered = []
        for zoo in cls.all:
            if zoo.location == location:
                filtered.append(zoo)
        return filtered


z1 = Zoo( 'Micke Grove Zoo', 'Lodi, CA' )
a1 = Animal( 'Lion', 75, 'Luke', z1 )
a2 = Animal( 'Dog', 50, 'Ammo', z1 )
a3 = Animal( 'Dog', 50, 'Cici', z1 )

z2 = Zoo('Bronx Zoo', 'The Bronx')
a1 = Animal( 'Lion', 75, 'Luke', z2 )
a2 = Animal( 'Dog', 50, 'Ammo', z2 )
a3 = Animal( 'Dog', 50, 'Cici', z2 )



ipdb.set_trace()