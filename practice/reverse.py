def reversing(str):
    x = str[::-1]
    vowels = "aeiouAEIOU"
    count = sum(str.count(vowel) for vowel in vowels)
    return {x : count}