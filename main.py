#! /usr/bin/env python
import sys
import argparse
import os
import subprocess
from familyScreener import familyScreener
from bitscore import bitscore
from getFasta import updateFasta


def parse_args(args):
    ###### Command Line Argument Parser
    parser = argparse.ArgumentParser(description="Check the help flag")
    parser.add_argument('fastafile', help='Path to the fasta file to run TErex on')
    parser.add_argument('dfamPath', help='Path to the Dfam database that would like to be used')
    parser.add_argument('outputPath', help='Path that you would like the outputted files to be outputted to')
    parser.add_argument('-families', help='Path to the text file with list of families that you want filtered. If no option is chosen, every family will be displayed. Format of the file should be a line of family names separated by commas. Example file is provided in TErex1.0/test/family_example')
    parser.add_argument('--bitscoreThreshold', help='Input the value of the SMALLEST bitscore you would want to obtain. i.e. if a value of 30 is chosen, every bitscore below 30 will be thrown out. If no value is chosen, our default method which chooses every bitscore >= mean - onestandard deviation', type=int)
    parser.add_argument('--evalueThreshold', help='Input the value of the SMALLEST evalue you would accept. i.e. if an evalue of 1e-30 is chosen, every e-value below 1e-30 will be thrown out (this is WAY too stringent). If no value is specified an evalue of 0.01 is chosen', type=float)
    parser.add_argument('--tester', help='Test that everything is working fine. The test method will be to run: python main.py ./Test/test.fa ./Test/DfamSubset.hmm ./Test', action='store_true')
    return parser.parse_args()


def main():

    if '--tester' in sys.argv:
        args_test = "python main.py ./Test/test.fa ./Test/DfamSubset.hmm ./Test"
        args = args_test.split()
        subprocess.call(args)
        sys.exit()

    args = parse_args(sys.argv[1:])

    #get fasta file to read
    fastafile = args.fastafile

    #get dfampath
    dfampath = args.dfamPath

    #check if the user wants to input the families they would like to look for 
    familyOption = False
    if args.families:
        famFile = args.families
        familyOption = True

    #check if user would like to put their own bitscoreThreshold or use our default
    bitscoreThresholdUsed = False
    if args.bitscoreThreshold:
        bst = args.bitscoreThreshold
        bitscoreThresholdUsed = True
    else:
        bst = None

    #check if user would like to put their own evalueThreshold or use our default
    evalueThresholdUsed = False
    if args.evalueThreshold:
        evt = args.evalueThreshold
    else:
        evt = 0.01

    #Create output file directory structures
    outputPath = os.path.join(args.outputPath, 'Output')
    try:
        os.makedirs(outputPath)
    except OSError:
        if not os.path.isdir(outputPath):
            raise

    fastaPath = os.path.join(outputPath, 'Fasta_File')
    try:
        os.makedirs(fastaPath)
    except OSError:
        if not os.path.isdir(fastaPath):
            raise

    internalFilePath = os.path.join(outputPath, 'Internal_Files')
    try:
        os.makedirs(internalFilePath)
    except OSError:
        if not os.path.isdir(internalFilePath):
            raise
    dfamRaw = os.path.join(internalFilePath, 'dfamRaw.out')

    #run dfamscan.pl w/ evalue threshold
    print ("Dfam running... (this may take a while)")
    args_str = "perl dfamscan.pl -fastafile %s -hmmfile %s -dfam_outfile %s -E %s" % (fastafile, dfampath, dfamRaw, evt)
    args = args_str.split()
    if subprocess.call(args) != 0:
        sys.exit(2)
    print ("Dfam finished!")

    #conduct family screen
    if familyOption:
        print ("Family Screen running...")
        dfamScreen1 = os.path.join(internalFilePath, "dfamScreened.out")
        familyScreener(famFile, dfamRaw, dfamScreen1)
        print ("Family Screen finished!")
    else:
        dfamScreen1 = dfamRaw

    #conduct bitscore Threshold screen
    print ("Bitscore Screen running...")
    dfamScreen2 = os.path.join(internalFilePath, "bitscoreScreened.out")
    bitscore(dfamScreen1, bst, dfamScreen2)
    print ("Bitscore Screen finished!")

    #output fasta file!
    print ("Creating final fasta file")
    finalFile = os.path.join(fastaPath, "filteredFasta.fa")
    updateFasta(dfamScreen2, fastafile, finalFile)
    print ("Files outputted in the following directory: %s" % outputPath)
    print ("Completed!")


    #<3 <3 <3
    print("")
    print("Thanks for using TErex!")
    terex = """\


               @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
               @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
               @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
               @@@@@@@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
               @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
               @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
               @@@@@@@@@@@@@@@@@@@@@@,@       @  @    *.   @* .  & @
               @@@@@@@@@@@@@@@@@@@@@@,   @@       @  @        @(.  @
               @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
               @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
               @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
               @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
               @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
               @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
               @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
               @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
               @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
               @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
               @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
               @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
               @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
               @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
               @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
               @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
               @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
               @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
                  @@@@@@@@         @@@@@@@@
                  @@@@@@@@         @@@@@@@@
                  @@@@@@@@         @@@@@@@@

"""
    print(terex)
    print ("TErex is brought to you by Jenny, Jigar, Lowan, and Arya. We love you <3")

if __name__ == '__main__':
    main()
