def numJewelsInStones(J: str, S: str) -> int:
    count = 0
    for index, c in enumerate(S):
        if c in J:
            count += 1
    print(count)


print(numJewelsInStones('aA', S='aAAbbbb'))
