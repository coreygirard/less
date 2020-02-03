import unittest
import doctest
import handle_draw

from hypothesis import given
from hypothesis.strategies import floats, lists, one_of, randoms

strat_floats = floats(allow_nan=False,
                      allow_infinity=False)
strat_lists = lists(strat_floats)
class TestHbarConvertToAllLists(unittest.TestCase):
    @given(lists(one_of(strat_floats,
                        strat_lists)),
           strat_lists,
           randoms())
    def test_has_some_lists(self, f, g, r):
        f.append(g)
        r.shuffle(f)

        assert any(map(lambda s: isinstance(s, list), f))

        result = handle_draw._hbar_convert_to_all_lists(f)

        assert all(map(lambda s: isinstance(s, list), result))

    @given(lists(strat_floats))
    def test_has_no_lists(self, f):
        assert all(map(lambda s: not isinstance(s, list), f))

        result = handle_draw._hbar_convert_to_all_lists(f)

        assert all(map(lambda s: isinstance(s, list), result))

    @given(lists(strat_lists))
    def test_has_all_lists(self, before):
        after = handle_draw._hbar_convert_to_all_lists(before)

        self.assertEqual(before, after)

'''
class TestBarGetData(unittest.TestCase):
    @given()
    def test_(self, f):
        print(f)
'''

def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite())
    return tests

if __name__ == '__main__':
    unittest.main()
