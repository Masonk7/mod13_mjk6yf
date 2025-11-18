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

def test_chart_type_valid(self):
    self.assertTrue(validate_chart_type("1"))
    self.assertTrue(validate_chart_type("2"))
def test_chart_type_invalid(self):
    self.assertFalse(validate_chart_type("0"))
    self.assertFalse(validate_chart_type("3"))
    self.assertFalse(validate_chart_type("a"))
    self.assertFalse(validate_chart_type("12"))

def test_time_series_valid(self):
    self.assertTrue(validate_time_series("1"))
    self.assertTrue(validate_time_series("2"))
    self.assertTrue(validate_time_series("3"))
    self.assertTrue(validate_time_series("4"))
def test_time_series_invalid(self):
    self.assertFalse(validate_time_series("0"))
    self.assertFalse(validate_time_series("5"))
    self.assertFalse(validate_time_series("x"))
    self.assertFalse(validate_time_series("12"))

def test_start_date_valid(self):
    self.assertTrue(validate_date("2024-01-31"))
def test_start_date_invalid(self):
    self.assertFalse(validate_date("2024/01/31"))
    self.assertFalse(validate_date("31-01-2024"))
    self.assertFalse(validate_date("2024-02-30"))
    self.assertFalse(validate_date("not-a-date"))
    self.assertFalse(validate_date("2024-13-01"))
    self.assertFalse(validate_date("2024-01-00"))


def test_end_date_valid(self):
    self.assertTrue(validate_date("2025-01-31"))
def test_end_date_invalid(self):
    self.assertFalse(validate_date("2025/01/31"))
    self.assertFalse(validate_date("31-01-2025"))
    self.assertFalse(validate_date("2025-02-30"))
    self.assertFalse(validate_date("not-a-date"))
    self.assertFalse(validate_date("2025-13-01"))
    self.assertFalse(validate_date("2025-01-00"))

if __name__ == "__main__":
    unittest.main()