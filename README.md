# cmg-cmssw-private
```bash
cmsrel CMSSW_7_2_3
cd CMSSW_7_2_3/src
cmsenv

# checkout RA1 specific codes
git init
git remote add cmsra1 git@github.com:CMSRA1/cmg-cmssw-private.git

git fetch cmsra1

git config core.sparsecheckout true
cp /afs/cern.ch/user/c/cmgtools/public/sparse-checkout_72X_heppy .git/info/sparse-checkout

# check out RA1 code
git checkout cmsra1/CMGTools-from-CMSSW_7_2_3
git checkout -b CMGTools-from-CMSSW_7_2_3

# compile
scram b -v -j 9

#To update
git pull cmsra1 CMGTools-from-CMSSW_7_2_3

#Update from the central cmg repo
#This should be done regularly to make sure we keep up to date

#If not added do:
git remote add cmg-central git@github.com:CERN-PH-CMG/cmg-cmssw.git

#Then each time to update
git pull cmg-central CMGTools-from-CMSSW_7_2_3
```
#TTHAnalysis
```
# set up the TTHAnalysis code
cd CMGTools/TTHAnalysis/python/plotter
root.exe -b -l -q smearer.cc++ mcCorrections.cc++
root.exe -b -l -q functions.cc++
root.exe -b -l -q fakeRate.cc++
root -b
gSystem->SetIncludePath("-I$ROOFITSYS/include");
.L TH1Keys.cc++
.q
cd ../../../../

# compile
scram b -v -j 9

# run for 1000 events to test
cd CMGTools/TTHAnalysis/cfg/ 

#for 723 and after
heppy TESTsusy run_susyAlphaT_cfg.py -N 1000 -f

```

#Installation of CMG Codes at IC
```
source /vols/cms/grid/setup.sh
cmsrel CMSSW_7_2_3
cd CMSSW_7_2_3/src
cmsenv

# checkout RA1 cmg-tools
git init
git remote add cmg-ra1 git@github.com:CMSRA1/cmg-cmssw-private.git
git fetch cmg-ra1
git config core.sparsecheckout true
cat /vols/ssd00/cms/lucienlo/susy/phys14/public/CMSSW723/sparse-checkout >> .git/info/sparse-checkout
# check out alphaT code
git checkout cmg-ra1/Phys14_723
git checkout -b Phys14_723

# modify CMGTools/TTHAnalysis/BuildFile
sed -i 's@/afs/cern.ch/cms@/cvmfs/cms.cern.ch@g' CMGTools/TTHAnalysis/BuildFile.xml

# compile
scram b -v -j 9
```
