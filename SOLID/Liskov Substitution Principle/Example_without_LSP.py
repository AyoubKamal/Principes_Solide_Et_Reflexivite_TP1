class Bird:
    def fly(self):
        return "I can fly"

class Penguin(Bird):
    def fly(self):
        # Penguins can't fly, violating LSP
        return "I can't fly"

def bird_info(bird):
    return bird.fly()

# Creating instances
bird = Bird()
penguin = Penguin()

# Displaying information
print(bird_info(bird))      # Output: I can fly
print(bird_info(penguin))   # Output: I can't fly (violates LSP)
