def format_from_account(input_from_account: str):
    """
    Форматирует номер счета отправителя, приводя его к виду, в котором часть номера срыта
    :param input_from_account: Строка с номером счета отправителя
    :return: Строка с отформатированным номером счета отправителя
    """
    from_account_split = input_from_account.split(" ")

    account_list = []
    for i in from_account_split[1]:
        account_list.append(i)

    for i in range(6, 12):
        account_list[i] = "*"

    counter = 0
    new_account = []

    for num in account_list:
        new_account.append(num)
        counter += 1
        if counter == 4:
            new_account.append(' ')
            counter = 0

    del new_account[len(new_account) - 1]
    from_account = ''.join(new_account)
    from_account_split[1] = from_account

    return " ".join(from_account_split)


def format_to_account(input_to_account: str):
    """
    Форматирует номер счета получателя, приводя его к виду, в котором часть номера срыта
    :param input_to_account: Строка с номером счета получателя
    :return: Строка с отформатированным номером счета получателя
    """
    to_account_split = input_to_account.split(" ")
    to_account_list = []
    for i in to_account_split[1]:
        to_account_list.append(i)

    for num in range(0, 16):
        to_account_list[num] = "*"
    to_account_split[1] = "".join(to_account_list)[-6:]

    return " ".join(to_account_split)
