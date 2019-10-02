from festive.transitions import rgb_color_transition


def test_rgb_color_transition():
    start = (0.0, 0.0, 0.0)
    end = (1.0, 1.0, 1.0)

    result = [c for c in rgb_color_transition(start, end, 10)]

    assert len(result) == 10

    for i, rgb in zip(range(10), result):
        value = i/10.0
        assert rgb == (value, value, value)
