def b_sort(list):

    for i in range(len(list)):
        for j in range(len(list)-1):
            if list[j]>list[j+1]:
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp








list=[4,7,2,45,87,90,43,1]
b_sort(list)
print(list)