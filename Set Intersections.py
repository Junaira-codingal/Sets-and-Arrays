setx = {"green","blue"}
sety = {"blue","yellow"}

print("Original set elements: ")
print(setx)
print(sety)

print("\nIntersection of two sai sets: ")
setz = setx.intersection(sety)
print(setz)

print("\nUnion of two sai sets: ")
setz = setx.union(sety)
print(setz)

print("\nDifference of two sai sets: ")
setz = setx.difference(sety)
print(setz)

print("\nSymmetric Difference of two sai sets: ")
setz = setx.symmetric_difference(sety)
print(setz)