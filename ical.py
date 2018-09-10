from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta, MO, SU
from icalendar import Calendar, Event, vDatetime
import pytz
import uuid

SCHOOL_6A_CALENDAR = [
    dict(
        summary='A. PLASTIQUES',
        location='A7',
        duration=timedelta(hours=1),
        start=(13, 30),
        rrule=dict(byday=['MO']),
    ),
    dict(
        summary='ANGLAIS',
        location='B6',
        duration=timedelta(hours=1),
        start=(14, 30),
        rrule=dict(byday=['MO']),
    ),
    dict(
        summary='ED MUSICALE',
        location='D2',
        duration=timedelta(hours=1),
        start=(15, 30),
        rrule=dict(byday=['MO']),
    ),
    dict(
        summary='EPS',
        location='',
        duration=timedelta(hours=2),
        start=(8, 30),
        rrule=dict(byday=['MO']),
    ),
    dict(
        summary='Mathématiques',
        location='C5',
        duration=timedelta(hours=1),
        start=(10, 30),
        rrule=dict(byday=['MO']),
        week_type='a'
    ),
    dict(
        summary='Français',
        location='D5',
        duration=timedelta(hours=1),
        start=(11, 30),
        rrule=dict(byday=['MO']),
    ),
    dict(
        summary='HIST. GEO. EN. MOR. CIV.',
        location='A5',
        duration=timedelta(hours=1),
        start=(10, 30),
        rrule=dict(byday=['MO']),
        week_type='b'
    ),
    dict(
        summary='HIST. GEO. EN. MOR. CIV.',
        location='a5',
        duration=timedelta(hours=1),
        start=(8, 30, 1),
        rrule=dict(byday=['TU']),
    ),
    dict(
        summary='Français',
        location='D5',
        duration=timedelta(hours=2),
        start=(9, 30, 1),
        rrule=dict(byday=['TU']),
    ),
    dict(
        summary='Mathématiques',
        location='C5',
        duration=timedelta(hours=1),
        start=(11, 30, 1),
        rrule=dict(byday=['TU']),
    ),
    dict(
        summary='ANGLAIS',
        location='B5',
        duration=timedelta(hours=1),
        start=(13, 30, 1),
        rrule=dict(byday=['TU']),
    ),
    dict(
        summary='EPS',
        location='',
        duration=timedelta(hours=2),
        start=(8, 30, 2),
        rrule=dict(byday=['WE']),
    ),
    dict(
        summary='ANGLAIS',
        location='B6',
        duration=timedelta(hours=1),
        start=(10, 30, 2),
        rrule=dict(byday=['WE']),
    ),
    dict(
        summary='TECHNOLOGIE',
        location='A6',
        duration=timedelta(hours=1),
        start=(10, 30, 3),
        rrule=dict(byday=['TH']),
        week_type='a'
    ),
    dict(
        summary='Mathématiques',
        location='C5',
        duration=timedelta(hours=1),
        start=(10, 30, 3),
        rrule=dict(byday=['TH']),
        week_type='b'
    ),
    dict(
        summary='Français',
        location='D5',
        duration=timedelta(hours=1),
        start=(11, 30, 3),
        rrule=dict(byday=['TH']),
    ),
    dict(
        summary='HIST. GEO. EN. MOR. CIV.',
        location='A3',
        duration=timedelta(hours=1),
        start=(13, 30, 3),
        rrule=dict(byday=['TH']),
    ),
    dict(
        summary='ANGLAIS',
        location='B4',
        duration=timedelta(hours=1),
        start=(14, 30, 3),
        rrule=dict(byday=['TH']),
    ),
    dict(
        summary='Mathématiques',
        location='C5',
        duration=timedelta(hours=1),
        start=(15, 30, 3),
        rrule=dict(byday=['TH']),
    ),
    dict(
        summary='HIST. GEO. EN. MOR. CIV.',
        location='A3',
        duration=timedelta(hours=1),
        start=(9, 30, 4),
        rrule=dict(byday=['FR']),
        week_type='a'
    ),
    dict(
        summary='Mathématiques',
        location='C5',
        duration=timedelta(hours=1),
        start=(9, 30, 4),
        rrule=dict(byday=['FR']),
        week_type='b'
    ),
    dict(
        summary='PHYSIQUE-CHIMIE',
        location='',
        duration=timedelta(hours=1),
        start=(10, 30, 4),
        rrule=dict(byday=['FR']),
    ),
    dict(
        summary='SVT',
        location='D8',
        duration=timedelta(hours=1),
        start=(11, 30, 4),
        rrule=dict(byday=['FR']),
    ),
    dict(
        summary='TECHNOLOGIE',
        location='A6',
        duration=timedelta(hours=1),
        start=(13, 30, 4),
        rrule=dict(byday=['FR']),
        week_type='a'
    ),
    dict(
        summary='SVT',
        location='D8',
        duration=timedelta(hours=1),
        start=(14, 30, 4),
        rrule=dict(byday=['FR']),
        week_type='a'
    ),
    dict(
        summary='Français',
        location='D5',
        duration=timedelta(hours=1),
        start=(13, 30, 4),
        rrule=dict(byday=['FR']),
        week_type='b'
    ),
    dict(
        summary='TECHNOLOGIE',
        location='A6',
        duration=timedelta(hours=1),
        start=(14, 30, 4),
        rrule=dict(byday=['FR']),
        week_type='b'
    ),
    dict(
        summary='Mathématiques',
        location='C5',
        duration=timedelta(hours=1),
        start=(15, 30, 4),
        rrule=dict(byday=['FR']),
    ),
]

SCHOOL_6F_CALENDAR = [
    dict(
        summary='EPS',
        location='',
        duration=timedelta(hours=1),
        start=(9, 30),
        rrule=dict(byday=['MO']),
    ),
    dict(
        summary='TECHNOLOGIE',
        location='A6',
        duration=timedelta(hours=1),
        start=(10, 30),
        rrule=dict(byday=['MO']),
    ),
    dict(
        summary='ANGLAIS',
        location='B6',
        duration=timedelta(hours=1),
        start=(11, 30),
        rrule=dict(byday=['MO']),
    ),
    dict(
        summary='HIST. GEO. EN. MOR. CIV.',
        location='A3',
        duration=timedelta(hours=1),
        start=(13, 30),
        rrule=dict(byday=['MO']),
    ),
    dict(
        summary='Français',
        location='C1',
        duration=timedelta(hours=1),
        start=(14, 30),
        rrule=dict(byday=['MO'],until=datetime(2018, 10, 15)),
    ),
    dict(
        summary='Français',
        location='C1',
        duration=timedelta(hours=1),
        start=(9, 30, 1),
        rrule=dict(byday=['TU']),
    ),
    dict(
        summary='Mathématiques',
        location='C5',
        duration=timedelta(hours=1),
        start=(10, 30, 1),
        rrule=dict(byday=['TU']),
    ),
    dict(
        summary='A. PLASTIQUES',
        location='A7',
        duration=timedelta(hours=1),
        start=(13, 30, 1),
        rrule=dict(byday=['TU']),
    ),
    dict(
        summary='Français',
        location='C1',
        duration=timedelta(hours=1),
        start=(14, 30, 1),
        rrule=dict(byday=['TU']),
    ),
    dict(
        summary='ANGLAIS',
        location='B6',
        duration=timedelta(hours=1),
        start=(15, 30, 1),
        rrule=dict(byday=['TU']),
    ),
    dict(
        summary='ANGLAIS',
        location='',
        duration=timedelta(hours=1),
        start=(8, 30, 2),
        rrule=dict(byday=['WE']),
    ),
    dict(
        summary='PHYSIQUE-CH',
        location='D10',
        duration=timedelta(hours=1),
        start=(9, 30, 2),
        rrule=dict(byday=['WE']),
    ),
    dict(
        summary='ED MUSICALE',
        location='D1',
        duration=timedelta(hours=1),
        start=(10, 30, 2),
        rrule=dict(byday=['WE']),
    ),
    dict(
        summary='Français',
        location='C1',
        duration=timedelta(hours=1),
        start=(11, 30, 2),
        rrule=dict(byday=['WE']),
    ),
    dict(
        summary='Français',
        location='C1',
        duration=timedelta(hours=1),
        start=(8, 30, 3),
        rrule=dict(byday=['TH']),
        week_type='a'
    ),
    dict(
        summary='SVT',
        location='D8',
        duration=timedelta(hours=1),
        start=(8, 30, 3),
        rrule=dict(byday=['TH']),
        week_type='b'
    ),
    dict(
        summary='Mathématiques',
        location='C5',
        duration=timedelta(hours=1),
        start=(9, 30, 3),
        rrule=dict(byday=['TH']),
        week_type='a'
    ),
    dict(
        summary='TECHNOLOGIE',
        location='A6',
        duration=timedelta(hours=1),
        start=(9, 30, 3),
        rrule=dict(byday=['TH']),
        week_type='b'
    ),
    dict(
        summary='Français',
        location='C1',
        duration=timedelta(hours=1),
        start=(10, 30, 3),
        rrule=dict(byday=['TH']),
        week_type='a'
    ),
    dict(
        summary='SVT',
        location='D8',
        duration=timedelta(hours=1),
        start=(10, 30, 3),
        rrule=dict(byday=['TH']),
        week_type='b'
    ),
    dict(
        summary='Mathématiques',
        location='C5',
        duration=timedelta(hours=1),
        start=(13, 30, 3),
        rrule=dict(byday=['TH']),
    ),
    dict(
        summary='HIST. GEO. EN. MOR. CIV.',
        location='A3',
        duration=timedelta(hours=1),
        start=(14, 30, 3),
        rrule=dict(byday=['TH']),
    ),
    dict(
        summary='EPS',
        location='',
        duration=timedelta(hours=2),
        start=(15, 30, 3),
        rrule=dict(byday=['TH']),
    ),
    dict(
        summary='HIST. GEO. EN. MOR. CIV.',
        location='A3',
        duration=timedelta(hours=1),
        start=(8, 30, 4),
        rrule=dict(byday=['FR']),
    ),
    dict(
        summary='SVT',
        location='D6',
        duration=timedelta(hours=1),
        start=(9, 30, 4),
        rrule=dict(byday=['FR']),
        week_type='a'
    ),
    dict(
        summary='Français',
        location='C1',
        duration=timedelta(hours=1),
        start=(9, 30, 4),
        rrule=dict(byday=['FR']),
        week_type='b'
    ),
    dict(
        summary='Mathématiques',
        location='C5',
        duration=timedelta(hours=1),
        start=(10, 30, 4),
        rrule=dict(byday=['FR']),
    ),
    dict(
        summary='ANGLAIS',
        location='B6',
        duration=timedelta(hours=1),
        start=(13, 30, 4),
        rrule=dict(byday=['FR']),
    ),
    dict(
        summary='Mathématiques',
        location='C5',
        duration=timedelta(hours=1),
        start=(14, 30, 4),
        rrule=dict(byday=['FR']),
    ),
    dict(
        summary='EPS',
        location='',
        duration=timedelta(hours=1),
        start=(15, 30, 4),
        rrule=dict(byday=['FR']),
    ),
]

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
        start=(12, 38, 2),
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
        start=(16, 45, 3),
        duration=timedelta(minutes=1),
        location='place du clos',
        rrule=dict(
            byday=['TH', 'FR'],
        )
    ),
]

TEST_CALENDAR = [
    dict(
        summary='test calendrier',
        start=(7, 51),
        duration=timedelta(minutes=1),
        location='roseraie',
        rrule=dict(
            byday=['MO', 'TU', 'WE', 'TH', 'FR'],
        )
    ),
]

class Planning(object):
    def __init__(self,
            events: list,
            start: datetime,
            end: datetime,
            frequency: str = None,
            name: str = 'Calendrier',
            description: str = 'Calendrier',
            timezone=pytz.timezone('Europe/Paris'),
            excluded_days: list = list(),
        ):

        self.name = name
        self.events = events
        self.start = start
        self.end = end
        self.frequency = frequency
        self.timezone = timezone
        self.excluded_days = excluded_days

        self.calendar = Calendar()
        self.calendar.add('version', '2.0')
        self.calendar.add('calscale', 'GREGORIAN')
        self.calendar.add('prodid', '-// planning-renderer //')
        self.calendar.add('x-wr-timezone', self.timezone)
        self.calendar.add('x-wr-calname', name)
        self.calendar.add('x-wr-caldesc', description)

    def render_calendar(self, set_missing_uid: bool = False) -> str:
        '''
        Return a calendar for school bus
        '''

        if self.name == 'test':
            print('Tests function enabled')

        for event in self.events:
            calendar_event = Event()
            event_week = None

            # Set week occurency in title
            week_type = event.pop('week_type', False)
            event_summary = event.pop('summary', False)
            if event_summary:
                if week_type:
                    calendar_event.add('summary', f'({week_type}) {event_summary}')
                else:
                    calendar_event.add('summary', event_summary)

            # Complete reccurence rule
            if event.get('rrule'):
                # Looks like iCal does NOT manage BYWEEKNO... shame
                event['rrule'].update(dict(
                    freq=self.frequency,
                    interval=1,
                    until=self.end,
                ))

            # Parse and all all remaining keys
            for key, value in event.items():
                # start/end must be 'converted' to dtstart/dtend
                if key in ['start', 'end']:
                    # Optionnal offset to fix display in google agenda
                    if len(value) == 2:
                        hours, minutes = value
                        day_offset = 0
                    elif len(value) == 3:
                        hours, minutes, day_offset = value
                    else:
                        raise ValueError

                    # Workaround for issues on dtend / dtstart format
                    value = '{year}{month:02d}{day:02d}T{hour:02d}{minute:02d}00'.format(
                        year=self.start.year,
                        month=self.start.month,
                        day=self.start.day + day_offset,
                        hour=hours,
                        minute=minutes,
                    )

                    if key == 'start':
                        dtstart_hour = hours
                        dtstart_minute = minutes

                    calendar_event.add(f'dt{key}', value, encode=0)
                    continue

                calendar_event.add(key, value)

            # EXRULE is obsolete in latest RFC!
            # if self.excluded_weeks:
            #     calendar_event.add('exrule', dict(
            #         freq='yearly',
            #         byweekno=self.excluded_weeks
            #     ))

            # If UUID is dyn generated, it will result in duplicated events on iOS
            if set_missing_uid and not event.get('uid'):
                calendar_event.add('uid', uuid.uuid4())

            # CREATED
            # This is the timestamp of when an event-object was created in a calendar application. Each event-object can be identified by a unique Identifier (UID).
            if not event.get('created'):
                calendar_event.add('created', self.start)

            # DTSTAMP
            # This is the timestamp of the creation of a VEVENT-message in an ical or ics file. There are different types of such VEVENT-message, creating a new event-object is just one of them. You also can change existing events and even cancel events if you add the correct UID to the VEVENT-message to identify which event-object it belongs to. So for one event-object in your calendar application (identified by its UID) you can receive many VEVENT-events, each with its own DTSTAMP, but all referring to an event with just one CREATED date.
            if not event.get('dtstamp'):
                calendar_event.add('dtstamp', vDatetime(datetime.now(pytz.utc)), encode=0)

            # EXDATE must have the same TIME that DSTART
            for exdate in self.excluded_days:
                exdate_format = '%Y%m%d' # The format
                exdate_datime = datetime.strptime(exdate, exdate_format)

                if all([
                    exdate_datime >= self.start,
                    exdate_datime <= self.end,
                ]):
                    calendar_event.add(
                        f'exdate',
                        f'{exdate}T{dtstart_hour:02d}{dtstart_minute:02d}00',
                        encode=0
                    )

            # Add event to calendar
            self.calendar.add_component(calendar_event)

        # Convert from binary
        return self.calendar.to_ical().decode()

class WeeklyPlanning(Planning):

    def __init__(self, *args, **kwargs):
        super(WeeklyPlanning, self).__init__(*args, **kwargs)
        self.frequency = 'weekly'


def merge_calendars(calendars: list) -> Calendar:
    '''
    Merge a list of calendars into one
    Property of the first calendars are kept
    '''
    mega_calendar = calendars.pop(0)
    for current_calendar in calendars:
        for event in current_calendar.walk(name='VEVENT'):
            mega_calendar.add_component(event)

    return mega_calendar

def days_off(
        date_start: datetime,
        date_end: datetime,
        source_calendar_file: str = 'frenchholidays.ics'
    ) -> list:
    '''
    Return all days off for given period
    Day format is {year}{month}{day}
    Source: https://www.thunderbird.net/en-US/calendar/holidays/#F
    '''
    result = list()

    with open(source_calendar_file) as file_descriptor:
        data = file_descriptor.read()

    calendar = Calendar.from_ical(data)
    for event in calendar.walk(name='VEVENT'):
        event_date = event.get('dtstart').dt
        event_rrule = event.get('rrule')

        # Event occurs every year (ex. Christmas)
        if event_rrule and 'yearly' in event_rrule.to_ical().lower().decode():
            for year in [date_start.year, date_end.year]:
                current_year_date = date(year, event_date.month, event_date.day)
                if all([
                    current_year_date >= date_start.date(),
                    current_year_date <= date_end.date(),
                ]):
                    result.append('{year}{month:02d}{day:02d}'.format(
                        year=year,
                        month=event_date.month,
                        day=event_date.day,
                    ))
        elif all([
            event_date >= date_start.date(),
            event_date <= date_end.date(),
        ]):
            result.append('{year}{month:02d}{day:02d}'.format(
                year=event_date.year,
                month=event_date.month,
                day=event_date.day,
            ))

    return result


def get_school_year_boundaries(holidays_file: str = ('calendrier_scolaire.ics')) -> list:
    '''
    Return a list of datetime. 
    List is an alternance of start / stop
    '''

    with open(holidays_file) as file_descriptor:
        data = file_descriptor.read()

    holidays_calendar = Calendar.from_ical(data)
    all_events = list()
    for event in holidays_calendar.walk(name='VEVENT'):
        if 'enseignants' in event.get('summary', ''):
            continue

        for field in ['dtstart', 'dtend']:
            if event.get(field):
                all_events.append(event[field].dt)
    
    all_events = sorted(all_events)
    end_date = all_events[0] + relativedelta(months=11)

    result = [datetime.combine(boundarie, datetime.min.time()) for boundarie in all_events if boundarie < end_date]
    # result = [boundarie for boundarie in all_events if boundarie < end_date]

    return result


def render_calendars(date_boundaries, **kwargs) -> list:
    '''
    Generate multiple calendars
    '''
    if any([
        len(date_boundaries) %2 != 0,
        len(date_boundaries) < 2,
    ]):
        raise ValueError(f'Boundaries has a wrong size ({len(date_boundaries)})')

    common_name = kwargs.get('name', '')
    common_description = kwargs.get('description', '')
    common_events = kwargs.get('events')
    common_excluded_days = kwargs.get('excluded_days', list()),

    common_arguments = dict(
        name=kwargs.get('name', ''),
        description=kwargs.get('description', ''),
        events=kwargs.get('events'),
    )

    if kwargs.get('excluded_days'):
        common_arguments.update(dict(excluded_days=kwargs['excluded_days']))

    calendars = list()
    while date_boundaries:
        date_start = date_boundaries.pop(0)
        date_stop = date_boundaries.pop(0)

        # print(f'Doing from {date_start} to {date_stop}')

        partial_calendar = WeeklyPlanning(
            **common_arguments,
            start=date_start,
            end=date_stop,
        )
        partial_calendar.render_calendar()
        calendars.append(partial_calendar.calendar)

    return merge_calendars(calendars).to_ical().decode()

if __name__ == '__main__':
    school_year_boundaries = get_school_year_boundaries()
    the_meg = render_calendars(
        date_boundaries=school_year_boundaries,
        name='test',
        description='Calendrier de tests a base de bus',
        events=TEST_CALENDAR,
    )

    print(the_meg)
    # app.config['test_bus_planning'] = WeeklyPlanning(
    #     name='test',
    #     description='Calendrier de tests a base de bus',
    #     events=TEST_CALENDAR,
    #     start=calendars_start,
    #     end=calendars_end,
    #     excluded_days=excluded_days,
    # ).render_calendar()

# End file