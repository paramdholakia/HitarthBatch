x = ("apple", "banana", "cherry")

y = list(x)
y[1] = "kiwi"

y.append("orange")

x = tuple(y)

print(x)