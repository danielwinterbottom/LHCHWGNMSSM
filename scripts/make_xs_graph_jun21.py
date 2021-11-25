######################################

# Store X->Yh maximum cross sections provided by Ulrich Ellwanger in Jun21 as TGraph2D
# These values correspond to additional H3->Hs(->bb)+h125(->tautau) numbers that were used to produce 2D "exclusion" regions in CMS_HIG-20-014 
# Sent by mail from Ulrich Ellwanger -> NMSSM conveners + CMS_HIG-20-014 authors on 04/06/21

######################################

import ROOT
from array import array

fout = ROOT.TFile('output/HXSG_NMSSM_recommendations_Jun21.root','RECREATE')

x = [400.,400.,450.,450.,500.,500.,550.,550.,600.,600.]
y = [190.,250.,190.,250.,250.,300.,190.,250.,150.,170.]
z = [0.2870E-01,0.8118E-02,0.2278E-01,0.1722E-01,0.1217E-01,0.7850E-02,0.9352E-02,0.7609E-02,0.004257,0.5056E-02]

g = ROOT.TGraph2D(len(x),array('d',x),array('d',y),array('d',z))

g.SetTitle('H3#rightarrow H_{S}(#rightarrow bb) + h_{125}(#rightarrow#tau#tau); m(H3) [GeV]; m(H_{S}) [GeV]; #sigma #times BR [pb]')

g.Write('tautaubb')

fout.Close()

