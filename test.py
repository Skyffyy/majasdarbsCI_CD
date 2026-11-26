import os
import subprocess
import sys
import time
import unittest

import app


# APP_DIR - mape, kur atrodas app.py (pec deploy ta ir production mape)
APP = os.path.join(os.environ.get("APP_DIR", "."), "app.py")


def run_app(a, op, b):
    return subprocess.run([sys.executable, APP, a, op, b], capture_output=True, text=True)


class UnitTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(app.add(2, 3), 5)

    def test_sub(self):
        self.assertEqual(app.sub(10, 4), 6)

    def test_mul(self):
        self.assertEqual(app.mul(6, 7), 42)

    def test_div(self):
        self.assertEqual(app.div(20, 5), 4)

    def test_div_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            app.div(1, 0)


class IntegrationTest(unittest.TestCase):
    def test_calculate(self):
        self.assertEqual(app.calculate(2, "+", 3), 5)
        self.assertEqual(app.calculate(9, "/", 3), 3)

    def test_unknown_operation(self):
        with self.assertRaises(ValueError):
            app.calculate(2, "%", 3)


class RegressionTest(unittest.TestCase):
    def test_old_cases(self):
        self.assertEqual(app.calculate(0, "+", 0), 0)
        self.assertEqual(app.calculate(0, "-", 5), -5)
        self.assertEqual(app.calculate(-3, "*", -3), 9)
        self.assertEqual(app.calculate(7, "/", 2), 3.5)


class RegistrationTest(unittest.TestCase):
    def test_all_operations_registered(self):
        self.assertEqual(sorted(app.OPERATIONS), ["*", "+", "-", "/"])


class StressTest(unittest.TestCase):
    def test_many_calculations(self):
        start = time.time()
        for i in range(100000):
            app.calculate(i, "+", 1)
        self.assertLess(time.time() - start, 5)


class SmokeTest(unittest.TestCase):
    def test_app_runs(self):
        result = run_app("2", "+", "3")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "5.0")


if __name__ == "__main__":
    unittest.main()