
# from find_ft_type import all_thing_is_obj

def all_thing_is_obj(object: any) -> int:
    # print( type(object))
    if(object):
        types_set = {  
            list: "List",
            tuple: "Tuple",
            set: "Set",
            dict: "Dict",
            str: "Str",
            }
        for typo in types_set  :
            if isinstance(object, typo):
                if isinstance(object, str):
                    print(object , "is in the kitchen :" , f"{type(object)}")
                else:
                    print(f"{types_set[typo]} : " , f"{type(object)}")
                return 42
        
        print("Type not found")
        return 42
    else :
        return 0

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

all_thing_is_obj(ft_list)
all_thing_is_obj(ft_tuple)
all_thing_is_obj(ft_set)
all_thing_is_obj(ft_dict)
all_thing_is_obj("Brian")
all_thing_is_obj("Toto")
print(all_thing_is_obj(10))




# if __name__ == "__main__": all_thing_is_obj(ft_list)