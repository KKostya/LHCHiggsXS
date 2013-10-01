import urllib2
import pprint
import lxml.html

f    = urllib2.urlopen("https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageBR3")
root = lxml.html.parse(f)

brs = {}

def ProcessTable(tid, cols, commonErr = False):
    rows    = iter(root.xpath("//table[@id='{0}']".format(tid))[0])
    headersA = [c.text for c in next(rows)]
    headersB = [c.text for c in next(rows)]
    for r in rows:
        row = [c.text for c in r]
        mass = float(row[0])
        if not mass  in brs: brs[mass] = {}
        for n,idx in cols:
            if not n in brs[mass]: brs[mass][n] = {}
            brs[mass][n]['br' if n != 'total' else 'width'] =  float(row[idx])
            if commonErr:  brs[mass][n]['err'] =  float(row[-1])
            else:          brs[mass][n]['err'] = (float(row[idx+1]),float(row[idx+2]))

# 2body tables
ProcessTable("table2", [('hbb', 1), ('htautau', 4), ('hmumu', 7), ('hcc', 10), ('hss', 13), ('htt'  , 16)])
ProcessTable("table3", [('hgg', 1), ('haa'    , 4), ('hza'  , 7), ('hww', 10), ('hzz', 13), ('total', 16)])

# 2body tables
ProcessTable("table4", [('hLLLL', 1), ('hllll', 2), ('heeee', 3), ('heemm', 4), ('hLLnn', 5), ('hllnn', 6), ('heenn',7),('hemnn',8)],True)
ProcessTable("table6", [('hLLqq', 1), ('hllqq', 2), ('hlnqq', 3), ('hnnqq', 4), ('hqqqq', 5), ('hffff', 6)],True)


pprint.pprint(brs)
