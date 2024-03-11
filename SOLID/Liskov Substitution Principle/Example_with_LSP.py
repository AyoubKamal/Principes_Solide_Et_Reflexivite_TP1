from abc import ABC, abstractmethod

class Bird(ABC):
    @abstractmethod
    def fly(self):
        pass

class FlyingBird(Bird):
    def fly(self):
        return "I can fly"

class Penguin(Bird):
    def swim(self):
        return "I can swim"

    def fly(self):
        raise NotImplementedError("Penguins cannot fly")


def bird_info(bird):
    if isinstance(bird, Bird):
        return bird.fly()
    else:
        raise ValueError("Object should be an instance of Bird")

# Creating instances
flying_bird = FlyingBird()
penguin = Penguin()

# Displaying information
print(bird_info(flying_bird))   # Output: I can fly
#print(bird_info(penguin))      # Raises ValueError (respects LSP)
