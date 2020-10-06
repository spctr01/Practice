def per(string):
    if string =='':
        return ['']
    ls = []

    for x in string:
        new_string = per(string.replace(x, '', 1))
        for i in new_string:
            ls.append(x+i)
    return ls

print(per('abcd'))