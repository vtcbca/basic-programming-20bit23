def triangle_pattern_while_loop(n):
    i = 1
    while i <= n:
        print(" " * (n - i) * 2, end="")
        j = 1
        while j < 2 * i:
            print(j, end=" ")
            j += 1
        print()
        i += 1

n = int(input("Enter the number of lines: "))
triangle_pattern_while_loop(n)
