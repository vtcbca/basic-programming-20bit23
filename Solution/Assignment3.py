def fibonacci_recursion(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    sequence = fibonacci_recursion(n - 1)
    sequence.append(sequence[-1] + sequence[-2])
    return sequence

num_terms = int(input("Enter the number of terms: "))
print(f"Fibonacci sequence (up to {num_terms} terms): {fibonacci_recursion(num_terms)}")
