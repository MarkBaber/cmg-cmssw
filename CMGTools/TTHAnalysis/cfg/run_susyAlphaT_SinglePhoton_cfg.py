import PhysicsTools.HeppyCore.framework.config as cfg

#Load all analyzers with defaults for alphaT analysis
from CMGTools.TTHAnalysis.analyzers.susyAlphaTCore_cff import *
import sys
import os

# Configurables
puRegime = "PU20bx25" 
cutFlow = "Signal"
test = 0
host = os.environ["HOSTNAME"]

if puRegime != "PU20bx25":
    sys.exit("Only PU20bx25 available for Phys14 don't have samples for anything else")

#Cuts
photonAna.ptMin = 165
photonAna.etaMax = 1.45
ttHPhotonSkim.minObjects  = 1
ttHPhotonSkim.maxObjects  = 1 
ttHAlphaTSkim.alphaTCuts = [(0.55, 375,99999 )]   
ttHAlphaTControlSkim.photonDeltaRCut = 1.0
ttHAlphaTSkim.mhtDivMetCut = ('mhtJet40j','met',9999) #turn off MHT/MET cut
 
##------------------------------------------
##  PRODUCER
##------------------------------------------
from CMGTools.TTHAnalysis.analyzers.treeProducerSusyAlphaT import * 
## Tree Producer
treeProducer = cfg.Analyzer(
     AutoFillTreeProducer, name='treeProducerSusyAlphaT',
     vectorTree = True,
     saveTLorentzVectors = False,  # can set to True to get also the TLorentzVectors, but trees will be bigger
     PDFWeights = PDFWeights,
     globalVariables = susyAlphaT_globalVariables,
     globalObjects = susyAlphaT_globalObjects,
     collections = susyAlphaT_collections,
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

selectedComponents = QCDHT + GJetsHT #GJets missing 400 - 600 


#-------- SEQUENCE

#Insert the skimmers after their analysers in susyCoreSequence (for efficiency)
susyCoreSequence.insert(susyCoreSequence.index(ttHCoreEventAna)+1,ttHJetMETSkim)
susyCoreSequence.insert(susyCoreSequence.index(photonAna)+1,ttHPhotonSkim)
susyCoreSequence.insert(susyCoreSequence.index(lepAna)+1,ttHMuonSkim)
susyCoreSequence.insert(susyCoreSequence.index(lepAna)+1,ttHElectronSkim)
susyCoreSequence.insert(susyCoreSequence.index(isoTrackAna)+1,ttHIsoTrackSkim)


sequence = cfg.Sequence(susyCoreSequence + [
                        ttHAlphaTAna,
                        ttHAlphaTControlAna,
                        ttHAlphaTSkim,
                        ttHAlphaTControlSkim,
                        treeProducer,
                        ])

if test == 1 :
    selectedComponents = [WJetsToLNu_HT600toInf]
    for comp in selectedComponents:
        comp.splitFactor = 1
        comp.files = comp.files[:1]



# the following is declared in case this cfg is used in input to the heppy.py script
from PhysicsTools.HeppyCore.framework.eventsfwlite import Events
config = cfg.Config( components = selectedComponents,
                     sequence = sequence,
                     services = [],  
                     events_class = Events)


