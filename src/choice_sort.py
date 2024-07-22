def choice_sort(elements: list):
    assert isinstance(elements, list), TypeError("Error type")

    if not elements:
        return []

    elif len(elements) == 1:
        return elements

    else:
        lenght = len(elements)
        count_change = 0
        count_comparison = 0
        for i in range(0, lenght - 1, 1):
            i_min = i
            for j in range(i + 1, lenght, 1):
                count_comparison += 1
                if elements[i_min] > elements[j]:
                    i_min = j
            if i != i_min:
                count_change += 1
                elements[i], elements[i_min] = elements[i_min], elements[i]

        return elements, count_change, count_comparison

