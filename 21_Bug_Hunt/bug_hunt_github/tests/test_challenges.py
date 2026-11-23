"""Basic integrity tests for the Bug Hunt challenge bank."""
import unittest

import bug_hunt


class ChallengeBankTests(unittest.TestCase):
    def test_challenge_bank_has_twenty_entries(self):
        self.assertEqual(len(bug_hunt.CHALLENGES), 20)

    def test_each_challenge_has_required_fields(self):
        required = {
            "level", "title", "goal", "happens", "lines",
            "bug", "type", "hint", "explain", "fix"
        }
        for challenge in bug_hunt.CHALLENGES:
            with self.subTest(title=challenge["title"]):
                self.assertTrue(required.issubset(challenge))
                self.assertIn(challenge["level"], {"Easy", "Medium", "Hard"})
                self.assertIn(challenge["type"], {"Syntax", "Runtime", "Logic"})
                self.assertTrue(challenge["lines"])
                self.assertTrue(challenge["bug"])
                self.assertTrue(all(
                    1 <= line_number <= len(challenge["lines"])
                    for line_number in challenge["bug"]
                ))


if __name__ == "__main__":
    unittest.main()
