import PhysicsTools.HeppyCore.framework.config as cfg

#Load all analyzers with defaults for alphaT analysis
from CMGTools.TTHAnalysis.analyzers.susyAlphaTCore_cff import *
import os

ttHMuonSkim.idCut = "abs(object.eta()) < 2.1"
ttHMuonSkim.ptCuts = [30.] 
ttHMuonSkim.minObjectsBeforeRequirements  = 1
ttHMuonSkim.maxObjectsBeforeRequirements  = 1
ttHMuonSkim.minObjects  = 1
ttHMuonSkim.maxObjects  = 1
ttHIsoTrackSkim.allowedMuon  = 1 #
ttHAlphaTSkim.alphaTCuts = [(0.0, 200,99999 )]   #Turn off AlphaT cut 
ttHAlphaTSkim.mhtDivMetCut = ('mhtJet40j','metNoMu',1.25)
ttHAlphaTControlSkim.maxLeps = 1
ttHAlphaTControlSkim.mtwCut = (30,125)
ttHAlphaTControlSkim.lepDeltaRCut = 0.5
ttHJetMETSkim.jetPtCuts   = [100,40]                #Remove second jet cut for the asymmetric dijet bin


selectedComponents = []

#NEED to add WZ,WW,ZZ samples FIXME

#THESE ARE THE OLD SELECTED COMPONENTS, FOR NOW FILL THEM IN AS THEY APPEAR IN python/samples/samples_13TeV_74X.py
#selectedComponents = QCDHT_fixPhoton + WJetsToLNuHT + [TTJets] + SingleTop

if bunchSpacing == '25ns':
    selectedComponents = [TTJets, TTJets_LO, WJetsToLNu] + WJetsToLNuHT + QCDPt
else:
    sys.exit("Only for 25ns atm")

if test == "1" :
    selectedComponents = [TTJets]
    for comp in selectedComponents:
        comp.splitFactor = 1
        comp.files = comp.files[:1]

#Option just to use one file per sample
if test=="2":

    for comp in selectedComponents:
        comp.splitFactor = 1
        comp.files = comp.files[:1]

if test == "3" :
    selectedComponents = [DYJetsToLL_M50]
    for comp in selectedComponents:
        comp.splitFactor = 1
        #comp.files = comp.files[:1]



# the following is declared in case this cfg is used in input to the heppy.py script
from PhysicsTools.HeppyCore.framework.eventsfwlite import Events
config = cfg.Config( components = selectedComponents,
                     sequence = sequence,
                     services = [],  
                     events_class = Events)


