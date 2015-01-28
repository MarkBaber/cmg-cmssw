import PhysicsTools.HeppyCore.framework.config as cfg

#Load all analyzers with defaults for alphaT analysis
from CMGTools.TTHAnalysis.analyzers.susyAlphaTCore_cff import *
import sys
import os

# Configurables
puRegime = "PU20bx25" 
test = 0
host = os.environ["HOSTNAME"]

if puRegime != "PU20bx25":
    sys.exit("Only PU20bx25 available for Phys14 don't have samples for anything else")

#Cuts for DoubleMu
lepAna.loose_muon_pt   = 30.
lepAna.loose_muon_eta  = 2.1
ttHMuonSkim.minObjects  = 2
ttHMuonSkim.maxObjects  = 2
ttHIsoTrackSkim.allowedMuon  = 2 #
ttHAlphaTSkim.alphaTCuts = [(0.0, 200,99999 )]   #Turn off AlphaT cut
ttHAlphaTSkim.mhtDivMetCut = ('mhtJet40j','metNoMu',1.25)
ttHAlphaTControlSkim.mllCut = (66.2,116.2)
ttHAlphaTControlSkim.lepDeltaRCut = 0.5


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

selectedComponents = QCDHT + DYJetsM50HT

if test == 1 :

    #Change any cuts
    ttHAlphaTSkim.mhtDivMetCut = ('mhtJet40j','metNoMu',999)

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


