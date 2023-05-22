class Triathlon:
    def __init__(self, first_name, last_name, location, swim_time, cycle_time, run_time):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.swim_time = swim_time
        self.cycle_time = cycle_time
        self.run_time = run_time
        self.total_time = swim_time + cycle_time + run_time

    def print_details(self):
        print(f"Name: {self.first_name} {self.last_name} | Location: {self.location} | "
              f"Swim Time: {self.swim_time} | Cycle Time: {self.cycle_time} | "
              f"Run Time: {self.run_time} | Total Time: {self.total_time}")

athlete1 = Triathlon("John", "Doe", "London", 30, 60, 45)
athlete1.print_details()
#Output：Name: John Doe | Location: London | Swim Time: 30 | Cycle Time: 60 | Run Time: 45 | Total Time: 135
