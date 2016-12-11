import numpy as np

# filters file using bitscore threshold
def bitscore(file, threshold, output):
    threshold = threshold
    sum = 0
    bitscoreList = [] # stores the bitscore from the file

    with open(file) as dfamfile:
        # skips the first 5 lines
        for i in range(5):
            next(dfamfile)
        # loops through file and adds all the bitscores to list
        for line in dfamfile:
            s1 = line.rstrip().split()
            bitscoreList.append(float(s1[3]))
    dfamfile.close()

    # if no threshold is provided, uses defualt
    if (threshold == None):
        threshold = defaultThreshold(bitscoreList)

    # reads each line and adds them into list inputFile
    dfamfile = open(file)
    inputFile = dfamfile.readlines()
    dfamfile.close()

    # creates the outputFile
    outputFile = open(output, 'w')

    # writes first 5 lines into outputFile
    for i in range(5):
        outputFile.write(inputFile[i])

    # checks if the bitscore is higher than threshold,
    # if so, it will be copied to the filtered outputFile
    k = 0
    for j in range(5,len(inputFile)):
        if (bitscoreList[k] >= threshold):
            outputFile.write(inputFile[j])
        k += 1
    outputFile.close()

# calculates the threshold of the bitscore if none provided
# filters out outliers
def defaultThreshold(list):
    q3 = np.percentile(list, 75)
    q1 = np.percentile(list, 25)
    iqr = q3 - q1

    threshold = q1 - (iqr * 1.5)
    return threshold
