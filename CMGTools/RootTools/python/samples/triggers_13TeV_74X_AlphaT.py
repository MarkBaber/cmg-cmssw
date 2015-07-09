# ******************************************************************************************************************
# *                                                                                                                *
# *                                                  AlphaT Run 2 triggers                                         *
# *                                                                                                                *
# ******************************************************************************************************************

# ----------------------------------------
# Signal triggers
# ----------------------------------------
signalTriggerBits   = { # Primary
                        "PFHT200_DiPFJetAve90_PFAlphaT0p57" : ["HLT_PFHT200_DiPFJetAve90_PFAlphaT0p57_v"],
                        "PFHT250_DiPFJetAve90_PFAlphaT0p55" : ["HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55_v"],
                        "PFHT300_DiPFJetAve90_PFAlphaT0p53" : ["HLT_PFHT300_DiPFJetAve90_PFAlphaT0p53_v"],
                        "PFHT350_DiPFJetAve90_PFAlphaT0p52" : ["HLT_PFHT350_DiPFJetAve90_PFAlphaT0p52_v"],
                        "PFHT400_DiPFJetAve90_PFAlphaT0p51" : ["HLT_PFHT400_DiPFJetAve90_PFAlphaT0p51_v"],
                        
                        # Backup
                        "PFHT200_DiPFJetAve90_PFAlphaT0p63" : ["HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63_v"],
                        "PFHT250_DiPFJetAve90_PFAlphaT0p58" : ["HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58_v"],
                        "PFHT300_DiPFJetAve90_PFAlphaT0p54" : ["HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54_v"],
                        "PFHT350_DiPFJetAve90_PFAlphaT0p53" : ["HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53_v"],
                        "PFHT400_DiPFJetAve90_PFAlphaT0p52" : ["HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52_v"],
                        
                        # HT trigger
                        "PFHT800"                           : ["HLT_PFHT800_v"],
                        }
# "PFHT350_PFMET120_NoiseCleaned" : ["HLT_PFHT350_PFMET120_NoiseCleaned_v"], # Could be used


# Trigger bits for testing only - Only bits available in miniAOD
dummySignalTriggerBits   = {   
                        "PFHT200_DiPFJet90_PFAlphaT0p57" : ["HLT_PFHT200_DiPFJet90_PFAlphaT0p57_v*"],
                        "PFHT250_DiPFJet90_PFAlphaT0p55" : ["HLT_PFHT250_DiPFJet90_PFAlphaT0p55_v*"],
                        "PFHT300_DiPFJet90_PFAlphaT0p53" : ["HLT_PFHT300_DiPFJet90_PFAlphaT0p53_v*"],
                        "PFHT350_DiPFJet90_PFAlphaT0p52" : ["HLT_PFHT350_DiPFJet90_PFAlphaT0p52_v*"],
                        "PFHT400_DiPFJet90_PFAlphaT0p51" : ["HLT_PFHT400_DiPFJet90_PFAlphaT0p51_v*"],

                        # HT trigger
                        "PFHT900"                        : ["HLT_PFHT900_v"],
}

# Monojet triggers
monojetTriggerBits   = {
    "PFMETNoMu120_NoiseCleaned_PFMHTNoMu120_IDTight"                    : ["HLT_PFMETNoMu120_NoiseCleaned_PFMHTNoMu120_IDTight_v*"],
    "PFMETNoMu90_NoiseCleaned_PFMHTNoMu90_IDTight"                      : ["HLT_PFMETNoMu90_NoiseCleaned_PFMHTNoMu90_IDTight_v*"],
    "MonoCentralPFJet80_PFMETNoMu90_NoiseCleaned_PFMHTNoMu90_IDTight"   : ["HLT_MonoCentralPFJet80_PFMETNoMu90_NoiseCleaned_PFMHTNoMu90_IDTight_v*"],
    "MonoCentralPFJet80_PFMETNoMu120_NoiseCleaned_PFMHTNoMu120_IDTight" : ["HLT_MonoCentralPFJet80_PFMETNoMu120_NoiseCleaned_PFMHTNoMu120_IDTight_v*"],
    "PFMET170_NoiseCleaned"                                             : ["HLT_PFMET170_NoiseCleaned_v*"],
    "CaloMET200_NoiseCleaned"                                           : ["HLT_CaloMET200_NoiseCleaned_v*"],
    "CaloJet500_NoJetID"                                                : ["HLT_CaloJet500_NoJetID_v*"],
}

# ----------------------------------------
# Muon triggers
# ----------------------------------------
muonTriggerBits     = {"IsoMu24_eta2p1" : ["HLT_IsoMu24_eta2p1_v"],
                       "IsoMu24"        : ["HLT_IsoMu24_v"],
                       
                       }

# ----------------------------------------
# Electron triggers
# ----------------------------------------
electronTriggerBits = { "Ele27_eta2p1_WPLoose_Gsf_v1": ["HLT_Ele27_eta2p1_WPLoose_Gsf"]
                      }

# ----------------------------------------
# Photon triggers
# ----------------------------------------
photonTriggerBits   = { "Photon175"  : ["HLT_Photon175_v"], 
                        "Photon120"  : ["HLT_Photon120_v"],
                      }

# ----------------------------------------
# Hadronic control triggers
# ----------------------------------------
hadronicTriggerBits = { "PFHT200" : ["HLT_PFHT200_v"],
                        "PFHT250" : ["HLT_PFHT250_v"],
                        "PFHT300" : ["HLT_PFHT300_v"],
                        "PFHT350" : ["HLT_PFHT350_v"],
                        "PFHT400" : ["HLT_PFHT400_v"],
                        #"HLT_PFHT475" : ["HLT_PFHT475_v"], # Could be used
                        }

# Trigger bits for testing only - Only bits available in miniAOD
dummyHadronicTriggerBits = { "HT200" : ["HLT_HT200_v"],
                             "HT250" : ["HLT_HT250_v"],
                             "HT300" : ["HLT_HT300_v"],
                             "HT350" : ["HLT_HT350_v"],
                             "HT400" : ["HLT_HT400_v"],
                             #"PFHT475" : ["HLT_PFHT475_v"], # Could be used
                        }


def appendTriggerDict(t1, t2):
    temp = t1.copy()
    temp.update(t2)
    return temp
