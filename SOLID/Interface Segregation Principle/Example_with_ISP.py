from abc import ABC, abstractmethod

class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class SuperWorker(Workable, Eatable):
    def work(self):
        return "Super working"

    def eat(self):
        return "Super eating"

class OrdinaryWorker(Workable, Eatable):
    def work(self):
        return "Ordinary working"

    def eat(self):
        return "Ordinary eating"

# Client code
def manage_worker(worker):
    if isinstance(worker, Workable):
        print(worker.work())
    if isinstance(worker, Eatable):
        print(worker.eat())

# Creating instances
super_worker = SuperWorker()
ordinary_worker = OrdinaryWorker()

# Using the workers
manage_worker(super_worker)      # Output: Super working \n Super eating
manage_worker(ordinary_worker)   # Output: Ordinary working \n Ordinary eating
