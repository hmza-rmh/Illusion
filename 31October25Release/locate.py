from os import getcwd as c; b, newb = c().split('/'), [];
for x in b: newb.append("'"+x+"'") if ' ' in x else newb.append(x)
re = '/'.join(kk for kk in newb); re = re[1:] if re.startswith('/') else re; print(re.replace('emulated/0', 'shared'))