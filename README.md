Higgs cross sections for LHC 
===========================

Python tool for easy access/interpolation of the values of LHC Higgs cross-sections and branching ratios.
The data is taken from [HXSWG page](https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CrossSections)  

# Using
To obtain the tool just clone it from GitHub:

    git clone https://github.com/KKostya/LHCHiggsXS.git

Then in python:

    import LHCHiggsXS as xs

    print "M = 125 Glu-Glu Higgs production cross-section:"
    print "At sqrt(s) = 8TeV", xs.EightTeV(125)['gg']['xsec']
    print "At sqrt(s) = 7TeV", xs.SevenTeV(125)['gg']['xsec']

    print "Corresponding pdf+alphas uncertaities:"
    print "At sqrt(s) = 8TeV", xs.EightTeV(125)['gg']['pdf']
    print "At sqrt(s) = 7TeV", xs.SevenTeV(125)['gg']['pdf']

    print "M = 230 Higgs branching to ZZ:" , xs.Br(230)['hzz']['br']
    print "Interpolated value for M = 642:", xs.Br(642)['hzz']['br']

