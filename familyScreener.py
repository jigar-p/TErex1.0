#screen families!
def familyScreener(family, dfam, output):
    with open(output, 'w') as output:
        with open(family, 'r') as family:
            #loop through family file and pick out which families the user would like to screen
            for familyLines in family:
                filterFams = familyLines.rstrip().split(',')
                filterFams = [x.strip(' ') for x in filterFams]

            #run through dfam file and output selected fams to a new screened dfamfile
            with open(dfam, 'r') as dfam:
                for dfamlines in dfam:
                    if dfamlines.startswith('#'):
                        output.write(dfamlines)
                        continue
                    dfamlinessplit = dfamlines.rstrip().split()
                    famname = dfamlinessplit[0]
                    for fams in filterFams:
                        if fams in famname:
                            output.write(dfamlines)


def main():
    familyScreener("/home/akaul/Desktop/family", "/home/akaul/Desktop/updated/Output/Internal_Files/dfamRaw.out", "/home/akaul/Desktop/updated/Output/Internal_Files/dfamScreen.out")


if __name__ == "__main__":
    main()
