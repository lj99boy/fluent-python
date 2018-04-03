"""

"""

colors = ['black','white']
sizes =['S','M','L']

# print(tuple(('%s %s'%(c,s) for c in colors for s in sizes)))
for tshirt in ('%s %s'%(c,s) for c in colors for s in sizes):
    print(tshirt)