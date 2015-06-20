import PhysicsTools.HeppyCore.framework.config as cfg

#Load all analyzers with defaults for alphaT analysis
from CMGTools.TTHAnalysis.analyzers.susyAlphaTCore_cff import *
import os

#Cuts
ttHPhotonSkim.idCut = "abs(object.eta()) < 1.45"
ttHPhotonSkim.ptCuts = [165.]
ttHPhotonSkim.minObjectsBeforeRequirements  = 1
ttHPhotonSkim.maxObjectsBeforeRequirements  = 1
ttHPhotonSkim.minObjects  = 1
ttHPhotonSkim.maxObjects  = 1 
ttHAlphaTSkim.alphaTCuts = [(0., 200,99999 )] #turn off alphaT cut
ttHAlphaTControlSkim.maxPhotons = 1
ttHAlphaTControlSkim.photonDeltaRCut = 1.0
ttHAlphaTSkim.mhtDivMetCut = ('mhtJet40j','metNoPhoton',1.25) 
ttHJetMETSkim.jetPtCuts   = [100,40]                #Remove second jet cut for the asymmetric dijet bin

selectedComponents = []

#NEED to add WZ,WW,ZZ samples FIXME


#THESE ARE THE OLD SELECTED COMPONENTS, FOR NOW FILL THEM IN AS THEY APPEAR IN python/samples/samples_13TeV_74X.py
#selectedComponents = QCDHT_fixPhoton + GJets_fixPhoton

if bunchSpacing == '25ns':
    selectedComponents = QCDPt # +GJets
else:
    sys.exit("Only for 25ns atm")

if test == "1" :
    selectedComponents = [GJets_HT600toInf_fixPhoton]
    for comp in selectedComponents:
        comp.splitFactor = 1
        comp.files = comp.files[:1]

#Option just to use one file per sample
if test=="2":

    for comp in selectedComponents:
        comp.splitFactor = 1
        comp.files = comp.files[:1]


# the following is declared in case this cfg is used in input to the heppy.py script
from PhysicsTools.HeppyCore.framework.eventsfwlite import Events
config = cfg.Config( components = selectedComponents,
                     sequence = sequence,
                     services = [],  
                     events_class = Events)


