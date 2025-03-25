

with open('text.txt','r',encoding='utf-8') as rf:
    a = rf.read()

lines = a.split('\n')
lines = [x for x in lines if x!='']

for i in '|।॥ \t १२३४५६७८९०1234567890.,':
    a=a.replace(i,'')

print(a)

verses = a.split('\n')
verses = [x for x in verses if x!='']

print(verses)

#lenth counter
lnc = [] 
nc = '्ािीुूेैोौंःँ᳚।ृॢॄॣꣳऽ़॥॒॑ᳲᳳॐ' + ',.| \t' +'1234567890१२३४५६७८९०'
count=0
for w in verses:
    for c in w:
      if c in nc:
        if c == '्':
          count-=1
      else: count+=1
    if count != 0:
      lnc.append(f'{count}') 
    count=0
print(lnc)




#syllabifier
syl=[[]]

matra ='ािीुूेैोौंःँ᳚ꣳ़॒ᳲॄॣ॑ᳳृॢऽ'

for verse in verses:
    A = False
    for n,ch in enumerate(verse): 
        try:
            
            if ch != '्' and verse[n-1] == '्' and A==False and n!=0:
                syl[-1][-1]+=ch

            else: 
                if ch !='्' and verse[n+1] != '्': A=True

                if verse[n+1]!='्' and ch!='्' and ch not in matra:
                    syl[-1].append(ch)
                if verse[n+1]=='्' or ch=='्' or ch in matra:
                    syl[-1][-1]+=ch
                elif ch in '॒॑᳚':
                    syl[-1][-1]+=ch
                
        except:
            if verse[-1]!='्' and ch not in matra:
                syl[-1].append(ch)
            if verse[-1]=='्' or ch in matra:
                syl[-1][-1]+=ch
            
    syl.append([])

print(syl)
print('\n',[len(s) for s in syl],'\n\n')



writetxt=''


# Identify Guru & Laghu (heavy & light, H L)
l='िुृॢ'

#h="्ाीूेैोौंःँᳲᳳꣳॄॣआईऊएऐओऔ"

h= "ाीूेैोौंःँᳲᳳꣳॄॣआईऊएऐओऔ"
hal = '्'

heavy, light= 'H','L'
HL=[[]]


for vn,ver in enumerate(syl):
    for s in ver:
        if   any(ch in h for ch in s):  HL[-1].append(heavy)
        elif any(ch in hal for ch in s): HL[-1].append(heavy)
        else: HL[-1].append(light) 
    HL.append([])
print(HL)


#Identify Swara pattern from the syllables
# *=anudata, -=udatta, ^=svarita, /=dirghaSvarita
swa = [[]]

for vn,ver in enumerate(syl):
    for s in ver:
        # if   '॒' in s: swa[-1].append('*') #low
        # elif '॑' in s: swa[-1].append('^') #high
        # elif '᳚' in s: swa[-1].append('/') #vhigh
        # else: swa[-1].append('-')  #mid
        if   '॒' in s: swa[-1].append('A') #low
        elif '॑' in s: swa[-1].append('S') #high
        elif '᳚' in s: swa[-1].append('D') #vhigh
        else: swa[-1].append('U')  #mid
    swa.append([])
print(swa)

#write and print
for nH,H in enumerate(HL):
    for n2H, H2 in enumerate(H):
        print(syl[nH][n2H],HL[nH][n2H], swa[nH][n2H], end=' | ')
        writetxt += f"{syl[nH][n2H]} {HL[nH][n2H]} {swa[nH][n2H]} | "
    print()
    writetxt+='\n'

writetxt+='\n\n'

#write and print 2

m = 16
k = 4
for nh,H in enumerate(HL):

    try: writetxt += lines[nh]+ f'  [{lnc[nh]}] \n\n'
    except: pass

    for nn, hh in enumerate(H):
        try:
            writetxt += f"{syl[nh][nn]} "
            if (nn+1)%(k)==0:writetxt+=', '  
        except:pass

    writetxt+='\n'

    for nn, hh in enumerate(H):
        try:
            writetxt += f"{HL[nh][nn]} "
            if (nn+1)%(k)==0:writetxt+=', '
        except:pass

    writetxt+='\n'

    for nn, hh in enumerate(H):
        try:
            writetxt += f"{swa[nh][nn]} "
            if (nn+1)%(k)==0:writetxt+=', '
        except:pass
    writetxt+='\n\n\n'
    

#write in file
with open('analysis.txt','w',encoding='utf-8') as wf:
    wf.write(writetxt)
    





'''
m = 16
for nh,H in enumerate(HL):
    for nn, hh in enumerate(H):

    try:
        writetxt += f"{' '.join(syl[nh][:m])}\n{' '.join(HL[nh][:m])}\n{' '.join(swa[nh][:m])}\n"
        writetxt += f"{' '.join(syl[nh][m:])}\n{' '.join(HL[nh][m:])}\n{' '.join(swa[nh][m:])}\n"   
        writetxt+=''
    except:pass

for sy1, h1, sw1 in [syl, HL, swa]:
    for sy2, h2, sw2 in [sy1, h1, sw1]:
        print(sy2,' ',h2,' ',sw2, end=' | ')
    print()

for i in range(len(HL)):
    for j in HL[i]:
        print()



        if s[-1] in '॒॑᳚':
            if   s[-2] in h: HL[-1].append(heavy)
            elif s[-1] in l: HL[-1].append(light)
            else:HL[-1].append(light)
        else:
            if   s[-1] in h: HL[-1].append(heavy)
            elif s[-1] in l: HL[-1].append(light)
            else:HL[-1].append(light)


for vn,ver in enumerate(syl):

    for s in ver:
        try :
            print(lines[vn])
            writetxt+=lines[vn]+'\n'
        except:pass

    print(s, end=' ')
    writetxt += s +' '
    
    print(HL[vn][n],end=' ')
    writetxt += HL[vn][n]
    writetxt += ' '

    print()
    writetxt += '\n'


    if (n+1) % 8 ==0:
        print()
        writetxt += '\n'

    

    for n,s in enumerate(s):
        print(s, end=' ')
        writetxt += s +' '
        o=0
        for j in h:
            if j in s:
                HL.append(heavy)
                o=1
                break
        if o==0:
            HL.append(light)
'''
'''
for n,i in enumerate(syl):
    if i == []: syl.remove([])
    else:
        for nc,ch in enumerate(i):
            if ch == ' ': syl[n].remove(' ')
            break 
''' 
