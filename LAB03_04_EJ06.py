#E6
a = 8
b = 6
c = 148

ecu1 = '%d + %d = %d' %(a,b,c)
ecu2 = '-%d = %d' %(b,(a-b))
ecu3 = '%d * %d = %d' %(a,b,(a*b))

ecu4 ='%d / %d = %f'%(a,b,(a/b))
#ecu5 ='%d % %d' %()
ecu6 ='//%d = %d' %(b, (0//a))
ecu7 ='%d**%d = %d' %(a,b,(a**b))


print(ecu1)
print(ecu2)
print(ecu3)
print(ecu4)
print(ecu6)
print(ecu7)