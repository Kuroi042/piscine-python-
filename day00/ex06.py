


# def iseven(num):
#     return num %2 == 0


# def isodd(num):
#     return num%2 !=0   


def ft_filter(funct , iterable):

    return [i for i in iterable if funct(i)]

# itera = {0 , 5 , 2 , 88 , 100}

# print(ft_filter(isodd, itera))

# print(ft_filter(iseven, itera))

#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
import sys

try:
    assert(len(sys.argv)==3) , "argument must be 2 "
    S = sys.argv[1]
    try:
        N = int(sys.argv[2])
    except ValueError:
        raise AssertionError("second arg should be integer")
    assert isinstance(S, str), "First argument must be a string"
    is_longuer = lambda word : len(word)>N
    res =  ft_filter(is_longuer, S.split())
    print(res)




except AssertionError as e:
    print("AssertionError " , e)


    
    



    
    

    