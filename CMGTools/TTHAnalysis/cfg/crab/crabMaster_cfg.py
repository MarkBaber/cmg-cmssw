import os
from optparse import OptionParser

#-----------------------------------------------------------------------------#
#------------------------------Configuration----------------------------------#
#-----------------------------------------------------------------------------#

#Choose the name of the folder crab makes
#production_label = 'testSplit'
production_label = 'alphaT'

#The directory to store the crab logs- can be quite big so put in
#work directory
log_directory = '/afs/cern.ch/work/a/aelwood/alphat/crabLogs'

#The storage site is set as T2_UK_London_IC by default
#to change it, please edit L28 of heppy_crab_config.py

#Choose the configs to run over
alphaTCfgs = [
        "../run_susyAlphaT_CrabTest_cfg.py",
        #"../run_susyAlphaT_Signal_cfg.py",
        # "../run_susyAlphaT_SingleMu_cfg.py",
        # "../run_susyAlphaT_DoubleMu_cfg.py",
        # "../run_susyAlphaT_SinglePhoton_cfg.py",
        # "../run_susyAlphaT_SingleEle_cfg.py",
        # "../run_susyAlphaT_DoubleEle_cfg.py"
        ]

#-----------------------------------------------------------------------------#
#-----------------------------------------------------------------------------#
#-----------------------------------------------------------------------------#

def parseArgs():

    parser = OptionParser()
    parser.add_option('--submit',action='store_true',dest='submit',default=False,
            help='Submit all alphaT crab jobs')
    parser.add_option('--status',action='store_true',dest='status',default=False,
            help='Check status of all alphaT crab jobs')
    parser.add_option('--resubmit',action='store_true',dest='resubmit',default=False,
            help='Resubmit all alphaT crab jobs')

    options,args = parser.parse_args()

    return options

if __name__ == '__main__':


    options = parseArgs()

    if options.submit:
        for cfg in alphaTCfgs:
            print "Running "+cfg
            os.system('ln -s -f '+cfg+' heppy_config.py')
            os.system('python launchall.py')

    elif options.status:
        logDir = log_directory+"/crab_"+production_label
        for dir in os.listdir(logDir):
            os.system('crab status '+logDir+'/'+dir)
            print '---------------------------------------------\n'

    elif options.resubmit:
        logDir = log_directory+"/crab_"+production_label
        for dir in os.listdir(logDir):
            os.system('crab resubmit '+logDir+'/'+dir)
            print '---------------------------------------------\n'

    else:
        print 'Please provide the option --submit, --status, --resubmit'

