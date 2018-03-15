import csv

print("""
This program is developed for MAT271E course in ITU.
It only works with CSV files.
If you are not using windows and trying to find an alternative for minitab,
you can download, use, change and redistribute this file.
______________________________________________________________________________
""")
file = input("\n\n\nWrite down the name of CSV file (for ex: example.csv):")

with open(file) as input_file:
    content = []
    for row in csv.reader(input_file):
        for element in row:
            try:
                element = float(element)
                content.append(element)
            except:
                continue

sorted_content = sorted(content)
			

def quartile():
	if len(content)%2 == 1:
		index = (len(content)-1) // 2 #from formula it is +1 but indexes starts
		#from 0. So its used as -1 her
		median = sorted_content[index]

	else:
		index = len(content)//2
		median = (sorted_content[index] +  sorted_content[index-1]) / 2

	q1 = []
	q3 = []
	for element in sorted_content:
		if element < median:
			q1.append(element)
		elif element>median:
			q3.append(element)
	if len(q1)%2 == 0:
		index = len(q1) // 2
		q1 = (q1[index]+q1[index-1]) / 2
		print("First quartile = {}\n\n".format(q1))
	else:
		index = (len(q1) -1) //2
		q1 = q1[index]
		print("First quartile = {}\n\n".format(q1))
	if len(q3)%2 == 0:
		index = len(q3) // 2
		q3 = (q3[index]+q3[index-1]) / 2
		print("Third quartile = {}\n\n".format(q3))
	else:
		index = (len(q3) -1) //2
		q3 = q3[index]
		print("First quartile = {}\n\n".format(q3))
	
		

def mean():
    mean = 0
    for element in content:
        mean += element
    mean = mean / len(content)
    print("Mean = {}\n\n\n".format(mean))

def median_calc():

    if len(content)%2 == 1:
        index = (len(content)-1) // 2 #from formula it is +1 but indexes starts
                                      #from 0. So its used as -1 here
        median = sorted_content[index]
        print("Median = {}\n\n\n".format(median))

    else:
        index = len(content)//2
        median = (sorted_content[index] +  sorted_content[index-1]) / 2
        print("Median = {}\n\n\n".format(median))

def mode():
    freq = 0
    mode = []
    for element in content:
        counting = content.count(element)
        if counting > freq:
            freq = counting
            mode = []
            mode.append(element)
        elif counting == freq:
            if element not in mode:
                mode.append(element)
        else:
            continue
    print("Mode set: = {}\n\n\n".format(mode))

def variance():
    t = 0
    for element in content:
        t += float(element)
    mean = t / (len(content))
    var = 0
    for element in content:
        var += (float(element) - mean) ** 2
    var = var / (len(content)-1)
    print("Variance = {}\n\n\n".format(var))

def std_deviation():
    t = 0
    for element in content:
        t += float(element)
    mean = t / (len(content))
    var = 0
    for element in content:
        var += (float(element) - mean) ** 2
    var = var / (len(content)-1)
    std_dev = var**2
    print("Standard Deviation = {}\n\n\n".format(std_dev))


def frequency_table():
    table_list = []
    table_str= """
Frequency Table:

Data           |      Frequency
_______________________________
"""
    for element in content:
        if element not in table_list:
            table_list.append(element)
        else:
            continue
    table_list = [float(i) for i in table_list]
    table_list.sort()
    for element in table_list:
        table_str += "\n{:<15}|{:>15}".format(element, content.count(element))
    print(table_str + "\n\n\n\n")

def stem_leaf():
    print("""\n\n\n\n
Stem and Leaf Diagram:
__________________________________________________________
""")
    stems = []
    leafs = []
    for element in content:
        element = str(element).split(".")
        element = int(element[0])
        if element not in stems:
            stems.append(element)
    stems = sorted(stems)
    for element in content:
        element = str(element)
        element = element.split(".")
        leafs.append(element)
    leafs = sorted(leafs)
    for stem in stems:
        row = [stem]
        for leaf in leafs:
            if int(leaf[0]) == stem:
                row.append(leaf[1])
        stem = row[0]
        leaves = row[1::]
        sorted(leaves)
        star_leaves = []
        dot_leaves = []
        for element in leaves:
            if int(element) >= 5:
                star_leaves.append(element)
            else:
                dot_leaves.append(element)

        if len(dot_leaves) != 0:
            print("{}.|{}".format(stem, dot_leaves))
        if len(star_leaves) != 0:
            print("{}*|{}".format(stem, star_leaves))

mode()
median_calc()
quartile()
mean()
variance()
std_deviation()
frequency_table()
stem_leaf()
