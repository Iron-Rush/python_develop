# ReStudy_Split.py
import re
ls = re.split(r'[1-9]\d{5}', 'BIT100081 TSU100084')
print(ls)
# 限制最大分割数maxsplit
ls = re.split(r'[1-9]\d{5}', 'BIT100081 TSU100084', maxsplit=1)
print(ls)