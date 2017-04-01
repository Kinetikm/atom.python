from datetime import date, timedelta

READY = 'ready'
IN_PROGRESS = 'in_progress'
VALID_STATES = {READY, IN_PROGRESS}


class Task:

    def __init__(self, title, estimate, state=IN_PROGRESS):
        self.title = title
        if isinstance(estimate, date):
            self.estimate = estimate
        else:
            raise ValueError("Incorrect date!")
        if state in VALID_STATES:
            self.state = state
        else:
            raise ValueError("Incorrect state!")

    @property
    def is_failed(self):
        return date.today() < self.estimate and self.state == READY

    @property
    def remaining(self):
        return timedelta() if self.state == READY else self.estimate - date.today()

    @property
    def is_critical(self):
        return self.is_failed or (self.state == IN_PROGRESS and self.remaining.days < 3)

    def ready(self):
        self.state = READY

    def __str__(self):
        return 'Task(title="%s",estimate=%s,state=%s)' % (self.title, self.estimate, self.state)

    def __repr__(self):
        return str(self)