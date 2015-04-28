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


## Dataset at IC-tier-2

#### Background
QCD_HT_100To250 = kreator.makeMCComponentFromIC("QCD_HT_100To250", "/QCD_HT-100To250_13TeV-madgraph/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root")
QCD_HT_250To500 = kreator.makeMCComponentFromIC("QCD_HT_250To500", "/QCD_HT_250To500_13TeV-madgraph/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root")
QCD_HT_250To500_ext1 = kreator.makeMCComponentFromIC("QCD_HT_250To500_ext1", "/QCD_HT_250To500_13TeV-madgraph/Phys14DR-PU20bx25_PHYS14_25_V1_ext1-v2/MINIAODSIM", "CMS", ".*root")
QCD_HT_500To1000 = kreator.makeMCComponentFromIC("QCD_HT_500To1000", "/QCD_HT-500To1000_13TeV-madgraph/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root")
QCD_HT_500To1000_ext1 = kreator.makeMCComponentFromIC("QCD_HT_500To1000_ext1", "/QCD_HT-500To1000_13TeV-madgraph/Phys14DR-PU20bx25_PHYS14_25_V1_ext1-v1/MINIAODSIM", "CMS", ".*root")
QCD_HT_1000ToInf = kreator.makeMCComponentFromIC("QCD_HT_1000ToInf", "/QCD_HT_1000ToInf_13TeV-madgraph/Phys14DR-PU20bx25_PHYS14_25_V1_ext1-v1/MINIAODSIM", "CMS", ".*root")
QCD_HT_1000ToInf_ext1 = kreator.makeMCComponentFromIC("QCD_HT_1000ToInf_ext1", "/QCD_HT_1000ToInf_13TeV-madgraph/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root")


QCDHT = [
QCD_HT_100To250,
QCD_HT_250To500,
QCD_HT_500To1000,
QCD_HT_1000ToInf,
QCD_HT_250To500_ext1,
QCD_HT_500To1000_ext1,
QCD_HT_1000ToInf_ext1
]

WJetsToLNu = kreator.makeMCComponentFromIC("WJetsToLNu","/WJetsToLNu_13TeV-madgraph-pythia8-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root",20508.9)

WJetsToLNu_HT100to200 = kreator.makeMCComponentFromIC("WJetsToLNu_HT100to200", "/WJetsToLNu_HT-100to200_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root",1817.0*1.23)
WJetsToLNu_HT200to400 = kreator.makeMCComponentFromIC("WJetsToLNu_HT200to400", "/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root",471.6*1.23)
WJetsToLNu_HT400to600 = kreator.makeMCComponentFromIC("WJetsToLNu_HT400to600", "/WJetsToLNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root",55.61*1.23)
WJetsToLNu_HT600toInf = kreator.makeMCComponentFromIC("WJetsToLNu_HT600toInf", "/WJetsToLNu_HT-600toInf_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root",18.81*1.23)
WJetsToLNuHT = [
WJetsToLNu_HT100to200,
WJetsToLNu_HT200to400,
WJetsToLNu_HT400to600,
WJetsToLNu_HT600toInf,
]

DYJetsToLL_M50_HT100to200 = kreator.makeMCComponentFromIC("DYJetsToLL_M50_HT100to200", "/DYJetsToLL_M-50_HT-100to200_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root",194.3*1.27)
DYJetsToLL_M50_HT200to400 = kreator.makeMCComponentFromIC("DYJetsToLL_M50_HT200to400", "/DYJetsToLL_M-50_HT-200to400_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root",52.24*1.27)
DYJetsToLL_M50_HT400to600 = kreator.makeMCComponentFromIC("DYJetsToLL_M50_HT400to600", "/DYJetsToLL_M-50_HT-400to600_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root",6.546*1.27)
DYJetsToLL_M50_HT600toInf = kreator.makeMCComponentFromIC("DYJetsToLL_M50_HT600toInf", "/DYJetsToLL_M-50_HT-600toInf_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root",2.179*1.27)
DYJetsM50HT = [
DYJetsToLL_M50_HT100to200,
DYJetsToLL_M50_HT200to400,
DYJetsToLL_M50_HT400to600,
DYJetsToLL_M50_HT600toInf,
]

GJets_HT100to200 = kreator.makeMCComponentFromIC("GJets_HT100to200", "/GJets_HT-100to200_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root",1534)
GJets_HT200to400 = kreator.makeMCComponentFromIC("GJets_HT200to400", "/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root",489.9)
GJets_HT400to600 = kreator.makeMCComponentFromIC("GJets_HT400to600", "/GJets_HT-400to600_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root")
GJets_HT600toInf = kreator.makeMCComponentFromIC("GJets_HT600toInf", "/GJets_HT-600toInf_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root",20.87)
GJetsHT = [
GJets_HT100to200,
GJets_HT200to400,
GJets_HT400to600,
GJets_HT600toInf,
]

ZJetsToNuNu_HT100to200 = kreator.makeMCComponentFromIC("ZJetsToNuNu_HT100to200", "/ZJetsToNuNu_HT-100to200_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root",372.6*1.27)
ZJetsToNuNu_HT200to400 = kreator.makeMCComponentFromIC("ZJetsToNuNu_HT200to400", "/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root",100.8*1.27)
ZJetsToNuNu_HT400to600 = kreator.makeMCComponentFromIC("ZJetsToNuNu_HT400to600", "/ZJetsToNuNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v2/MINIAODSIM", "CMS", ".*root",11.99*1.27)
ZJetsToNuNu_HT600toInf = kreator.makeMCComponentFromIC("ZJetsToNuNu_HT600toInf", "/ZJetsToNuNu_HT-600toInf_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root",4.113*1.27)
ZJetsToNuNuHT = [
ZJetsToNuNu_HT100to200,
ZJetsToNuNu_HT200to400,
ZJetsToNuNu_HT400to600,
ZJetsToNuNu_HT600toInf,
]

# https://twiki.cern.ch/twiki/bin/viewauth/CMS/SingleTopSigma
TToLeptons_tch = kreator.makeMCComponentFromIC("TToLeptons_tch", "/TToLeptons_t-channel-CSA14_Tune4C_13TeV-aMCatNLO-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root", 136.05*0.108) 
TToLeptons_sch = kreator.makeMCComponentFromIC("TToLeptons_sch", "/TToLeptons_s-channel-CSA14_Tune4C_13TeV-aMCatNLO-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root", 7.20*0.108)
TBarToLeptons_tch = kreator.makeMCComponentFromIC("TBarToLeptons_tch", "/TBarToLeptons_t-channel_Tune4C_CSA14_13TeV-aMCatNLO-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root", 80.97*0.108)
TBarToLeptons_sch = kreator.makeMCComponentFromIC("TBarToLeptons_sch", "/TBarToLeptons_s-channel-CSA14_Tune4C_13TeV-aMCatNLO-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root",  4.16*0.108)
TBar_tWch = kreator.makeMCComponentFromIC("TBar_tWch", "/Tbar_tW-channel-DR_Tune4C_13TeV-CSA14-powheg-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root",35.6)
T_tWch = kreator.makeMCComponentFromIC("T_tWch", "/T_tW-channel-DR_Tune4C_13TeV-CSA14-powheg-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root",35.6)

SingleTop = [
    TToLeptons_tch, TToLeptons_sch, TBarToLeptons_tch, TBarToLeptons_sch, TBar_tWch, T_tWch
]

TTJets = kreator.makeMCComponentFromIC("TTJets", "/TTJets_MSDecaysCKM_central_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root",809.1)
TTWJets = kreator.makeMCComponentFromIC("TTWJets", "/TTWJets_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root",0.6647)
TTZJets = kreator.makeMCComponentFromIC("TTZJets", "/TTZJets_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root",0.8565)
TTH = kreator.makeMCComponentFromIC("TTH", "/TTbarH_M-125_13TeV_amcatnlo-pythia8-tauola/Phys14DR-PU20bx25_tsg_PHYS14_25_V1-v2/MINIAODSIM", "CMS", ".*root",0.5085)

## Susy Signal samples
SMS_T2tt_2J_mStop850_mLSP100 = kreator.makeMCComponentFromIC("SMS_T2tt_2J_mStop850_mLSP100", "/SMS-T2tt_2J_mStop-850_mLSP-100_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_tsg_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root",0.0189612)
SMS_T2tt_2J_mStop650_mLSP325 = kreator.makeMCComponentFromIC("SMS_T2tt_2J_mStop650_mLSP325", "/SMS-T2tt_2J_mStop-650_mLSP-325_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_tsg_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root",0.107045)
SMS_T2tt_2J_mStop500_mLSP325 = kreator.makeMCComponentFromIC("SMS_T2tt_2J_mStop500_mLSP325", "/SMS-T2tt_2J_mStop-500_mLSP-325_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_tsg_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root",0.51848)
SMS_T2tt_2J_mStop425_mLSP325 = kreator.makeMCComponentFromIC("SMS_T2tt_2J_mStop425_mLSP325", "/SMS-T2tt_2J_mStop-425_mLSP-325_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_tsg_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root",1.31169)
SMS_T2qq_2J_mStop600_mLSP550 = kreator.makeMCComponentFromIC("SMS_T2qq_2J_mStop600_mLSP550", "/SMS-T2qq_2J_mStop-600_mLSP-550_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_tsg_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root",1.76645)
SMS_T2qq_2J_mStop1200_mLSP100 = kreator.makeMCComponentFromIC("SMS_T2qq_2J_mStop1200_mLSP100", "/SMS-T2qq_2J_mStop-1200_mLSP-100_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_tsg_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root",0.0162846)
SMS_T2bb_2J_mStop900_mLSP100 = kreator.makeMCComponentFromIC("SMS_T2bb_2J_mStop900_mLSP100", "/SMS-T2bb_2J_mStop-900_mLSP-100_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_tsg_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root",0.0128895)
SMS_T2bb_2J_mStop600_mLSP580 = kreator.makeMCComponentFromIC("SMS_T2bb_2J_mStop600_mLSP580", "/SMS-T2bb_2J_mStop-600_mLSP-580_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_tsg_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root",0.174599)
SMS_T1tttt_2J_mGl1500_mLSP100 = kreator.makeMCComponentFromIC("SMS_T1tttt_2J_mGl1500_mLSP100", "/SMS-T1tttt_2J_mGl-1500_mLSP-100_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_tsg_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root",0.0141903)
SMS_T1tttt_2J_mGl1200_mLSP800 = kreator.makeMCComponentFromIC("SMS_T1tttt_2J_mGl1200_mLSP800", "/SMS-T1tttt_2J_mGl-1200_mLSP-800_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_tsg_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root",0.0856418)
SMS_T1qqqq_2J_mGl1400_mLSP100 = kreator.makeMCComponentFromIC("SMS_T1qqqq_2J_mGl1400_mLSP100", "/SMS-T1qqqq_2J_mGl-1400_mLSP-100_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_tsg_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root",0.0252977)
SMS_T1qqqq_2J_mGl1000_mLSP800 = kreator.makeMCComponentFromIC("SMS_T1qqqq_2J_mGl1000_mLSP800", "/SMS-T1qqqq_2J_mGl-1000_mLSP-800_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_tsg_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root",0.325388)
SMS_T1bbbb_2J_mGl1500_mLSP100 = kreator.makeMCComponentFromIC("SMS_T1bbbb_2J_mGl1500_mLSP100", "/SMS-T1bbbb_2J_mGl-1500_mLSP-100_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_tsg_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root",0.0141903)
SMS_T1bbbb_2J_mGl1000_mLSP900 = kreator.makeMCComponentFromIC("SMS_T1bbbb_2J_mGl1000_mLSP900", "/SMS-T1bbbb_2J_mGl-1000_mLSP-900_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_tsg_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root",0.325388)
SusySignalSamples = [
SMS_T2tt_2J_mStop850_mLSP100, 
SMS_T2tt_2J_mStop650_mLSP325, 
SMS_T2tt_2J_mStop500_mLSP325, 
SMS_T2tt_2J_mStop425_mLSP325, 
SMS_T2qq_2J_mStop600_mLSP550, 
SMS_T2qq_2J_mStop1200_mLSP100, 
SMS_T2bb_2J_mStop900_mLSP100, 
SMS_T2bb_2J_mStop600_mLSP580, 
SMS_T1tttt_2J_mGl1500_mLSP100, 
SMS_T1tttt_2J_mGl1200_mLSP800, 
SMS_T1qqqq_2J_mGl1400_mLSP100, 
SMS_T1qqqq_2J_mGl1000_mLSP800, 
SMS_T1bbbb_2J_mGl1500_mLSP100, 
SMS_T1bbbb_2J_mGl1000_mLSP900,
]

## DM Signal samples
DM_Monojet_M1000_V = kreator.makeMCComponentFromIC("DM_Monojet_M1000_V", "/DarkMatter_Monojet_M-1000_V_Tune4C_13TeV-madgraph/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root")
DM_Monojet_M100_V = kreator.makeMCComponentFromIC("DM_Monojet_M100_V", "/DarkMatter_Monojet_M-100_V_Tune4C_13TeV-madgraph/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root")
DM_Monojet_M10_V = kreator.makeMCComponentFromIC("DM_Monojet_M10_V", "/DarkMatter_Monojet_M-10_V_Tune4C_13TeV-madgraph/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root")
DM_Monojet_M10_AV = kreator.makeMCComponentFromIC("DM_Monojet_M10_AV", "/DarkMatter_Monojet_M-10_AV_Tune4C_13TeV-madgraph/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root")

DmSignalSamples = [
DM_Monojet_M1000_V, 
DM_Monojet_M100_V,
DM_Monojet_M10_V, 
DM_Monojet_M10_AV,
]

DM_TTDMDM_M1000 = kreator.makeMCComponentFromIC("DM_TTDMDM_M1000", "/TTDMDMJets_M1000GeV_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root")
DM_TTDMDM_M200 = kreator.makeMCComponentFromIC("DM_TTDMDM_M200", "/TTDMDMJets_M200GeV_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root")
DM_TTDMDM_M10 = kreator.makeMCComponentFromIC("DM_TTDMDM_M10", "/TTDMDMJets_M10GeV_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root")
DM_TTDMDM_M600 = kreator.makeMCComponentFromIC("DM_TTDMDM_M600", "/TTDMDMJets_M600GeV_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root")
DM_TTDMDM_M50 = kreator.makeMCComponentFromIC("DM_TTDMDM_M50", "/TTDMDMJets_M50GeV_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root")
DM_TTDMDM_M1 = kreator.makeMCComponentFromIC("DM_TTDMDM_M1", "/TTDMDMJets_M1GeV_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root")

DmSignalSamples2 = [
DM_TTDMDM_M1000,
DM_TTDMDM_M200, 
DM_TTDMDM_M10,
DM_TTDMDM_M600, 
DM_TTDMDM_M50,
DM_TTDMDM_M1 
]

Test = [
QCD_HT_100To250,
]

mcSamples = Test + QCDHT + WJetsToLNuHT + DYJetsM50HT + GJetsHT + ZJetsToNuNuHT + SingleTop + [TTJets] + [TTWJets] + [TTZJets] + [TTH] + SusySignalSamples + DmSignalSamples + DmSignalSamples2

for comp in mcSamples:
    comp.isMC = True
    comp.isData = False
    comp.splitFactor = 500 if comp.name in [ "TTJets" ] else 250
    comp.puFileMC=dataDir+"/puProfile_Summer12_53X.root"
    comp.puFileData=dataDir+"/puProfile_Data12.root"
    comp.efficiency = eff2012


