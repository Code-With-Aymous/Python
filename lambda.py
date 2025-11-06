# lambda function to check even or odd

check = lambda n: "Even" if n % 2 == 0 else "Odd"
print(check(9))

# this function verfies the each element is even or odd.

def check(x):
    if x % 2 == 0: return f"even: {x}" 
    else: return f"odd: {x}"

num = [1, 2, 3, 4]
print(list(map(check, num)))

# filter odd numbers from an list using filter() and lambda keyword.

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(lambda x: x % 2 == 1, num)))

# filter even numbers from an list using filter() and lambda keyword.

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(lambda x: x % 2 == 0, num)))
