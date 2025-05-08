import math

print("let's see how numbers grow:")
print("Numbers\tlog2(n)\tn^2")
print("-" * 25)

# show values from 1 to 10
for n in range(1, 11):
    log_value = round(math.log2(n), 2) # log base 2 of n
    squared = n ** 2
    print(f"{n}\t{log_value:.2f}\t{squared}")