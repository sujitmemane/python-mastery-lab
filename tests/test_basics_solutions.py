import unittest
import importlib.util

from pathlib import Path


ROOT = Path(__file__).parents[1]


def load_solution(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


variables = load_solution(
    "variables_solution", "01-basics/01-variables/solution.py"
)
conversion = load_solution(
    "conversion_solution", "01-basics/03-type-conversion/solution.py"
)


class BasicsSolutionTests(unittest.TestCase):
    def test_variables_solution(self):
        self.assertEqual(variables.swap_values("left", "right"), ("right", "left"))
        self.assertEqual(variables.demonstrate_aliasing(), ([1, 2, 3], [1, 2, 3]))

    def test_safe_int(self):
        self.assertEqual(conversion.safe_int("12"), 12)
        self.assertIsNone(conversion.safe_int("twelve"))


if __name__ == "__main__":
    unittest.main()