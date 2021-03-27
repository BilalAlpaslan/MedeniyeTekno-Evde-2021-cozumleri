a,b=input().split(" ")

def harfconvert(sayi):
    if sayi=="a":return 1
    if sayi=="b":return 2
    if sayi=="c":return 3
    if sayi=="d":return 4
    if sayi=="e":return 5
    if sayi=="f":return 6
    if sayi=="g":return 7
    if sayi=="h":return 8
    if sayi=="i":return 9
    if sayi=="j":return 10
    if sayi=="k":return 11
    if sayi=="l":return 12
    if sayi=="m":return 13
    if sayi=="n":return 14
    if sayi=="o":return 15
    if sayi=="p":return 16
    if sayi=="q":return 17
    if sayi=="r":return 18
    if sayi=="s":return 19
    if sayi=="t":return 20
    if sayi=="u":return 21
    if sayi=="v":return 22
    if sayi=="w":return 23
    if sayi=="x":return 24
    if sayi=="y":return 25
    if sayi=="z":return 26

def coz(a,b):
    if b-a>=0:x=b-a
    else:x=26-(a-b)
    harflist=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    return harflist[x]


for i,j in zip(a,b):print(coz(harfconvert(i.lower()),harfconvert(j.lower())).upper(),sep="",end="")
    