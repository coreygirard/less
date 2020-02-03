import unittest
import doctest
import handle_draw

from hypothesis import given
from hypothesis.strategies import floats, lists, one_of, randoms, just, tuples


strat_floats = floats(allow_nan=False,
                      allow_infinity=False)
strat_float_or_none = one_of(just(None),
                             strat_floats)
strat_lim = tuples(strat_float_or_none,
                   strat_float_or_none,
                   strat_float_or_none,
                   strat_float_or_none)
class TestSyncScales(unittest.TestCase):
    @given(tuples(strat_lim,
                  strat_lim,
                  strat_lim,
                  strat_lim))
    def test_sync_scales(self, e):
        d = {}
        for k, v in zip(['left',
                         'right',
                         'top',
                         'bottom'],
                        e):
            temp = {i: j for i, j in zip(['xmin',
                                          'xmax',
                                          'ymin',
                                          'ymax'],
                                         v) if not j is None}
            d[k] = temp

        ax = handle_axes.Axes()

        '''
        for k in ['left',
                  'right',
                  'top',
                  'bottom']:
        '''








def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite())
    return tests

if __name__ == '__main__':
    unittest.main()
