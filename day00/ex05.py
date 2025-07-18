import sys
import os 



def calculate(text):
    digit = 0
    upper = 0
    lower = 0
    spaces = 0
    punct = 0
    if text:
        # for i in range (1, len(text)):
        #     string = text[i]
            # print(string)
            
        for char in text:
                
                # print(string)
                if char.isdigit() == True:
                                    digit+=1
                elif(char.isupper()==True):
                                    upper+=1
                elif(char.islower()==True):
                                    lower+=1
                elif(char.isspace()==True):
                                    spaces+=1
                elif(ponctuations(char) == True):
                                    punct+=1


        

        print("The  text contains ",f"{len(text)}", "characters:")
        print(upper ," upper letters" )
        print(lower , " lower letters")
        print(punct , " punctuation marks")
        print(spaces, " spaces")
        print(digit , " digits")
    
def ponctuations(jomla )->int:
    
    count = 0
    data =   "!/#$%&'()*+,-./:;<=>?@""[\]^_`{|}~"

    for n in data:
        if jomla == n:
            count+=1

        
    return count

        
    
def main():
    

    if (len(sys.argv)<2):
        print("What is the text to count?")
        try:
            string = sys.stdin.read()
        except KeyboardInterrupt:
            print("\nInput interrupted.")
            return

    else:
        string = ' '.join(sys.argv[1:])
    
    calculate(string)
    
if __name__ == "__main__":
    main()
