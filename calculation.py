array=[5,'+',2,'-',3,'/',3,'*',4,'**',2]
li=[]
li1=[]
def calc(array:list):
    for a in array:
        if a == "+":
            print("a")
            li.extend(a)
        elif a=="-" :
            li.extend(a)
        elif a=="/" :
            li.extend(a)
        elif a=="*" :
            li.extend(a)
        elif a=="**" :
            li.append(a)
        else:
            li1.append(a)
    print(li)
    print(li1)

calc(array)

def operation(li:list,li1:list):
    for b in range(0,len(li)):
        if b == 0:
            result = li1.pop(0)
            num2=li1.pop(0)

        if li[b]=="+":
            result = result+num2;
    
        if li[b]=="-":
            num3=li1.pop(0)
            result = result-num3;
        
        if li[b]=="/":
            num4=li1.pop(0)
            result = result/num4;

        if li[b]=="*":
            num5=li1.pop(0)
            result = result*num5;

        if li[b]=="**":
            num5=li1.pop(0)
            result = result**num5;
    print(result)
        

operation(li,li1)
                
        

