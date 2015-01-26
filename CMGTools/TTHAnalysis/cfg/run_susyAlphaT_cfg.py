import PhysicsTools.HeppyCore.framework.config as cfg
from CMGTools.RootTools.RootTools import *

#Load all analyzers
from CMGTools.TTHAnalysis.analyzers.susyCore_modules_cff import *

##------------------------------------------
## Redefine analyzer parameters
##------------------------------------------

# Muons
#------------------------------
lepAna.loose_muon_pt               = 10.,
lepAna.loose_muon_eta              = 2.5,
lepAna.loose_muon_dxy              = 0.5
lepAna.loose_muon_dz               = 1.0
#lepAna.loose_muon_relIso           = 0.15

# Electrons
#------------------------------
lepAna.loose_electron_id           = "POG_Cuts_ID_2012_Veto"
lepAna.loose_electron_pt           = 10
lepAna.loose_electron_eta          = 2.5
lepAna.loose_electron_dxy          = 0.5
lepAna.loose_electron_dz           = 0.
# lepAna.loose_electron_relIso       = 0.15
# lepAna.loose_electron_lostHits     = 999 # no cut
# lepAna.inclusive_electron_lostHits = 999 # no cut
# lepAna.ele_isoCorr                 = "deltaBeta"
# lepAna.ele_tightId                 = "Cuts_2012"

# Photons
#------------------------------
photonAna.ptMin                        = 25,
photonAna.epaMax                       = 2.5,

# Taus 
#------------------------------
tauAna.etaMax         = 2.3
tauAna.dxyMax         = 99999.
tauAna.dzMax          = 99999.
tauAna.vetoLeptons    = False
tauAna.vetoLeptonsPOG = True


# Jets (for event variables do apply the jetID and not PUID yet)
#------------------------------
jetAna.relaxJetId      = False
jetAna.doPuId          = False
jetAna.jetEta          = 5.
jetAna.jetEtaCentral   = 3.
jetAna.jetPt           = 50.
jetAna.recalibrateJets = False
jetAna.jetLepDR        = 0.4


# Energy sums
#------------------------------
# NOTE: Currently energy sums are calculated with 40 GeV jets (ttHCoreEventAnalyzer.py)
#       However, the input collection is cleanjets which have a 50 GeV cut so this is a labeling problem

metAna.doMetNoMu=True
metAna.doMetNoPhoton=True

# Jet-MET based Skim (generic, but requirements depend on the final state)
from CMGTools.TTHAnalysis.analyzers.ttHJetMETSkimmer import ttHJetMETSkimmer
ttHJetMETSkim = cfg.Analyzer(
   ttHJetMETSkimmer, name='ttHJetMETSkimmer',
   jets      = "cleanJets", # jet collection to use
   jetPtCuts = [],  # e.g. [60,40,30,20] to require at least four jets with pt > 60,40,30,20
   jetVetoPt =  0,  # if non-zero, veto additional jets with pt > veto beyond the ones in jetPtCuts
   metCut    =  0,  # MET cut
   htCut     = ('htJet40j', 0), # cut on HT defined with only jets and pt cut 40, at zero; i.e. no cut
                                # see ttHCoreEventAnalyzer for alternative definitions
   mhtCut    = ('mhtJet40', 0), # cut on MHT defined with all leptons, and jets with pt > 40.
   nBJet     = ('CSVv2IVFM', 0, "jet.pt() > 30"),     # require at least 0 jets passing CSV medium and pt > 30
   )

ttHJetMETSkim.htCut       = ('htJet50j', 0)
ttHJetMETSkim.mhtCut      = ('htJet40j', 0)
ttHJetMETSkim.nBJet       = ('CSVM', 0, "jet.pt() > 50")     # require at least 0 jets passing CSVM and pt > 50

##------------------------------------------
##  ISOLATED TRACK
##------------------------------------------

isoTrackAna.setOff=False

##------------------------------------------
##  ALPHAT VARIABLES
##------------------------------------------

from CMGTools.TTHAnalysis.analyzers.ttHAlphaTVarAnalyzer import ttHAlphaTVarAnalyzer
from CMGTools.TTHAnalysis.analyzers.ttHAlphaTControlAnalyzer import ttHAlphaTControlAnalyzer
# Tree Producer
ttHAlphaTAna = cfg.Analyzer(
            ttHAlphaTVarAnalyzer, name='ttHAlphaTVarAnalyzer'
            )

ttHAlphaTControlAna = cfg.Analyzer(
                        ttHAlphaTControlAnalyzer,name='ttHAlphaTControlAnalyzer'
                        )
##------------------------------------------
##  EXTRA GEN STUFF
##------------------------------------------

# Gen Info Analyzer
from CMGTools.TTHAnalysis.analyzers.ttHGenBinningAnalyzer import ttHGenBinningAnalyzer
ttHGenBinAna = cfg.Analyzer(
    ttHGenBinningAnalyzer, name = 'ttHGenBinningAnalyzer'
    )


#------------------------------------------
##  PRODUCER
##------------------------------------------
from CMGTools.TTHAnalysis.analyzers.treeProducerSusyAlphaT import * 
## Tree Producer
treeProducer = cfg.Analyzer(
     AutoFillTreeProducer, name='treeProducerSusyAlphaT',
     vectorTree = True,
     saveTLorentzVectors = False,  # can set to True to get also the TLorentzVectors, but trees will be bigger
     PDFWeights = PDFWeights,
     globalVariables = susyAlphaT_globalVariables,
     globalObjects = susyAlphaT_globalObjects,
     collections = susyAlphaT_collections,
)

#-------- SEQUENCE

sequence = cfg.Sequence(susyCoreSequence + [
                        ttHAlphaTAna,
                        ttHAlphaTControlAna,
                        ttHGenBinAna,
                        treeProducer,
                        ])


#-------- SAMPLES AND TRIGGERS -----------
from CMGTools.TTHAnalysis.samples.samples_13TeV_CSA14 import *

#-------- SAMPLES AND TRIGGERS -----------
#Import general PHYS14 samples and RA1-specific samples
#if 'hep.ph.ic.ac.uk' in host:
from CMGTools.TTHAnalysis.samples.samples_13TeV_AlphaT_PHYS14 import *
if 'lxplus' in host:
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

if cutFlow == 'Signal':
    selectedComponents = QCDHT + WJetsToLNuHT + [TTJets] + SingleTop + ZJetsToNuNuHT + SusySignalSamples #Zinv missing 400-600

elif cutFlow == 'SingleMu':
    selectedComponents = QCDHT + WJetsToLNuHT + [TTJets] 

elif cutFlow == 'DoubleMu':
    selectedComponents = QCDHT + DYJetsM50HT

elif cutFlow == 'SinglePhoton':
    selectedComponents = QCDHT + GJetsHT #GJets missing 400 - 600 

elif cutFlow == 'MultiJetEnriched':
    selectedComponents = QCDHT

elif cutFlow == 'Inclusive':
    selectedComponents = QCDHT + WJetsToLNuHT + [TTJets] + DYJetsM50HT + GJetsHT + SusySignalSamples

else:
    print 'Please choose correct cutFlow and PU regime'
    #selectedComponents.extend( mcSamples )



#-------- HOW TO RUN
test = 1

# Test a single component, using a single thread.
#--------------------------------------------------
if test==1:
    comp               = TTJets_PU20bx25
    #comp.files = ['/afs/cern.ch/work/p/pandolf/CMSSW_7_0_6_patch1_2/src/CMGTools/TTHAnalysis/cfg/pickevents.root']
    comp.files         = comp.files[:1]
    
    selectedComponents = [comp]
    comp.splitFactor   = 1
#--------------------------------------------------

# Test all components (1 thread per component).
#--------------------------------------------------
elif test==2:
    for comp in selectedComponents:
        comp.splitFactor = 1
        comp.files       = comp.files[:1]
#--------------------------------------------------

# Run on local files
#--------------------------------------------------
elif test==4:
    comp = TTJets_PU20bx25
#    comp.name = 'TTJets'
    #    comp.files = [ '/store/mc/Spring14miniaod/TT_Tune4C_13TeV-pythia8-tauola/MINIAODSIM/PU20bx25_POSTLS170_V5-v1/00000/063013AD-9907-E411-8135-0026189438BD.root' ]

    comp.files = [ '/afs/cern.ch/user/m/mbaber/WORK/public/CSA14Samples/TT_Tune4C_13TeV-pythia8_PU20bx25.root' ]

    selectedComponents = [comp]
    comp.splitFactor = 1
#--------------------------------------------------


#config = cfg.Config( components = selectedComponents,
#                     sequence = sequence )

#printComps(config.components, True)
        # the following is declared in case this cfg is used in input to the heppy.py script

#-------- SEQUENCE

#Insert the skimmers after their analysers in susyCoreSequence (for efficiency)
susyCoreSequence.insert(susyCoreSequence.index(ttHCoreEventAna)+1,ttHJetMETSkim)
susyCoreSequence.insert(susyCoreSequence.index(photonAna)+1,ttHPhotonSkim)
susyCoreSequence.insert(susyCoreSequence.index(lepAna)+1,ttHMuonSkim)
susyCoreSequence.insert(susyCoreSequence.index(lepAna)+1,ttHElectronSkim)
susyCoreSequence.insert(susyCoreSequence.index(isoTrackAna)+1,ttHIsoTrackSkim)


sequence = cfg.Sequence(susyCoreSequence + [
                        ttHAlphaTAna,
                        ttHAlphaTControlAna,
                        ttHAlphaTSkim,
                        ttHAlphaTControlSkim,
                        treeProducer,
                        ])

if alphaTPSet.limitFiles:
    for comp in selectedComponents:
        comp.splitFactor = 1
        comp.files = comp.files[:1]

if test == 1 :
    selectedComponents = testOption()


# the following is declared in case this cfg is used in input to the heppy.py script
from PhysicsTools.HeppyCore.framework.eventsfwlite import Events
config = cfg.Config( components = selectedComponents,
                     sequence = sequence,
                     services = [],  
                     events_class = Events)

