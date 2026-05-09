def caseN(text: str):
    words = text.split(" ")
    for i in range(len(words)):
        if words[i] == "(up," and i > 0:
            snum_str = words[i+1].rstrip(")")
            snum = int(snum_str)
            for j in range(i - 1, max(0, i - snum)- 1, -1):
                words[j] = words[j].upper()
        if words[i] == "(cap," and i > 0:
            snum_str = words[i+1].rstrip(")")
            snum = int(snum_str)
            for j in range(i-1, max(0, i - snum)-1, -1):
                words[j] = words[j].capitalize()
                words[:i-1] + words[i+2:]
        elif words[i] == "(low," and i > 0:
            snum_str = words[i+1].rstrip(")")
            snum = int(snum_str)
            for j in range(i-1, max(0, i -snum) -1, -1):
                words[j] = words[j].lower()
                words[:i-1] + words[i+2:]
    return " ".join(words)