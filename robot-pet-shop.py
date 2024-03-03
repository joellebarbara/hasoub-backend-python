### no ui - you should make it dynamic
### your employee class inherits a lot of unecccessary properties, are you ok with this?


class Robot:
    def __init__(self, main_material, price, cost_to_fix_per_day, name, robot_id, battery_type, animal_type, status="For Sale"):
        self.main_material = main_material
        self.price = price
        self.cost_to_fix_per_day = cost_to_fix_per_day
        self.name = name
        self.robot_id = robot_id
        self.battery_type = battery_type
        self.animal_type = animal_type
        self.status = status

    def sell(self):
        if self.status == "For Sale":
            print(f"Robot {self.name} has been sold for ${self.price}.")
            return self.price
        else:
            print(f"Robot {self.name} is not available for sale.")

    def repair(self):
        if self.status == "Broken":
            print(f"Robot {self.name} is under repair.")
            return self.cost_to_fix_per_day
        else:
            print(f"Robot {self.name} does not need repair.")

    def prepare_for_shipment(self):
        self.status = "Prepared for Shipment"
        print(f"Robot {self.name} is prepared for shipment.")


class Employee(Robot):
    def __init__(self, name, robot_id, battery_type, daily_salary):
        super().__init__("Metal", 0, 0, name, robot_id, battery_type, "Employee", status="Working")
        self.daily_salary = daily_salary

    def get_salary(self):
        return self.daily_salary


class RobotPetShop:
    def __init__(self):
        self.balance = 0
        self.pets_for_sale = []
        self.robots_in_repair = []
        self.employees = []

    ### is this selling or adding to the inventory? if its adding, why change the balance?
    def add_robot_for_sale(self, robot):
        self.pets_for_sale.append(robot)
        self.balance += robot.price

    def add_robot_in_repair(self, robot):
        self.robots_in_repair.append(robot)
        self.balance -= robot.cost_to_fix_per_day

    def add_employee(self, employee):
        self.employees.append(employee)
        self.balance -= employee.daily_salary

    def print_pets_for_sale(self):
        print("Robots available for sale:")
        for robot in self.pets_for_sale:
            print(f"{robot.name} - Price: ${robot.price}")

    def print_robots_in_repair(self):
        print("Robots in repair:")
        for robot in self.robots_in_repair:
            print(f"{robot.name} - Repair Cost per Day: ${robot.cost_to_fix_per_day}")

    def print_pets_in_price_range(self, min_price, max_price):
        print(f"Robots available for sale in the price range ${min_price} - ${max_price}:")
        for robot in self.pets_for_sale:
            if min_price <= robot.price <= max_price:
                print(f"{robot.name} - Price: ${robot.price}")

    def print_employees_salary_cost(self):
        total_salary_cost = sum(employee.get_salary() for employee in self.employees)
        print(f"Total employees' salary cost: ${total_salary_cost}")

    def print_store_balance(self):
        print(f"Store Balance: ${self.balance}")

    def print_robot_details(self, identifier):
        for robot in self.pets_for_sale + self.robots_in_repair + self.employees:
            if robot.robot_id == identifier or robot.name == identifier:
                print(f"Robot Details for {robot.name}:")
                print(f"ID: {robot.robot_id}")
                print(f"Main Material: {robot.main_material}")
                print(f"Battery Type: {robot.battery_type}")
                print(f"Animal Type: {robot.animal_type}")
                ### good detial to notice
                if isinstance(robot, Employee):
                    print(f"Daily Salary: ${robot.daily_salary}")
                else:
                    print(f"Price: ${robot.price}")
                    print(f"Cost to Fix per Day: ${robot.cost_to_fix_per_day}")
                    print(f"Status: {robot.status}")
                return
        print(f"No robot found with ID or name: {identifier}")


shop = RobotPetShop()

### dry + magic numbers + hardcoding
robot1 = Robot("Iron", 100, 10, "RoboDog", 1, "Lithium", "Carnivore")
robot2 = Robot("Steel", 150, 15, "RoboCat", 2, "Alkaline", "Herbivore")

employee1 = Employee("RoboWorker1", 101, "Lithium", 50)
employee2 = Employee("RoboWorker2", 102, "Alkaline", 60)

shop.add_robot_for_sale(robot1)
shop.add_robot_for_sale(robot2)
shop.add_employee(employee1)
shop.add_employee(employee2)

shop.print_pets_for_sale()
shop.print_robots_in_repair()
shop.print_pets_in_price_range(100, 200)
shop.print_employees_salary_cost()
shop.print_store_balance()

robot1.sell()
robot2.prepare_for_shipment()

shop.print_store_balance()

shop.print_robot_details(1)
shop.print_robot_details("RoboCat")
