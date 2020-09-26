from datetime import timedelta, datetime
from typing import List

from icalendar import Calendar, Event

from .due_model import DueModel


def generate_ical(info: List[DueModel]):
    cal = Calendar()
    cal['summary'] = "WebCMS3 Due date calendar"

    event = Event()
    event.add('summary', "NEW")
    event.add('dtstart', datetime.now())
    event.add('description', "Calendar was updated on " + str(datetime.now()))

    for i in info:
        due = Event()
        due.add('dtstart', i.due_date - timedelta(minutes=10))  # 10 mins before
        due.add('dtend', i.due_date)
        due.add('summary', i.name)
        due.add('description', i.course_code + " " + i.url)

        cal.add_component(due)

    return cal.to_ical()
