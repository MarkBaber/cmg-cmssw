from CMGTools.RootTools.RootTools import *
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
#ttHLepAna.loose_muon_relIso           = 0.15

# Electrons
#------------------------------
lepAna.loose_electron_id           = "POG_Cuts_ID_2012_Veto"
lepAna.loose_electron_pt           = 10
lepAna.loose_electron_eta          = 2.5
lepAna.loose_electron_dxy          = 0.5
lepAna.loose_electron_dz           = 0.
# ttHLepAna.loose_electron_relIso       = 0.15
# ttHLepAna.loose_electron_lostHits     = 999 # no cut
# ttHLepAna.inclusive_electron_lostHits = 999 # no cut
# ttHLepAna.ele_isoCorr                 = "deltaBeta"
# ttHLepAna.ele_tightId                 = "Cuts_2012"

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

# ttHJetMCAna.smearJets     = False

# Energy sums
#------------------------------
# NOTE: Currently energy sums are calculated with 40 GeV jets (ttHCoreEventAnalyzer.py)
#       However, the input collection is cleanjets which have a 50 GeV cut so this is a labeling problem


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

susyCoreSequence.insert(susyCoreSequence.index(ttHCoreEventAna), 
                        ttHJetMETSkim)

#-------------------------------------------
# CUTS AND VETOS
#-------------------------------------------

#Start with the signal region default cut flow

metAna.doMetNoMu=True

#ESums
ttHJetMETSkim.htCut       = ('htJet50j', 0)
ttHJetMETSkim.mhtCut      = ('htJet40j', 0)
ttHJetMETSkim.nBJet       = ('CSVM', 0, "jet.pt() > 50")     # require at least 0 jets passing CSVM and pt > 50

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
            mhtDivMetCut = ('mhtJet50j','met',1.25), #MHT/MET cut
            )

ttHAlphaTControlSkim = cfg.Analyzer(
            ttHAlphaTControlSkimmer,name='ttHAlphaTControlSkimmer',
            mtwCut = (-99999,99999),
            mllCut = (-99999,99999),
            lepDeltaRCut = 0,
            photonDeltaRCut = 0,
            )



