import math
import unittest

from wrapping_calculator import calculate_wrapping


class TestCalculateWrapping(unittest.TestCase):
    def test_sample_inputs(self):
        result = calculate_wrapping(width=5970, height=3000, length=6000, bays=3)

        self.assertEqual(set(result), {"uprightCutLength", "rafterCutLength", "baseRailCutLength"})
        self.assertAlmostEqual(result["uprightCutLength"], 2420.0)
        self.assertAlmostEqual(result["rafterCutLength"], 2236.5 / math.cos(math.radians(15.0)))
        self.assertAlmostEqual(result["baseRailCutLength"], 5800 / 3 - 295.0)

    def test_rejects_non_positive_bays(self):
        with self.assertRaises(ValueError):
            calculate_wrapping(width=5970, height=3000, length=6000, bays=0)


if __name__ == "__main__":
    unittest.main()
