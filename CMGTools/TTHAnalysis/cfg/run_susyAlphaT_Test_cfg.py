import PhysicsTools.HeppyCore.framework.config as cfg

#Load all analyzers with defaults for alphaT analysis
from CMGTools.TTHAnalysis.analyzers.susyAlphaTCore_cff import *
import sys
import os

# Configurables
host = os.environ["HOSTNAME"]


#Cuts
#ttHAlphaTSkim.alphaTCuts = [(0.5, 200,99999 )]   #Flatten AlphaT Cut
ttHAlphaTSkim.alphaTCuts = [(0.5,200,900),(0.0,900,99999)]
ttHJetMETSkim.jetPtCuts   = [100,40]                #Remove second jet cut for the asymmetric dijet bin

#-------- SAMPLES AND TRIGGERS -----------
#Import general PHYS14 samples and RA1-specific samples
#if 'hep.ph.ic.ac.uk' in host:
from CMGTools.TTHAnalysis.samples.samples_13TeV_AlphaT_PHYS14 import *
if 'hep.ph.ic.ac.uk' not in host:
    from CMGTools.TTHAnalysis.samples.samples_13TeV_PHYS14 import *

# triggerFlagsAna.triggerBits = {
#             'Bulk'     : triggers_RA1_Bulk,
#             'Prompt'   : triggers_RA1_Prompt,
#             'Parked'   : triggers_RA1_Parked,
#             'SingleMu' : triggers_RA1_Single_Mu,
#             'Photon'   : triggers_RA1_Photon,
#             'Muon'     : triggers_RA1_Muon,
# }

selectedComponents = []

#NEED to add WZ,WW,ZZ samples FIXME

selectedComponents = [TTJets]
for comp in selectedComponents:
    comp.splitFactor = 2
    comp.files = comp.files[:2]

#Get testing from command line
from PhysicsTools.HeppyCore.framework.heppy import getHeppyOption
test = getHeppyOption('test')
if test: print "Will run test scenario %r" % test

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
   


# the following is declared in case this cfg is used in input to the heppy.py script
from PhysicsTools.HeppyCore.framework.eventsfwlite import Events
config = cfg.Config( components = selectedComponents,
                     sequence = sequence,
                     preprocessor = preprocessor,
                     services = [],  
                     events_class = Events)


