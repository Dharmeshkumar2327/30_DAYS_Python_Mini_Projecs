import unittest

from password_checker import check_password


class TestPasswordChecker(unittest.TestCase):

    def test_weak_short_password(self):
        self.assertEqual(check_password("abc")["rating"], "Weak")

    def test_common_password_is_weak(self):
        result = check_password("Password123")
        self.assertEqual(result["rating"], "Weak")
        self.assertEqual(result["score"], 0)

    def test_medium_password(self):
        self.assertEqual(check_password("hello2024")["rating"], "Medium")

    def test_strong_password(self):
        self.assertEqual(check_password("My$ecureP4ss!")["rating"], "Strong")

    def test_strong_password_has_no_suggestions(self):
        self.assertEqual(check_password("My$ecureP4ss!")["suggestions"], [])

    def test_missing_symbol_suggestion(self):
        result = check_password("Abcdefg1")
        self.assertIn("Add symbols like ! @ # $ %.", result["suggestions"])

    def test_space_warning(self):
        result = check_password("My Pass 1!")
        self.assertIn("Avoid spaces in your password.", result["suggestions"])


if __name__ == "__main__":
    unittest.main()
