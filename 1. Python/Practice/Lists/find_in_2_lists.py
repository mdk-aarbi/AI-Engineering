#Nested if with list comprehension.
basket = ["apple", "guava", "cherry", "banana"]
my_fruits = ["apple", "kiwi", "grapes", "banana"]
# add new list from my fruits and items if the fruit exists in basket and also starts with "a".
result = [fruit for fruit in my_fruits if fruit in basket if fruit.startswith("a")]
print(result)