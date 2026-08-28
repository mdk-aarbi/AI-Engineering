# Find languages which start with letter p.
languages = ["java", "python", "php", "c", "javascript"]
result = [ind for ind in languages if ind[0] == "p"]
print(result)