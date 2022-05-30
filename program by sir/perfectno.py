Enemy,Friend=5,2
st='no better Friend no worse enemy'.split()
re=st[Enemy%20] and None if Enemy+Friend<len(st)else st[Friend%20]
print(re,eval(re))