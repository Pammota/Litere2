#importing letter matrix and dict from letters.py
from letters import *

#the function that converts a string to ascii console text
def strToAscii(string,builder='█'):
  '''
  Info:This is a function that takes as arguments a string and a character and creates a 5x5 pixel representation of that string in ASCII, printing it in the console.


  :param string:Insert a string of text.
  :param builder:Insert the builder of the ascii words. If left empty then '█' will be used.
  '''
  
  #converts list to ascii line and prints it
  def picLine(li):
    le = len(li)
    for i in range(0,le):
      if  li[i] == 0:
        print(' ',end='',sep='')
      elif li[i] == 1:
        print(str(builder),end='',sep='')

  #formatting prints
  print()
  print()
  print()
  #formatting prints

  #initializari
  li = list(string)
  stlen = len(li)
  mxlen = 19

 #goes line by line on all matrix at once and prints
  def lineByLinePrint(lis,stln):
    for y in range(0,5):
      for x in range(0,stln):
        picLine(chtoli[lis[x]][y])
        print(' ',end='')
      if y == 5:
        print()
      else:
        print()

  #splits string in 19 char max lists
  def splitter(strng, mxlene):
    def afisam(lest):
      s = ' '.join(lest)
      l = list(s)
      lineByLinePrint(l,len(l))

    #returneaza cate caractere mai sunt pana la 
    #terminarea propozitiei, de la cuvantul cu indicele i in colo
    def remaincalc(li,i):
      #listcpy = li.copy()
      lendelist = len(li)
      emptylist=[]
      for j in range(i,lendelist):
       emptylist.append(li[j])
       if j!=lendelist-1:
          emptylist.append(' ')
      news = ''.join(emptylist)
      return len(news)
    
    #returneaza o lista cu cuvintele ramase dupa indicele i din lista li
    def remainshow(li,i):
      #listcpy = li.copy()
      lendelist = len(li)
      emptylist=[]
      for j in range(i,lendelist):
        emptylist.append(li[j])
      return emptylist
      
    #initializari
    lister = strng.split() #lista cuvinte 
    constructlist = [] #lista goala
    le = len(lister) # lungime lista cuvinte
    #strng = sirul initial in format string
    
    if len(strng) <= mxlene: #mxlene=19
      lineByLinePrint(list(strng),len(strng)) #nu depaseste 19 char, afisam!
    else:
      i = 0
      indexi =0
      while i<le:#parcurgem lista cu cuvinte
        if (len(' '.join(constructlist))+len(lister[i])+1) <= mxlene: #mxlene=19
          constructlist.insert(i,lister[i]) #daca adaugam cuvantul urmator la lista de constructie nu depaseste 19
          i+=1
        else: #mxlene =19
          afisam(constructlist) #afisam ce am construit, stergem, si reluam
          print()
          constructlist.clear() #curata functia pt urmatoarea linie din propozitie
          indexi=i
      afisam(remainshow(lister,indexi))
                
  #calling the master function
  splitter(string,mxlen)

  #formatting prints
  print()
  print()
  print()
  #formatting prints
  
#ciclu infinit pana la citirea lui 2
while True:
  print('''What do you want to do?
    1.Enter text;
    2.Exit;
  ''')
  doit = input()
  if doit=='1':
    inp = input("Enter text:\n")
    strToAscii(inp)
    input()
  elif doit=='2':
    break
  else:
    print("Invalid option, try again.\n")
    
#finished 23/10/2020 - 01:14 AM
