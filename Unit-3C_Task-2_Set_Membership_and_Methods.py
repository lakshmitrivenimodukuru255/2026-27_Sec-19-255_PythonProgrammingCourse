fruits = {"apple", "banana", "cherry"}

print("Initial set:", fruits)
print("Is 'banana' in fruits?", "banana" in fruits)
print("Is 'mango' not in fruits?", "mango" not in fruits)

fruits.add("mango")
print("After add('mango'):", fruits)

fruits.remove("banana")
print("After remove('banana'):", fruits)

fruits.discard("grape")
print("After discard('grape'):", fruits)
