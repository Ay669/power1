print("let's learn powers of 2!")
print("here are the powers of 4 from 0 to 10:\n")

# step 1: show the powers of 2 
for i in range(11):
    print(f"4^{i} = {4 ** i}")

# step 2: simple quiz
print("\nTime for a quick quiz!")
answer = int(input("what is 4 to the power of 2? "))

if answer == 4 ** 2:
    print("Correct! 4^2 = 16")
else:
    print("Incorrect. 4^2 = 16")
    print("Better luck next time!")