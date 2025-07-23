import sys



MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..--', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', '/': '-..-.',
    '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...',
    ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-',
    '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
    ' ': '/'
}
try:
    assert len(sys.argv ) == 2, "number of args should be 1"
    
    try:   #... --- ...$
        
        S = sys.argv[1]
        print(S)
    except ValueError:
        raise AssertionError("bad argument")
    assert isinstance(S, str) , " the string should not containt special chracters"
    messages = ""
    for i in S:
        print(i , " ")
        assert  i.upper() in MORSE_CODE_DICT ,"AssertionError: the arguments are bad"
        messages +=MORSE_CODE_DICT[i.upper()]
    print(messages)
    

except AssertionError as e:
    print("AssertionError : " , e)
