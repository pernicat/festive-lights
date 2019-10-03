from datetime import timedelta

from festive.seasons.theme import Theme, ADJUSTMENT_RANGE
from festive.colors import RED, WHITE, BLUE, BLACK

COLORS = [RED, WHITE, BLUE]
DURATION = timedelta(0)

MOCK = Theme(colors=COLORS, background=BLACK, duration=DURATION)


def calculate_adjustment_args_length() -> int:
    # total color combinations
    total_combos = len(MOCK.color_combos)

    # backgrounds can be any of the colors plus the background color
    total_backgrounds = len(COLORS) + 1

    # The total number of possible adjustments
    # (need to subtract 1*ADJUSTMENT_RANGE because one of the ranges starts at 1)
    adj_ranges = (ADJUSTMENT_RANGE - 1) * ADJUSTMENT_RANGE

    # sum of the color count from each combination
    combo_sum = sum(len(c) for c in MOCK.color_combos)
    # number of things filtered because one of the colors is the same as the background
    filtered_bg = combo_sum * adj_ranges

    # calculates the number of times the color will just be a solid color
    filtered_solids = len(COLORS) * (ADJUSTMENT_RANGE - 1) * total_backgrounds

    # total unfiltered combinations
    total = total_combos * adj_ranges * total_backgrounds

    # some of the filters apply to multiple times so we need to add them back
    filter_overlap = len(COLORS) * (ADJUSTMENT_RANGE - 1)

    # maths!
    # return total - filtered_bg - filtered_solids + filter_overlap
    return total - filtered_bg - filtered_solids + filter_overlap


def test_color_combinations():
    assert len(MOCK.color_combos) == 7

    assert COLORS in MOCK.color_combos
    assert [RED, WHITE] in MOCK.color_combos
    assert [BLUE] in MOCK.color_combos


def test_adjustment_args():
    assert len(MOCK.adjustment_args) == calculate_adjustment_args_length()

    assert ([RED, WHITE], 3, 5, BLUE) in MOCK.adjustment_args


def test_patterns():
    assert len(MOCK.patterns) == calculate_adjustment_args_length()
    assert [RED, RED, BLACK, BLACK] in MOCK.patterns
