import csv
import extcolors
import colorpredictor
from pathlib import Path
def coloriser(filename):
	colors, pixel_count = extcolors.extract(filename)
	rgb=[]
	for item in colors:
		rgb.append(item[0])
	sorted_rgb= rgb[1:]
	colors = []
	for item in sorted_rgb:
		colors.append(colorpredictor.get_colour_name(item))
	colors_sorted=set(colors)
	for item in colors_sorted:
		row=[]
		row.append(filename)
		row.append(item)
		with open('pook.csv', 'a') as csvFile:
    			writer = csv.writer(csvFile)
    			writer.writerow(row)
		csvFile.close()
		
	
for filename in Path('/Users/pranoy/Desktop/pookalam/static/pookalams').glob('**/*.jpg'):
    coloriser(filename)


