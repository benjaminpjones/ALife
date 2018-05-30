# for loop, while loop, list, print, string, comparisons

item_tuple = ['apple','blueberry','cherry']
item_list = ['one','two','three']

for item in item_tuple:
    print item
else:
    print 'All items are there!'

while len(item_list) > 0:
    item = item_list.pop(-1)
    print item

