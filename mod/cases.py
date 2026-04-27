def cases(s:str):
    each = s.split(" ")
    for i in range((len(each)- 1), 0, -1):
        if each[i] == "(hex)" and i > 0:
            each[i-1] = str(int(each[i-1], 16))
            each = each[:i] + each[i+1:]
        elif each[i] == "(bin)" and i > 0:
            each[i-1] = str(int(each[i-1], 2))
            each = each[:i] + each[i+1:]
        elif each[i] == "(up)" and i > 0 :
            each[i-1] = each[i-1].upper()
            each = each[:i]+each[i+1:]
        elif each[i] == "(low)" and i > 0:
            each[i-1] = each[i-1].lower()
            each = each[:i]+each[i+1:]
        elif each[i] == "(cap)" and i > 0:
            each[i-1] = each[i-1].capitalize()
            each = each[:i]+each[i+1:]
    return " ".join(each)