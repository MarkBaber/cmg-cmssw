import PhysicsTools.HeppyCore.framework.config as cfg
from PhysicsTools.Heppy.analyzers.gen.LHEAnalyzer import LHEAnalyzer

#Load all analyzers with defaults for alphaT analysis
from CMGTools.TTHAnalysis.analyzers.susyAlphaTCore_cff import *
import sys
import os

# Configurables
puRegime = "PU20bx25" 
host = os.environ["HOSTNAME"]

if puRegime != "PU20bx25":
    sys.exit("Only PU20bx25 available for Phys14 don't have samples for anything else")

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
ttHJetMETSkim.jetPtCuts   = [0]
ttHJetMETSkim.htCut       = ('htJet40j', 0)


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


# LHE
susyAlphaT_globalVariables.append(NTupleVariable("lheHT", lambda ev : ev.lheHT, help="LHE HT( q + g )"))

sequence.insert(sequence.index(treeProducer)-1,lheAna)

selectedComponents = []

#NEED to add WZ,WW,ZZ samples FIXME

selectedComponents = QCDHT + [TTJets] + WJetsToLNuHT + SingleTop + ZJetsToNuNuHT + GJetsHT + DYJetsM50HT

#Limit the files as inclusive
for comp in selectedComponents:
    comp.splitFactor = 2
    comp.files = comp.files[:1]

#Get testing from command line
from PhysicsTools.HeppyCore.framework.heppy import getHeppyOption
test = getHeppyOption('test')
if test: print "Will run test scenario %r" % test

if test == "1" :

    #Select samples and limit the files
    selectedComponents = [GJets_HT600toInf]
    for comp in selectedComponents:
        comp.splitFactor = 1
        comp.files = comp.files[:1]



# the following is declared in case this cfg is used in input to the heppy.py script
from PhysicsTools.HeppyCore.framework.eventsfwlite import Events
config = cfg.Config( components = selectedComponents,
                     sequence = sequence,
                     services = [],  
                     events_class = Events)


