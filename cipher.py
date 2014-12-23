CS303
=====

projects 

import math
import sys

#Encrypting the variable, encry_message
def encrypt(encry_message):
  odd_str =""
  even_str =""
  for i in range(0, len(encry_message), 2):
    even_str += encry_message[i]
  for j in range(1, len(encry_message), 2):
    odd_str += encry_message[j]
  return odd_str + even_str

#Decrypting the variable, decry_message
def decrypt(decry_message):
  odd_str ="" 
  even_str =""
  for i in range (0, int(math.floor(len(decry_message)/2))):
    odd_str += decry_message[i]
  for j in range (int(math.floor(len(decry_message)/2)), len(decry_message)):
    even_str += decry_message[j]
  message =""
  for i in range (0, len(odd_str)):
    message += even_str[i]
    message += odd_str[i]
  return message

def main():
  E=""
  D=""
  line = input('Do you want to encrpyt or decrypt? (E/D):')
    
#Reponse should open input.txt file
  line = str (line)
  outputstr=""
  if (line != 'E' and line !='D'):
    print('Wrong input. Bye.')
  elif (line == 'E' or line == 'D'):
    s = open('input.txt', 'r')
    outputstr = encrypt(s.readline())
    s.close()
  else: 
    s = open('input.txt', 'r')
    outputstr = decrypt(s.readline())
    s.close()
  o = open('output.txt', 'w')
  o.write(outputstr)
  o.close()
  print('Output written to output.txt')
main()
