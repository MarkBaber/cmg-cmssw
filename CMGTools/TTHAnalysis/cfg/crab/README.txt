1) make sure crab is in the path (then may need to redo cmsenv)
> source /cvmfs/cms.cern.ch/crab3/crab.sh
> cmsenv

2) edit crabMaster_cfg.py to choose the cut flows and everything you want

3) run!!!
> voms-proxy-init -voms cms --valid=50:00
Enter GRID pass phrase for this identity: xxxx

# To run on a single config
> python launchall.py 

# for alphaT users to submit everything
> python crabMaster_cfg.py --submit 

# for alphaT users to check everything
> python crabMaster_cfg.py --status

# for alphaT users to resubmit everything
> python crabMaster_cfg.py --resubmit

Notes: 
- debugging: debug option can be set on launchall.py (be smart and choose a single component in the cfg)
- if useAAA=True in launchall.py, xrootd will be use instead of the default eos (from samples.py)
- modify heppy_crab_config.py to run only on your favorite sites
