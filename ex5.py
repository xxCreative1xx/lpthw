name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
kilograms = .453592
centimeters = 2.54
weight_in_kilograms = weight * kilograms
height_in_centimeters = centimeters * height

print (f"Let's talk about {name}.")
print (f"He's {height} inches tall.")
print (f"He's {weight} pounds heavy.")
print ("Actually that's not too heavy.")
print (f"Hes's got {eyes} eyes and {hair} hair.")
print (f"His teeth are usually {teeth} depnding on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print (f"If I add {age}, {height}, and {weight} I get {total}.")
print (f"Converting to the metric system, that would be {weight_in_kilograms} and {height_in_centimeters}")
