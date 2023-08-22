from course_project_3 import message
import pytest


@pytest.fixture
def operation():
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }

@pytest.fixture
def operation_without_from():
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "to": "Счет 64686473678894779589"
    }

def test_message(operation):
    assert message.get_message(operation) == """26.08.2019 Перевод организации
Maestro 1596 83** **** 5199 -> Счет **9589
31957.58 руб. 
"""


def test_message_withot_from(operation_without_from):
    assert message.get_message(operation_without_from) == """26.08.2019 Перевод организации
Счет отправителя неизвестен -> Счет **9589
31957.58 руб. 
"""
