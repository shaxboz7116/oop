import random

class RandomSimvols:
    def __init__(self):
        self.rand_simvols = [random.randint(0, 100) for _ in range(15)]

random_obj = RandomSimvols()

print("Tasodifiy sonlar:", random_obj.rand_simvols)