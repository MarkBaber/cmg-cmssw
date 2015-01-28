#!/usr/bin/env python
#Script to attach all the cmg tools output together to follow the cut flow

#Explicitly list to get the correct cut flow order
filenames=[
        'ttHMuonSkimmer/events.txt',
        'ttHElectronSkimmer/events.txt',
        'ttHLepSkimmer/events.txt',
        'isoTrackAnalyzer/events.txt',
        'ttHIsoTrackSkimmer/events.txt',
        'ttHPhotonSkimmer/events.txt',
        'ttHJetMETSkimmer/events.txt',
        'ttHAlphaTSkimmer/events.txt',
        'ttHAlphaTControlSkimmer/events.txt',
        ]
with open('summary.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            x = []
            for y in fname:
                if y != '/':
                    x.append(y)
                else: 
                    break
            outfile.write("".join(x)+'\n')
            print "".join(x)+'\n'
            outfile.write(infile.read())
            infile.seek(0)
            print infile.read()
