n = int(input("Enter a number: "))
evens = [x for x in range(1, n) if x % 2 == 0]
odds = [x for x in range(1, n) if x % 2 != 0]
print(evens)
print(odds)
