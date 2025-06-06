#even numbers
even_numbers = {2, 4, 6, 12, 34}

#prime numbers
prime_numbers = {2, 3, 5, 7}

#union of even and prime numbers
#while True:
def union_numbers():
    outcome = even_numbers.union(prime_numbers)
    guess = input("What do you think will be the union of even and prime numbers?: ")
    guess_set = set(int(num) for num in guess.split())
    if guess_set == outcome:
        print(f"Correct! The union is: {outcome}") 
    else:
        print(f"Incorrect! The union is: {outcome}")

#intersection of even and prime numbers
def intersection_numbers():
    return even_numbers.intersection(prime_numbers)

#difference of even and prime numbers
def difference_numbers():
    return even_numbers.difference(prime_numbers)

union_numbers()
