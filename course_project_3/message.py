from course_project_3 import format_accounts
from course_project_3 import format_date


def get_message(operation: dict):
    """
    По полученным данным из словаря генерирует сообщение пользователю
    :param operation: Словарь с данными по операции
    :return: Сообщение об операции
    """
    date = format_date.format_date(operation['date'])
    description = operation['description']
    if 'from' not in operation.keys():
        from_account = 'Счет отправителя неизвестен'
    else:
        from_account = format_accounts.format_from_account(operation['from'])
    to_account = format_accounts.format_to_account(operation['to'])
    amount = operation['operationAmount']['amount']
    currency = operation['operationAmount']['currency']['name']

    first_line_list = [date, description]
    second_line_list = [from_account, '->', to_account]
    third_line_list = [amount, currency, '\n']

    first_line = ' '.join(first_line_list)
    second_line = ' '.join(second_line_list)
    third_line = ' '.join(third_line_list)

    return '\n'.join([first_line, second_line, third_line])
