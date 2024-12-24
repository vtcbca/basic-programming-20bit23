def is_prime_recursive(n, divisor=2):
    if n <= 1:
        return False
    if divisor > int(n**0.5):
        return True
    if n % divisor == 0:
        return False
    return is_prime_recursive(n, divisor + 1)

num = int(input("Enter a number: "))
print(f"{num} is {'a prime' if is_prime_recursive(num) else 'not a prime'} number.")
