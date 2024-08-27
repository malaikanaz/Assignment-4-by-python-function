#Assignment-04 write programs using fuction
#Question#1
#Calculate your age based on the current year and your birth year.
print("Age Calculator")
def ageCalculator()->int:
    #birth year
    birthyear:int = int(input("Enter your birth year= "))
    #current year
    currentyear:int= int(input("Enter the current year="))
    age:int=currentyear-birthyear
    return age
output = ageCalculator()
print("Your age is=", output )

#Question#2
#Write a program that calculates the area of a rectangle using length and width variables.
print("Rectangular Area Calculator")
def RectangularAreaCalculator()->int:
    #length of rectangle
    length:int=int(input("Enter the length of the rectangle= "))
    #length of width
    width:int=int(input("Enter the width of the rectangle= "))
    area:int=length*width
    return area
rectangle=RectangularAreaCalculator()
print("Area of rectangle is=",rectangle)

#Question#3
#Write a program that calculates the area of a circle.
print("Circle Area Calculator")
def CircleAreaCalculator()->float:
    #radius
    radius:float  = float(input("Enter the radius of cirlce = "))
    #value of pie
    pie:float= 3.14159
    circlearea=pie*radius*2
    return circlearea
circle=CircleAreaCalculator()
print("The area of circle is=",circle)
    
#Question#4
#Write a program that calculates the area of the cube.
print("Cube Area Calculator")
def CubeAreaCalculator()->int:
    value:int=6
    #number of sides
    sides=int(input("Enter the number of sides="))
    cubearea=value*sides**2
    return cubearea
cube=CubeAreaCalculator()
print("The area of your cube is=",cube)

#Question#5
# Create a program that converts a temperature from Fahrenheit to Celsius and vice versa using a variable.
print("Temperature Converter From Farenheit To Celsius")
def temperatureconverter()->int:
    temperature = int(input("Enter your temperature in Fahrenheit = "))
    farenheittocelcius=(temperature-32)*5/9
    return  farenheittocelcius
incelsius= temperatureconverter()
print("Temperature in celsius is=",incelsius)

print("Temperature Converter From Celsius To Farenheit")
def covertinfarenheit()->int:
    temperature = int(input("Enter your temperature in celsius = "))
    celciustofarenheit=(temperature*9/5)+32
    return celciustofarenheit
infarenheit=covertinfarenheit()
print("Temperature in farenheit is=",infarenheit)

#Question#6
#Convert a given number of seconds into minutes and seconds using variables.
print("Time Converter From Second To Minutes")
def secondstominutes()->int:
    seconds=float(input("Enter your time in seconds="))
    inminutes=(seconds/60)
    return  inminutes
inmin=secondstominutes()
print("Time in minutes is=",inmin)

print("Time Converter From Minutes To Second ")
def minutestoseconds()->int:
    timeminutes = int(input("Enter your time in minutes = "))
    inseconds=(timeminutes*60)
    return inseconds
insec=minutestoseconds()
print("Time in seconds is=",insec)

#Question#7
#Write a program that calculates the percentage.
print("Percentage Calculator")
def PercentageCalculator()->int:
    obtainedmarks:int= int(input("Enter your obtained marks = "))
    totalmarks:int= int(input("Enter your  total marks = "))
    percentage=(obtainedmarks /totalmarks)*100
    return percentage
percen=PercentageCalculator()
print("percentageis=",percen)

#Question#8
#Write a program that calculates the BMI using height (in meters) and weight (in kilograms) variables.
print("BMI Calculator")
def BMICalculator()->int:
    weight:int = int(input("enter weight in kilogram = "))
    height :int= int(input("enter height in meters = ")) 
    bmi= weight/height**2
    return bmi
BMICALC=BMICalculator()
print("result=",BMICALC)

 #Question#9
   #Write a program that calculates the volume of a cylinder using the formula .
print("Cylinder Volume Calculator")
def CylinderVolumeCalculator()->int:
    radius:int= int(input("Enter the radius of cylinder = "))
    height:int = int(input("Enter the height of cylinder =  "))
    pie:float = 3.141592653589793238462643383279502884197
    volume= pie*(radius**2)*height
    return volume
cylindervolume=CylinderVolumeCalculator()
print("The volume of a cylinderis=",cylindervolume)
