import CMGTools.RootTools.fwlite.Config as cfg

HT2012AlphaTCut = [	(0.65, 200, 275),   #AlphaT cut in HT region
			(0.60, 275, 325),   #(aT, HTlow, HThigh)
			(0.55, 325, 99999)]#Any region not specified will be vetoed

looseAlphaTCut = [(0.51, 200, 99999)]


HT2015AlphaTCut = [	(0.65, 200, 250),   #AlphaT cut in HT region
			(0.60, 250, 300),   #(aT, HTlow, HThigh)
			(0.55, 300, 99999)]#Any region not specified will be vetoed
			

signalCut = cfg.CFG(
	ttHAlphaTSkim_alphaTCuts = looseAlphaTCut
)

singleMuCut = cfg.CFG(
    loose_muon_pt   = 30.,
    loose_muon_eta  = 2.1,
    ttHMuonSkim_minObjects  = 1,
    ttHMuonSkim_maxObjects  = 1,
    ttHIsoTrackSkim_allowedMuon  = 1, #
    ttHAlphaTSkim_alphaTCuts = [(0.0, 200,99999 )],   #Turn off AlphaT cut 
    # ttHAlphaTSkim_mhtDivMetCut = ('mhtJet50j','metNoMu',1.25),
    ttHAlphaTSkim_mhtDivMetCut = ('mhtJet40j','metNoMu',1.25),
    ttHAlphaTControlSkim_mtwCut = (30,125),
    ttHAlphaTControlSkim_lepDeltaRCut = 0.5,
)

doubleMuCut = cfg.CFG(
	lepAna_loose_muon_pt   = 30.,
    lepAna_loose_muon_eta  = 2.1,
    ttHMuonSkim_minObjects  = 2,
    ttHMuonSkim_maxObjects  = 2,
    ttHIsoTrackSkim_allowedMuon  = 2, #
    ttHAlphaTSkim_alphaTCuts = [(0.0, 200,99999 )],   #Turn off AlphaT cut
    # ttHAlphaTSkim_mhtDivMetCut = ('mhtJet50j','metNoMu',1.25),
    ttHAlphaTSkim_mhtDivMetCut = ('mhtJet40j','metNoMu',1.25),
    ttHAlphaTControlSkim_mllCut = (66.2,116.2),
    ttHAlphaTControlSkim_lepDeltaRCut = 0.5,
)

singlePhotonCut = cfg.CFG(
    photonAna_ptMin = 165,
    photonAna_etaMax = 1.45,
    ttHPhotonSkim_minObjects  = 1,
    ttHPhotonSkim_maxObjects  = 1 ,
    ttHAlphaTSkim_alphaTCuts = [(0.55, 375,99999 )],
    ttHAlphaTContolSkim_photonDeltaRCut = 1.0,
    ttHAlphaTSkim_mhtDivMetCut = ('mhtJet40j','met',9999), #turn off MHT/MET cut
    # ttHAlphaTSkim_mhtDivMetCut = ('mhtJet50j','met',9999), #turn off MHT/MET cut
)


singleEleCut = cfg.CFG(
    ttHElectronSkim_minObjects  = 1,
    ttHElectronSkim_maxObjects  = 1,
    ttHIsoTrackSkim_allowedElectron  = 1, #
)

doubleEleCut = cfg.CFG(
    ttHElectronSkim_minObjects  = 2,
    ttHElectronSkim_maxObjects  = 2,
    ttHIsoTrackSkim_allowedElectron  = 2, #
)

multiJetEnrichedCut = cfg.CFG(
	ttHAlphaTSkim_invertAlphaT = True,
)

inclusiveCut = cfg.CFG(
    ttHJetMETSkim_jetPtCuts   = [0], # require the lead two jets to be above 100GeV
    ttHJetMETSkim_htCut       = ('htJet40j', -1000),
    ttHJetMETSkim_mhtCut      = ('mhtJet40j', -1000),
    ttHElectronSkim_minObjects  = 0 ,
    ttHElectronSkim_maxObjects  = 9999,
    ttHMuonSkim_minObjects  = 0,
    ttHMuonSkim_maxObjects  = 9999,
    ttHPhotonSkim_minObjects  = 0,
    ttHPhotonSkim_maxObjects  = 9999, 
    ttHIsoTrackSkim_minObjects = 0,
    ttHIsoTrackSkim_maxObjects = 9999,
    ttHAlphaTSkim_alphaTCuts = [(0.0, -1000,99999 )],   #Turn off AlphaT cut
    ttHAlphaTSkim_mhtDivMetCut = ('mhtJet40j','met',9999), #turn off MHT/MET cut

)

testCut = cfg.CFG(
    ttHMuonSkim_maxObjects     = 99,
    ttHMuonSkim_minObjects     = 0,
    ttHElectronSkim_maxObjects     = 99,
    ttHElectronSkim_minObjects     = 0,
    ttHAlphaTSkim_invertAlphaT = True,
    ttHPhotonSkim_minPhotons  = 0,
    ttHPhotonSkim_maxPhotons  = 9999,
    ttHPhotonSkim_ptCuts = [25],
    ttHIsoTrackSkim_minObjects  = 0, # 
    ttHIsoTrackSkim_maxObjects  = 9999, #
)



