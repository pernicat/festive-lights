from datetime import date

from festive.seasons import Events, event_for_date


def test_get_event_for_date():
    assert event_for_date(date(2019, 10, 1)) == Events.HALLOWEEN
    assert event_for_date(date(2019, 10, 31)) == Events.HALLOWEEN
    assert event_for_date(date(2019, 11, 10)) == Events.FALL
    assert event_for_date(date(2019, 11, 25)) == Events.CHRISTMAS
    assert event_for_date(date(2019, 12, 15)) == Events.CHRISTMAS
    assert event_for_date(date(2020, 1, 3)) == Events.CHRISTMAS
    assert event_for_date(date(2019, 1, 15)) == Events.WINTER
    assert event_for_date(date(2019, 2, 11)) == Events.VALENTINES
    assert event_for_date(date(2019, 3, 15)) == Events.SAINT_PATRICK
    assert event_for_date(date(2019, 4, 12)) == Events.EASTER
    assert event_for_date(date(2019, 5, 1)) == Events.SPRING
    assert event_for_date(date(2019, 6, 10)) == Events.SUMMER
    assert event_for_date(date(2019, 6, 29)) == Events.INDEPENDENCE_DAY
    assert event_for_date(date(2019, 7, 1)) == Events.INDEPENDENCE_DAY
    assert event_for_date(date(2019, 7, 31)) == Events.SUMMER
    assert event_for_date(date(2019, 8, 15)) == Events.SUMMER

