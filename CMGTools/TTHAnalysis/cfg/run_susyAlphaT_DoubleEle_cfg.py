import PhysicsTools.HeppyCore.framework.config as cfg

#Load all analyzers with defaults for alphaT analysis
from CMGTools.TTHAnalysis.analyzers.susyAlphaTCore_cff import *
import os

lepAna.loose_electron_id = "POG_Cuts_ID_PHYS14_25ns_v1_Tight"
ttHElectronSkim.idCut = "abs(object.eta()) < 2.1"
ttHElectronSkim.ptCuts = [30.,30.] 
ttHElectronSkim.minObjectsBeforeRequirements  = 2
ttHElectronSkim.maxObjectsBeforeRequirements  = 2
ttHElectronSkim.minObjects = 2
ttHElectronSkim.maxObjects = 2
ttHIsoTrackSkim.allowedElectron = 2
ttHAlphaTSkim.alphaTCuts = [(0.0, 200,99999 )]   #Turn off AlphaT cut
ttHAlphaTSkim.mhtDivMetCut = ('mhtJet40j','metNoEle',1.25)
ttHAlphaTControlSkim.maxLeps = 2
ttHAlphaTControlSkim.mllCut = (66.2,116.2)
ttHAlphaTControlSkim.lepDeltaRCut = 0.5
ttHJetMETSkim.jetPtCuts   = [100,40]                #Remove second jet cut for the asymmetric dijet bin

selectedComponents = []

#NEED to add WZ,WW,ZZ samples FIXME

if bunchSpacing == '25ns':
    selectedComponents = QCDPt + [DYJetsToLL_M50]
else:
    sys.exit("Only for 25ns atm")


if test == "1" :

    #Change any cuts
    ttHAlphaTSkim.mhtDivMetCut = ('mhtJet40j','metNoMu',999)

    #Select samples and limit the files
    selectedComponents = [DYJetsToLL_M50]
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
