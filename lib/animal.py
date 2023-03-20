class Animal:

    all = []

    def __init__(self, species, weight, nickname, zoo):
        self.species = species
        self.weight = weight
        self.nickname = nickname
        self.zoo = zoo
        Animal.all.append(self)

    @classmethod
    def find_by_species(cls, species):
        # filtered = []
        # for animal in cls.all:
        #     if animal.species == species:
        #         filtered.append(animal)
        # return filtered
        return [a for a in cls.all if a.species == species]





