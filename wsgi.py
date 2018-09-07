import datetime
from dateutil.relativedelta import relativedelta, MO
from flask import Flask, current_app, abort, make_response
from ical import generate_school_bus_calendar

def create_app() -> Flask:
    ''' Return a Flask application '''

    # Get these from official ICS ?? .env ?
    # first_monday = arrow.get('2018-09-03')
    # last_monday = arrow.get('2019-07-01')
    # holidays_file = ('calendrier_scolaire_20172018_et_20182019.ics')


    app = Flask(__name__)

    return app

FLASK_APP = create_app()

@FLASK_APP.route('/planning/<planning_name>.ics', methods=['GET'])
def get_ical(planning_name: str) -> str:
    '''
    Return the bus calendar for current year
    '''
    if planning_name == 'bus':
        result = generate_school_bus_calendar()
    # elif planning_name == '6a':
    #     from ical import schedule_6a as requested_planning
    # elif planning_name == '6f':
    #     from ical import schedule_6f as requested_planning
    else:
        abort(404)

    

    response = make_response(result.to_ical())
    response.headers['Content-Type'] = 'text/calendar; charset=utf-8'

    return response
