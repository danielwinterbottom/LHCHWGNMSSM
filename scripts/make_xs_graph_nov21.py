######################################

# Store X->Yh maximum cross sections provided by Ulrich Ellwanger in Nov21 as TGraph2D

# Numbers provided for A2->A1(->gamgam)+h125(->tautau)
# Sent by private mail from Ulrich Ellwanger -> Daniel Winterbottom on 24/11/21

# Numbers provided for H3->Hs(->bb)+h125(->bb) and H3->Hs(->bb)+h125(->tautau)
# Sent by mail from Ulrich Ellwanger -> NMSSM conveners on 16/11/21 

######################################

import ROOT
from array import array

fout = ROOT.TFile('output/HXSG_NMSSM_recommendations_Nov21.root','RECREATE')

# tautaugammagamma: 

x1 = [410.,500.,600.,700., 410.,500.,600.,700., 415.,500.,600.,700.]
y1 = [70., 70., 70., 70., 100., 100., 100., 100., 200., 200., 200., 200.]
z1 = [0.408E-2, 0.916E-3, 0.214E-3, 0.668E-4, 0.885E-2, 0.162E-2, 0.365E-3, 0.110E-3, 0.486E-2, 0.144E-2, 0.370E-3, 0.118E-3]

g1 = ROOT.TGraph2D(len(x1),array('d',x1),array('d',y1),array('d',z1))

g1.SetTitle('A2#rightarrow A1(#rightarrow #gamma#gamma) + h_{125}(#rightarrow#tau#tau); m(A2) [GeV]; m(A1) [GeV]; #sigma #times BR [pb]')

g1.Write('tautaugamgam')

# bbbb and tautaubb numbers

x2=[]
y2=[]
z2=[] # bbbb xs
z3=[] # tautaubb xs

infile = open('input/table_bbbb-bbtautau', 'r')
for l in infile.readlines():
  x = l.split()
  if len(x)!=5: continue 
  if not x[0].isdigit(): continue 
  x2.append(float(x[0])) 
  y2.append(float(x[1]))
  z2.append(float(x[2])) 
  z3.append(float(x[3])) 
infile.close()

# bbbb

g2 = ROOT.TGraph2D(len(x2),array('d',x2),array('d',y2),array('d',z2))

g2.SetTitle('H3#rightarrow H_{S}(#rightarrow bb) + h_{125}(#rightarrow bb); m(H3) [GeV]; m(H_{S}) [GeV]; #sigma #times BR [pb]')

g2.Write('bbbb')

# tautaubb

g3 = ROOT.TGraph2D(len(x2),array('d',x2),array('d',y2),array('d',z3))

g3.SetTitle('H3#rightarrow H_{S}(#rightarrow bb) + h_{125}(#rightarrow #tau#tau); m(H3) [GeV]; m(H_{S}) [GeV]; #sigma #times BR [pb]')

g3.Write('tautaubb')

fout.Close()
