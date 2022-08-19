# ho11_3_KO.py
# Author: Khason Ong
# Last updated: April 14, 2022
# Purpose: To practice concepts from chapters 2 to 6 with real life data
# Program uses: Methods readline(), readlines() and the for loop.
#

# open file called "drug_data.txt"
experiment_file = open('drug_data.txt')
# read the first line of the file with readline()
header = experiment_file.readline()

# compute the average Molecular Weight of drugs in this data set
# That means we have to add up all the values in the molecular weight column
# and divide it by the number of values we added together

# initialize molecular weight to zero
MW = 0

# initialize count to zero
count = 0
# iterate through the file handle to get one item (line in file) at a time
MW_list = []
for line in experiment_file:
    # split line using the tab character "\t" as delimiter
    # don't forget about the invisible newline character at the end of the files!
    columns = line.rstrip().split('\t')
    # increment mw by the value obtained from the fourth column
    molecular_weight = columns[3]
    # increment count
    count = count + 1
    MW_list.append(float(molecular_weight))
# print(MW_list)

# compute the average molecular weight
average = sum(MW_list) / len(MW_list)
# print(average)

# the print average molecular weight for this data set
print("Average molecular weight of drugs is " + str(average))

# close experiment_file
experiment_file.close()
