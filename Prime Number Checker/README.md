Prime Number Checker

This Python program allows you to check if a given number is prime or not.

Introduction:
Prime numbers are positive integers greater than 1 that are divisible by only 1 and themselves. This program, written in Python, helps you determine whether a given number is prime or not.

Usage:
1. Make sure you have Python installed on your system.

2. Download the prime_num_checker.py file.

3. Open a terminal or command prompt and navigate to the directory where prime_num_checker.py is located.

4. Run the program by executing the following command: python prime_num_checker.py

5. Enter the number you want to check for primality when prompted.

6. The program will display whether the input number is prime or not.

How it Works:
The program works by iteratively checking if the input number is divisible by any integer between 2 and the input number itself (exclusive). If it finds any such divisor, it sets a flag (is_prime) to False, indicating that the number is not prime. Otherwise, if no divisors are found, the flag remains True, indicating that the number is prime.

After the loop completes, the program prints the result based on the value of the is_prime flag.
