#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import subprocess

print "*************************************************"
print "*                 BASIT TARAYICI                *"
print "*************************************************"
ip = raw_input("[?] Lütfen basit tarama yapılacak ip adresini giriniz. (Format: X.X.X.X))\n")

if not os.path.exists('/usr/bin/nmap'):
	print "[X] NMAP kurulu değil. (Bakilan dizin: /usr/bin/nmap)"
else:
	NMAP_KOMUT = "nmap -sS -sV -Pn -p80,443,139,445,161,3389 %s" % ip
	subprocess.Popen([NMAP_KOMUT], stdout=subprocess.PIPE)
