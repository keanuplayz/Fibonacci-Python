# Fibonacci-Python - A project for IT class which displays a specified amount of numbers from the Fibonacci sequence.
# Started writing in 2020 by Keanu Timmermans
# To the extent possible under law, the author(s) have dedicated all copyright and related and neighboring rights to this software to the public domain worldwide. This software is distributed without any warranty.
# You should have received a copy of the Apache License 2.0. If not, see <https://www.apache.org/licenses/LICENSE-2.0>.

InputNumber=int(input("Enter the terms: "))                     # Voer hier het aantal Fibonacci nummers in
                                                                # Het aantal Fibonacci nummers die worden weergegeven hangen af van de input van InputNumber

FirstElement=0                                                  # Definitie voor het eerste element
SecondElement=1                                                 # Definitie voor het tweede element

if InputNumber<=0:                                              # Als er een nummer onder de 0 wordt ingevoerd, print:
    print("The requested series is",FirstElement)
else:                                                           # Anders, start de Fibonacci reeks met het aangegeven nummer bij InputNumer
    print(FirstElement,SecondElement,end=" ")
    for x in range(2,InputNumber):
        next=FirstElement+SecondElement                           
        print(next,end=" ")
        FirstElement=SecondElement
        SecondElement=next


                                                                # Translation of comments in order of appearance:
                                                                # Enter the amount of Fibonacci numbers here
                                                                # The amount of Fibonacci numbers that are displayed depend on the integer entered in InputNumber
                                                                # Definition for the first element
                                                                # Definition for the second element
                                                                # If a number below 0 is entered, print:
                                                                # Else, start the Fibonacci sequence with the indicated integer from InputNumber