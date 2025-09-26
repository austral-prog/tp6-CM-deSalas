def remove_elements(list_to_remove_elements):
    new_list = list_to_remove_elements[:]
    for i in [5, 4, 0]:
        if i < len(new_list):
            del new_list[i]
    return new_list


def add_elements(list_to_add_elements):
    new_list = list_to_add_elements[:]
    new_list.insert(0, "Pink")
    new_list.append("Yellow")
    return new_list


def is_empty(list_to_check):
    return len(list_to_check) == 0


def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1) >= 3 and len(list_to_compare2) >= 3:
        return list_to_compare1[2] == list_to_compare2[2]
    return False


def list_of_lists(list_of_lists_to_modify):
    result = []
    if len(list_of_lists_to_modify) >= 1:
        result.append(list_of_lists_to_modify[0][:2])
    if len(list_of_lists_to_modify) >= 2:
        result.append(list_of_lists_to_modify[1][1:4])
    if len(list_of_lists_to_modify) >= 3:
        result.append(list_of_lists_to_modify[2][-2:])
    return result
