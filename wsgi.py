import datetime
from dateutil.relativedelta import relativedelta, MO
from flask import Flask, current_app, abort
from ical import render_calendar
from ics import Calendar
import arrow

def create_app() -> Flask:
    ''' Return a Flask application '''

    # Get these from official ICS ?? .env ?
    # first_monday = arrow.get('2018-09-03')
    # last_monday = arrow.get('2019-07-01')
    holidays_file = ('calendrier_scolaire_20172018_et_20182019.ics')


    app = Flask(__name__)
    with open(holidays_file) as file_descriptor:
        app.config['holidays_calendar'] = Calendar(file_descriptor.read())

    app.config['first_school_monday'] = arrow.get('2018-09-03')
    app.config['last_school_monday'] = arrow.get('2019-07-01')

    return app

FLASK_APP = create_app()

@FLASK_APP.route('/planning/<planning_name>', methods=['GET'])
def get_ical(planning_name: str) -> str:
    '''
    Return the bus calendar for current year
    '''
    if planning_name == 'bus':
        from ical import schedule_bus as requested_planning
    elif planning_name == '6a':
        from ical import schedule_6a as requested_planning
    elif planning_name == '6f':
        from ical import schedule_6f as requested_planning
    else:
        abort(404)

    today = datetime.datetime.utcnow()
    first_monday = arrow.get(today + relativedelta(weekday=MO(-1)))
    last_monday = arrow.get(first_monday + relativedelta(months=1))

    if last_monday >= first_monday:
        last_monday = current_app.config['last_school_monday']

    result = render_calendar(
        planning=requested_planning,
        start_monday=first_monday,
        end_monday=last_monday,
        holidays_calendar=current_app.config['holidays_calendar']
    )

    return str(result)
