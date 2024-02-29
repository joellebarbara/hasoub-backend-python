class TaskScheduler:
    def __init__(self):
        self.week_schedule = [[None] * 8 for _ in range(5)]
        self.day_to_index = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4}

    def print_schedule(self):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        print("\nWeekly Schedule:")
        print("{:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12}".format("Day", "8 AM", "9 AM", "10 AM", "11 AM", "12 PM", "1 PM", "2 PM"))
        for i, day in enumerate(self.week_schedule):
            print("{:<12}".format(days[i]), end="")
            for hour in day:
                if hour:
                    print("{:<12}".format(hour), end="")
                else:
                    print("{:<12}".format("Free"), end="")
            print()

    def add_task(self, task_name, task_duration, day=None, starting_hour=None):
        if day is not None and starting_hour is not None:
            if self.is_time_range_available(day, starting_hour, task_duration):
                self.populate_time_range(day, starting_hour, task_name, task_duration)
                print(f"Task '{task_name}' added to the schedule on {day} at {starting_hour}:00 for {task_duration} hours.")
            else:
                conflicting_task = self.get_conflicting_task(day, starting_hour)
                print(f"Time range is already populated with '{conflicting_task}'.")
                decision = input("Do you want to overwrite the old task with the new task? (yes/no): ").lower()
                if decision == "yes":
                    self.overwrite_task(day, starting_hour, task_name, task_duration)
                    print(f"Task '{task_name}' overwritten at {day} {starting_hour}:00.")
                else:
                    new_day = input("Enter a new day for the task: ").capitalize()
                    new_starting_hour = int(input("Enter a new starting hour for the task: "))
                    self.add_task(task_name, task_duration, new_day, new_starting_hour)
        else:
            for i in range(5):
                for j in range(9 - task_duration):
                    if self.is_time_range_available(i, j, task_duration):
                        self.populate_time_range(i, j, task_name, task_duration)
                        print(f"Task '{task_name}' added to the schedule on {self.get_day_name(i)} at {j}:00 for {task_duration} hours.")
                        return
            print(f"No available time range found for '{task_name}' with duration {task_duration} hours.")

    def is_time_range_available(self, day, starting_hour, duration):
        index = self.day_to_index[day]
        for hour in range(starting_hour, starting_hour + duration):
            if self.week_schedule[index][hour]:
                return False
        return True

    def get_conflicting_task(self, day, starting_hour):
        index = self.day_to_index[day]
        conflicting_task = self.week_schedule[index][starting_hour]
        return conflicting_task

    def populate_time_range(self, day, starting_hour, task_name, duration):
        index = self.day_to_index[day]
        for hour in range(starting_hour, starting_hour + duration):
            self.week_schedule[index][hour] = task_name

    def overwrite_task(self, day, starting_hour, task_name, duration):
        index = self.day_to_index[day]
        for hour in range(starting_hour, starting_hour + duration):
            self.week_schedule[index][hour] = task_name

    def get_day_name(self, day):
        return ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"][day]


def main():
    task_scheduler = TaskScheduler()

    while True:
        task_name = input("Enter task name (or 'exit' to finish): ")
        if task_name.lower() == 'exit':
            break

        task_duration = int(input("Enter task duration in hours: "))
        specific_day = input("Enter specific day (leave empty for any): ").capitalize()
        starting_hour = int(input("Enter starting hour (leave empty for any): ") or -1)

        task_scheduler.add_task(task_name, task_duration, specific_day, starting_hour)

    task_scheduler.print_schedule()


main()
