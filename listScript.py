names=['Kevin', 'Gonzalez', 'Revo', 'Coder']

print("The first person name is " , names[0])

names[0]='KevinGonzalez'
names[1]='RevoCoder'
names[2]='ThanZawAou'
names[3]='Robots'

print(names)
print(len(names))

newList=['Tankhoe', 'Village']

fullList=newList+names

print(len(fullList))

print(fullList[4], "was born in",fullList[0] , fullList[1],".")


for ele in fullList:
    print(ele,end="\n")


for i in range(0,12):
    print(i)