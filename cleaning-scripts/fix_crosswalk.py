"""Script to clearn and format crosswalk datafile."""
# call: python fix_healthcare.py [infile] [outfile]
# replaces blank and other missing values with "NA"
# creates an additional file with no dental plans, indicated by the prefix "qhp" (qualified health plan)
# recodes records in the qhp file with more intuitive names for categorical values
import os
import sys
import string
import tempfile

from formatFcns import *

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print '*' * 50
        print '* ERROR'
        print '* Usage: python fix_healthcare.py [infile] [outfile]'
        print '*' * 50
        sys.exit(1)

    _, infile, outfile = sys.argv
    fin = open(infile,'r')
    fout = open(outfile,'w')
    tmp = outfile.split('.')
    fout_f = open(tmp[0]+'_formatted.csv','w')   
    fout_fnod = open(tmp[0]+'_formatted_qhp.csv','w')
    lc = 0
    for line in fin:
        line = line.strip()
        if lc == 0:
            print >> fout,line
            print >> fout_f, line
            print >> fout_fnod, line
            lc = 1
            continue
        lc += 1
        if lc %10000 == 0: print line
        tmp = line.split(',')
        # make sure there are exactly 21 columns, in not break
        x = checkCols(tmp)
        tmp = checkRow(tmp)
        tstr = ','.join(tmp) 
        print >> fout,tstr
        tmp[1] = planType(tmp[1])
        #if lc %10000 == 0: print tmp
        tmp[4] = stateField(tmp[4])
        tmp[6] = adultChild(tmp[6])
        tmp[8] = wholeCtyCheck(tmp[8])
        tmp[9] = crosswalkLevel(tmp[9])
        tmp[10] = crosswalkReason(tmp[10])
        tmp[11] = planIDCheck(tmp[11])
        tmp[12] = issuerIDCheck(tmp[12])
        tmp[13] = stateField(tmp[13])
        tmp[15] = adultChild(tmp[15])
        tmp[16] = ageOffIDCheck(tmp[16])
        tmp[17] = ageoffIssuerIDCheck(tmp[17])
        tmp[18] = stateField(tmp[18])
        tmp[20] = adultChild(tmp[20])
        if lc %10000 == 0: print tmp
        tstr = ','.join(tmp)
        print >> fout_f,tstr
        # print out version with better variable names
        if tmp[1]=="health": print >> fout_fnod,tstr

        
