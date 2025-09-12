# 1 Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
def calc(n):
  try:
    return 1/n
  except ZeroDivisionError:
    return 'Noldan boshqa son kirit!'
print(calc(2))

# 2. Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer
def calc(n):
  try:
    return 1/int(n)
  except ValueError:
    return 'Raqam kirit!'
print(calc(input('Son kiriting '))) 

# 3 Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.
def calc(n):
  try:
    with open(n,'r') as f:
        return f.read()
  except FileNotFoundError:
    return 'Fayl topilmadi!'
print(calc(input('Fayl nomi va joylashgan joyini kiriting ')))  

# 4 Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.
def calc(w1,w2):
  try:
      for i in (w1,w2):
          if i not in ('0123456789'):
              1+i
      else:
          print('ok')
  except TypeError:
    return 'Raqam kiritilmagan!'
w1=input('Raqam kirit ')
w2=input('Yana raqam kirit ')
print(calc(w1,w2)) 

# 5. Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue.
def calc(tx):
  try:
      with open (tx,'w') as f:
          f.write('tttaaaa')
      return 'OK'
  except PermissionError:
    return 'Fayl ochiq!'
print(calc(input('Faylni ko`rsat '))) 

# 6. Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.
def calc(t):
    try:
        a=[1,2,3,4]
        return a[t]
    except IndexError:
        return 'Noto`g`ri raqam!'
print(calc(int(input('Raqam kirit '))))  

# 7. Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input.
try:
    a=input('Raqam kirit! ')
    print(a)
except KeyboardInterrupt:
    print('Toxtatma')


# 8. Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.
try:
    10/0
except ArithmeticError:
    print('Xato')

# 9. Write a Python program that opens a file and handles a UnicodeDecodeError exception if there is an encoding issue.
try:
    with open('D:\jj.txt','r',encoding='utf-16') as f:
        print(f.read())
except UnicodeDecodeError:
    print('Xato')

# 10. Write a Python program that executes a list operation and handles an AttributeError exception if the attribute does not exist.
try:
    class Dog:
        def bark(self):
            print("Woof!")
    dog = Dog()
    dog.meow()
except AttributeError:
    print('Xato')

####    File Input/Output Exercises

#1. Write a Python program to read an entire text file.
with open ('D:\jj.txt','r') as f:
    print(f.read())

#2. Write a Python program to read first n lines of a file.
with open ('D:\jj.txt','r') as f:
    print(f.readline())

# 3. Write a Python program to append text to a file and display the text.
with open ('D:\jj.txt','a') as f:
    print(f.write('\n 999'))
with open ('D:\jj.txt','r') as f:
    print(f.read())

# 4. Write a Python program to read last n lines of a file.
def rd(n):
    with open ('D:/rbt.txt','r') as f:
        for t in f.readlines()[-n:]:
            print(t)
rd(2)

# 5. Write a Python program to read a file line by line and store it into a list.
def rd():
    ls=[]
    with open ('D:/rbt.txt','r') as f:
        for t in f.readlines():
            ls.append(t)
    return ls
print(rd())

# 6. Write a Python program to read a file line by line and store it into a variable.
def rd():
    dr=""
    with open ('D:/rbt.txt','r') as f:
        for t in f.readlines():
            dr+=t
    return dr
print(rd())

# 7.Write a Python program to read a file line by line and store it into an array.
import array
def rd():
    with open ('D:/rbt.txt','r') as f:
        a=0
        for d in f.readlines():
            if a==0:
                da=array.array('u',d)
            else:
                da.extend(d)
            a+=1
    return da
print(rd())

# 8. Write a Python program to find the longest words.
ls=["ss","ssss","s","sssssss"]
lngst=0  
for l in ls:
    if len(l)>lngst:
        lngst=len(l)
        wrd=l
print(l)

# 9. Write a Python program to count the number of lines in a text file.
sn=0
with open ('D:/rbt.txt','r') as f:
    for n in f.readlines():
        sn+=1
print(sn)

#10. Write a Python program to count the frequency of words in a file.
sn={}
with open ('D:/rbt.txt','r') as f:
    for n in f.readlines():
        for nn in n.split():
            if nn not in sn:
                sn[nn]=1
            else:
                sn[nn]+=1
print(sn)

# 11. Write a Python program to get the file size of a plain file.
import os
print(os.stat('D:/rbt.txt').st_size)

# 12. Write a Python program to write a list to a file.
ls=[1,2,3]
with open ('D:/mis.txt','w') as f:
    f.write(str(ls))

# 13. Write a Python program to copy the contents of a file to another file.
with open ('D:/mis.txt','r') as f, open ('D:/rbt.txt','a') as f2:
    for l in f:
        f2.write(l)

# 14. Write a Python program to combine each line from the first file with the corresponding line in the second file.
with open ('D:/mis.txt') as f, open ('D:/rbt.txt') as f2:
    for l,l2 in zip(f,f2):
        print(l+l2)

# 15. Write a Python program to read a random line from a file.
import random
def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)
print(random_line('D:/rbt.txt'))
# 16. Write a Python program to assess if a file is closed or not.
f = open('D:/rbt.txt','r')
print(f.closed)
f.close()
print(f.closed)

# 17. Write a Python program to remove newline characters from a file.
def nwln(file):
    newfile=open(file).readlines()
    return [x.rstrip('\n') for x in newfile]
print(nwln('D:/rbt.txt'))

#18. Write a Python program that takes a text file as input and returns the number of words in a given text file.
def nwln(file):
    newfile=open(file).read()
    return len(newfile.replace(',',' ').split())
print(nwln('"C:Desktop/rbt.txt"'))

#19. Write a Python program to extract characters from various text files and put them into a list.
import glob
nlst=[]
for n in glob.glob('D:\**.txt'):
    nlst.append(open(n).read())
print(nlst)

#20. Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.
import string
for f in string.ascii_uppercase:
    with open (f'D:/e/{f}.txt','w') as f:
        f.write('')

# 21. Write a Python program to create a file where all letters of the English alphabet are listed with a specified number of letters on each line.
import string
def f_copy(a):
    strin=string.ascii_uppercase
    with open ('D:ktk.txt','a') as f:
        for let in range(int(len(strin)/a+1)):
            f.write(f'{strin[let*a:let*a+a]}\n')
f_copy(3)
