#creating initial commit

import unittest
from unittests import(
    validate_symbol,
    validate_chart_type,
    validate_time_series,
    validate_date,
)

def test_symbol_valid(self):
    self.assertTrue(validate_symbol("AAPL"))
    self.assertTrue(validate_symbol("A"))
    self.AssertTrue(validate_symbol("ABCDEFG"))
def test_symbol_invalid(self):
    self.assertFalse(validate_symbol("ABCDEFGH"))
    self.assertFalse(validate_symbol("aapl"))
    self.assertFalse(validate_symbol("AAP1"))

