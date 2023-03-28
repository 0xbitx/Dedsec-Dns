<h1 align="center"> DEDSEC DNS SPOOFING </h1>
Use this powerful tool to spoof DNS responses and redirect traffic to any IP address of your choosing. Perfect for testing network security or for educational purposes. 

## Prerequisites
* ettercap
* sudo - [ MUST ]

## Installation
```
git clone https://github.com/0xbitx/Dedsec-Dns.git
cd Dedsec-Dns
sudo python3 dedsec-dns.py 
```

```
  configure /etc/ettercap/etter.dns to redirect targets
     
         www.github.com  PTR 192.168.1.30
         www.github.com  A 192.168.1.30
           *.github.com  A 192.168.1.30
           *.github.com  AAAA ::
```

### TESTED ON FOLLOWING:
* Kali Linux
* Parrot OS
* Ubuntu
* Arch Linux

<h1 align="center"> DISCLAIMER </h1>

<h4 align="center">I'm not responsible for anything you do with this program, so please only use it for good and educational purposes. </h4>

