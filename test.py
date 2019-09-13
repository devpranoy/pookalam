import csv
import extcolors
import colorpredictor
from pathlib import Path
def filtercolors(color):
	item = []
	for a in color:
		item.append(a)
	for i in range(len(item)):
		if item[i] == "silver":
			color.remove(item[i])
			color.append("white")
		if item[i] == "gray":
			color.remove(item[i])
		if item[i] == "maroon":
			color.remove(item[i])
			color.append("red")
		if item[i] == "olive":
			color.remove(item[i])
			color.append("yellow")
		if item[i] == "lime":
			color.remove(item[i])
			color.append("green")
		if item[i] == "aqua" or item[i] == "teal" or item[i] == "navy":
			color.remove(item[i])
			color.append("blue")
		if item[i] == "fuchsia":
			color.remove(item[i])
			color.append("purple")
		if item[i] == "black":
			color.remove(item[i])
	return color

def coloriser(filename):
	colors, pixel_count = extcolors.extract(filename)
	rgb=[]
	for item in colors:
		rgb.append(item[0])
	color1 = []
	for item in rgb:
		color1.append(colorpredictor.get_colour_name(item))
	filtered_colors = set(color1)
	colors_sorted=filtercolors(list(filtered_colors))
	final = set(colors_sorted)
	final = list(final)	
	row = []
	filename_sorted = str(filename).split('/')
	row.append(filename_sorted[-1])
	for i in range(8):
		row.append("0")
	for items in final:
		if items == "red":
			row[1] = "1"
		if items == "blue":
			row[2] = "1"
		if items == "green":
			row[3] = "1"
		if items == "white":
			row[4] = "1"
		if items == "pink":
			row[5] = "1"
		if items == "orange":
			row[6] = "1"
		if items == "yellow":
			row[7] = "1"
		if items == "purple":
			row[8] = "1"
	with open('onehotencoded.csv', 'a') as csvFile:
    		writer = csv.writer(csvFile)
    		writer.writerow(row)
	csvFile.close()
		
	
for filename in Path('/Users/pranoy/Desktop/pookalam/static/pookalams').glob('**/*.jpg'):
	print(filename)
	coloriser(filename)


