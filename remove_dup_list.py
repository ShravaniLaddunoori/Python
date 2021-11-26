input_list = [5,8,3,1,7,3,9,7,0,5]
print('List is:'+str(input_list))
res = []
for x in input_list:
    if x not in res:
        res.append(x)
print('After removing duplicates'+str(res))
