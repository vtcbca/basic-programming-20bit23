def pattern_nested_for(rows):
    for i in range(1, rows + 1):
        for j in range(i):
            print("*", end=" ")
        print()

rows = int(input("Enter the number of rows: "))
pattern_nested_for(rows)
