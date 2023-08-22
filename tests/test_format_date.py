from course_project_3 import format_date


def test_format_date():
    assert format_date.format_date('2019-08-26T10:50:58.294041') == '26.08.2019'
