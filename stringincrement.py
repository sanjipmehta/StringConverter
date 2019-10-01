#write a program for following requirement?
#-->a4k3b2
#ans-->aeknbd

input1=input("Enter the mix of string and number:")
l1=[]
l2=[]
out=[]
for x in range(0,len(input1)):
	
	if input1[x].isalpha():
		l1.append(input1[x])
	else:
		l2.append(input1[x])
for x in range(0,len(l2)):

	k=chr((ord(l1[x])+int(l2[x])))
	m=l1[x]+k
	out.append(m)
final=''.join(out)
print(final)