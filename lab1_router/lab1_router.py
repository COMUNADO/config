
#from telnetlib import Telnet
#with Telnet('172.17.9.151', 4008) as tn:
#   tn.interact()

#   file = open('bebra.txt',encodind='utf-8')
#   for row in file:
#       print (row)


from distutils.command.config import config
import telnetlib

HOST = "172.17.9.151"
port = 4008


tn = telnetlib.Telnet(HOST, port)
config_filename='bebra.txt'
with open(config_filename, 'r') as config_file:
    for line in config_file:
        tn.write(line.encode('utf-8') + b"\n")


#tn.read_until(b"# ")

#config_filename = 'bebra.txt'
## �������� ����������� ��� ����� �������
#tn.write(b"configure terminal\n")
#with open(config_filename, 'r') as config_file:
#    for line in config_file:
#        tn.write(line.encode('ascii') + b"\n")
#        tn.read_until(b"# ")


#import telnetlib

## ��������� ����������� � ����������� Cisco
#host = '172.17.9.151:'


## ��� ����� � �������������, ������� ����� ���������
#config_filename = 'bebra.txt'

## ����������� � ����������� Cisco ����� Telnet
#try:
#    tn = telnetlib.Telnet(host)
#except Exception as e:
#    print(f"������ ��� �����������: {str(e)}")
#    exit()


## �������� ����������� ��� ����� �������
#tn.read_until(b"# ")

## �������� ������� ��� �������� ������������ �� �����
#tn.write(b"configure terminal\n")
#with open(config_filename, 'r') as config_file:
#    config_text = config_file.read()
#    tn.write(config_text.encode('ascii') + b"\n")
#    tn.write(b"end\n")

## ���������� ������ Telnet
#tn.write(b"exit\n")

#print("������������ ��������� �������.")




