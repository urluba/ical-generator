from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta, MO, SU
from icalendar import Calendar, Event
import pytz

BUS_CALENDAR_START = datetime(2018, 9, 3)
BUS_CALENDAR_END = datetime(2019, 7, 8)

SCHOOL_CALENDAR_START = BUS_CALENDAR_START
SCHOOL_CALENDAR_END = BUS_CALENDAR_END

BUS_CALENDAR = [
    dict(
        summary='roseraie',
        start=(7, 51),
        duration=timedelta(minutes=1),
        location='roseraie',
        rrule=dict(
            byday=['MO', 'TU', 'WE', 'TH', 'FR'],
        )
    ),
    dict(
        summary='roseraie',
        start=(8, 57),
        duration=timedelta(minutes=1),
        location='roseraie',
        rrule=dict(
            byday=['MO', 'TU', 'WE', 'TH', 'FR'],
        )
    ),
    dict(
        summary='place du clos',
        start=(12, 38),
        duration=timedelta(minutes=1),
        location='place du clos',
        rrule=dict(
            byday=['WE'],
        )
    ),
    dict(
        summary='place du clos',
        start=(15, 42),
        duration=timedelta(minutes=1),
        location='place du clos',
        rrule=dict(
            byday=['MO', 'TU', 'WE', 'TH', 'FR'],
        )
    ),
    dict(
        summary='place du clos',
        start=(16, 42),
        duration=timedelta(minutes=1),
        location='place du clos',
        rrule=dict(
            byday=['MO', 'TU', 'WE', 'TH', 'FR'],
        )
    ),
    dict(
        summary='place du clos',
        start=(17, 39),
        duration=timedelta(minutes=1),
        location='place du clos',
        rrule=dict(
            byday=['MO', 'TU', 'WE', 'TH', 'FR'],
        )
    ),
    dict(
        summary='place du clos',
        start=(16, 45),
        duration=timedelta(minutes=1),
        location='place du clos',
        rrule=dict(
            byday=['TH', 'FR'],
        )
    ),
]

def generate_school_bus_calendar() -> Calendar:
    '''
    Return a calendar for school bus
    '''
    result = Calendar()
    result.add('version', '2.0')
    result.add('calscale', 'GREGORIAN')
    result.add('X-WR-CALNAME', 'Bus scolaires')

    # school_weeks = [str(x) for x in get_school_weeks()]
    school_weeks = get_school_weeks()

    for event in BUS_CALENDAR:
        calendar_event = Event()
        for key, value in event.items():
            if key in ['start', 'end']:
                # If we use relative datetime, calculate absolute value
                hours, minutes = value
                value = BUS_CALENDAR_START + timedelta(hours=hours, minutes=minutes)
                calendar_event.add(f'dt{key}', value)
            elif key == 'rrule':
                value.update(dict(
                    byweekno=school_weeks,
                    freq='yearly',
                    until=BUS_CALENDAR_END,
                ))
                calendar_event.add(key, value)
            else:
                calendar_event.add(key, value)

        result.add_component(calendar_event)

    return result

def get_holidays_weeks() -> list:
    '''
    Return a list of all holidays weeks number
    '''
    result = list()

    holidays_file = ('calendrier_scolaire_20172018_et_20182019.ics')
    with open(holidays_file) as file_descriptor:
        data = file_descriptor.read()

    holidays_calendar = Calendar.from_ical(data)
    for event in holidays_calendar.walk(name='VEVENT'):
        # Get all holidays for Zone C:
        if all([
            'Vacances' in event.get('summary'),
            'Zone A' not in event.get('summary'),
            'Zone B' not in event.get('summary'),
        ]):
            dt_start = event.get('dtstart').dt.replace(
                tzinfo=pytz.timezone('Europe/Paris')
            )

            dt_end = event.get('dtend').dt.replace(
                tzinfo=pytz.timezone('Europe/Paris')
            )

            # Summer holidays has no duration
            if dt_start == dt_end:
                continue

            # Official calendar starts holidays at the end of the week
            dt_start = dt_start + relativedelta(weekday=MO(1))

            # Official calendars has both calendar and scholar years
            if dt_start < SCHOOL_CALENDAR_START.replace(tzinfo=pytz.timezone('Europe/Paris')):
                continue

            if dt_end > SCHOOL_CALENDAR_END.replace(tzinfo=pytz.timezone('Europe/Paris')):
                continue

            start_week = dt_start.isocalendar()[1]
            end_week = dt_end.isocalendar()[1]

            # if 'Vacances de Noël' == event['summary']:
            if start_week > end_week:
                last_yearly_week = date(dt_start.isocalendar()[0], 12, 28).isocalendar()[1]

                holidays_weeks = list()
                holidays_weeks.extend(range(start_week, last_yearly_week+1))
                holidays_weeks.extend(range(1, end_week))
            else:
                holidays_weeks = range(start_week, end_week)


            result.extend(holidays_weeks)

    return result

def get_school_weeks() -> list:
    '''
    List all week numbers of school
    '''
    result = list()
    holidays_weeks = get_holidays_weeks()

    school_start_week = SCHOOL_CALENDAR_START.isocalendar()[1]
    school_end_week = SCHOOL_CALENDAR_END.isocalendar()[1]
    last_yearly_week = date(SCHOOL_CALENDAR_START.isocalendar()[0], 12, 28).isocalendar()[1]

    school_weeks = list()
    school_weeks.extend(range(school_start_week, last_yearly_week+1))
    school_weeks.extend(range(1, school_end_week))

    result = sorted(list(set(school_weeks) - set(holidays_weeks)))

    return result

if __name__ == '__main__':
    generate_school_bus_calendar()
