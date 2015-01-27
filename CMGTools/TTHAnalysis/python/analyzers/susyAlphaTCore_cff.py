from CMGTools.RootTools.RootTools import *
from CMGTools.TTHAnalysis.analyzers.susyCore_modules_cff import *

#All cuts chosen as ones for the signal region from the 2012 analysis

##------------------------------------------
## Redefine analyzer parameters
##------------------------------------------
# Muons
#------------------------------
lepAna.loose_muon_pt               = 10.,
lepAna.loose_muon_eta              = 2.5,
lepAna.loose_muon_id               = "POG_ID_Tight"
lepAna.loose_muon_dxy              = 0.2
lepAna.loose_muon_dz               = 0.5
lepAna.loose_muon_relIso           = 0.12

# Electrons
#------------------------------
lepAna.loose_electron_id           = "POG_Cuts_ID_2012_Veto_full5x5"
lepAna.loose_electron_pt           = 10
lepAna.loose_electron_eta          = 2.5
lepAna.loose_electron_dxy          = 0.02
lepAna.loose_electron_dz           = 0.2
lepAna.loose_electron_relIso       = 0.15
lepAna.loose_electron_lostHits     = 1 
# ttHLepAna.inclusive_electron_lostHits = 999 # no cut
lepAna.ele_isoCorr                 = "rhoArea"
lepAna.ele_tightId                 = "Cuts_2012"

# Photons
#------------------------------
photonAna.ptMin                        = 25
photonAna.etaMax                       = 2.5
photonAna.gammaID                     = "PhotonCutBasedIDTight"

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
jetAna.jetPt           = 40.
jetAna.recalibrateJets = "MC"
jetAna.jetLepDR        = 0.4
jetAna.smearJets       = False

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
from CMGTools.TTHAnalysis.analyzers.ttHAlphaTVarAnalyzer import ttHAlphaTVarAnalyzer
from CMGTools.TTHAnalysis.analyzers.ttHAlphaTControlAnalyzer import ttHAlphaTControlAnalyzer
# Tree Producer
ttHAlphaTAna = cfg.Analyzer(
            ttHAlphaTVarAnalyzer, name='ttHAlphaTVarAnalyzer'
            )

ttHAlphaTControlAna = cfg.Analyzer(
            ttHAlphaTControlAnalyzer, name='ttHAlphaTControlAnalyzer'
            )


#-------------------------------------------
# CUTS AND VETOS
#-------------------------------------------

#Start with the signal region default cut flow

metAna.doMetNoMu=True

#ESums
ttHJetMETSkim.jetPtCuts   = [100,100]
ttHJetMETSkim.htCut       = ('htJet40j', 200)
ttHJetMETSkim.mhtCut      = ('htJet40j', 0)
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


