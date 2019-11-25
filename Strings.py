def left(a:str)->str:
    return a.lstrip();

print(left("    sabin    "));


def right(a:str)->str:
    '''this is a function '''
    return a.rstrip();

print(right("    sabin    "));



def strip(a:str)->str:
    return a.strip();

print(strip("    sabin    "));


def Upper(li: list , num):
        print( li[num].capitalize());

Upper(["dog","cat","rat"],2);


def func(li: list):
        print( f" \t he is a {li[0]} \n I am a {li[1]} \n You are a {li[2]}");

func(["Doctor","Engineer","Lab techincian"]);


def func(li: list):
        li[0]="Chef"
        print( f" \t he is a {li[0]} \n I am a {li[1]} \n You are a {li[2]}");

func(["Doctor","Engineer","Lab techincian"]);

list1 = ["a","b","c","d","e"]
list1.extend(["f","g"])
list1.insert(2,"c")
print(list1)
