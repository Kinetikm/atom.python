import Task
from datetime import date


class Roadmap:
    def __init__(self, tasks=[]):
        self.tasks = tasks
        if len(tasks) != 0:
            if not all(isinstance(n, Task) for n in tasks):
                raise ValueError('Bad type of tasks')
            return self
        else:
            return self

    def today(self):
        return [task for task in self.tasks if task.estimate == date.today()]

    def filter(self, state):
        return [task for task in self.tasks if task.state == state]