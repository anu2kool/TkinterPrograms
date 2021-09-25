#lists
lst=[3,2,4,1,5,6,7]
#function1->sorting of the lists
lst.sort(reverse=False)
print(lst)

#function2->append
for i in range(5):
    lst.append(3)
print(lst)

#function3->count
lst.append(10)
print(lst.count(9))
#function4->insert
lst.insert(0,9)
#lst.append(9)
lst.extend((1,2,3,7))
print(lst)
int->1424