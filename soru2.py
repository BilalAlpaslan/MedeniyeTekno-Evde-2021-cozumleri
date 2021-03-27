a,i,b = input().split()

def sayiconvert(sayi):
    if sayi=="bir":return 1
    if sayi== "iki":return 2
    if sayi=="uc":return 3
    if sayi=="dort":return 4
    if sayi== "bes":return 5
    if sayi=="alti":return 6
    if sayi=="yedi":return 7
    if sayi=="sekiz":return 8
    if sayi=="dokuz":return 9
    if sayi=="sifir":return 0
    else:return int(sayi)

def islemconvert(islem,a,b):
    if islem=="eksi" or islem=="-":return a - b
    if islem=="bolu" or islem=="/":return a // b
    if islem=="carpi" or islem=="*":return a * b
    if islem=="arti" or islem=="-":return a + b

print(islemconvert(i,sayiconvert(a),sayiconvert(b)))