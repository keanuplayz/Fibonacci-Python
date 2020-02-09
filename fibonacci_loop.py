# Enter number of terms needed                   #0,1,1,2,3,5....
InputNumber=int(input("Enter the terms: "))
FirstElement=0                                         #first element of series
SecondElement=1                                         #second element of series
if InputNumber<=0:
    print("The requested series is",FirstElement)
else:
    print(FirstElement,SecondElement,end=" ")
    for x in range(2,InputNumber):
        next=FirstElement+SecondElement                           
        print(next,end=" ")
        FirstElement=SecondElement
        SecondElement=next