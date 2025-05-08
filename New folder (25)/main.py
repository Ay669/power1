print("let's learn powers of 2!")
print("here are the powers of 2 from 0 to 10:\n")

# step 1: show the powers of 2 
for i in range(11):
    print(f"2^{i} = {2 ** i}")

# step 2: simple quiz
print("\nTime for a quick quiz!")
answer = int(input("what is 2 to the power of 3? "))

if answer == 2 ** 3:
    print("Correct! 2^3 = 8")
else:
    print("Incorrect. 2^3 = 8")
    print("Better luck next time!")