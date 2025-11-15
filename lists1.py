
start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))
squares = []
even_squares = []
odd_squares = []
for num in range(start, end + 1):
    sq = num * num
    squares.append(sq)
    if sq % 2 == 0:
        even_squares.append(sq)
    else:
        odd_squares.append(sq)
print("All square values:", squares)
print("Even squares:", even_squares)
print("Odd squares:", odd_squares)
