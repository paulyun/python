#using if and elseif(elif) statements

weather_condition = input("How is the weather today???" + "\n")

if (weather_condition == "rainy"):
    print("It is rainy today")
    
elif(weather_condition == "sunny"):
    print("It is sunny today")
    
elif(weather_condition == "windy"):
    print("It is windy today")
    
else:
    print("Not a recognizable input")