#!/usr/bin/env python3

"""
This is a project from Automate The Boring
Stuff where you create a password
Locker, from the 6th chapter
"""

# Pyperclip allows to copy to clipboard
# it need some installation extras (stackoverflow)
import sys, pyperclip

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

if len(sys.argv) < 2:
	print('Usage: python pw.py [account] - copy account password')
	sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
	pyperclip.copy(PASSWORDS[account])
	print('Password for '+account+' copied to clipboard')
else:
	print('There is no account named '+ account)


