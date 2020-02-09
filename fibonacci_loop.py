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