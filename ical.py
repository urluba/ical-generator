# pylint: disable=import-error, invalid-name
'''
Generate ICS files from hardcoded planning
TODO:
- Fix TZ issue
- Review global vars
- Bus
- Web version ?
'''
from datetime import datetime, timedelta
import arrow
from ics import Calendar, Event

def is_during_holidays(searched_date: arrow.Arrow, calendar: object) -> bool:
    '''
    Return true if given date is during holidays else False
    '''
    searched_event = Event()
    searched_event.begin = searched_date
    searched_event.make_all_day()

    for holidays in calendar.events:
        # Ignore others zones and non holidays events
        if any([
                'Vacances' not in holidays.name,
                'Zone A' in holidays.name,
                'Zone B' in holidays.name,
        ]):
            continue

        if all([
                searched_event.begin >= holidays.begin,
                searched_event.end <= holidays.end,
        ]):
            return True

    return False

week_6f_a = [
    # Monday
    [
        ('eps', 9, 30, 60),
        ('techno', 10, 30, 60),
        ('anglais', 11, 30, 60),
        ('hist/geo', 13, 30, 60),
    ],
    # Tuesday
    [
        ('francais', 9, 30, 60),
        ('math', 10, 30, 60),
        ('dessin', 13, 30, 60),
        ('francais', 14, 30, 60),
        ('anglais', 15, 30, 60),
    ],
    # Wednesday
    [
        ('anglais', 8, 30, 60),
        ('physique', 9, 30, 60),
        ('musique', 10, 30, 60),
        ('francais', 11, 30, 60),
    ],
    # Thursday
    [
        ('francais', 8, 30, 60),
        ('math', 9, 30, 60),
        ('francais', 10, 30, 60),
        ('math', 13, 30, 60),
        ('hist/geo', 14, 30, 60),
        ('eps', 15, 30, 120),
    ],
    # Friday
    [
        ('hist/geo', 8, 30, 60),
        ('svt', 9, 30, 60),
        ('math', 10, 30, 60),
        ('anglais', 13, 30, 60),
        ('math', 14, 30, 60),
        ('eps', 15, 30, 60),
    ],
]

week_6f_b = list(week_6f_a)

week_6f_b[3] = [
    ('svt', 8, 30, 60),
    ('techno', 9, 30, 60),
    ('svt', 10, 30, 60),
    ('math', 13, 30, 60),
    ('hist/geo', 14, 30, 60),
    ('eps', 15, 30, 120),
]

week_6f_b[4] = [
    ('hist/geo', 8, 30, 60),
    ('francais', 9, 30, 60),
    ('math', 10, 30, 60),
    ('anglais', 13, 30, 60),
    ('math', 14, 30, 60),
    ('eps', 15, 30, 60),
]

schedule_6f = [
    week_6f_a,
    week_6f_b,
]

week_6a_a = [
    # Monday
    [
        ('eps', 8, 30, 120),
        ('math', 10, 30, 60),
        ('francais', 11, 30, 60),
        ('dessin', 13, 30, 60),
        ('anglais', 14, 30, 60),
        ('musique', 15, 30, 60),
    ],
    # Tuesday
    [
        ('hist/geo', 8, 30, 60),
        ('francais', 9, 30, 120),
        ('math', 11, 30, 60),
        ('anglais', 13, 30, 60),
    ],
    # Wednesday
    [
        ('eps', 8, 30, 120),
        ('anglais', 10, 30, 60),
    ],
    # Thursday
    [
        ('techno', 10, 30, 60),
        ('francais', 11, 30, 60),
        ('hist/geo', 13, 30, 60),
        ('anglais', 14, 30, 60),
        ('math', 15, 30, 60),
    ],
    # Friday
    [
        ('hist/geo', 9, 30, 60),
        ('physique', 10, 30, 60),
        ('svt', 11, 30, 60),
        ('techno', 13, 30, 60),
        ('svt', 14, 30, 60),
        ('math', 15, 30, 60),
    ],
]

week_6a_b = list(week_6a_a)

# Monday
week_6a_b[0] = [
    ('eps', 8, 30, 120),
    ('hist/geo', 10, 30, 60),
    ('francais', 11, 30, 60),
    ('dessin', 13, 30, 60),
    ('anglais', 14, 30, 60),
    ('musique', 15, 30, 60),
]

# Thursday
week_6a_b[3] = [
    ('math', 10, 30, 60),
    ('francais', 11, 30, 60),
    ('hist/geo', 13, 30, 60),
    ('anglais', 14, 30, 60),
    ('math', 15, 30, 60),
]

# Friday
week_6a_b[4] = [
    ('math', 9, 30, 60),
    ('physique', 10, 30, 60),
    ('svt', 11, 30, 60),
    ('francais', 13, 30, 60),
    ('techno', 14, 30, 60),
    ('math', 15, 30, 60),
]

schedule_6a = [
    week_6a_a,
    week_6a_b,
]

common_morning_bus = [
    ('roseraie', 7, 51, 1),
    ('roseraie', 8, 57, 1),
    # ('place du clos', 8, 26, 1),
    # ('place du clos', 9, 12, 1),
]

common_afternoon_bus = [
    ('place du clos', 15, 42, 1),
    ('place du clos', 16, 42, 1),
    ('place du clos', 17, 39, 1),
]

week_bus = [
    common_morning_bus + common_afternoon_bus,
    common_morning_bus + common_afternoon_bus,
    common_morning_bus + [('place du clos', 12, 38, 1)],
    common_morning_bus + common_afternoon_bus + [('place du clos', 16, 45, 1)],
    common_morning_bus + common_afternoon_bus + [('place du clos', 16, 45, 1)],
]

schedule_bus = [week_bus, week_bus]

def generate_week_events(planning: list, target: Calendar, monday: arrow.Arrow):
    '''
    Add all events in planning into specified calendar
    '''
    # Iterate over days of the week
    for day_number, courses in enumerate(planning):
        # Iterate over courses of the day
        for current_course in courses:
            start_time = arrow.get(
                datetime.utcfromtimestamp(monday.timestamp) + timedelta(
                    days=day_number,
                    hours=current_course[1] - 2,    # TODO fix this TZ issue
                    minutes=current_course[2],
                )
            )
            target.events.add(
                Event(
                    name=current_course[0],
                    begin=start_time,
                    duration={'minutes': current_course[3]}
                )
            )

def render_calendar(
        planning: list,
        start_monday: arrow.Arrow,
        end_monday: arrow.Arrow,
        holidays_calendar: Calendar
    ) -> Calendar:
    '''
    Returns a calendar populated with provided events
    '''

    result = Calendar()
    week_type = 0

    for current_monday in arrow.Arrow.range('week', start_monday, end_monday):
        # Holidays are skipped :)
        if is_during_holidays(current_monday, calendar=holidays_calendar):
            pass
        else:
            generate_week_events(
                monday=current_monday,
                target=result,
                planning=planning[week_type],
            )

            # Change planning for next week
            week_type = (week_type + 1) % 2

    return result

if __name__ == '__main__':
    first_school_monday = arrow.get('2018-09-03')
    last_school_monday = arrow.get('2019-07-01')

    holidays_file = ('calendrier_scolaire_20172018_et_20182019.ics')
    with open(holidays_file) as fd:
        holidays_cal = Calendar(fd.read())

    for current_planning, output_file in [
            (schedule_6a, 'calendrier_6a.ics'),
            (schedule_6f, 'calendrier_6f.ics'),
            (schedule_bus, 'calendrier_bus.ics')
    ]:
        new_calendar = render_calendar(
            planning=current_planning,
            start_monday=first_school_monday,
            end_monday=last_school_monday,
            holidays_calendar=holidays_cal
        )

        print(f'Writing {output_file}')
        with open(output_file, 'w') as fd:
            fd.writelines(new_calendar)
