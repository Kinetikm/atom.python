from datetime import date


class Task:
    def __init__(self, title, estimate, state='In progress'):
        self.title = title
        try:
            self.estimate = date(estimate)
            self.state = state
            return self
        except Exception as ex:
            print('There is bad type of estimate')

    def is_failed(self):
        if (self.estimate - date.today() < 0) and self.state == 'In progress':
            return True
        else:
            return False

    def remaining(self):
        return self.estimate - date.today()

    def ready(self):
        self.state = 'Ready'
        return self