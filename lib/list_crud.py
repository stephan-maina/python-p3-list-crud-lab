def create_an_empty_list():
    """Create and return an empty list."""
    return []


def create_a_list(elements=None):
    """Create and return a list with optional initial elements."""
    if elements is None:
        elements = []
    return list(elements)


def add_element_to_end_of_list(lst, element):
    """Add an element to the end of the list and return the modified list."""
    lst.append(element)
    return lst


def add_element_to_start_of_list(lst, element):
    """Add an element to the start of the list and return the modified list."""
    lst.insert(0, element)
    return lst


def remove_element_from_end_of_list(lst):
    """Remove and return the last element from the list."""
    if lst:
        return lst.pop()
    else:
        raise IndexError("Cannot remove from an empty list")


def remove_element_from_start_of_list(lst):
    """Remove and return the first element from the list."""
    if lst:
        return lst.pop(0)
    else:
        raise IndexError("Cannot remove from an empty list")


def retrieve_first_element_from_list(lst):
    """Retrieve and return the first element from the list."""
    if lst:
        return lst[0]
    else:
        raise IndexError("List is empty")


def retrieve_element_from_index(lst, index):
    """Retrieve and return an element from the list by index."""
    if 0 <= index < len(lst):
        return lst[index]
    else:
        raise IndexError("Index out of range")


def retrieve_last_element_from_list(lst):
    """Retrieve and return the last element from the list."""
    if lst:
        return lst[-1]
    else:
        raise IndexError("List is empty")

