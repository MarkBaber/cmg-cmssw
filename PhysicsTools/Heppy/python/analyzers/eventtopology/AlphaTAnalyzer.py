import operator 
import itertools
import copy
from math import *

from PhysicsTools.HeppyCore.utils.deltar import deltaR, deltaPhi
from PhysicsTools.Heppy.analyzers.core.Analyzer import Analyzer
from PhysicsTools.HeppyCore.framework.event import Event
from PhysicsTools.HeppyCore.statistics.counter import Counter, Counters
from PhysicsTools.Heppy.analyzers.core.AutoHandle import AutoHandle

from PhysicsTools.Heppy.physicsobjects.PhysicsObjects import Jet

import ROOT
from ROOT.heppy import AlphaT
import os

class AlphaTAnalyzer( Analyzer ):
    def __init__(self, cfg_ana, cfg_comp, looperName ):
        super(AlphaTAnalyzer,self).__init__(cfg_ana,cfg_comp,looperName) 

    def declareHandles(self):
        super(AlphaTAnalyzer, self).declareHandles()
        #genJets 
        #self.handles['genJets'] = AutoHandle( 'slimmedGenJets','std::vector<reco::GenJet>')

    def beginLoop(self,setup):
        super(AlphaTAnalyzer,self).beginLoop(setup)
        self.counters.addCounter('pairs')
        count = self.counters.counter('pairs')
        count.register('all events')


    # Calculate alphaT using jet ET
    def makeAlphaT(self, jets, jetFlag, minDeltaHT):

        if len(jets) == 0:
            return 0.
        
        px  = ROOT.std.vector('double')()
        py  = ROOT.std.vector('double')()
        et  = ROOT.std.vector('double')()

        #Make alphaT from lead 10 jets
	for jet in jets[:10]:
            px.push_back(jet.px())
            py.push_back(jet.py())
            et.push_back(jet.et())

        alphaTCalc = AlphaT()
        return alphaTCalc.getAlphaT( et, px, py, jetFlag, minDeltaHT)

    def process(self, event):
        self.readCollections( event.input )

	minDeltaHT = ROOT.Double(0.)
	jetFlags   = ROOT.std.vector('int')()

        event.alphaT     = self.makeAlphaT(event.cleanJets,jetFlags,minDeltaHT)
	event.minDeltaHT = minDeltaHT
	for i,jet in enumerate(event.cleanJets):
		if i >= jetFlags.size():
			jet.pseudoJetFlag = -1
			jet.inPseudoJet = False
		else:
			jet.pseudoJetFlag = jetFlags[i]
			jet.inPseudoJet = True
	
	genMinDeltaHT = ROOT.Double(0.)
	genJetFlags   = ROOT.std.vector('int')()

        #Do the same with gen jets for MC
        if self.cfg_comp.isMC:
            event.genAlphaT = self.makeAlphaT(event.cleanGenJets,genJetFlags,genMinDeltaHT)
            event.genMinDeltaHT = genMinDeltaHT
            pass

        return True
