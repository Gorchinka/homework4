def count_consonants_and_vowels(word):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowels = 'aeiou'
    
    consonant_count = 0
    vowel_count = 0
    
    for char in word:
        if char in consonants:
            consonant_count += 1
        elif char in vowels:
            vowel_count += 1
            
    return consonant_count, vowel_count

word = input("Введите слово: ")
consonant_count, vowel_count = count_consonants_and_vowels(word)

print("Количество согласных букв:", consonant_count)
print("Количество гласных букв:", vowel_count)