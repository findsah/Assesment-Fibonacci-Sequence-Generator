**Fibonacci Sequence Generator**

This Python library provides functions for generating the Fibonacci sequence. 
In this series, each number is the sum of the two preceding ones and usually starts with 0 and 1.

_Functions_

The library contains three functions to generate the Fibonacci sequence:

* fibonacci_recursive(n): This function generates the Fibonacci sequence recursively. It takes an integer n as input and returns a list of the first n Fibonacci numbers.
* 
* fibonacci_non_recursive(n): This function generates the Fibonacci sequence non-recursively. It also takes an integer n as input and returns a list of the first n Fibonacci numbers.
* 
* fibonacci_generator(n): This function generates the Fibonacci sequence using a generator. It takes an integer n as input and yields the Fibonacci numbers one at a time.

**Usage of Library**
To use the library, first import it into your Python script:

**Given Code**
import fibonacci
Use code with caution. Learn more
Then, we can call one of the functions to generate the Fibonacci sequence. For example, to generate the first 5 Fibonacci numbers,
we could use this code:

**test code example**
fib_seq = fibonacci.fibonacci_recursive(5)
print(fib_seq)
we can call upon all functions in similar way for further testing.
This would print:

[0, 1, 1, 2, 3]
we can also use the fibonacci_non_r