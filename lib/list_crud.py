def create_an_empty_list():
    empty_list = []
    return empty_list

def create_a_list():
    new_list = [None] * 4
    return new_list

def add_element_to_end_of_list(l, element):
    l.append(element)
    return l


def add_element_to_start_of_list(l, element):
    l.insert(0, element)
    return l
def remove_element_from_end_of_list(l):
    if len(l) > 0:
        l.pop()
    return l
def remove_element_from_start_of_list(l):
    if len(l) > 0:
        l.pop(0)
    return l
def retrieve_first_element_from_list(l):
    return l[0]

def retrieve_element_from_index(l, index):
    return l[index]

def retrieve_last_element_from_list(l):
    return l[-1]
