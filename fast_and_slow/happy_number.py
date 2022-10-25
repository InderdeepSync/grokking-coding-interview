def sum_square_digits(num):
    result = 0
    while num:
        digit = num % 10
        result += digit * digit
        num //= 10

    return result


def isHappy(n: int) -> bool: # Verified on Leetcode
    slow = fast = n
    while fast != 1 and sum_square_digits(fast) != 1:
        slow = sum_square_digits(slow)
        fast = sum_square_digits(sum_square_digits(fast))

        if slow == fast:
            return False

    return True


if __name__ == "__main__":
    print(isHappy(52))