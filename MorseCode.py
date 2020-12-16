ra_lst = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',' ','','0','1','2','3','4','5','6','7','8','9']
en_lst = ["._","_...","_._.","_..",".",".._.","__.","....","..",".___","_._","._..","__","_.","___",".__.","__._","._.","...","_",".._","..._",".__","_.._","_.__","__.."," ",'',"_____",".____","..___","...__","...._",".....","_....","__...","___..","____."]
def enCode(raw_txt):
    encoded = ""
    for i in raw_txt:
        if en_lst[ra_lst.index(i)] != ' ':
            encoded += en_lst[ra_lst.index(i)] + ' '
        else:
            encoded += '/ '
    return encoded
def deCode(en_txt):
    raw_txt = ""
    for i in en_txt:
        lst = i.split(' ')
        for j in lst:
            raw_txt += ra_lst[en_lst.index(j)]
        raw_txt += ' '
    return raw_txt
if __name__ == "__main__":
    print("(1) --> Encode\n(2) --> Decode")
    c = int(input("Enter your Choice : "))
    while c < 1 or c > 2:
        print("Please Enter valid inputs! (It should be either 1 or 2)")
        c = int(input("Enter your Choice again : "))
    if c == 1:
        raw_txt = str(input("Enter the string to encode (a-z, A-z, 0-9) : ")).upper()
        print(enCode(raw_txt))
    else:
        en_txt = str(input("Enter the string to encode (It should only contain morse code elements, that are '.', '_', ' ', '/') : ")).split("/")
        print(deCode(en_txt))
    n = input("Press Enter to continue...")
