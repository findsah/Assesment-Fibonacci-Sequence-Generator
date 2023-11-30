import unittest
import sys

def fibonacci_recursive(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_seq = fibonacci_recursive(n - 1)
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq


def fibonacci_non_recursive(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    fib_seq = []
    a, b = 0, 1
    for _ in range(n):
        fib_seq.append(a)
        a, b = b, a + b
    return fib_seq


def fibonacci_generator(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


class TestFibonacci(unittest.TestCase):

    def test_recursive(self):
        self.assertEqual(fibonacci_recursive(1), [0])
        self.assertEqual(fibonacci_recursive(2), [0, 1])
        self.assertEqual(fibonacci_recursive(5), [0, 1, 1, 2, 3])

    def test_non_recursive(self):
        self.assertEqual(fibonacci_non_recursive(1), [0])
        self.assertEqual(fibonacci_non_recursive(2), [0, 1])
        self.assertEqual(fibonacci_non_recursive(5), [0, 1, 1, 2, 3])

    def test_generator(self):
        gen = fibonacci_generator(5)
        self.assertEqual(list(gen), [0, 1, 1, 2, 3])

    def test_large_n(self):
        #here I have added a testing condition for python version less than 3.8
        unittest.skipIf(sys.version_info < (3, 8), "Requires Python 3.8 or later")
        self.assertEqual(len(fibonacci_recursive(100)), 100)
        self.assertEqual(len(fibonacci_non_recursive(100)), 100)

        gen = fibonacci_generator(100)
        self.assertEqual(len(list(gen)), 100)

    def test_negative_n(self):
        with self.assertRaises(ValueError):
            fibonacci_recursive(-1)
            fibonacci_non_recursive(-1)

        gen = fibonacci_generator(-1)
        with self.assertRaises(ValueError):
            next(gen)


if __name__ == "__main__":
    unittest.main()
