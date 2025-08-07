def sort_by_values(d):
    l = sorted(d.items(), key=lambda item: item[1])
    return dict(l)

a = {"a" : 1, "b" : 3, "c" : 2}
print(sort_by_values(a))