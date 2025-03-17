name=input("enter any string :")
print(f"entered string has {len(name)} characters")

#modified progrom to return length of string without counting space
name=input("enter any string :")
print(f"entered string has {len(name.strip())} characters")