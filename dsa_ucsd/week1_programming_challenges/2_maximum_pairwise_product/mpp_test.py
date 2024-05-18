from hypothesis import given, example, strategies as st
import pytest


from max_pairwise_product import max_pairwise_product


@given(ls=st.lists(st.integers(min_value=0, max_value=1000), min_size=2, max_size=1000))
def test_mpp(ls):
    sorted_ls = sorted(ls)
    print(ls)
    assert max_pairwise_product(ls) == sorted_ls[-1] * sorted_ls[-2]
