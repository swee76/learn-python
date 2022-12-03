# Building a Translator

# Giraffe Language
# Vowels -> g
# -------------

# dog -> dgg
# cat -> cgt

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter a phrase: ")))

# we can write this below line as
#  if letter in "AEIOUaeiou":
# Like in this way
# if letter.lower() in "aeiou"
