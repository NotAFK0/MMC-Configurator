import math
import unittest

from wrapping_calculator import calculate_wrapping_cuts


class TestCalculateWrappingCuts(unittest.TestCase):
    def test_sample_inputs(self):
        result = calculate_wrapping_cuts(width=5970, height=3000, length=6000, bays=3)
        pitch = math.radians(15.0)
        bay_size = 5800 / 3

        self.assertEqual(set(result), {"dimensions", "portals", "cuts"})
        self.assertAlmostEqual(result["dimensions"]["peakHeight"], 3000 + 2985 * math.tan(pitch))
        self.assertAlmostEqual(result["dimensions"]["baySize"], bay_size)
        self.assertEqual(result["portals"], 4)

        self.assertAlmostEqual(result["cuts"]["upright"]["cutLength"], 2420.0)
        self.assertEqual(result["cuts"]["upright"]["qty"], 8)
        self.assertAlmostEqual(result["cuts"]["rafter"]["cutLength"], 2236.5 / math.cos(pitch))
        self.assertEqual(result["cuts"]["rafter"]["qty"], 8)
        self.assertAlmostEqual(result["cuts"]["baseRail"]["cutLength"], bay_size - 295.0)
        self.assertEqual(result["cuts"]["baseRail"]["qty"], 6)

    def test_rejects_non_positive_bays(self):
        with self.assertRaises(ValueError):
            calculate_wrapping_cuts(width=5970, height=3000, length=6000, bays=0)


if __name__ == "__main__":
    unittest.main()
