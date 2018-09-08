from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta, MO, SU
from icalendar import Calendar, Event, vDatetime
import pytz
import uuid

TIMEZONE = pytz.timezone('Europe/Paris')
BUS_CALENDAR_START = datetime(2018, 9, 3, 0, 0, 0, 0, pytz.utc)
BUS_CALENDAR_END = datetime(2019, 7, 8, 0, 0, 0, 0, pytz.utc)

SCHOOL_CALENDAR_START = BUS_CALENDAR_START
SCHOOL_CALENDAR_END = BUS_CALENDAR_END

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

class Planning(object):
    def __init__(self,
            events: list,
            start: datetime,
            end: datetime,
            frequency: str = None,
            name: str = 'Calendrier',
            description: str = 'Calendrier',
            timezone=pytz.timezone('Europe/Paris'),
            excluded_weeks: list = None,
        ):

        self.events = events
        self.start = start
        self.end = end
        self.frequency = frequency
        self.excluded_weeks = excluded_weeks
        self.timezone = timezone

        self.calendar = Calendar()
        self.calendar.add('version', '2.0')
        self.calendar.add('calscale', 'GREGORIAN')
        self.calendar.add('prodid', '-// planning-renderer //')
        self.calendar.add('x-wr-timezone', self.timezone)
        self.calendar.add('x-wr-calname', name)
        self.calendar.add('x-wr-caldesc', description)

    def render_calendar(self) -> str:
        '''
        Return a calendar for school bus
        '''

        for event in self.events:
            calendar_event = Event()
            for key, value in event.items():
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

                    calendar_event.add(
                        f'dt{key};{self.timezone}', value, encode=0
                    )
                elif key == 'rrule':
                    value.update(dict(
                        freq='weekly',
                        interval=1,
                        until=self.end,
                    ))
                    calendar_event.add(key, value)
                else:
                    calendar_event.add(key, value)

            if self.excluded_weeks:
                calendar_event.add('exrule', dict(
                    freq='yearly',
                    byweekno=self.excluded_weeks
                ))

            if not event.get('uid'):
                calendar_event.add('uid', uuid.uuid4())

            # TODO check dtstamp, created at and co
            if not event.get('dtstamp'):
                calendar_event.add('dtstamp', vDatetime(datetime.now(pytz.utc)), encode=0)

            # TODO jours feries
            calendar_event.add(f'exdate;{self.timezone}', '20181101T000000', encode=0)

            self.calendar.add_component(calendar_event)

        # Convert from binary
        return self.calendar.to_ical().decode()

class WeeklyPlanning(Planning):

    def __init__(self, *args, **kwargs):
        super(WeeklyPlanning, self).__init__(*args, **kwargs)
        self.frequency = 'weekly'

def generate_school_calendar(
    weeks_number: list, school_planning: dict, title: str = None,
    ) -> Calendar:
    '''
    Return calendar for 6a
    '''
    result = Calendar()
    result.add('version', '2.0')
    result.add('calscale', 'GREGORIAN')
    result.add('prodid', '-// schoolbus-scheduler //')
    result.add('x-wr-timezone', TIMEZONE)
    if title:
        result.add('x-wr-calname', title)
        result.add('x-wr-caldesc', f'Agenda pour la {title}')

    weeks_number_type = dict(
        a=[number for index, number in enumerate(weeks_number) if index % 2 == 0],
        b=[number for index, number in enumerate(weeks_number) if index % 2 == 1],
    )

    for event in school_planning:
        calendar_event = Event()
        week_type = 'always'
        rrule = None
        for key, value in event.items():
            if key in ['start', 'end']:
                # If we use relative datetime, calculate absolute value
                if len (value) == 2:
                    hours, minutes = value
                    current_value = SCHOOL_CALENDAR_START + timedelta(hours=hours, minutes=minutes)
                elif len (value) == 3:
                    hours, minutes, days = value
                    current_value = SCHOOL_CALENDAR_START + timedelta(hours=hours, minutes=minutes, days=days)
                else:
                    raise ValueError
                calendar_event.add(f'dt{key}', current_value)
            elif key == 'week_type':
                week_type = value
            elif key == 'rrule':
                rrule = value
            else:
                calendar_event.add(key, value)

        if not event.get('uid'):
            calendar_event.add('uid', uuid.uuid4())

        if not event.get('dtstamp'):
            calendar_event.add('dtstamp', vDatetime(datetime.now(pytz.utc)), encode=0)

        if rrule:
            current_weeks_number = weeks_number_type.get(
                week_type, weeks_number
            )

            until = rrule.get('until', SCHOOL_CALENDAR_END)
            rrule.update(dict(
                freq='weekly',
                until=until,
            ))
            calendar_event.add('rrule', rrule)

        result.add_component(calendar_event)

    return result

def get_holidays_weeks(date_start: datetime, date_end: datetime) -> list:
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
            if dt_start < date_start.replace(tzinfo=pytz.timezone('Europe/Paris')):
                continue

            if dt_end > date_end.replace(tzinfo=pytz.timezone('Europe/Paris')):
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

    return sorted(result)

if __name__ == '__main__':
    bus_planning = WeeklyPlanning(
        name='bus',
        description='Calendrier des bus',
        events=BUS_CALENDAR,
        start=BUS_CALENDAR_START,
        end=BUS_CALENDAR_END,
        excluded_weeks=get_holidays_weeks(date_start=SCHOOL_CALENDAR_START, date_end=SCHOOL_CALENDAR_END),
    )

    print(bus_planning.render_calendar())
