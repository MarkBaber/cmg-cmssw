import PhysicsTools.HeppyCore.framework.config as cfg
import os

from samples_13TeV_PHYS14 import *

################## PU20 bx25ns (default of phys14, so no postfix) ##############
#### Background samples


QCD_HT_100To250 = kreator.makeMCComponent("QCD_HT_100To250", "/QCD_HT-100To250_13TeV-madgraph/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root")
QCD_HT_250To500 = kreator.makeMCComponent("QCD_HT_250To500", "/QCD_HT_250To500_13TeV-madgraph/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root")
QCD_HT_250To500_ext1 = kreator.makeMCComponent("QCD_HT_250To500_ext1", "/QCD_HT_250To500_13TeV-madgraph/Phys14DR-PU20bx25_PHYS14_25_V1_ext1-v2/MINIAODSIM", "CMS", ".*root")
QCD_HT_500To1000 = kreator.makeMCComponent("QCD_HT_500To1000", "/QCD_HT-500To1000_13TeV-madgraph/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root")
QCD_HT_500To1000_ext1 = kreator.makeMCComponent("QCD_HT_500To1000", "/QCD_HT-500To1000_13TeV-madgraph/Phys14DR-PU20bx25_PHYS14_25_V1_ext1-v1/MINIAODSIM", "CMS", ".*root")
QCD_HT_1000ToInf = kreator.makeMCComponent("QCD_HT_1000ToInf", "/QCD_HT_1000ToInf_13TeV-madgraph/Phys14DR-PU20bx25_PHYS14_25_V1_ext1-v1/MINIAODSIM", "CMS", ".*root")
QCD_HT_1000ToInf_ext1 = kreator.makeMCComponent("QCD_HT_1000ToInf", "/QCD_HT_1000ToInf_13TeV-madgraph/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root")
QCD = [
QCD_HT_100To250,
QCD_HT_250To500,
QCD_HT_500To1000,
QCD_HT_1000ToInf,
QCD_HT_250To500_ext1,
QCD_HT_500To1000_ext1,
QCD_HT_1000ToInf_ext1
]

# QCD = QCDHT
# HT:100To250 250To500 250To500 500To1000

WJetsToLNu = kreator.makeMCComponent("WJetsToLNu","/WJetsToLNu_13TeV-madgraph-pythia8-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root",20508.9)
WJetsToLNu_HT100to200 = kreator.makeMCComponent("WJetsToLNu_HT100to200", "/WJetsToLNu_HT-100to200_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root",1817.0*1.23)
WJetsToLNu_HT200to400 = kreator.makeMCComponent("WJetsToLNu_HT200to400", "/WJetsToLNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root",471.6*1.23)
WJetsToLNu_HT400to600 = kreator.makeMCComponent("WJetsToLNu_HT400to600", "/WJetsToLNu_HT-400to600_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root",55.61*1.23)
WJetsToLNu_HT600toInf = kreator.makeMCComponent("WJetsToLNu_HT600toInf", "/WJetsToLNu_HT-600toInf_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root",18.81*1.23)
WJetsToLNu = [
WJetsToLNu_HT100to200,
WJetsToLNu_HT200to400,
WJetsToLNu_HT400to600,
WJetsToLNu_HT600toInf,
]
# WJetsToLNu = WJetsToLNuHT
# HT: 100to200 200to400 400to600 600toInf

DYJetsToLL_M50_HT100to200 = kreator.makeMCComponent("DYJetsToLL_M50_HT100to200", "/DYJetsToLL_M-50_HT-100to200_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root",194.3*1.27)
DYJetsToLL_M50_HT200to400 = kreator.makeMCComponent("DYJetsToLL_M50_HT200to400", "/DYJetsToLL_M-50_HT-200to400_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root",52.24*1.27)
DYJetsToLL_M50_HT400to600 = kreator.makeMCComponent("DYJetsToLL_M50_HT400to600", "/DYJetsToLL_M-50_HT-400to600_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root",6.546*1.27)
DYJetsToLL_M50_HT600toInf = kreator.makeMCComponent("DYJetsToLL_M50_HT600toInf", "/DYJetsToLL_M-50_HT-600toInf_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root",2.179*1.27)
DYJetsToLL = DYJetsM50HT
# HT: 100to200 200to400 400to600 600toInf

GJets_HT100to200 = kreator.makeMCComponent("GJets_HT100to200", "/GJets_HT-100to200_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root",1534)
GJets_HT200to400 = kreator.makeMCComponent("GJets_HT200to400", "/GJets_HT-200to400_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root",489.9)
GJets_HT600toInf = kreator.makeMCComponent("GJets_HT600toInf", "/GJets_HT-600toInf_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root",20.87)
GJets = [
GJets_HT100to200,
GJets_HT200to400,
GJets_HT600toInf,
]
# GJets = GJetsHT
# HT: 100to200 200to400 600toInf

ZJetsToNuNu_HT100to200 = kreator.makeMCComponent("ZJetsToNuNu_HT100to200", "/ZJetsToNuNu_HT-100to200_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root",372.6*1.27)
ZJetsToNuNu_HT200to400 = kreator.makeMCComponent("ZJetsToNuNu_HT200to400", "/ZJetsToNuNu_HT-200to400_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root",100.8*1.27)
ZJetsToNuNu_HT600toInf = kreator.makeMCComponent("ZJetsToNuNu_HT600toInf", "/ZJetsToNuNu_HT-600toInf_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root",4.113*1.27)
ZJetsToNuNu = [
ZJetsToNuNu_HT100to200,
ZJetsToNuNu_HT200to400,
ZJetsToNuNu_HT600toInf,
]
# ZJetsToNuNu = [ZJetsToNuNuHT]
# HT: 100to200 200to400 600toInf

TTJets = kreator.makeMCComponent("TTJets", "/TTJets_MSDecaysCKM_central_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root",809.1)
TTbar = [TTJets]

mcSamples = QCD + WJetsToLNu + DYJetsToLL + GJets + ZJetsToNuNu + TTbar

#Define splitting
for comp in mcSamples:
    comp.isMC = True
    comp.isData = False
    comp.splitFactor = 250 #  if comp.name in [ "WJets", "DY3JetsM50", "DY4JetsM50","W1Jets","W2Jets","W3Jets","W4Jets","TTJetsHad" ] else 100
    comp.puFileMC=dataDir+"/puProfile_Summer12_53X.root"
    comp.puFileData=dataDir+"/puProfile_Data12.root"
    comp.efficiency = eff2012