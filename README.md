For installation instructions of 743 see:

https://twiki.cern.ch/twiki/bin/viewauth/CMS/CMGToolsReleasesExperimental#Git_MiniAOD_release_for_Summer_2

and:

https://twiki.cern.ch/twiki/bin/viewauth/CMS/SUSYCMGfwk#7_4_3_and_Heppy_and_Spring15

for now


#Running CMG

See: https://twiki.cern.ch/twiki/bin/view/CMS/AlphaT#Running_Heppy_CMGTools_flat_tree

# Magnetic field package compilation problems
If you are getting a compilation problem for modules found in the Magnetic field package, you may need to add the line /MagneticField/ParametrizedEngine/ to your sparse-checkout:
```bash
cd $CMSSW_BASE/src

#Append the sparse-checkout
echo /MagneticField/ParametrizedEngine/ >> .git/info/sparse-checkout

#Update your new checkout
git read-tree -mu HEAD
```

# cmg-cmssw-private
```bash
cmsrel CMSSW_7_4_3
cd CMSSW_7_4_3/src
cmsenv

# checkout RA1 specific codes
git cms-init
git remote add cmsra1 git@github.com:CMSRA1/cmg-cmssw-private.git
git fetch cmsra1

git config core.sparsecheckout true
cp /afs/cern.ch/user/c/cmgtools/public/sparse-checkout_74X_heppy .git/info/sparse-checkout

# check out RA1 code
git checkout -b RA1-CMGTools-from-CMSSW_7_4_3 cmsra1/RA1-CMGTools-from-CMSSW_7_4_3

# compile
scram b -v -j8

#To update
git pull cmsra1 RA1-CMGTools-from-CMSSW_7_4_3

#Update from the central cmg repo
#This should be done regularly to make sure we keep up to date

#If not added do:
git remote add cmg-central git@github.com:CERN-PH-CMG/cmg-cmssw.git

#Then each time to update
git pull cmg-central CMGTools-from-CMSSW_7_4_3
```
#TTHAnalysis
```bash
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
scram b -v -j8

# run for 1000 events to test
cd CMGTools/TTHAnalysis/cfg/ 

#for 723 and after (verbosity can be reduced with addition of the flags: -q -p 0)
heppy TESTsusy run_susyAlphaT_Inclusive_cfg.py -N 1000 -f -o test=1 -q -p 0


#Installation of CMG Codes at IC for 723
```bash
# make sure you have the required architechture
export SCRAM_ARCH=slc6_amd64_gcc481

source /cvmfs/cms.cern.ch/cmsset_default.sh
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
git checkout cmg-ra1/RA1-CMGTools-from-CMSSW_7_2_3
git checkout -b RA1-CMGTools-from-CMSSW_7_2_3

# modify CMGTools/TTHAnalysis/BuildFile
sed -i 's@/afs/cern.ch/cms@/cvmfs/cms.cern.ch@g' CMGTools/TTHAnalysis/BuildFile.xml

# compile
scram b -v -j 9
```

#Installation of CMG Codes at IC for 706
```
source /vols/cms/grid/setup.sh
cmsrel CMSSW_7_0_6_patch1
cd CMSSW_7_0_6_patch1/src
cmsenv

# checkout RA1 cmg-tools
git init
git remote add cmg-ra1 git@github.com:CMSRA1/cmg-cmssw-private.git
git fetch cmg-ra1
git config core.sparsecheckout true
cat /vols/ssd00/cms/lucienlo/susy/phys14/public/sparse-checkout >> .git/info/sparse-checkout
# check out alphaT code
#(if this branch doesn't work use ImperialPort-CMSSW_7_0_6 if it exists)
git checkout cmg-ra1/CMG_MiniAOD_Lite_V6_0_from-CMSSW_7_0_6
git checkout -b CMG_MiniAOD_Lite_V6_0_from-CMSSW_7_0_6

# compile
scram b -v -j 9
# cmg-cmssw-private
```

#Installation of CMG Codes at Bristol for 743
###Logging into soolin (from local machine or lxplus)
```
ssh <username>@seis.bris.ac.uk
 -> ssh <username>@soolin.phy.bris.ac.uk
```
###Setting up CMG Framework
```
export SCRAM_ARCH=slc6_amd64_gcc491
# Setup CMSSW   
. /cvmfs/cms.cern.ch/cmsset_default.sh
cmsrel CMSSW_7_4_3
cd CMSSW_7_4_3/src
cmsenv
git init
# Add trunk from Dom's Repo (for now)
git remote add cmg-ra1-bristol git@github.com:dsmiff/cmg-cmssw-private.git
git fetch cmg-ra1-bristol
cp /users/ds13962/public/alphat/sparse-checkout .git/info/sparse-checkout
git config core.sparsecheckout true
git checkout cmg-ra1-bristol/Trunk_Bristol_RA1-CMGTools-from-CMSSW_7_4_3
# Create your branch and compile
git checkout -b <branch name>
scram b -v -j 8
```

