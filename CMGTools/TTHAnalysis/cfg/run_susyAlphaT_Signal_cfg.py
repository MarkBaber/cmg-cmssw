import PhysicsTools.HeppyCore.framework.config as cfg

#Load all analyzers with defaults for alphaT analysis
from CMGTools.TTHAnalysis.analyzers.susyAlphaTCore_cff import *
import sys
import os

#Cuts
#ttHAlphaTSkim.alphaTCuts = [(0.5, 200,99999 )]   #Flatten AlphaT Cut
ttHAlphaTSkim.alphaTCuts = [(0.5,200,800),(0.0,800,99999)]
ttHJetMETSkim.jetPtCuts   = [100,40]                #Remove second jet cut for the asymmetric dijet bin


#NEED to add WZ,WW,ZZ samples FIXME

#THESE ARE THE OLD SELECTED COMPONENTS, FOR NOW FILL THEM IN AS THEY APPEAR IN python/samples/samples_13TeV_74X.py
#selectedComponents = QCDHT_fixPhoton + WJetsToLNuHT + [TTJets] + SingleTop + ZJetsToNuNuHT + SusySignalSamples #+DmSignalSamples

if bunchSpacing == '25ns':
    selectedComponents = [TTJets, TTJets_LO, WJetsToLNu] + WJetsToLNuHT + QCDPt
else:
    sys.exit("Only for 25ns atm")

#For testing one file from a dataset listed in samples/...
if test == "1" :

    selectedComponents = [TTJets]
    for comp in selectedComponents:
        comp.splitFactor = 1
        comp.files = comp.files[:1]

#Option just to use one file per sample
if test=="2":

    for comp in selectedComponents:
        comp.splitFactor = 1
        comp.files = comp.files[:1]

#For running on a local file
if test == "3" :

    comp = cfg.MCComponent(
            name = "DM_test",
            files =  [ 
            '/afs/cern.ch/work/p/penning/public/fastsim/miniAOD_A_mDM200_mPhi100_fast.root',
            # '/afs/cern.ch/work/p/penning/public/fastsim/miniAOD_A_mDM300_mPhi800_fast.root',
            # '/afs/cern.ch/work/p/penning/public/fastsim/miniAOD_A_mDM50_mPhi1100_fast.root',
            # '/afs/cern.ch/work/p/penning/public/fastsim/miniAOD_S_mDM100_mPhi200_fast.root',
            # '/afs/cern.ch/work/p/penning/public/fastsim/miniAOD_S_mDM300_mPhi800_fast.root',
            # '/afs/cern.ch/work/p/penning/public/fastsim/miniAOD_S_mDM50_mPhi900_fast.root',
            ],
            #files =  [ '/afs/cern.ch/work/a/aelwood/public/ntuples/TtbarMiniAOD.root'],
            xSection = 1,
        )

    selectedComponents = [comp]
    comp.splitFactor = 1

#For running on multiple local files
if test == "4" :

    selectedComponents = [
            cfg.MCComponent(
            name = "mDM200_mPhi100_A",
            files =  [ 
            '/afs/cern.ch/work/p/penning/public/fastsim/miniAOD_A_mDM200_mPhi100_fast.root',
            ],
            xSection = 3.4527877671218938 ,
            ),

            cfg.MCComponent(
            name = "mDM300_mPhi800_A",
            files =  [ 
            '/afs/cern.ch/work/p/penning/public/fastsim/miniAOD_A_mDM300_mPhi800_fast.root',
            ],
            xSection = 2.8572701088551558,
            ),
            
            cfg.MCComponent(
            name = "mDM50_mPhi1100_A",
            files =  [ 
            '/afs/cern.ch/work/p/penning/public/fastsim/miniAOD_A_mDM50_mPhi1100_fast.root',
            ],
            xSection = 3.7660291027678352,
            ),
            
            cfg.MCComponent(
            name = "mDM100_mPhi200_S",
            files =  [ 
            '/afs/cern.ch/work/p/penning/public/fastsim/miniAOD_S_mDM100_mPhi200_fast.root',
            ],
            xSection = 0.10175623329662978,
            ),

            cfg.MCComponent(
            name = "mDM300_mPhi800_S",
            files =  [ 
            '/afs/cern.ch/work/p/penning/public/fastsim/miniAOD_S_mDM300_mPhi800_fast.root',
            ],
            xSection = 0.0273193576555718284,
            ),
            
            cfg.MCComponent(
            name = "mDM50_mPhi900_S",
            files =  [ 
            '/afs/cern.ch/work/p/penning/public/fastsim/miniAOD_S_mDM50_mPhi900_fast.root',
            ],
            xSection = 6.0530406614865466,
            ),

            ]

    comp.splitFactor = 1

#Testing on data
if test == '5' :
    from CMGTools.TTHAnalysis.samples.samples_8TeV_AlphaT import *
    selectedComponents = [singleMu2012D]

    for comp in selectedComponents:
        comp.splitFactor = 1
        comp.files = comp.files[:1]


# the following is declared in case this cfg is used in input to the heppy.py script
from PhysicsTools.HeppyCore.framework.eventsfwlite import Events
config = cfg.Config( components = selectedComponents,
                     sequence = sequence,
                     services = [],  
                     events_class = Events)


