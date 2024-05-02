# Declare a list with any value and number of item/element
state = ["KANO", "LAGOS", "ABIA", "BENUE", "OGUN", "OSUN", "DELTA"]

# Print the list in console
print("All states:",state)

# Sort the list
state.sort()

# Print the list in console again
print("sort-asc:", state)


# reverse
before_reverse = state
after_reverse = state.reverse()
print(before_reverse, after_reverse)

# extend
state.extend(["EDO", "IMO", "KADUNA", "JIGAWA", "KANO"])
print(state)

# pop
state.pop()
print(state)

#count
count_state = state.count("KANO")
# print(vegetables)
print("Count:",count_state)

# Other List functions
#len
length = len(state)
print("Length:",length)