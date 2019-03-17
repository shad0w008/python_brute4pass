#coding=utf-8

import random
import hashlib
import re
import sys
from config import *



def md5_calc(key):
  return hashlib.md5(key).hexdigest()


def sha1_encrypt(key):
  return hashlib.sha1(key).hexdigest()


# randomize the dict elements
def inits(n):
  while n:
    random.shuffle(tmp)
    n-=1


#q=eval("(('{}{}{}{}'.format(h,i,j,k),hashlib.md5('{}{}{}{}'.format(h,i,j,k)).hexdigest()) for h in c1 for i in c2 for j in c3 for k in c4)")


def loops(p,z1,single,salt=''):
  signs=False
  z2=1
  z4=len(p)
  if z4==32 or z4==16:
    a4='md5'
  elif z4==40:
    a4='sha1'
  elif z4==56:
    a4='sha224'
  elif z4==64:
    a4='sha256'
  elif z4==96:
    a4='sha384'
  elif z4==128:
    a4='sha512'
  else:
    print('Invalid Format.')
    return
  if single:
    z2=1
  else:
    z2=z1
  while z2<=z1:
    print('test password with length:'+str(z2)+'\n')
    a1='{}'*z2+salt
    a2=','.join(alls[:z2])
    a3=''
    for z3 in range(z2):
      a3+=' for {} in tmp'.format(alls[z3])
    expr="(('{0}'.format({1}),hashlib.{3}('{0}'.format({1})).hexdigest()){2})".format(a1,a2,a3,a4)
    #print(expr)
    pp=eval(expr)
    if z4 !=16:
      for x,y in pp:
        if y==p:
          print('Found KEY:\n')
          if len(salt) !=0:
            print('text:',x[:-len(salt)],'salt:',salt,a4,y)
          else:
            print('text:',x,a4,y)
          signs=True
          break
        else:
          continue
    else:
      for x,y in pp:
        if y[8:-8]==p:
          print('Found KEY:\n')
          if len(salt) !=0:
            print('text:',x[:-len(salt)],'salt:',salt,a4,y)
          else:
            print('text:',x,a4,y)
          signs=True
          break
        else:
          continue
    if signs:
      break
    z2+=1



def main():  
  p=raw_input('input encrypted pass:')
  p=p.strip()
  print('')
  p0=raw_input('input salt or press ENTER if no salt:')
  salt=p0.strip()
  print('')
  n=raw_input('input the text length(predict):')
  n=n.strip()
  try:
    t=re.findall('\d+',n)[0]
  except:
    print('Invid parameter!!!')
    exit()
  print('')
  ts='Only try length of {0}(input Y) or 1-{0}(input N):'.format(n)
  n0=raw_input(ts)
  s0=n0.strip()
  if s0 not in ['Y','y','N','n']:
    print('Please input Y/y or N/n!!!')
    exit()
  print('')
  if s0 in ['Y','y']:
    single=False
  if s0 in ['N','n']:
    single=True
  if p and n and t==n:
    inits(int(n))
    loops(p,int(n),single,salt)
  
  
if __name__=='__main__': 
  main()
  
