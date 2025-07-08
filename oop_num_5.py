
def print_stars(n):
    if n == 0:
        return
    print("*", end='')
    print_stars(n - 1)

print_stars(5)

print()

def count_char(c, word):
    if word == "":
        return 0
    first = word[0]
    if first == c:
        return 1 + count_char(c, word[1:])
    else:
        return count_char(c, word[1:])


print(count_char("a", "banana"))

print()

def print_digits_forward(num):
    if num < 10:
        print(num, end=' ')
        return
    print_digits_forward(num // 10)
    print(num % 10, end=' ')


# Example:
print_digits_forward(527)
# Output: 5 2 7

print()

def count_odd_digits(n):
    if n < 10:
        if n % 2 == 0:
            return 0
        return 1

    last_digit = n % 10
    count =+ 1 if last_digit % 2 == 1 else 0
    return count + count_odd_digits(n // 10)


print(count_odd_digits(13572))


def reverse_print(word):
    if len(word) == 0:
        return
    print(word[-1], end="")
    reverse_print(word[:-1])


# Example:
reverse_print("hello")
# Output: olleh


