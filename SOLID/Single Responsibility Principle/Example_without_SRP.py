class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class EmployeeManagement:
    def __init__(self, employees):
        self.employees = employees

    def hire_employee(self, employee):
        # Logique pour embaucher un employé
        self.employees.append(employee)

    def fire_employee(self, employee):
        # Logique pour licencier un employé
        self.employees.remove(employee)

    def generate_report(self):
        # Logique pour générer un rapport basé sur la liste des employés
        # Cette méthode effectue deux responsabilités différentes
        pass

if __name__ == "__main__":
    employees = []  # Initialiser une liste d'employés
    emp_management = EmployeeManagement(employees)

    emp_management.hire_employee(Employee("John Doe", 50000))
    emp_management.generate_report()
