number = 10
for i in range(number):
    print("Number ", i)


print("\nContinue\n")

for i in range(number):
    if i == 2:
        continue
    print("Number ", i)

print("\nBreak\n")

for i in range(number):
    if i == 8:
        break
    print("Number ", i)