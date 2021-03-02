
text = input()

symbols = {}

for ch in text:
    symbols[ch] = text.count(ch)

sorted_date = sorted(symbols.items(), key=lambda x: x[0])
for el in sorted_date:
    print(f"{el[0]}: {el[1]} time/s")