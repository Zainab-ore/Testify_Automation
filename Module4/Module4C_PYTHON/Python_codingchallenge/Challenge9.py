# Return the number of vowels in a string

def vowelsCount(vow_str):
    vowels = 'aeiouAEIOU'
    count = 0

    for char in vow_str:
        if char in vowels:
            count += 1

    return count


vowelsCountString = 'Return the number Of vowels in this string now'

print('The number of vowels in this string is:', vowelsCount(vowelsCountString))