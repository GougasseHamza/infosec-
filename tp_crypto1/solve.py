apl = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def encrypt(c , k ) : 
    res=""
    for char in c : 
        if char == ' ' : 
            res+=" "
            continue
        idx = apl.index(char)
        nidx = (idx + k )%26 
        res+=apl[nidx]
    return res 




def decrypt(e , k) : 

    res=""
    for char in e : 
        if char == ' ' : 
            res+=" "
            continue
        idx = apl.index(char)
        nidx = (idx - k +26 )%26 
        res+=apl[nidx]
    return res 

print(encrypt('CRYPTO IS FUN UNTIL THE PROFESSOR SAYS QUIZ', 4))
print(decrypt('GWCL JMBBMZ VWB JM CAQVO BWWTA BW AWTDM BPQA', 8))


def  deckeyunknown(e) : 
    for k in range(1,27) : 
        print(decrypt(e,k)) 

print(deckeyunknown("ESP VPJ TD FYVYZHY ECJ MCFEP QZCNP"))


sub = {
    'A': 'Q',
    'B': 'M',
    'C': 'J',
    'D': 'Z',
    'E': 'T',
    'F': 'G',
    'G': 'F',
    'H': 'K',
    'I': 'P',
    'J': 'W',
    'K': 'L',
    'L': 'S',
    'M': 'B',
    'N': 'O',
    'O': 'X',
    'P': 'N',
    'Q': 'C',
    'R': 'R',
    'S': 'Y',
    'T': 'E',
    'U': 'V',
    'V': 'H',
    'W': 'I',
    'X': 'A',
    'Y': 'D',
    'Z': 'U',
    " " :" "
}


rev={}

for key in sub : 
    rev[sub[key]] = key 


def subcipher(c) : 
    res=""
    for char in c : 
        res+=sub[char]
    return res 

def subdecipher(e) :
    res=""
    for char in e : 
        res+=rev[char]
    return res 


print(subcipher("KEEP THE SECRET SAFE"))

print(subdecipher("ERVYE DXVR SXFPJ"))

sub ={}
rev={}

def freq(c):
    cnt={}
    for char in c: 
        cnt[char]=cnt.get(char , 0) +1
    return cnt 


order=['E', 'T', 'R', 'S', 'O' ,'A', 'H', 'N', 'D' , 'I', 'G', 'L']
from collections import Counter
def deciphersub(ct) : 
    letters = [c for c in ct if c.isalpha()]
    counts = Counter(letters)
    total = len(letters)
    ordered=counts.most_common()
    mapping={}

    for i in range(len(ordered)) : 
        l=ordered[i][0]
        if i < len(order) : 
            mapping[l]=order[i]
        else : 
            mapping[l]="*"
    res=""
    for c in ct : 
        if c.isalpha() :
            res+=mapping[c]
        else : 
            res+=c
    return res 

ct="""EKT YTJRTE BTYYQFT PY KPZZTO PO EKPY NQRQFRQNK.
STEETR GRTCVTOJD ZXTY OXE RTHTQS EKT IKXST LTD,
MVE PE FPHTY Q FXXZ YEQRE.
SXXL GXR JXBBXO IXRZY, RTNTQETZ NQEETROY,
QOZ YKXRE IXRZY.
IKTO DXV RTJXHTR EKT BTYYQFT,
EKT HPFTOTRT LTD KQY GXVR STEETRY."""
print(deciphersub(ct))


"ABCD"
"THE"
"EKT"
from collections import Counter

ct = """VVHWGQUIVYHIRSUPGTWXJSVIPCWIUPHGCIVIVVHPGHWITSDTRSDVUSYITMZL
GFHIXSUCVSDQOSPFGFVLQIOHEVHGMSDGJQRPWAQWGSNXJSPSUHIVGEXIPHVC
OPRPCBGYUSLXVCUIECYITHKIMSBAJSQXJSPIUGDKGPHGQAHWEZHETSQXGFWL
GOFGGGVAQFGIEZLTUS"""

ct = ''.join(c for c in ct.upper() if c.isalpha())

groups = [ct[i::4] for i in range(4)]

for i, group in enumerate(groups):
    counts = Counter(group)
    ordered = counts.most_common()
    for letter, count in ordered:
        freq = count /len(group) * 100
def findkey(cipher, plain):
    cipher = ''.join(c for c in cipher.upper() if c.isalpha())
    plain= ''.join(c for c in plain.upper() if c.isalpha())
    key = ""
    for c, p in zip(cipher, plain):
        ci=apl.index(c)
        pi=apl.index(p)
        ki=(ci-pi+26) % 26
        key+= apl[ki]

    return key

key=""

for group in groups :
    counts=Counter(group)
    mostfrequent=counts.most_common(1)[0][0]
    key+=findkey(mostfrequent,"E")

print("Key:",key)


def vigenere_decrypt(cipher,key) :
    res=""
    for i in range(len(cipher)) :
        ci=apl.index(cipher[i])
        ki=apl.index(key[i%len(key)])
        pi=(ci-ki+26)%26
        res+=apl[pi]
    return res


plaintext=vigenere_decrypt(ct,key)
print("Plaintext:",plaintext)

