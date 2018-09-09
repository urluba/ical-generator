from datetime import datetime, timedelta, date
from flask import Flask, current_app, abort, make_response
import pytz
from ical import WeeklyPlanning, get_holidays_weeks
from ical import BUS_CALENDAR, SCHOOL_6A_CALENDAR, SCHOOL_6F_CALENDAR

def create_app() -> Flask:
    ''' Return a Flask application '''

    calendars_start = datetime(2018, 9, 3, 0, 0, 0, 0, pytz.utc)
    calendars_end = datetime(2019, 7, 8, 0, 0, 0, 0, pytz.utc)

    app = Flask(__name__)
    app.config['bus_planning'] = WeeklyPlanning(
        name='bus',
        description='Calendrier des bus',
        events=BUS_CALENDAR,
        start=calendars_start,
        end=calendars_end,
        excluded_weeks=get_holidays_weeks(date_start=calendars_start, date_end=calendars_end),
    ).render_calendar()

    app.config['class_6a_planning'] = WeeklyPlanning(
        name='6A',
        description='Calendrier de la 6°A',
        events=SCHOOL_6A_CALENDAR,
        start=calendars_start,
        end=calendars_end,
        excluded_weeks=get_holidays_weeks(date_start=calendars_start, date_end=calendars_end),
    ).render_calendar()

    app.config['class_6f_planning'] = WeeklyPlanning(
        name='6F',
        description='Calendrier de la 6°F',
        events=SCHOOL_6F_CALENDAR,
        start=calendars_start,
        end=calendars_end,
        excluded_weeks=get_holidays_weeks(date_start=calendars_start, date_end=calendars_end),
    ).render_calendar()

    return app

FLASK_APP = create_app()

@FLASK_APP.route('/planning/<planning_name>.ics', methods=['GET'])
def get_ical(planning_name: str) -> str:
    '''
    Return the bus calendar for current year
    '''

    if planning_name == 'bus':
        result = current_app.config['bus_planning']
    elif planning_name == '6a':
        result = current_app.config['class_6a_planning']
    elif planning_name == '6f':
        result = current_app.config['class_6f_planning']
    else:
        abort(404)

    response = make_response(result)
    response.headers['Content-Type'] = 'text/calendar; charset=utf-8'

    return response
