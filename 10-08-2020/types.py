from typing import Tuple, List, Union, Optional,Any

def delete_o(string: str):
    """

    :param string:
    :return:
    """
    return string.replace('o', '')

# def count_products(products: Tuple[str, str, str]):
def count_products(products: Tuple[str, ...]):
    return len(products)

def get_sum(arg: List[Union[int, float]]) -> Union[int, float]:
    return sum(arg)

def test_func(a: Optional[int] = 40) :
    # Optional - Unoin[Any, None]
# def test_func(a: Any):
    pass
# delete_o('10')

products_cart = ('ibm', ' milk', 'patetu')
count_products(products_cart)

get_sum([10, 2, 3, 10.1])
test_func(100)