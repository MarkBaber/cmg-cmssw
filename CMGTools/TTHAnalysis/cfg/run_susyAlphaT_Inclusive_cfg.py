import PhysicsTools.HeppyCore.framework.config as cfg

#Load all analyzers with defaults for alphaT analysis
from CMGTools.TTHAnalysis.analyzers.susyAlphaTCore_cff import *
import sys
import os

# Configurables
puRegime = "PU20bx25" 
test = 1
host = os.environ["HOSTNAME"]

if puRegime != "PU20bx25":
    sys.exit("Only PU20bx25 available for Phys14 don't have samples for anything else")

#Cuts forInclusive 
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
ttHAlphaTSkim.alphaTCuts = [(0.0, 0,99999 )]   #Turn off AlphaT cut
ttHAlphaTSkim.mhtDivMetCut = ('mhtJet40j','metNoMu',999)
ttHAlphaTSkim.forwardJetVeto = False
ttHJetMETSkim.jetPtCuts   = [0]
ttHJetMETSkim.htCut       = ('htJet40j', 0)

# Gen Info Analyzer
ttHGenAna = cfg.Analyzer(
    'ttHGenLevelAnalyzer',
    filterHiggsDecays = [0, 15, 23, 24],
    verbose = False,
    PDFWeights = [ pdf for pdf,num in PDFWeights ]
    )

#Add this to the sequence
sequence.insert(sequence.index(ttHAlphaTControlSkim)+1,ttHGenAna)

#Add new variables to the tree
susyAlphaT_globalVariables.extend([ 
     NTupleVariable("genBin", lambda ev : ev.genBin, help="Generator level binning quantity"),
     NTupleVariable("genQScale", lambda ev : ev.genQScale, help="Generator level binning quantity, QScale")]
     )

#-------- SAMPLES AND TRIGGERS -----------
#Import general PHYS14 samples and RA1-specific samples
#if 'hep.ph.ic.ac.uk' in host:
from CMGTools.TTHAnalysis.samples.samples_13TeV_AlphaT_PHYS14 import *
if 'lxplus' in host:
    from CMGTools.TTHAnalysis.samples.samples_13TeV_PHYS14 import *


triggerFlagsAna.triggerBits = {
            'Bulk'     : triggers_RA1_Bulk,
            'Prompt'   : triggers_RA1_Prompt,
            'Parked'   : triggers_RA1_Parked,
            'SingleMu' : triggers_RA1_Single_Mu,
            'Photon'   : triggers_RA1_Photon,
            'Muon'     : triggers_RA1_Muon,
}

selectedComponents = []

#NEED to add WZ,WW,ZZ samples FIXME

selectedComponents = QCDHT + [TTJets] + WJetsToLNuHT + SingleTop + ZJetsToNuNuHT + GJetsHT + DYJetsM50HT

#Limit the files as inclusive
for comp in selectedComponents:
    comp.splitFactor = 2
    comp.files = comp.files[:1]

if test == 1 :

    #Select samples and limit the files
    selectedComponents = [DYJetsToLL_M50_HT600toInf]
    for comp in selectedComponents:
        comp.splitFactor = 1
        comp.files = comp.files[:1]



# the following is declared in case this cfg is used in input to the heppy.py script
from PhysicsTools.HeppyCore.framework.eventsfwlite import Events
config = cfg.Config( components = selectedComponents,
                     sequence = sequence,
                     services = [],  
                     events_class = Events)


