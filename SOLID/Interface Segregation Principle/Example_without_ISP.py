from abc import ABC, abstractmethod

class Worker(ABC):
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass

class SuperWorker(Worker):
    def work(self):
        return "Super working"

    def eat(self):
        return "Super eating"

class OrdinaryWorker(Worker):
    def work(self):
        return "Ordinary working"

    def eat(self):
        return "Ordinary eating"

# Client code
def manage_worker(worker):
    print(worker.work())
    print(worker.eat())

# Creating instances
super_worker = SuperWorker()
ordinary_worker = OrdinaryWorker()

# Using the workers
manage_worker(super_worker)      # Output: Super working \n Super eating
manage_worker(ordinary_worker)   # Output: Ordinary working \n Ordinary eating
