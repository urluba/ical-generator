import datetime
from dateutil.relativedelta import relativedelta, MO
from flask import Flask, current_app, abort, make_response
from ical import generate_school_bus_calendar, get_school_weeks
from ical import generate_6f_calendar, generate_6a_calendar

def create_app() -> Flask:
    ''' Return a Flask application '''

    app = Flask(__name__)
    app.config['school_weeks'] = get_school_weeks()

    return app

FLASK_APP = create_app()

@FLASK_APP.route('/planning/<planning_name>.ics', methods=['GET'])
def get_ical(planning_name: str) -> str:
    '''
    Return the bus calendar for current year
    '''

    if planning_name == 'bus':
        result = generate_school_bus_calendar(current_app.config['school_weeks'])
    elif planning_name == '6a':
        result = generate_6a_calendar(current_app.config['school_weeks'])
    elif planning_name == '6f':
        result = generate_6f_calendar(current_app.config['school_weeks'])
    else:
        abort(404)

    response = make_response(result.to_ical().decode().replace('\r\n ', '').replace('\r\n', '\n'))
    response.headers['Content-Type'] = 'text/calendar; charset=utf-8'

    return response
