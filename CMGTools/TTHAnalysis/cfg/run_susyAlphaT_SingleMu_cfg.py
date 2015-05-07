import PhysicsTools.HeppyCore.framework.config as cfg

#Load all analyzers with defaults for alphaT analysis
from CMGTools.TTHAnalysis.analyzers.susyAlphaTCore_cff import *
import sys
import os

# Configurables
puRegime = "PU20bx25" 
cutFlow = "Signal"
host = os.environ["HOSTNAME"]

if puRegime != "PU20bx25":
    sys.exit("Only PU20bx25 available for Phys14 don't have samples for anything else")

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

#-------- SAMPLES AND TRIGGERS -----------
#Import general PHYS14 samples and RA1-specific samples
#if 'hep.ph.ic.ac.uk' in host:
from CMGTools.TTHAnalysis.samples.samples_13TeV_AlphaT_PHYS14 import *
if 'hep.ph.ic.ac.uk' not in host:
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

selectedComponents = QCDHT_fixPhoton + WJetsToLNuHT + [TTJets] + SingleTop

#Get testing from command line
from PhysicsTools.HeppyCore.framework.heppy import getHeppyOption
test = getHeppyOption('test')
if test: print "Will run test scenario %r" % test

if test == "1" :
    selectedComponents = [TTJets]
    for comp in selectedComponents:
        comp.splitFactor = 1
        comp.files = comp.files[:1]

if test == "2" :
    selectedComponents = [DYJetsToLL_M50_HT400to600]
    for comp in selectedComponents:
        comp.splitFactor = 1
        #comp.files = comp.files[:1]



# the following is declared in case this cfg is used in input to the heppy.py script
from PhysicsTools.HeppyCore.framework.eventsfwlite import Events
config = cfg.Config( components = selectedComponents,
                     sequence = sequence,
                     services = [],  
                     events_class = Events)


