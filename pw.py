#! python3
# pw.py - An insecure password locker program.

import sys
import pyperclip

PASSWORDS = {'email': 'Azula1002',
             'gmail': 'MyPassword21'}

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for {} copied to clipboard'.format(account))
else:
    print('There is no account named {}'.format(account))
