# ReStudy_Match.py
import re
matchA = re.match(r'[1-9]\d{5}', 'BIT 100055')
matchB = re.match(r'[1-9]\d{5}', '100033 BIT')
if matchA:
    print(matchA.group(0))
if matchB:
    print(matchB.group(0))