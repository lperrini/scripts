#!/usr/bin/env python
import os,sys
import getopt
import commands

Samples = [ 
"MC8TeV_DY1JetsToLL_50toInf_0.root",
"MC8TeV_DY1JetsToLL_50toInf_1.root",
"MC8TeV_DY1JetsToLL_50toInf_2.root",
]

for s in Samples:
#copy from ULB to UCL
   os.system('lcg-cp --verbose -b -D srmv2 "srm://ingrid-se02.cism.ucl.ac.be:8444/srm/managerv2?SFN=/storage/data/cms/users/quertenmont/Higgs/Ntuples/13_10_15/'+s+'" "srm://srm-eoscms.cern.ch:8443/srm/v2/server?SFN=/eos/cms//store/group/phys_higgs/cmshzz2l2v/2013_08_30/'+s+'" &> LOG_'+s+' &')
   os.system('lcg-cp --verbose -b -D srmv2 "srm://maite.iihe.ac.be:8443/srm/managerv2?SFN=/pnfs/iihe/cms/store/user/lperrini/'+s+'" "srm://ingrid-se02.cism.ucl.ac.be:8444/srm/managerv2?SFN=/storage/data/cms/users/lperrini/'+s+'" &> LOG_'+s+' &')


