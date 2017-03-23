import Task
from datetime import date


class Roadmap:
    def __init__(self, tasks=None):
        self.tasks = tasks
        if tasks is not None:
            if not all(isinstance(n, Task) for n in tasks):
                raise ValueError('Bad type of tasks')
            return self
        else:
            self.tasks = []
            return self

    def today(self):
        return [task for task in self.tasks if task.estimate == date.today()]

    def filter(self, state):
        return [task for task in self.tasks if task.state == state]