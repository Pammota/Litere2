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

  li = list(string)
  stlen = len(li)

  #goes line by line on all matrix at once and prints
  for y in range(0,5):
    for x in range(0,stlen):
      picLine(chtoli[li[x]][y])
      print(' ',end='')
    print()

  #formatting prints
  print()
  print()
  print()
  #formatting prints
  

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
    continue


 #to do:
 #make auto text wrap
 
