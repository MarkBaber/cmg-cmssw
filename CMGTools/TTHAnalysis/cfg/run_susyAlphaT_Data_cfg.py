import PhysicsTools.HeppyCore.framework.config as cfg
from PhysicsTools.Heppy.analyzers.gen.LHEAnalyzer import LHEAnalyzer

#Load all analyzers with defaults for alphaT analysis
from CMGTools.TTHAnalysis.analyzers.susyAlphaTCore_cff import *
import sys
import os

# LHE
lheAna = cfg.Analyzer(    LHEAnalyzer, name = 'LHEAnalyzer' )

#Cuts forInclusive (turn off all skimmers)
ttHIsoTrackSkim.minObjects  = 0
ttHIsoTrackSkim.maxObjects  = 999
ttHLepSkim.minObjects       = 0
ttHLepSkim.maxObjects       = 999
ttHElectronSkim.minObjects  = 0
ttHElectronSkim.maxObjects  = 999
ttHMuonSkim.minObjects      = 0
ttHMuonSkim.maxObjects      = 999
ttHPhotonSkim.minObjects    = 0
ttHPhotonSkim.maxObjects    = 999
ttHAlphaTSkim.alphaTCuts    = [(-9999, 0,99999 )]   #Turn off AlphaT cut
ttHAlphaTSkim.mhtDivMetCut  = ('mhtJet40j','metNoMu',999)
ttHAlphaTSkim.forwardJetVeto = False
ttHJetMETSkim.jetPtCuts     = []
ttHJetMETSkim.htCut         = ('htJet40j', 0)

# LHE
# susyAlphaT_globalVariables.append(NTupleVariable("lheHT", lambda ev : ev.lheHT, help="LHE HT( q + g )"))
# sequence.insert(sequence.index(treeProducer)-1,lheAna)

selectedComponents = []






# --------------------------------------------------------------------------------

dataDir = "$CMSSW_BASE/src/CMGTools/TTHAnalysis/data"
json    = dataDir+'/json/Cert_DCSONLY_Run2015B.json'


# Configure data JECs
# --------------------

GT_Express = 'GR_E_V49'
GT_Prompt  = 'GR_P_V56'

# Express stream
jetAna.dataGT = GT_Express

comp = cfg.DataComponent(
    name = "SingleMu",
    files =  [
            '/vols/cms04/RA1/Trigger/miniAOD/miniAOD-express_PAT_run251244.root',
            '/vols/cms04/RA1/Trigger/miniAOD/miniAOD-express_PAT_run251251.root',
            '/vols/cms04/RA1/Trigger/miniAOD/miniAOD-express_PAT_run251252.root',
        ],
    intLumi = 1, 
    #triggers = triggers, 
    json = json
    )

selectedComponents = [comp]
comp.splitFactor   = 1



#sequence.remove(jsonAna)

# --------------------------------------------------------------------------------




if test == "0" :
    for comp in selectedComponents:
        comp.splitFactor = 1
        comp.files = comp.files[:1]



# the following is declared in case this cfg is used in input to the heppy.py script
from PhysicsTools.HeppyCore.framework.eventsfwlite import Events
config = cfg.Config( components = selectedComponents,
                     sequence = sequence,
                     services = [],  
                     events_class = Events)


