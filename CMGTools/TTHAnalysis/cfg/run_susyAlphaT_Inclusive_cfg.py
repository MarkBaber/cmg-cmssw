import PhysicsTools.HeppyCore.framework.config as cfg
from PhysicsTools.Heppy.analyzers.gen.LHEAnalyzer import LHEAnalyzer

#Load all analyzers with defaults for alphaT analysis
from CMGTools.TTHAnalysis.analyzers.susyAlphaTCore_cff import *
import sys
import os

# LHE
lheAna = cfg.Analyzer(
    LHEAnalyzer, name = 'LHEAnalyzer'
)

#Cuts forInclusive (turn off all skimmers)
ttHIsoTrackSkim.minObjects  = 0
ttHIsoTrackSkim.maxObjects  = 999
ttHLepSkim.minObjects  = 0
ttHLepSkim.maxObjects  = 999
ttHElectronSkim.minObjects  = 0
ttHElectronSkim.maxObjects  = 999
ttHMuonSkim.minObjects  = 0
ttHMuonSkim.maxObjects  = 999
ttHPhotonSkim.minObjects  = 0
ttHPhotonSkim.maxObjects  = 999
ttHAlphaTSkim.alphaTCuts = [(-9999, 0,99999 )]   #Turn off AlphaT cut
ttHAlphaTSkim.mhtDivMetCut = ('mhtJet40j','metNoMu',999)
ttHAlphaTSkim.forwardJetVeto = False
ttHJetMETSkim.jetPtCuts   = []
ttHJetMETSkim.htCut       = ('htJet40j', 0)

# LHE
susyAlphaT_globalVariables.append(NTupleVariable("lheHT", lambda ev : ev.lheHT, help="LHE HT( q + g )"))

sequence.insert(sequence.index(treeProducer)-1,lheAna)

selectedComponents = []

#NEED to add WZ,WW,ZZ samples FIXME

if bunchSpacing == '25ns':
    selectedComponents = [TTJets, TTJets_LO, WJetsToLNu, DYJetsToLL_M50] + WJetsToLNuHT + QCDPt
else:
    sys.exit("Only for 25ns atm")

#Limit the files as inclusive
for comp in selectedComponents:
    comp.splitFactor = 2
    comp.files = comp.files[1:3]

if test == "1" :

    #Select samples and limit the files
    selectedComponents = [WJetsToLNu]
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


