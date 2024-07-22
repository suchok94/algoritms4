import pytest

from src.bubble_sort import bubble_sort

@pytest.mark.parametrize('list, extend_result', [
    ([], []),
    ([1], [1]),
    ([2,3,1,4,6,5], [1,2,3,4,5,6])
])
def test_bubble_sort_positive(list, extend_result):
    assert bubble_sort(list) == extend_result



# @pytest.mark.parametrize('list, extend_result', [
#     ([2,3,1,4,6,5], [6,5,4,3,2,1])
# ])
def test_bubble_sort_positive_decrease(list =[2,3,1,4,6,5], extend_result= [6,5,4,3,2,1], by_order= lambda x, y: x < y):
    assert bubble_sort(list, by_order) == extend_result