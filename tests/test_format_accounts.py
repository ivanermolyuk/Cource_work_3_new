from course_project_3 import format_accounts


def test_format_from_account():
    assert format_accounts.format_from_account('Maestro 1596837868705199') == 'Maestro 1596 83** **** 5199'


def test_format_to_account():
    assert format_accounts.format_to_account('Счет 64686473678894779589') == 'Счет **9589'
