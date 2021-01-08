#연습 104번
def make_list():
    list=[]
    fact=True
    while fact==True:
        num=input("숫자를 입력해주세요(종료를 원하면 0을 입력해주세요): ")
        if num=="0":
            fact=False  
        else:
            num=int(float(num))
            list.append(num)
    return list  
list=make_list()
list.sort()
print(list)


#연습 106번
def calculation(p):
    list=[]
    for i in range(p):
        num=int(input("데이터 값을 입력해주세요: "))
        list.append(num)
    list.sort()
    print("원래 데이터 목록은 {}입니다.".format(list))
    new_list=list
    del new_list[0]
    del new_list[0]
    del new_list[-1]
    del new_list[-1]
    print("특이치가 제거된 목록은 {}입니다.".format(new_list))
p=int(input("변수의 개수를 입력해주세요: "))
if p<=4:
    print("5개 이상의 숫자를 입력해주세요")
else:
    calculation(p)


#연습 108번
#음수와 양수의 크기비교가 잘 되어야함
def int_num():
    fact=True
    int_list=[]
    while fact==True:
        num=input("정수를 입력해주세요: ")
        if num=='':
            return int_list
        else:
            num=int(num)
            int_list.append(num)
int_list=int_num()
int_list.sort()
print(int_list)