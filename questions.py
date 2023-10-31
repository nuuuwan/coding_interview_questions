def is_palindrome(s):
    # Write a function that checks whether a given word or phrase is a
    # palindrome (i.e., it reads the same backward as forward, ignoring
    # spaces, punctuation, and capitalization).
    if len(s) <= 1:
        return True
    return s[0] is s[-1] and is_palindrome(s[1:-1])


def fibonacci(n):
    # Write a function that returns the n-th number in the Fibonacci sequence.
    if n <= 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def fuzz(n):
    # For numbers 1 through 100, print "Fizz" for numbers divisible by 3,
    # "Buzz" for numbers divisible by 5, "FizzBuzz" for numbers divisible by
    # both 3 and 5, and the number itself otherwise.
    if n % 15 == 0:
        return "FizzBuzz"

    if n % 3 == 0:
        return "Fizz"

    if n % 5 == 0:
        return "Buzz"

    return str(n)


def longest_substring_without_repeats(s):
    # Given a string, find the length of the longest substring without
    # repeating characters.

    used_chars = {}
    start = max_length = 0

    for i, char in enumerate(s):
        if char in used_chars and start <= used_chars[char]:
            start = used_chars[char] + 1
        else:
            max_length = max(max_length, i - start + 1)

        used_chars[char] = i

    return max_length


def array_rotate(arr, n):
    # Write a function that rotates an array to the right by a given number of
    # steps. For example, for the array `[1,2,3,4,5]` and 2 steps, the result
    # should be `[4,5,1,2,3]`.
    n = n % len(arr)
    return arr[-n:] + arr[:-n]
