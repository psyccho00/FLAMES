def remove_common(l1, l2):

    for i in range(len(l1)):
        if l1[i] in l2:
            x = l1[i]
            list2.remove(x)
            rem_list.append(x)

    for j in range(len(rem_list)):
        y=rem_list[j]
        list1.remove(y)

    list3= list1 + list2
    p.append(list3)
    return list3


p1= input("Enter player1 name: ").lower().strip()
p2= input("Enter player2 name: ").lower().strip()
list1=list(p1)
list2=list(p2)
rem_list=[]
p=[]

result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]

string=remove_common(list1,list2)
print(string)
game=True
while game is True:

    ls=len(string)
    lr=len(result)
    new_list=[]
    copy = string
    # fill= textwrap.fill(new_list,len(new_list))
    f_count=0
    l_count=lr
    for i in range(len(copy)):
        if ls>1:
            # a=copy[lr-1]
            right=copy[lr+1:]
            left=copy[:lr]
            print(right)
            print(left)
            rl = left + right

            # print(rl)
        else:
            game= False
