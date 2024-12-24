def alphabet_pattern_while_loop(n):
    i = 1
    while i <= n:
        print(" " * (n - i) * 2, end="")
        j = 1
        while j <= i:
            print(chr(64 + j), end=" ")
            j += 1
        j = i - 1
        while j > 0:
            print(chr(64 + j), end=" ")
            j -= 1
        print()
        i += 1

n = int(input("Enter the number of lines: "))
alphabet_pattern_while_loop(n)
