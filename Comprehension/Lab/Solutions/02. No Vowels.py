
text = input()

VOWELS = {'a', 'o', 'u', 'e', 'i'}

result = [ch for ch in text if ch.lower() not in VOWELS]

print(''.join(result))