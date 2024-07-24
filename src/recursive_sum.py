# def recursive_sum(array: list) -> float:
#     summ = 0
#     if len(array) == summ:
#         return summ
#
#     elif len(array) == 1:
#         summ = array[0]
#
#     else:
#         summ = array[0]
#         array.remove(array[0])
#         summ = summ + recursive_sum(array)
#
#
#     return summ


def recursive_sum(array: list) -> float:
    summ = array[0]

    if len(array) == 0:
        return 0

    elif len(array) > 1:
        array.remove(array[0])
        summ += recursive_sum(array)

    return summ
