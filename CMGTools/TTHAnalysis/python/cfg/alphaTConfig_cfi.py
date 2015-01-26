import CMGTools.RootTools.fwlite.Config as cfg
import os
##------------------------------------------
## Choose the type of cut flow and puRegime
## Signal or control sample
##------------------------------------------

alphaTPSet = cfg.CFG(
#puRegime = 'PU40bx50',
puRegime = 'PU20bx25',
#cutFlow = 'MultiJetEnriched',
#cutFlow = 'Signal',
cutFlow = 'SingleMu',
#cutFlow = 'DoubleMu',
#cutFlow = 'SinglePhoton',
#cutFlow = 'SingleEle',
#cutFlow = 'DoubleEle',
#cutFlow = 'Inclusive',
#cutFlow = 'Test',
test =  1, 
limitFiles = False,
host = os.environ['HOSTNAME'],
)

def testOption():

    from CMGTools.TTHAnalysis.samples.samples_13TeV_AlphaT_PHYS14 import *
    if 'lxplus' in os.environ['HOSTNAME']:
        from CMGTools.TTHAnalysis.samples.samples_13TeV_PHYS14 import *

    selectedComponents = [WJetsToLNu_HT600toInf]
    for comp in selectedComponents:
        comp.splitFactor = 1
        comp.files = comp.files[:1]

    return selectedComponents
