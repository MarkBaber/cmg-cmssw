#!/usr/bin/env python
#Script to automatically correctly fill the folder name for pybatch
import sys
import os
import subprocess
import datetime
import optparse
import whereAmI

cmssw_base = os.environ.get('CMSSW_BASE')
if cmssw_base == None:
    sys.exit('Please cmsenv in a CMSSW release with CMG tools')

from CMGTools.TTHAnalysis.config.config_cfi import alphaTPSet as PSet

def parse_args():
    parser = optparse.OptionParser()
    parser.add_option('-o','--outDir',help = 'output dir of jobs')
    options,args = parser.parse_args()
    if not options.outDir:
	parser.error('Need output directory')
    return options

def main(outDir):
    
    #Find out if at CERN or imperial
    location = whereAmI.whereAmI()
    
    #Get the relevant variables from the config
    now = datetime.datetime.now()
    
    outFolder= str(now.year)+str(now.month)+str(now.day)+"_"+PSet.cutFlow+"_"+PSet.puRegime
    outDir = os.path.abspath(outDir)

    output = os.path.join(outDir,outFolder)

    #Get the right submission argument
    if location == 'CERN':
        submissionArgs = "bsub -q 8nh -J "+output+" < batchScript.sh"
    elif location == 'Imperial':
        submissionArgs = "qsub -q hepshort.q batchScript.sh"
    else:
        sys.exit("Don't know where I am, can't submit correctly")

    if PSet.test!=0:
        print 'test not 0 please change it to submit'
    else:
        #os.system("pybatch.py -o "+output+" "+cmssw_base+"/src/CMGTools/TTHAnalysis/cfg/run_susyAlphaT_cfg.py -b '"+submissionArgs+"'")
    
        #Write the git tag and commit into the version info
        with open(output+'/versionInfo.txt', 'w') as versionInfo:

            #Get the info from git
            versionInfo.write("Tag for production: \n")
            versionInfo.write(os.popen("cd "+cmssw_base+"/src/CMGTools && git describe --tags").read())
    
            versionInfo.write("\nExtra information: \n")
            versionInfo.write(os.popen("cd "+cmssw_base+"/src/CMGTools && git show --quiet").read())

            
if __name__ == '__main__':
    main(**vars(parse_args()))

