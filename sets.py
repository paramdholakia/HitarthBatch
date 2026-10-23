A = {1, 2, 3, 4}
B = {3, 4, 5, 6}


print("Union:", A.union(B))                     # {1,2,3,4,5,6}  (A U B) 
print("Intersection:", A.intersection(B))       # {3,4} (A ∩ B)

print("Difference:", A.difference(B))           # {1,2} (A - B)
print("Difference (B-A):", B.difference(A))     # {5,6} (B - A)

print("Symmetric Difference:", A.symmetric_difference(B))  # {1,2,5,6}

print("Subset:", A.issubset(B))             # False
print("Superset:", A.issuperset(B))         # False
print("Disjoint:", A.isdisjoint(B))         # False


