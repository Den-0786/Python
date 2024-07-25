

def score_vowels(word):
    vowels = ["a", "e", "i", "o", "u", "y"]
    score = 0
    for letter in word:
        if letter in vowels:
            score += 2
        else:
            score += 0
    return score


user_input = input("Enter a word: \n")#.capitalize()
vowel_score = score_vowels(user_input)
print(f"The score for {user_input} is {vowel_score}.")