from CMGTools.TTHAnalysis.analyzers.treeProducerSusyCore import *
from CMGTools.TTHAnalysis.analyzers.ntupleTypes import *

susyAlphaT_globalVariables = susyCore_globalVariables + [
    #NTupleVariable("crossSection", lambda ev : ev.crossSection, help="process cross section in pb"),

    # Gen quantities
    ##----------------------------------------
    NTupleVariable("genBin", lambda ev : ev.genBin, help="Generator level binning quantity"),
    NTupleVariable("genQScale", lambda ev : ev.genQScale, help="Generator level binning quantity, QScale"),

    # Energy sums (RECO)
    ##----------------------------------------
    NTupleVariable("ht40",           lambda ev : ev.htJet40j,        help="H_{T} computed from only jets (with |eta|<3, pt > 40 GeV)"),
    NTupleVariable("deltaPhiMin",    lambda ev : ev.deltaPhiMin_had, help="minimal deltaPhi between the MET and the four leading jets with pt>40 and eta<2.4"),
    #NTupleVariable("diffMetMht",    lambda ev : ev.diffMetMht_had,  help="abs( vec(mht) - vec(met) )"),
    NTupleVariable("mht40_pt",       lambda ev : ev.mhtJet40j,       help="H_{T}^{miss} computed from only jets (with |eta|<3.0, pt > 40 GeV)"),
    NTupleVariable("mht40_phi",      lambda ev : ev.mhtPhiJet40j,    help="H_{T}^{miss} #phi computed from only jets (with |eta|<3.0, pt > 40 GeV)"),
    NTupleVariable("minDeltaHT",     lambda ev : ev.minDeltaHT,      help=" #Delta H_{T} between two pseudo jets"),


    # Energy sums (GEN)
    ##----------------------------------------
    NTupleVariable("genHt40",        lambda ev : ev.htGenJet40j,     help="H_{T} computed from only gen jets (with |eta|<3, pt > 40 GeV)"),
    NTupleVariable("genMht40_pt",    lambda ev : ev.mhtGenJet40j,    help="H_{T}^{miss} computed from only gen jets (with |eta|<3.0, pt > 40 GeV)"),
    NTupleVariable("genMht40_phi",   lambda ev : ev.mhtPhiGenJet40j, help="H_{T}^{miss} #phi computed from only gen jets (with |eta|<3.0, pt > 40 GeV)"),
    NTupleVariable("genMinDeltaHT" , lambda ev : ev.genMinDeltaHT,   help=" #Delta H_{T} between two pseudo genjets"),


    ##--------------------------------------------------

    # Physics object multplicities
    ##----------------------------------------

    NTupleVariable("nJet40Eta2p4",  lambda ev: sum([(j.pt() > 40 and abs(j.eta()) < 2.4) for j in ev.cleanJets]), int, help="Number of jets with pt > 40, |eta|<2.4"),
    NTupleVariable("nJet100",       lambda ev: sum([j.pt() > 100 for j in ev.cleanJets]), int, help="Number of jets with pt > 100, |eta|<3.0"),
    NTupleVariable("nJet100Eta2p4", lambda ev: sum([(j.pt() > 100 and abs(j.eta()) < 2.4) for j in ev.cleanJets]), int, help="Number of jets with pt > 100, |eta|<2.4"),
    NTupleVariable("nJet100a",      lambda ev: sum([j.pt() > 100 for j in ev.cleanJetsAll]), int, help="Number of jets with pt > 100, |eta|<5.0"),
    NTupleVariable("nMuons10",      lambda ev: sum([l.pt() > 10 and abs(l.pdgId()) == 13 for l in ev.selectedLeptons]), int, help="Number of muons with at least pt > 10"),
    NTupleVariable("nElectrons10",  lambda ev: sum([l.pt() > 10 and abs(l.pdgId()) == 11 for l in ev.selectedLeptons]), int, help="Number of electrons with at least pt > 10"),
    NTupleVariable("nTaus20",       lambda ev: sum([l.pt() > 20 for l in ev.selectedTaus]), int, help="Number of taus with pt > 20"),
    NTupleVariable("nGammas25",     lambda ev: sum([l.pt() > 25 for l in ev.selectedPhotons]), int, help="Number of photons with at least pt > 25"),
    NTupleVariable("nBJet40",       lambda ev: sum([j.btagWP("CSVv2IVFM") for j in ev.cleanJets if j.pt() > 40]), int, help="Number of jets with pt > 40 passing CSV medium"),
    NTupleVariable("nBJet50",       lambda ev: sum([j.btagWP("CSVv2IVFM") for j in ev.cleanJets if j.pt() > 50]), int, help="Number of jets with pt > 50 passing CSV medium"),
    NTupleVariable("nBJet40Eta2p4", lambda ev: sum([j.btagWP("CSVv2IVFM") for j in ev.cleanJets if j.pt() > 40 and abs(j.eta()) < 2.4]), int, help="Number of jets with pt > 40 passing CSV medium"),
    NTupleVariable("nBJet50Eta2p4", lambda ev: sum([j.btagWP("CSVv2IVFM") for j in ev.cleanJets if j.pt() > 50 and abs(j.eta()) < 2.4]), int, help="Number of jets with pt > 50 passing CSV medium"),

    # AlphaT variables
    ##----------------------------------------

    NTupleVariable("alphaT",        lambda ev: ev.alphaT,    help="AlphaT computed using jets with pt > 40, |eta|<3"),
    NTupleVariable("genAlphaT",     lambda ev: ev.genAlphaT, help="AlphaT computed using gen jets with pt > 40, |eta|<3"),

    NTupleVariable("biasedDPhi",    lambda ev: ev.biasedDPhi,help="biased delta phi"),


    # MT2
    ##--------------------------------------------------
    NTupleVariable("mt2_had",      lambda ev: ev.mt2_had,      float, help="mt2(j1,j2,met) with jets "),
    NTupleVariable("mt2ViaKt_had", lambda ev: ev.mt2ViaKt_had, float, help="mt2(j1,j2,met) with jets with KT pseudo jets"),
    NTupleVariable("mt2_bb",       lambda ev: ev.mt2bb,        float, help="mt2(b1,b2,met) with jets "),
    NTupleVariable("mt2_gen",      lambda ev: ev.mt2_gen,      float, help="mt2(j1,j2,met) with jets at genInfo"),
    NTupleVariable("mt2",          lambda ev: ev.mt2,          float, help="mt2(j1,j2,met) with jets and leptons"),
    NTupleVariable("gamma_mt2",    lambda ev: ev.gamma_mt2,    float, help="mt2(j1,j2,met) with photons added to met"),
    NTupleVariable("zll_mt2",      lambda ev: ev.zll_mt2,      float, help="mt2(j1,j2,met) with zll added to met, only hadrons"),


    # control sample variables
    ##--------------------------------------------------
    NTupleVariable("mtw",         lambda ev: ev.mtw,         help="mt(l,met)"),
    NTupleVariable("mtwTau",      lambda ev: ev.mtwTau,      help="mt(tau,met)"),
    NTupleVariable("mtwIsoTrack", lambda ev: ev.mtwIsoTrack, help="mt(isoTrack,met)"),
    NTupleVariable("mll",         lambda ev: ev.mll,         help="Invariant mass of the two lead leptons"),

    ##--------------------------------------------------
]

susyAlphaT_globalObjects = susyCore_globalObjects.copy()
susyAlphaT_globalObjects.update({
    # put more here
    # "pseudoJet1"       : NTupleObject("pseudoJet1",     fourVectorType, help="pseudoJet1 for hemishphere"),
    # "pseudoJet2"       : NTupleObject("pseudoJet2",     fourVectorType, help="pseudoJet2 for hemishphere"),
    "biasedDPhiJet": NTupleObject("biasedDPhiJet", fourVectorType, help="jet closest to missing energy vector"),
    "metNoMu"      : NTupleObject("metNoMu",       fourVectorType, help="met computed with muon momentum substracted"),
    "metNoEle"     : NTupleObject("metNoEle",      fourVectorType, help="met computed with electron momentum substracted"),
    "metNoPhoton"  : NTupleObject("metNoPhoton",   fourVectorType, help="met computed with photon momentum substracted"),

})


susyAlphaT_collections = susyCore_collections.copy()
susyAlphaT_collections.update({
    # put more here
    #"selectedLeptons"  : NTupleCollection("lep",      leptonTypeSusy,           50, help="Leptons after the preselection", filter=lambda l : l.pt()>10 ),
    "cleanJetsAll"     : NTupleCollection("jet",      jetTypeAlphaT,             100, help="all jets (w/ x-cleaning, w/ ID applied w/o PUID applied pt > 40 |eta| < 5) , sorted by pt", filter=lambda l : l.pt()>40  ),
    "selectedPhotons"  : NTupleCollection("gamma",    photonTypeSusy,           50, help="photons with pt > 25 and loose cut based ID"),
    "selectedIsoTrack" : NTupleCollection("isoTrack", isoTrackType,             50, help="isoTrack, sorted by pt"),

    # leptons and taus 
    "selectedMuons"     : NTupleCollection("muon", leptonTypeSusy, 50, help="Muons selected by the analysis"),
    "selectedElectrons" : NTupleCollection("ele",  leptonTypeSusy, 50, help="Electrons selected by the analysis"),
    "selectedTaus"      : NTupleCollection("tau",  tauTypeSusy,    50, help="Taus after the preselection"),

    #Gen collections
    #"genParticles"     : NTupleCollection("allGenPart", genParticleWithMotherId, 200, help="all pruned genparticles"),
    "cleanGenJets"      : NTupleCollection("genJet",     genParticleType, 10, help="Generated jets (cleaned)"),

    # dR jet lep for each lepton
    "minDeltaRLepJet"  : NTupleCollection("minDeltaRLepJet", objectFloat, 10, help="Min deltaR between a lepton and all the jets"),
    "minDeltaRPhoJet"  : NTupleCollection("minDeltaRPhoJet", objectFloat, 10, help="Min deltaR between a photon and all the jets"),

    "LHE_weights"    : NTupleCollection("LHEweight",  weightsInfoType, 1000, help="LHE weight info"),
})

            
