import math
counter = 0
while (counter < 100):
	outputstring = ""
	counter = counter + 1
	if counter % 3 == 0:
		outputstring = outputstring + "Fizz"
	if counter % 5 == 0:
		outputstring = outputstring + "Buzz"

	if outputstring == "":
		print(counter)
	else:
		print(outputstring)



