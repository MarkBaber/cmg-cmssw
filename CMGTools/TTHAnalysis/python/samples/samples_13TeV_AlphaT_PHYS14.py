import PhysicsTools.HeppyCore.framework.config as cfg
import os

from samples_13TeV_PHYS14 import *

################## PU20 bx25ns (default of phys14, so no postfix) ##############
#### Background samples

QCD = QCDHT
# HT:100To250 250To500 250To500 500To1000

WJetsToLNu = WJetsToLNuHT
# HT: 100to200 200to400 400to600 600toInf

DYJetsToLL = DYJetsM50HT
# HT: 100to200 200to400 400to600 600toInf

GJets = GJetsHT
# HT: 100to200 200to400 600toInf

ZJetsToNuNu = ZJetsToNuNuHT
# HT: 100to200 200to400 600toInf

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