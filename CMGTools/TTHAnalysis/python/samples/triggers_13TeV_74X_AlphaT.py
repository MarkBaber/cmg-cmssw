# ******************************************************************************************************************
# *                                                                                                                *
# *                                                  AlphaT Run 2 triggers                                         *
# *                                                                                                                *
# ******************************************************************************************************************

# ----------------------------------------
# Signal triggers
# ----------------------------------------
signalTriggerBits   = { # Primary
                        "HLT_PFHT200_DiPFJetAve90_PFAlphaT0p57" : ["HLT_PFHT200_DiPFJetAve90_PFAlphaT0p57_v"],
                        "HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55" : ["HLT_PFHT250_DiPFJetAve90_PFAlphaT0p55_v"],
                        "HLT_PFHT300_DiPFJetAve90_PFAlphaT0p53" : ["HLT_PFHT300_DiPFJetAve90_PFAlphaT0p53_v"],
                        "HLT_PFHT350_DiPFJetAve90_PFAlphaT0p52" : ["HLT_PFHT350_DiPFJetAve90_PFAlphaT0p52_v"],
                        "HLT_PFHT400_DiPFJetAve90_PFAlphaT0p51" : ["HLT_PFHT400_DiPFJetAve90_PFAlphaT0p51_v"],
                        
                        # Backup
                        "HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63" : ["HLT_PFHT200_DiPFJetAve90_PFAlphaT0p63_v"],
                        "HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58" : ["HLT_PFHT250_DiPFJetAve90_PFAlphaT0p58_v"],
                        "HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54" : ["HLT_PFHT300_DiPFJetAve90_PFAlphaT0p54_v"],
                        "HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53" : ["HLT_PFHT350_DiPFJetAve90_PFAlphaT0p53_v"],
                        "HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52" : ["HLT_PFHT400_DiPFJetAve90_PFAlphaT0p52_v"],
                        
                        # HT trigger
                        "HLT_PFHT800"                           : ["HLT_PFHT800_v"],
                        }
# "HLT_PFHT350_PFMET120_NoiseCleaned" : ["HLT_PFHT350_PFMET120_NoiseCleaned_v"], # Could be used


# Trigger bits for testing only - Only bits available in miniAOD
dummySignalTriggerBits   = {   
                        "HLT_PFHT200_DiPFJet90_PFAlphaT0p57" : ["HLT_PFHT200_DiPFJet90_PFAlphaT0p57_v*"],
                        "HLT_PFHT250_DiPFJet90_PFAlphaT0p55" : ["HLT_PFHT250_DiPFJet90_PFAlphaT0p55_v*"],
                        "HLT_PFHT300_DiPFJet90_PFAlphaT0p53" : ["HLT_PFHT300_DiPFJet90_PFAlphaT0p53_v*"],
                        "HLT_PFHT350_DiPFJet90_PFAlphaT0p52" : ["HLT_PFHT350_DiPFJet90_PFAlphaT0p52_v*"],
                        "HLT_PFHT400_DiPFJet90_PFAlphaT0p51" : ["HLT_PFHT400_DiPFJet90_PFAlphaT0p51_v*"],

                        # HT trigger
                        "HLT_PFHT900"                           : ["HLT_PFHT900_v"],
}


# ----------------------------------------
# Muon triggers
# ----------------------------------------
muonTriggerBits     = {"HLT_IsoMu24"        : ["HLT_IsoMu24_v"],
                       "HLT_IsoMu24_eta2p1" : ["HLT_IsoMu24_eta2p1_v"],
                       }

# ----------------------------------------
# Electron triggers
# ----------------------------------------
electronTriggerBits = { "HLT_Ele27_eta2p1_WPLoose_Gsf_v1": ["HLT_Ele27_eta2p1_WPLoose_Gsf"]
                      }

# ----------------------------------------
# Photon triggers
# ----------------------------------------
photonTriggerBits   = { "HLT_Photon175"  : ["HLT_Photon175_v"], 
                        "HLT_Photon120"  : ["HLT_Photon120_v"],
                      }

# ----------------------------------------
# Hadronic control triggers
# ----------------------------------------
hadronicTriggerBits = { "HLT_PFHT200" : ["HLT_PFHT200_v"],
                        "HLT_PFHT250" : ["HLT_PFHT250_v"],
                        "HLT_PFHT300" : ["HLT_PFHT300_v"],
                        "HLT_PFHT350" : ["HLT_PFHT350_v"],
                        "HLT_PFHT400" : ["HLT_PFHT400_v"],
                        #"HLT_PFHT475" : ["HLT_PFHT475_v"], # Could be used
                        }

# Trigger bits for testing only - Only bits available in miniAOD
dummyHadronicTriggerBits = { "HLT_HT200" : ["HLT_HT200_v"],
                             "HLT_HT250" : ["HLT_HT250_v"],
                             "HLT_HT300" : ["HLT_HT300_v"],
                             "HLT_HT350" : ["HLT_HT350_v"],
                             "HLT_HT400" : ["HLT_HT400_v"],
                             #"HLT_PFHT475" : ["HLT_PFHT475_v"], # Could be used
                        }


def appendTriggerDict(t1, t2):
    temp = t1.copy()
    temp.update(t2)
    return temp
