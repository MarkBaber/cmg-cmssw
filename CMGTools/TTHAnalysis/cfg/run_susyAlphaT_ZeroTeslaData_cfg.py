import PhysicsTools.HeppyCore.framework.config as cfg
from PhysicsTools.Heppy.analyzers.gen.LHEAnalyzer import LHEAnalyzer

#Load all analyzers with defaults for alphaT analysis
from CMGTools.TTHAnalysis.analyzers.susyAlphaTCore_cff import *
import sys
import os

# LHE
lheAna = cfg.Analyzer(    LHEAnalyzer, name = 'LHEAnalyzer' )

#Cuts forInclusive (turn off all skimmers)
ttHIsoTrackSkim.minObjects  = 0
ttHIsoTrackSkim.maxObjects  = 999
ttHLepSkim.minObjects       = 0
ttHLepSkim.maxObjects       = 999
ttHElectronSkim.minObjects  = 0
ttHElectronSkim.maxObjects  = 999
ttHMuonSkim.minObjects      = 0
ttHMuonSkim.maxObjects      = 999
ttHPhotonSkim.minObjects    = 0
ttHPhotonSkim.maxObjects    = 999
ttHAlphaTSkim.alphaTCuts    = [(-9999, 0,99999 )]   #Turn off AlphaT cut
ttHAlphaTSkim.mhtDivMetCut  = ('mhtJet40j','metNoMu',999)
ttHAlphaTSkim.forwardJetVeto = False
ttHJetMETSkim.jetPtCuts     = []
ttHJetMETSkim.htCut         = ('htJet40j', 0)

# LHE
# susyAlphaT_globalVariables.append(NTupleVariable("lheHT", lambda ev : ev.lheHT, help="LHE HT( q + g )"))
# sequence.insert(sequence.index(treeProducer)-1,lheAna)

selectedComponents = []

#NEED to add WZ,WW,ZZ samples FIXME

if bunchSpacing == '25ns':
    selectedComponents = [TTJets, TTJets_LO, WJetsToLNu, DYJetsToLL_M50] + WJetsToLNuHT + QCDPt
else:
    sys.exit("Only for 25ns atm")



#Limit the files as inclusive
for comp in selectedComponents:
    comp.splitFactor = 2
    comp.files = comp.files[1:3]



if test == "0" :


#    from 

    dataDir = "$CMSSW_BASE/src/CMGTools/TTHAnalysis/data"
    #json    = dataDir+'/json/Cert_246908-247381_13TeV_PromptReco_Collisions15_ZeroTesla.json'
    json    = dataDir+'/json/Cert_246908-247381_13TeV_PromptReco_Collisions15_ZeroTesla_JSON_CaloOnly.json'

    selectedTriggers = {"L1SingleJet16" : ["HLT_L1SingleJet16_v*"],
                        "L1SingleJet36" : ["HLT_L1SingleJet36_v*"],
                        "L1SingleJet68" : ["HLT_L1SingleJet68_v*"],
                        "Physics"       : ["HLT_Physics_v*"],        }

    triggerFlagsAna.triggerBits = selectedTriggers

    # Configure data JECs
    jetAna.dataGT = 'GR_P_V56'


    comp = cfg.DataComponent(
            name = "Jet",
            files =  [
            #'/vols/cms04/mb1512/MiniAODProduction/prodMiniAOD_Data_Run2ZeroTeslaPrompt_PAT_56.root',

	'root://gfe02.grid.hep.ph.ic.ac.uk/pnfs/hep.ph.ic.ac.uk/data/cms/store/user/mbaber/GR_P_V56_Run2015A_PromptReco_v1_19Jun15/Jet/crab_Jet/150619_090726/0000/prodMiniAOD_Data_Run2ZeroTeslaPrompt_PAT_55.root',
	'root://gfe02.grid.hep.ph.ic.ac.uk/pnfs/hep.ph.ic.ac.uk/data/cms/store/user/mbaber/GR_P_V56_Run2015A_PromptReco_v1_19Jun15/Jet/crab_Jet/150619_090726/0000/prodMiniAOD_Data_Run2ZeroTeslaPrompt_PAT_11.root',
	'root://gfe02.grid.hep.ph.ic.ac.uk/pnfs/hep.ph.ic.ac.uk/data/cms/store/user/mbaber/GR_P_V56_Run2015A_PromptReco_v1_19Jun15/Jet/crab_Jet/150619_090726/0000/prodMiniAOD_Data_Run2ZeroTeslaPrompt_PAT_16.root',
	'root://gfe02.grid.hep.ph.ic.ac.uk/pnfs/hep.ph.ic.ac.uk/data/cms/store/user/mbaber/GR_P_V56_Run2015A_PromptReco_v1_19Jun15/Jet/crab_Jet/150619_090726/0000/prodMiniAOD_Data_Run2ZeroTeslaPrompt_PAT_13.root',
	'root://gfe02.grid.hep.ph.ic.ac.uk/pnfs/hep.ph.ic.ac.uk/data/cms/store/user/mbaber/GR_P_V56_Run2015A_PromptReco_v1_19Jun15/Jet/crab_Jet/150619_090726/0000/prodMiniAOD_Data_Run2ZeroTeslaPrompt_PAT_18.root',
	'root://gfe02.grid.hep.ph.ic.ac.uk/pnfs/hep.ph.ic.ac.uk/data/cms/store/user/mbaber/GR_P_V56_Run2015A_PromptReco_v1_19Jun15/Jet/crab_Jet/150619_090726/0000/prodMiniAOD_Data_Run2ZeroTeslaPrompt_PAT_5.root',
	'root://gfe02.grid.hep.ph.ic.ac.uk/pnfs/hep.ph.ic.ac.uk/data/cms/store/user/mbaber/GR_P_V56_Run2015A_PromptReco_v1_19Jun15/Jet/crab_Jet/150619_090726/0000/prodMiniAOD_Data_Run2ZeroTeslaPrompt_PAT_21.root',
	'root://gfe02.grid.hep.ph.ic.ac.uk/pnfs/hep.ph.ic.ac.uk/data/cms/store/user/mbaber/GR_P_V56_Run2015A_PromptReco_v1_19Jun15/Jet/crab_Jet/150619_090726/0000/prodMiniAOD_Data_Run2ZeroTeslaPrompt_PAT_36.root',
	'root://gfe02.grid.hep.ph.ic.ac.uk/pnfs/hep.ph.ic.ac.uk/data/cms/store/user/mbaber/GR_P_V56_Run2015A_PromptReco_v1_19Jun15/Jet/crab_Jet/150619_090726/0000/prodMiniAOD_Data_Run2ZeroTeslaPrompt_PAT_28.root',
	'root://gfe02.grid.hep.ph.ic.ac.uk/pnfs/hep.ph.ic.ac.uk/data/cms/store/user/mbaber/GR_P_V56_Run2015A_PromptReco_v1_19Jun15/Jet/crab_Jet/150619_090726/0000/prodMiniAOD_Data_Run2ZeroTeslaPrompt_PAT_7.root',
	'root://gfe02.grid.hep.ph.ic.ac.uk/pnfs/hep.ph.ic.ac.uk/data/cms/store/user/mbaber/GR_P_V56_Run2015A_PromptReco_v1_19Jun15/Jet/crab_Jet/150619_090726/0000/prodMiniAOD_Data_Run2ZeroTeslaPrompt_PAT_8.root',
	'root://gfe02.grid.hep.ph.ic.ac.uk/pnfs/hep.ph.ic.ac.uk/data/cms/store/user/mbaber/GR_P_V56_Run2015A_PromptReco_v1_19Jun15/Jet/crab_Jet/150619_090726/0000/prodMiniAOD_Data_Run2ZeroTeslaPrompt_PAT_40.root',
	'root://gfe02.grid.hep.ph.ic.ac.uk/pnfs/hep.ph.ic.ac.uk/data/cms/store/user/mbaber/GR_P_V56_Run2015A_PromptReco_v1_19Jun15/Jet/crab_Jet/150619_090726/0000/prodMiniAOD_Data_Run2ZeroTeslaPrompt_PAT_10.root',
	'root://gfe02.grid.hep.ph.ic.ac.uk/pnfs/hep.ph.ic.ac.uk/data/cms/store/user/mbaber/GR_P_V56_Run2015A_PromptReco_v1_19Jun15/Jet/crab_Jet/150619_090726/0000/prodMiniAOD_Data_Run2ZeroTeslaPrompt_PAT_52.root',
	'root://gfe02.grid.hep.ph.ic.ac.uk/pnfs/hep.ph.ic.ac.uk/data/cms/store/user/mbaber/GR_P_V56_Run2015A_PromptReco_v1_19Jun15/Jet/crab_Jet/150619_090726/0000/prodMiniAOD_Data_Run2ZeroTeslaPrompt_PAT_6.root',
	'root://gfe02.grid.hep.ph.ic.ac.uk/pnfs/hep.ph.ic.ac.uk/data/cms/store/user/mbaber/GR_P_V56_Run2015A_PromptReco_v1_19Jun15/Jet/crab_Jet/150619_090726/0000/prodMiniAOD_Data_Run2ZeroTeslaPrompt_PAT_15.root',
	'root://gfe02.grid.hep.ph.ic.ac.uk/pnfs/hep.ph.ic.ac.uk/data/cms/store/user/mbaber/GR_P_V56_Run2015A_PromptReco_v1_19Jun15/Jet/crab_Jet/150619_090726/0000/prodMiniAOD_Data_Run2ZeroTeslaPrompt_PAT_2.root',
	'root://gfe02.grid.hep.ph.ic.ac.uk/pnfs/hep.ph.ic.ac.uk/data/cms/store/user/mbaber/GR_P_V56_Run2015A_PromptReco_v1_19Jun15/Jet/crab_Jet/150619_090726/0000/prodMiniAOD_Data_Run2ZeroTeslaPrompt_PAT_32.root',
	'root://gfe02.grid.hep.ph.ic.ac.uk/pnfs/hep.ph.ic.ac.uk/data/cms/store/user/mbaber/GR_P_V56_Run2015A_PromptReco_v1_19Jun15/Jet/crab_Jet/150619_090726/0000/prodMiniAOD_Data_Run2ZeroTeslaPrompt_PAT_47.root',
	'root://gfe02.grid.hep.ph.ic.ac.uk/pnfs/hep.ph.ic.ac.uk/data/cms/store/user/mbaber/GR_P_V56_Run2015A_PromptReco_v1_19Jun15/Jet/crab_Jet/150619_090726/0000/prodMiniAOD_Data_Run2ZeroTeslaPrompt_PAT_29.root',
	'root://gfe02.grid.hep.ph.ic.ac.uk/pnfs/hep.ph.ic.ac.uk/data/cms/store/user/mbaber/GR_P_V56_Run2015A_PromptReco_v1_19Jun15/Jet/crab_Jet/150619_090726/0000/prodMiniAOD_Data_Run2ZeroTeslaPrompt_PAT_9.root',
	'root://gfe02.grid.hep.ph.ic.ac.uk/pnfs/hep.ph.ic.ac.uk/data/cms/store/user/mbaber/GR_P_V56_Run2015A_PromptReco_v1_19Jun15/Jet/crab_Jet/150619_090726/0000/prodMiniAOD_Data_Run2ZeroTeslaPrompt_PAT_24.root',
	'root://gfe02.grid.hep.ph.ic.ac.uk/pnfs/hep.ph.ic.ac.uk/data/cms/store/user/mbaber/GR_P_V56_Run2015A_PromptReco_v1_19Jun15/Jet/crab_Jet/150619_090726/0000/prodMiniAOD_Data_Run2ZeroTeslaPrompt_PAT_41.root',
	'root://gfe02.grid.hep.ph.ic.ac.uk/pnfs/hep.ph.ic.ac.uk/data/cms/store/user/mbaber/GR_P_V56_Run2015A_PromptReco_v1_19Jun15/Jet/crab_Jet/150619_090726/0000/prodMiniAOD_Data_Run2ZeroTeslaPrompt_PAT_4.root',
	'root://gfe02.grid.hep.ph.ic.ac.uk/pnfs/hep.ph.ic.ac.uk/data/cms/store/user/mbaber/GR_P_V56_Run2015A_PromptReco_v1_19Jun15/Jet/crab_Jet/150619_090726/0000/prodMiniAOD_Data_Run2ZeroTeslaPrompt_PAT_35.root',
	'root://gfe02.grid.hep.ph.ic.ac.uk/pnfs/hep.ph.ic.ac.uk/data/cms/store/user/mbaber/GR_P_V56_Run2015A_PromptReco_v1_19Jun15/Jet/crab_Jet/150619_090726/0000/prodMiniAOD_Data_Run2ZeroTeslaPrompt_PAT_30.root',
	'root://gfe02.grid.hep.ph.ic.ac.uk/pnfs/hep.ph.ic.ac.uk/data/cms/store/user/mbaber/GR_P_V56_Run2015A_PromptReco_v1_19Jun15/Jet/crab_Jet/150619_090726/0000/prodMiniAOD_Data_Run2ZeroTeslaPrompt_PAT_3.root',
	'root://gfe02.grid.hep.ph.ic.ac.uk/pnfs/hep.ph.ic.ac.uk/data/cms/store/user/mbaber/GR_P_V56_Run2015A_PromptReco_v1_19Jun15/Jet/crab_Jet/150619_090726/0000/prodMiniAOD_Data_Run2ZeroTeslaPrompt_PAT_17.root',
	'root://gfe02.grid.hep.ph.ic.ac.uk/pnfs/hep.ph.ic.ac.uk/data/cms/store/user/mbaber/GR_P_V56_Run2015A_PromptReco_v1_19Jun15/Jet/crab_Jet/150619_090726/0000/prodMiniAOD_Data_Run2ZeroTeslaPrompt_PAT_23.root',
	'root://gfe02.grid.hep.ph.ic.ac.uk/pnfs/hep.ph.ic.ac.uk/data/cms/store/user/mbaber/GR_P_V56_Run2015A_PromptReco_v1_19Jun15/Jet/crab_Jet/150619_090726/0000/prodMiniAOD_Data_Run2ZeroTeslaPrompt_PAT_26.root',
	'root://gfe02.grid.hep.ph.ic.ac.uk/pnfs/hep.ph.ic.ac.uk/data/cms/store/user/mbaber/GR_P_V56_Run2015A_PromptReco_v1_19Jun15/Jet/crab_Jet/150619_090726/0000/prodMiniAOD_Data_Run2ZeroTeslaPrompt_PAT_54.root',
	'root://gfe02.grid.hep.ph.ic.ac.uk/pnfs/hep.ph.ic.ac.uk/data/cms/store/user/mbaber/GR_P_V56_Run2015A_PromptReco_v1_19Jun15/Jet/crab_Jet/150619_090726/0000/prodMiniAOD_Data_Run2ZeroTeslaPrompt_PAT_25.root',
	'root://gfe02.grid.hep.ph.ic.ac.uk/pnfs/hep.ph.ic.ac.uk/data/cms/store/user/mbaber/GR_P_V56_Run2015A_PromptReco_v1_19Jun15/Jet/crab_Jet/150619_090726/0000/prodMiniAOD_Data_Run2ZeroTeslaPrompt_PAT_14.root',
	'root://gfe02.grid.hep.ph.ic.ac.uk/pnfs/hep.ph.ic.ac.uk/data/cms/store/user/mbaber/GR_P_V56_Run2015A_PromptReco_v1_19Jun15/Jet/crab_Jet/150619_090726/0000/prodMiniAOD_Data_Run2ZeroTeslaPrompt_PAT_38.root',
	'root://gfe02.grid.hep.ph.ic.ac.uk/pnfs/hep.ph.ic.ac.uk/data/cms/store/user/mbaber/GR_P_V56_Run2015A_PromptReco_v1_19Jun15/Jet/crab_Jet/150619_090726/0000/prodMiniAOD_Data_Run2ZeroTeslaPrompt_PAT_48.root',
	'root://gfe02.grid.hep.ph.ic.ac.uk/pnfs/hep.ph.ic.ac.uk/data/cms/store/user/mbaber/GR_P_V56_Run2015A_PromptReco_v1_19Jun15/Jet/crab_Jet/150619_090726/0000/prodMiniAOD_Data_Run2ZeroTeslaPrompt_PAT_44.root',
	'root://gfe02.grid.hep.ph.ic.ac.uk/pnfs/hep.ph.ic.ac.uk/data/cms/store/user/mbaber/GR_P_V56_Run2015A_PromptReco_v1_19Jun15/Jet/crab_Jet/150619_090726/0000/prodMiniAOD_Data_Run2ZeroTeslaPrompt_PAT_53.root',
	'root://gfe02.grid.hep.ph.ic.ac.uk/pnfs/hep.ph.ic.ac.uk/data/cms/store/user/mbaber/GR_P_V56_Run2015A_PromptReco_v1_19Jun15/Jet/crab_Jet/150619_090726/0000/prodMiniAOD_Data_Run2ZeroTeslaPrompt_PAT_51.root',
	'root://gfe02.grid.hep.ph.ic.ac.uk/pnfs/hep.ph.ic.ac.uk/data/cms/store/user/mbaber/GR_P_V56_Run2015A_PromptReco_v1_19Jun15/Jet/crab_Jet/150619_090726/0000/prodMiniAOD_Data_Run2ZeroTeslaPrompt_PAT_22.root',
	'root://gfe02.grid.hep.ph.ic.ac.uk/pnfs/hep.ph.ic.ac.uk/data/cms/store/user/mbaber/GR_P_V56_Run2015A_PromptReco_v1_19Jun15/Jet/crab_Jet/150619_090726/0000/prodMiniAOD_Data_Run2ZeroTeslaPrompt_PAT_33.root',
	'root://gfe02.grid.hep.ph.ic.ac.uk/pnfs/hep.ph.ic.ac.uk/data/cms/store/user/mbaber/GR_P_V56_Run2015A_PromptReco_v1_19Jun15/Jet/crab_Jet/150619_090726/0000/prodMiniAOD_Data_Run2ZeroTeslaPrompt_PAT_42.root',
	'root://gfe02.grid.hep.ph.ic.ac.uk/pnfs/hep.ph.ic.ac.uk/data/cms/store/user/mbaber/GR_P_V56_Run2015A_PromptReco_v1_19Jun15/Jet/crab_Jet/150619_090726/0000/prodMiniAOD_Data_Run2ZeroTeslaPrompt_PAT_45.root',
	'root://gfe02.grid.hep.ph.ic.ac.uk/pnfs/hep.ph.ic.ac.uk/data/cms/store/user/mbaber/GR_P_V56_Run2015A_PromptReco_v1_19Jun15/Jet/crab_Jet/150619_090726/0000/prodMiniAOD_Data_Run2ZeroTeslaPrompt_PAT_50.root',
	'root://gfe02.grid.hep.ph.ic.ac.uk/pnfs/hep.ph.ic.ac.uk/data/cms/store/user/mbaber/GR_P_V56_Run2015A_PromptReco_v1_19Jun15/Jet/crab_Jet/150619_090726/0000/prodMiniAOD_Data_Run2ZeroTeslaPrompt_PAT_43.root',
	'root://gfe02.grid.hep.ph.ic.ac.uk/pnfs/hep.ph.ic.ac.uk/data/cms/store/user/mbaber/GR_P_V56_Run2015A_PromptReco_v1_19Jun15/Jet/crab_Jet/150619_090726/0000/prodMiniAOD_Data_Run2ZeroTeslaPrompt_PAT_56.root',
	'root://gfe02.grid.hep.ph.ic.ac.uk/pnfs/hep.ph.ic.ac.uk/data/cms/store/user/mbaber/GR_P_V56_Run2015A_PromptReco_v1_19Jun15/Jet/crab_Jet/150619_090726/0000/prodMiniAOD_Data_Run2ZeroTeslaPrompt_PAT_49.root',
	'root://gfe02.grid.hep.ph.ic.ac.uk/pnfs/hep.ph.ic.ac.uk/data/cms/store/user/mbaber/GR_P_V56_Run2015A_PromptReco_v1_19Jun15/Jet/crab_Jet/150619_090726/0000/prodMiniAOD_Data_Run2ZeroTeslaPrompt_PAT_31.root',
	'root://gfe02.grid.hep.ph.ic.ac.uk/pnfs/hep.ph.ic.ac.uk/data/cms/store/user/mbaber/GR_P_V56_Run2015A_PromptReco_v1_19Jun15/Jet/crab_Jet/150619_090726/0000/prodMiniAOD_Data_Run2ZeroTeslaPrompt_PAT_34.root',

            ],
            intLumi = 1, 
            #triggers = triggers, 
            json = json

        )

    selectedComponents = [comp]
    comp.splitFactor   = 1



if test == "1" :

    #Select samples and limit the files
    selectedComponents = [WJetsToLNu]
    for comp in selectedComponents:
        comp.splitFactor = 1
        comp.files = comp.files[:1]

#Option just to use one file per sample
if test=="2":

    for comp in selectedComponents:
        comp.splitFactor = 1
        comp.files = comp.files[:1]



# the following is declared in case this cfg is used in input to the heppy.py script
from PhysicsTools.HeppyCore.framework.eventsfwlite import Events
config = cfg.Config( components = selectedComponents,
                     sequence = sequence,
                     services = [],  
                     events_class = Events)


