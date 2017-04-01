from yaml import YAMLError
from Task import Task
from datetime import date
from parse import get_dataset

class Roadmap:

    def __init__(self, tasks=None):
        if tasks is None:
            self.tasks = []
        elif isinstance(tasks, str):
            try:
                self.tasks = [Task(title=x[0], state=x[1], estimate=x[2]) for x in get_dataset(tasks)]
            except YAMLError:
                raise YAMLError("Error in format")
            except ValueError as e:
                raise ValueError("Error in data")
            except OSError as e:
                raise OSError("Error in file")
            except Exception as e:
                raise Exception("Unknown")
        elif isinstance(tasks, list):
            if not all(isinstance(n, Task) for n in tasks):
                raise ValueError('Bad type of tasks')
            self.tasks = tasks
        else:
            raise ValueError("Not supported object provided")

    def today(self):
        return [task for task in self.tasks if task.estimate == date.today()]

    def filter(self, state):
        return filter(lambda x: x.state == state, self.tasks)

    def get_critical(self):
        return Roadmap(tasks=[x for x in self.tasks if x.is_critical])

    def __str__(self):
        return "Roadmap{%s}" % '\t\n'.join(map(str, self.tasks))

    def __repr__(self):
        return str(self)