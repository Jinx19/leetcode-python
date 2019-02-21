s = "0P"
if s is None:
    print(True)
lo, hi = 0, len(s) - 1
while not s[lo].isalnum():
    lo += 1
while not s[lo].isalnum():
    hi -= 1

if lo > hi:
    print(False)

tag = True

while lo < hi:
    while not s[lo].isalnum():
        lo += 1
    while not s[hi].isalnum():
        hi -= 1
    charLo = s[lo].lower()
    charHi = s[hi].lower()
    if charLo != charHi:
        tag = False
        break
    lo += 1
    hi -= 1

print(tag)
