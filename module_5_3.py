class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if 0 < new_floor < self.number_of_floors:
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print("Такого этажа не существует")

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
       return (f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        return self.number_of_floors + value

    def __iadd__(self, value):
        return self.number_of_floors + value

    def __radd__(self, value):
        return self.number_of_floors + value


h1 = House('Брусника', 9)
h2 = House('Нагорный', 20)
h1.go_to(4)
h2.go_to(21)

# __str__
print(len(h1))
print(len(h2))

# __str__
print(h1)
print(h2)

# __eq__
print(h1 == h2)

# __lt__
print(h1 < h2)

# __le__
print(h1 <= h2)

# __gt__
print(h1 > h2)

# __ge__
print(h1 >= h2)

# __ne__
print(h1 != h2)

# __add__
print(h1 + 1)

# __add__
print(h1 + 2)

# __add__
print(h2 + 3)

