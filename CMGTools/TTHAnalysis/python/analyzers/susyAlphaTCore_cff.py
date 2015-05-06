from CMGTools.RootTools.RootTools import *
from CMGTools.TTHAnalysis.analyzers.susyCore_modules_cff import *

#All cuts chosen as ones for the signal region from the 2012 analysis

##------------------------------------------
## Redefine analyzer parameters
##------------------------------------------
# Generator parameters
#------------------------------

#turn off LHE info for now, as it slows everything down
genAna.makeLHEweights = False
susyScanAna.doLHE = False

# Muons
#------------------------------
# Choose medium point from https://indico.cern.ch/event/357213/contribution/2/material/slides/0.pdf
# other things in https://twiki.cern.ch/twiki/bin/view/CMS/SWGuideMuonId2015
lepAna.loose_muon_pt               = 10.
lepAna.loose_muon_eta              = 2.5
lepAna.loose_muon_id               = "POG_ID_Medium"
lepAna.loose_muon_dxy              = 0.2
lepAna.loose_muon_dz               = 0.5
lepAna.loose_muon_relIso           = 0.12
lepAna.mu_isoCorr                  = "deltaBeta"
lepAna.loose_muon_isoCut     = lambda muon : muon.miniRelIso < 0.2

# Electrons
#------------------------------
# Choose loose point from https://twiki.cern.ch/twiki/bin/viewauth/CMS/CutBasedElectronIdentificationRun2
#lepAna.loose_electron_id           = "POG_Cuts_ID_2012_Veto_full5x5" #should be loose
lepAna.loose_electron_id           = "POG_Cuts_ID_PHYS14_25ns_v1_Loose"
lepAna.loose_electron_pt           = 10
lepAna.loose_electron_eta          = 2.5
lepAna.loose_electron_dxy          = 0.02
lepAna.loose_electron_dz           = 0.173670
lepAna.loose_electron_relIso       = 0.12
lepAna.loose_electron_isoCut     = lambda electron : electron.miniRelIso < 0.1
lepAna.loose_electron_lostHits     = 1 
# ttHLepAna.inclusive_electron_lostHits = 999 # no cut
lepAna.ele_isoCorr                 = "deltaBeta"
lepAna.ele_tightId                 = "Cuts_2012"
lepAna.doMiniIsolation = True
miniIsolationPUCorr = 'deltaBeta' 

# Photons
#------------------------------
photonAna.ptMin                        = 25
photonAna.etaMax                       = 2.5
photonAna.gammaID                     = "POG_PHYS14_25ns_Tight"

# Taus 
#------------------------------
tauAna.etaMax         = 2.3
tauAna.dxyMax         = 99999.
tauAna.dzMax          = 99999.
tauAna.vetoLeptons    = False
tauAna.vetoLeptonsPOG = True


# Jets (for event variables do apply the jetID and not PUID yet)
#------------------------------
jetAna.jetEta          = 5.
jetAna.jetEtaCentral   = 3.
jetAna.jetPt           = 40.
jetAna.mcGT = "PHYS14_V4_MC" 
jetAna.alwaysCleanPhotons = True
jetAna.cleanGenJetsFromPhoton = True

# ttHJetMCAna.smearJets     = False

# Energy sums
#------------------------------

##------------------------------------------
##  ISOLATED TRACK
##------------------------------------------

# those are the cuts for the nonEMu
isoTrackAna.setOff=False
isoTrackAna.candidates      ='packedPFCandidates'
isoTrackAna.candidatesTypes ='std::vector<pat::PackedCandidate>'
isoTrackAna.ptMin           = 10 ### for pion 
isoTrackAna.ptMinEMU        = 10 ### for EMU
isoTrackAna.dzMax           = 0.05
isoTrackAna.isoDR           = 0.3
isoTrackAna.ptPartMin       = 0
isoTrackAna.dzPartMax       = 0.1
isoTrackAna.maxAbsIso       = 8
isoTrackAna.MaxIsoSum       = 0.1 ### unused
isoTrackAna.MaxIsoSumEMU    = 0.2 ### unused
isoTrackAna.doSecondVeto    = False



##------------------------------------------
##  ALPHAT VARIABLES
##------------------------------------------
from PhysicsTools.Heppy.analyzers.eventtopology.AlphaTAnalyzer import AlphaTAnalyzer
from CMGTools.TTHAnalysis.analyzers.ttHAlphaTControlAnalyzer import ttHAlphaTControlAnalyzer
# Tree Producer
ttHAlphaTAna = cfg.Analyzer(
            AlphaTAnalyzer, name='AlphaTAnalyzer'
            )

ttHAlphaTControlAna = cfg.Analyzer(
            ttHAlphaTControlAnalyzer, name='ttHAlphaTControlAnalyzer'
            )

##------------------------------------------ 
##  CONTROL VARIABLES
##------------------------------------------ 

from CMGTools.TTHAnalysis.analyzers.ttHMT2Control import ttHMT2Control

ttHMT2Control = cfg.Analyzer(
            ttHMT2Control, name = 'ttHMT2Control'
            )



##------------------------------------------
##  TOLOLOGIAL VARIABLES: MT, MT2
##------------------------------------------

from CMGTools.TTHAnalysis.analyzers.ttHTopoVarAnalyzer import ttHTopoVarAnalyzer

ttHTopoJetAna = cfg.Analyzer(
            ttHTopoVarAnalyzer, name = 'ttHTopoVarAnalyzer',
            doOnlyDefault = True
            )


from PhysicsTools.Heppy.analyzers.eventtopology.MT2Analyzer import MT2Analyzer

MT2Ana = cfg.Analyzer(
            MT2Analyzer, name = 'MT2Analyzer',
            doOnlyDefault = True
            )

#-------------------------------------------
# CUTS AND VETOS
#-------------------------------------------

#Start with the signal region default cut flow

metAna.doMetNoMu=True
metAna.doMetNoEle=True
metAna.doMetNoPhoton=True

#ESums
ttHJetMETSkim.jetPtCuts   = [100,100]
ttHJetMETSkim.htCut       = ('htJet40j', 200)
ttHJetMETSkim.mhtCut      = ('mhtJet40j', 0)
ttHJetMETSkim.nBJet       = ('CSVM', 0, "jet.pt() > 40")     # require at least 0 jets passing CSVM and pt > 50

from CMGTools.TTHAnalysis.analyzers.ttHObjectSkimmer import ttHObjectSkimmer
from CMGTools.TTHAnalysis.analyzers.ttHIsoTrackSkimmer import ttHIsoTrackSkimmer
#Photons
ttHPhotonSkim = cfg.Analyzer(
    ttHObjectSkimmer, name = 'ttHPhotonSkimmer',
    objects = 'selectedPhotons',
    minObjects = 0,
    maxObjects = 0,
    #idCut  = "object.relIso03 < 0.2" # can give a cut
    #ptCuts = [20,10],                # can give a set of pt cuts on the objects
    )

#Muons
ttHMuonSkim = cfg.Analyzer(
    ttHObjectSkimmer, name = 'ttHMuonSkimmer',
    objects = 'selectedMuons',
    minObjects = 0,
    maxObjects = 0,
    #idCut  = "object.relIso03 < 0.2" # can give a cut
    #ptCuts = [20,10],                # can give a set of pt cuts on the objects
    )

#Electrons
ttHElectronSkim = cfg.Analyzer(
    ttHObjectSkimmer, name = 'ttHElectronSkimmer',
    objects = 'selectedElectrons',
    minObjects = 0,
    maxObjects = 0,
    #idCut  = "object.relIso03 < 0.2" # can give a cut
    #ptCuts = [20,10],                # can give a set of pt cuts on the objects
    )

#Isolated tracks
ttHIsoTrackSkim = cfg.Analyzer(
    ttHIsoTrackSkimmer, name = 'ttHIsoTrackSkimmer',
    objects = 'selectedIsoTrack',
    minObjects = 0,
    maxObjects = 0,
    allowedMuon = 0,
    allowedElectron = 0,
    #idCut  = "object.relIso03 < 0.2" # can give a cut
    #ptCuts = [20,10],                # can give a set of pt cuts on the objects
    )

#AlphaT Specific cuts
from CMGTools.TTHAnalysis.analyzers.ttHAlphaTSkimmer import ttHAlphaTSkimmer
from CMGTools.TTHAnalysis.analyzers.ttHAlphaTControlSkimmer import ttHAlphaTControlSkimmer

ttHAlphaTSkim = cfg.Analyzer(
            ttHAlphaTSkimmer, name='ttHAlphaTSkimmer',
            forwardJetVeto = True,
            alphaTCuts = [(0.65, 200, 275),   #AlphaT cut in HT region
                          (0.60, 275, 325),   #(aT, HTlow, HThigh)
                          (0.55, 325, 99999)],#Any region not specified will be vetoed
            invertAlphaT = False, #Invert the alphaT requirement
            mhtDivMetCut = ('mhtJet40j','met',1.25), #MHT/MET cut
            htJet = 'htJet40j'
            )

ttHAlphaTControlSkim = cfg.Analyzer(
            ttHAlphaTControlSkimmer,name='ttHAlphaTControlSkimmer',
            mtwCut = (-99999,99999),
            mllCut = (-99999,99999),
            lepDeltaRCut = 0,
            photonDeltaRCut = 0,
            )

##------------------------------------------
##  EXTRA GEN STUFF
##------------------------------------------

# Gen Info Analyzer
from CMGTools.TTHAnalysis.analyzers.ttHGenBinningAnalyzer import ttHGenBinningAnalyzer
ttHGenBinAna = cfg.Analyzer(
    ttHGenBinningAnalyzer, name = 'ttHGenBinningAnalyzer'
    )

 
##------------------------------------------
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

#Insert the skimmers after their analysers in susyCoreSequence (for efficiency)
susyCoreSequence.insert(susyCoreSequence.index(ttHCoreEventAna)+1,ttHAlphaTAna)
susyCoreSequence.insert(susyCoreSequence.index(ttHAlphaTAna)+1,ttHAlphaTSkim)
susyCoreSequence.insert(susyCoreSequence.index(ttHCoreEventAna)+1,ttHJetMETSkim)
susyCoreSequence.insert(susyCoreSequence.index(photonAna)+1,ttHPhotonSkim)
susyCoreSequence.insert(susyCoreSequence.index(lepAna)+1,ttHMuonSkim)
susyCoreSequence.insert(susyCoreSequence.index(lepAna)+1,ttHElectronSkim)
susyCoreSequence.insert(susyCoreSequence.index(isoTrackAna)+1,ttHIsoTrackSkim)

sequence = cfg.Sequence(susyCoreSequence + [
                        ttHAlphaTControlAna,
                        ttHAlphaTControlSkim,
                        ttHGenBinAna,
			ttHMT2Control,
			MT2Ana,
			ttHTopoJetAna,
                        treeProducer,
                        ])

#Increase the logging level to give us full information
import logging
logging.basicConfig(level=logging.INFO)
