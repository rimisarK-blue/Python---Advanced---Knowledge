
sequence = input()
opening = []
is_balanced = True

check = {'{': '}', '[': ']', '(': ')'}
for p in sequence:
    if p in "{[(":
        opening.append(p)
    else:
        if not opening:
            is_balanced = False
            break
        current_opening_p = opening.pop()
        if not check[current_opening_p] == p:
           is_balanced = False
           break

if is_balanced:
    print("YES")
else:
    print("NO")



