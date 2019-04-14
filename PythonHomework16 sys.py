import sys

English = ("`~!@#$%^&qwertyuiop[]asdfghjkl;'zxcvbnm,./QWERTYUIOP{}ASDFGHJKL:\"|ZXCVBNM<>?");
Russian = ("ёЁ!\"№;%:?йцукенгшщзхъфывапролджэячсмитьбю.ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭ/ЯЧСМИТЬБЮ,");

Word = sys.argv[0] 
RightWord=""

for sumbol in Word:
    RightWord = RightWord + Russian[English.find(sumbol)]
    


print(RightWord)