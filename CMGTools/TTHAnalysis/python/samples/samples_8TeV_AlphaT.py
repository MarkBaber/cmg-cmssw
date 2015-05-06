import PhysicsTools.HeppyCore.framework.config as cfg
import os

from CMGTools.TTHAnalysis.samples.ComponentCreator import ComponentCreator
kreator = ComponentCreator()

dataDir = os.environ['CMSSW_BASE']+"/src/CMGTools/TTHAnalysis/data"

from CMGTools.TTHAnalysis.setup.Efficiencies import *

# from samples_13TeV_PHYS14 import *

### ----> RA1 2012 triggers

triggers_RA1_Bulk = [
    "HLT_HT200_v*",
    "HLT_HT250_v*",
    "HLT_HT300_v*",
    "HLT_HT350_v*",
    "HLT_HT450_v*",
    "HLT_HT550_v*",
    "HLT_HT650_v*",
    "HLT_HT750_v*",
    ]
triggers_RA1_Parked = [
    "HLT_HT200_AlphaT0p57_v*",
    "HLT_HT300_AlphaT0p53_v*",
    "HLT_HT350_AlphaT0p52_v*",
    "HLT_HT400_AlphaT0p51_v*",
    ]
triggers_RA1_Prompt = [
    "HLT_HT250_AlphaT0p55_v*",
    "HLT_HT300_AlphaT0p53_v*",
    "HLT_HT350_AlphaT0p52_v*",
    "HLT_HT400_AlphaT0p51_v*",
    "HLT_HT350_AlphaT0p52_v*",
    ]
triggers_RA1_Single_Mu = ["HLT_IsoMu24_eta2p1_v*"]
triggers_RA1_Photon    = ["HLT_Photon150_v%d"%i for i in range(1,20)] + ["HLT_Photon160_v%d"%i for i in range(1,20)]
triggers_RA1_Muon      = ["HLT_IsoMu24_eta2p1_v%d"%i for i in range(1,20)]

#FIXME should find out which JSON and add it
json = None

singleMu2012D =  kreator.makeDataComponent("singleMu2012D","/SingleMu/CMSSW_7_4_0_pre9_ROOT6-GR_R_74_V8_1Apr_RelVal_sm2012D-v10/MINIAOD","CMS",".*root")

dataSamples = [
        singleMu2012D
        ]
#mcSamples = Test + QCDHT + WJetsToLNuHT + DYJetsM50HT + GJetsHT + ZJetsToNuNuHT + SingleTop + [TTJets] + [TTWJets] + [TTZJets] + [TTH] + SusySignalSamples + DmSignalSamples + DmSignalSamples2

for comp in dataSamples:
    comp.isMC = False
    comp.isData = True
    comp.splitFactor = 250
    comp.puFileMC=dataDir+"/puProfile_Summer12_53X.root"
    comp.puFileData=dataDir+"/puProfile_Data12.root"
    comp.efficiency = eff2012


