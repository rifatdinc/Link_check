#!/usr/bin/python3
import os
import nmap3
from subprocess import Popen, PIPE

# def subPro(ip):
# #     shell = subprocess.run(
# #         ["sudo",'nmap','-p','161',ip,'-sU'], check=True, capture_output=True)
# # #     udpPort = shell.stdout.decode()
# # #     return udpPort
# # # # subPro()


# def subPro(ip):
#     cmd = ['sudo', '-S','./udp.sh',ip]
#     sudopass = 'RootSifresi'
#     # print(sudopass)
#     p = Popen(cmd, stdin=PIPE, stderr=PIPE,universal_newlines=True, stdout=PIPE)
#     # print(sudopass)
#     output = p.communicate(sudopass + '\n')
#     for l in output:
#         asm = l[0:4]
#         print(asm)
#         return asm

# hostname = '10.123.7.3'
# response = os.system('ping -c 1 -W 0.5 ' + hostname)
# if response == 0:
#     print(response)
# else:
#     print('sda')
# print(response)


def Topla(a,b):
    return a * b + 2


print(Topla(105,250))
    



