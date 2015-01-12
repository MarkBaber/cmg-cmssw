import CMGTools.RootTools.fwlite.Config as cfg

##------------------------------------------
## Choose the type of cut flow and puRegime
## Signal or control sample
##------------------------------------------

alphaTPSet = cfg.CFG(
#puRegime = 'PU40bx50',
puRegime = 'PU20bx25',
#cutFlow = 'MultiJetEnriched',
#cutFlow = 'Signal',
#cutFlow = 'SingleMu',
#cutFlow = 'DoubleMu',
#cutFlow = 'SinglePhoton',
#cutFlow = 'SingleEle',
#cutFlow = 'DoubleEle',
cutFlow = 'Inclusive',
test =  2, #does nothing for now (may re add functionality in future)
limitFiles = False,
)


