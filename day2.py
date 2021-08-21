import math
import os
import random
import re
import sys

mealCost=float(input("Enter the cost=>"))
tipPercent=int(input("Enter the percent=>"))
taxPercent=int(input("Enter the percent=>"))
tipPercent=(mealCost*tipPercent)/100
taxPercent=(mealCost*taxPercent)/100
total=mealCost+tipPercent+taxPercent
print(round(total))
