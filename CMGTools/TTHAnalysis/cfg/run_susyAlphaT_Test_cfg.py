import PhysicsTools.HeppyCore.framework.config as cfg

#Load all analyzers with defaults for alphaT analysis
from CMGTools.TTHAnalysis.analyzers.susyAlphaTCore_cff import *
import os

#Cuts
#ttHAlphaTSkim.alphaTCuts = [(0.5, 200,99999 )]   #Flatten AlphaT Cut
ttHAlphaTSkim.alphaTCuts = [(0.5,200,900),(0.0,900,99999)]
ttHJetMETSkim.jetPtCuts   = [100,40]                #Remove second jet cut for the asymmetric dijet bin

selectedComponents = []

#NEED to add WZ,WW,ZZ samples FIXME

selectedComponents = [TTJets]
for comp in selectedComponents:
    comp.splitFactor = 2
    comp.files = comp.files[:2]

preprocessor = None

if test == "1" :
    from PhysicsTools.Heppy.utils.cmsswPreprocessor import CmsswPreprocessor
    preprocessor = CmsswPreprocessor("miniAOD-prod_PAT.py")

    selectedComponents = [
            cfg.MCComponent(
            name = "ttbarTest",
            files =  [ 
            '/afs/cern.ch/work/a/aelwood/public/alphaT/cmgtools/testAod/ttJetsAodSim.root',
            ],
            ),
            ]
 
#Option just to use one file per sample
if test=="2":

    for comp in selectedComponents:
        comp.splitFactor = 1
        comp.files = comp.files[:1]  


# the following is declared in case this cfg is used in input to the heppy.py script
from PhysicsTools.HeppyCore.framework.eventsfwlite import Events
config = cfg.Config( components = selectedComponents,
                     sequence = sequence,
                     preprocessor = preprocessor,
                     services = [],  
                     events_class = Events)


