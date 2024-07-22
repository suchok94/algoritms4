def bubble_sort(elements: list, key= lambda x: x, order_by= lambda x, y: x > y):
    assert isinstance(elements, list), TypeError('Error type')

    if not elements:
        return []

    elif len(elements) == 1:
        return elements

    else:
        for i in range(0, len(elements), 1):
            for j in range(0, len(elements) - i - 1, 1):
                if order_by(elements[j], elements[j + 1]):
                    elements[j], elements[j+1] = elements[j + 1], elements[j]

        return elements


