#lucas kiewek
#addition of two binary strings that returns the sum binary string

a = raw_input('enter a binary number: ')
b = raw_input('enter another binary number: ')

la = list(a)
lb = list(b)

la = la[::-1]
lb = lb[::-1]

bia = 1

for i in range (len(la)):
    la[i] = int(la[i])*bia
    bia *= 2
                
unbia = 0
for i in range (len(la)):
    unbia += la[i]
            
bib = 1
for i in range (len(lb)):
    lb[i] = int(lb[i])*bib
    bib *= 2
        
unbib = 0
for i in range (len(lb)):
    unbib += lb[i]

print unbia
print unbib
        
final = unbia + unbib

print final
        
print 'the sum uf these two binary numbers is: ', str(bin(final)[2:])
