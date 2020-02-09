# Fibonacci-Python - A project for IT class which displays a specified amount of numbers from the Fibonacci sequence.
# Started writing in 2020 by Keanu Timmermans
# To the extent possible under law, the author(s) have dedicated all copyright and related and neighboring rights to this software to the public domain worldwide. This software is distributed without any warranty.
# You should have received a copy of the Apache License 2.0. If not, see <https://www.apache.org/licenses/LICENSE-2.0>.

def FibRecursion(n):  
   if n <= 1:  
       return n  
   else:  
       return(FibRecursion(n-1) + FibRecursion(n-2))  
nterms = int(input("Enter the terms? "))                           # Pak hier de input van de gebruiker en sla het op in variabel nterms.
  
if nterms <= 0:                                                     # Als er een nummer onder de 0 wordt ingevoerd, print:
   print("Please enter a positive integer")  
else:  
   print("Fibonacci sequence:")  
   for i in range(nterms):  
       print(FibRecursion(i))