from datetime import datetime


class DueModel:
    def __init__(self, course_code: str, name: str, due_date: datetime, url: str):
        self.course_code = course_code
        self.name = name
        self.due_date = due_date
        self.url = url

    def __repr__(self):
        return str({
            'course_code': self.course_code,
            'name': self.name,
            'due_date': self.due_date,
            'url': self.url
        })
