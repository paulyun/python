miles =[]
gallons=[]
mpg = []
stops = int(input("Enter how many stops you are planning on taking during the trip: "))
miles.append(float(input("Enter the odometer reading on your car for the start of the trip: ")))

for i in range(stops):
  miles.append(float(input("Enter odometer reading for Stop#" +str(i+1)+ ": ")))
  gallons.append(float(input("Enter how many gallons of gas you filled up for Stop#" +str(i+1)+ ": ")))

for i in range(stops):
  mpg.append((miles[i+1]-miles[i]) / gallons[i])

avg = sum(mpg) / len(mpg)

print("Your avg MPG is: ", avg)