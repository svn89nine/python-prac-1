h = float(input("Your height in Inches: "))
w = float(input("Your weight in pounds: "))
i = h * 0.0254
p = w * 0.4536

import math
sh=(math.pow(i,2))
bmi= p / sh
print("Your BMI: "+ str(bmi))

