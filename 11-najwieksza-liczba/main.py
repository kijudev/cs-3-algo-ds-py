def biggest_number(string: str):
    return max([float(n) for n in string.split(";")])

string = "4.5;3.5;-2.5;42"
result = biggest_number(string)

print(f"string: {string}")
print(f"result: {result}")
