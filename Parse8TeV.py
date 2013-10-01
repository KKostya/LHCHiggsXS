import urllib2
import pprint
import lxml.html

f    = urllib2.urlopen("https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageAt7TeV")
root = lxml.html.parse(f)

xsec = {}

def ProcessTable(tid, process , errnames, extras = None ):
    rows    = iter(root.xpath("//table[@id='{0}']".format(tid))[0])
    headers = [c.text for c in next(rows)]
    for r in rows:
        row = [c.text for c in r]
        mass = float(row[0])
        if not mass    in xsec:       xsec[mass]          = {}
        if not process in xsec[mass]: xsec[mass][process] = {}
        xsec[mass][process]['xsec'] = float(row[1])
        for i in range(len(errnames)):
            xsec[mass][process][errnames[i]] = (float(row[2*i+2]),float(row[2*i+3]))
        if not extras: continue
        for i in range(len(extras)):
            xsec[mass][process][extras[i]] = float(row[i+2*len(errnames)+2])



ProcessTable("table2", 'ggh', ['scale', 'pdf'])
ProcessTable("table3", 'vbf', ['scale', 'pdf']) 
ProcessTable("table6", 'tth', ['scale', 'pdf']) 
ProcessTable("table4", 'wh',  ['scale', 'pdf'], ["wplusH", "wminusH"]) 
ProcessTable("table5", 'zh',  ['scale', 'pdf'], ["box"]) 

pprint.pprint(xsec)
