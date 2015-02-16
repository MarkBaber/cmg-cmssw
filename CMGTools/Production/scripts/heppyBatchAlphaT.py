#!/usr/bin/env python
#Script to automatically correctly fill the folder name for pybatch
import sys
import os
import subprocess
import time
import optparse
import whereAmI

cmssw_base = os.environ.get('CMSSW_BASE')
if cmssw_base == None:
    sys.exit('Please cmsenv in a CMSSW release with CMG tools')

def cutFlow_callback(option, opt, value, parser):
      setattr(parser.values, option.dest, value.split(','))

def parse_args():
    parser = optparse.OptionParser()
    parser.add_option('-o','--outDir',help = 'output dir of jobs')
    parser.add_option('-i','--cfg', type ='string',action='callback',callback=cutFlow_callback,
            help = 'Custom cfg file to be run. For multiple choices separate by spaces')
    parser.add_option('-c','--cutFlow', type ='string',action='callback',callback=cutFlow_callback,
            help = 'Standard cfg file to be run (for latest cut flows use e g --cutFlow SingleMu Signal ). For multiple choices separate by spaces')
    parser.add_option('-t','--tag',help = 'additional output to folder name',default = '')
    options,args = parser.parse_args()
    if not options.outDir:
        parser.error('Need output directory')
    if options.cfg and options.cutFlow:
        parser.error('Please choose custom cfg file (--cfg run_......py) or standard cut flow (e.g. --cutFlow SingleMu), not both')
    if not options.cfg and not options.cutFlow:
        parser.error('Please choose some form of input')
    return options

def main(outDir,cfg,cutFlow, tag):
    
    #Find out if at CERN or imperial
    location = whereAmI.whereAmI()
    
    #Get the relevant variables from the config
    now = time.strftime("%Y%m%d")

    outFolders = []
    if cfg:
        for name in cfg:
            outFolders.append( now+"_"+name.replace('/','_').replace('.py','')+tag )
    elif cutFlow:
        for name in cutFlow:
            outFolders.append( now+"_"+name+tag )

    outDir = os.path.abspath(outDir)

    outputs = []
    
    for outFolder in outFolders:
        outputs.append(os.path.join(outDir,outFolder))

   
    if cfg:
        for output,name in zip(outputs,cfg):

            #Get the right submission argument
            if location == 'CERN':
                submissionArgs = "bsub -u /dev/null -q 8nh -J "+output+" < batchScript.sh"
            elif location == 'Imperial':
                submissionArgs = "qsub -q hepshort.q batchScript.sh -o "+output+"/ -e "+output+"/"
            else:
                sys.exit("Don't know where I am, can't submit correctly")

            os.system("heppy_batch.py -o "+output+" "+ name +" -b '"+submissionArgs+"'")

    elif cutFlow:
        for output,name in zip(outputs,cutFlow):

            #Get the right submission argument
            if location == 'CERN':
                submissionArgs = "bsub -u /dev/null -q 8nh -J "+output+" < batchScript.sh"
            elif location == 'Imperial':
                submissionArgs = "qsub -q hepshort.q < batchScript.sh -o "+output+"/ -e "+output+"/"

            else:
                sys.exit("Don't know where I am, can't submit correctly")


            os.system("heppy_batch.py -o "+output+" "+cmssw_base+"/src/CMGTools/TTHAnalysis/cfg/run_susyAlphaT_"+name+"_cfg.py -b '"+submissionArgs+"'")

    #Write the git tag and commit into the version info
    for output in outputs:

        with open(output+'/versionInfo.txt', 'w') as versionInfo:
            #Get the info from git
            versionInfo.write("Tag for production: \n")
            versionInfo.write(os.popen("cd "+cmssw_base+"/src/CMGTools && git describe --tags").read())

            versionInfo.write("\nExtra information: \n")
            versionInfo.write(os.popen("cd "+cmssw_base+"/src/CMGTools && git show --quiet").read())

            
if __name__ == '__main__':
    main(**vars(parse_args()))

