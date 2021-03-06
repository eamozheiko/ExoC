#!/usr/bin/env python


"""
ExoC - Translocation detection from Exome capture Hi-C

# short decription

@version: $1.0$
@author: Evgeniy Mozheiko
@contact: eamozheiko@gmail.com
"""

import sys, os, time
import re
from pkg_resources import resource_filename
from ExoC.ArgsValidator import *
from ExoC.corelib import *

def statrun(args):
    opts = opt_validate_stat(args)
    
    path_to_stat_script = resource_filename('ExoC', 'scripts/sam_to_valid_pairs.sh')
    subprocess.call(path_to_stat_script + " " + opts.sam + " " + opts.outdir + " " + opts.name, shell=True)

    
    Info("Done! Find your stat results from %s" %(opts.outdir))
    return

def cnvrun(args):
    opts = opt_validate_cnv(args)
    

    Info("CNV module missing")
    return

def transrun(args):
    opts = opt_validate_trans(args)
    
    ## inter

    command = "Rscript %s %s %s %s %s %s %s %s"%(os.path.abspath('../ExoC/ExoC/inter_trans.R'), os.path.abspath('..'), opts.outdir, opts.case, opts.control, opts.binsize, opts.name, opts.thr_frame)
    print(command)
    run_cmd(command)
    
    ## intra
    command = "Rscript %s %s %s %s %s %s %s %s"%(os.path.abspath('../ExoC/ExoC/intra_trans.R'), os.path.abspath('..'), opts.outdir, opts.case, opts.control, opts.binsize, opts.name, opts.thr_frame)
    print(command)
    run_cmd(command)

    
    Info("Done! Find your translocation results from %s"%(opts.outdir))
    return
