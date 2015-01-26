import CMGTools.RootTools.fwlite.Config as cfg
from CMGTools.TTHAnalysis.cfg.phys14Cuts_cfi import *
import os
##------------------------------------------
## Choose the type of cut flow and puRegime
## Signal or control sample
##------------------------------------------

alphaTPSet = cfg.CFG(
#puRegime = 'PU40bx50',
puRegime = 'PU20bx25',
cutFlow = 'SingleMu',
test =  0,
limitFiles = False,
host = os.environ['HOSTNAME'],
cuts = singleMuCut

)

