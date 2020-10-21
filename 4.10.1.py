spam = ['apple', 'banana', 'tofu', 'cats', 'dogs']
# def combine(items):
#     items.insert(len(items)-1, 'and')
#     for each in items:
#         print(each+',', end='')
#
# combine(spam)

def combine(items):
    items_last = items[-1]
    items.remove(items[-1])
    for each in items:
        print(each + ',', end=' ')
    print('and' + ' ' + items_last)


combine(spam)