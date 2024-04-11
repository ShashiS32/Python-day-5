import random

print ("Welcome to Pass Gen")

chars = ["a" , "b" "c" , "d" , "e" , "f" , "g" , "h" , "i" , "j" , "k" , "l" , "m" , "n" ,"o" , "p" , "q" , "r" , "s" , "t" , "u" , "v" , "w" "x" , "y" , "z" , "A" , "B" , "C" ,"D" , "E" , "F" , "G" , "H" , "I" , "J" , "K" , "L" , "M" , "N" , "O" ,"P" , "Q" , "R" , "S" , "T" , "U" ,"V" , "W" , "X" , "Y" , "Z"]

numbers = ["1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "0" ]

symbols = ["!" , "@" , "#" , "$" , "%" , "^" , "&" , "*" , "(" , ")" , "-" , "_" , "=" , "+" , "[" , "{" , "]" , "}" , "|" , ";" , ":" , "<" , ">" , "," , "." , "/" , "?" , "`" , "~"]

password = []

num_of_chars = int(input("How many characters do you want in your password? "))
num_of_numbers = int(input("How many numbers do you want in your password? "))
num_of_symbols = int(input("How many symbols do you want in your password? "))
for letters in range (num_of_chars):
  password.append(random.choice(chars))
  
for letters in range (num_of_numbers):
  password.append(random.choice(numbers))
  
for letters in range (num_of_symbols):
  password.append(random.choice(symbols))

random.shuffle(password)
    
print ("".join(password))