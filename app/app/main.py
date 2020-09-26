from flask import Flask, request, make_response
from .request_due import request_webcms
from .ical import generate_ical


app = Flask(__name__)


@app.route('/')
def calendar():
    session = request.args.get('webcms_session')
    if session is None:
        return "PLEASE PROVIDE YOUR OWN WEBCMS SESSIN ID!!!"

    #  turn calendar data into a response
    due_list = request_webcms(session)
    ical_byte = generate_ical(due_list)
    response = make_response(ical_byte)
    response.headers["Content-Disposition"] = "attachment; filename=calendar.ics"
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=80)
