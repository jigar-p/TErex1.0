import re

#Variables
do = 2
tr = 3
qu = 4
ci = 5
nu = 9
dz = 10
ds = 14

def updateFasta( dfamOutFile, fastaFile, outputFile ) :
    #Read in file from dfam output
    dfam_out = read_dfamOutFile( dfamOutFile )
    fastafile = read_fastaFile( fastaFile )
    outFile = open(outputFile, 'w+')

    #Modify strings to arrays
    inputLines = re.split("\n",dfam_out)
    labels = inputLines[tr].split()

    for line in range(ci, len(inputLines)-1) :
        values = inputLines[line].split()
        outputContent = buildFastaString( fastafile, values )
        #Write to file
        outFile.write(outputContent)

    #Close outputFile
    outFile.close()

def read_dfamOutFile( dfamOutFile ) :
    f = open(dfamOutFile, "r")
    dfam = f.read()
    return dfam

def read_fastaFile( fastaFile ) :
    f2 = open(fastaFile, "r")

    #Little formatting
    f2.readline()
    fasta = f2.read()
    fasta = ''.join(re.split("\n",fasta))
    return fasta

def buildFastaString( fastafile, values ) :
    #Store values
    output = ""
    name = values[0]
    acc = values[1]
    bits = values[tr]
    e_val = values[qu]
    bias = values[ci]
    st = values[nu]
    en = values[dz]
    descrip = values[ds]
    length = int(en)-int(st)

    #Format string
    output = ">" + name + ";" + acc + ";" + bits + ";" + e_val + ";" + st + ";" + en + ";" + descrip + ";"

    #Forward strand
    if length > 0 :
        output += "+\n" + str(fastafile[int(st)-1:int(en)]) + "\n"
    else : # Reverse strand
        output += "-\n" + str(fastafile[int(en)-1:int(st)]) + "\n"
    return output
