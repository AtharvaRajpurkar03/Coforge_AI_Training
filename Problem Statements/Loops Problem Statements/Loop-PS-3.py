sentence=input("Enter a sentence: ").lower()
vowels=0
consonant=0
for ch in sentence:
    if ch==" ":
        continue
    if ch=="!":
        break
    if ch.isalpha():
        if ch in "aeiou":
            vowels+=1
        else:
            consonant+=1
print(vowels)
print(consonant)
