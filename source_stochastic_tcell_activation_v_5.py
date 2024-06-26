import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from math import e
import sdeint
from ipywidgets import *
from IPython.display import display
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import axes3d
import warnings
warnings.filterwarnings('ignore')

TbetL = []
GATA3L = []
BCL6L = []
RORGTL = []
FOXP3L = []

threshold = 0.2

DTCR = 1
DCD28 = 1
DAP1 = 1
DCD25 = 1
DIL2G = 1
DIL2E = 1
DMTOR = 1
DZAP70 = 1
DSTAT5 = 1
DNFAT = 1
DNFKB = 1
DAKT = 1
DBCL2 = 1
DNDRG1 = 1
DDAG = 1
DSOS = 1
DRASGTPR = 1
DLCK = 1
DPDK1 = 1
DLAT = 1
DPLC = 1
DPI3K = 1
DPIP2 = 1
DPIP3 = 1
DIP3 = 1
DCA = 1
DPKC = 1
DTBET = 1
DIFNG = 1
DGATA3 = 1
DIL4 = 1
DFOXP3 = 1
DIL10 = 1
DTGFB = 1
DRORGT = 1
DIL21 = 1
DIL17 = 1
DBCL6 =1
DIL6 = 1
DIL9 = 1
DCD40L = 1
DMTORC1 = 1
DMTORC2 = 1
DLKB1 = 1
DAMPK = 1
DGlycolysis = 1
DOXPHOS = 1
DAMPATPratio = 1
DHIF1A = 1
DGLUTAMINOLISIS = 1
DAKG = 1
DCTLA4 = 1
DCTLA4DIM = 1

def f(x, t, b, AttAnt, TAnt, AttCD8086, TCD8086, DCTLA4, DCTLA4DIM, IFNGE, IL12E, IL18E, IL33E, IL4E, TGFBE,
           IL10E, IL21E, IL6E, GLC, GLN, FA, TRP, O2, METF, RAPA, PRED, CS):

    TCR = x[0]
    CD28 = x[1]
    AP1 = x[2]
    CD25 = x[3]
    IL2G = x[4]
    IL2E = x[5]
    MTOR = x[6]
    ZAP70 = x[7]
    STAT5 = x[8]
    NFAT = x[9]
    NFKB = x[10]
    AKT = x[11]
    CTLA4 = x[12]
    CTLA4DIM = x[13]
    BCL2 = x[14]
    NDRG1 = x[15]
    DAG = x[16]
    SOS = x[17]
    RASGTPR = x[18]
    LCK = x[19]
    PDK1 = x[20]
    LAT = x[21]
    PLC = x[22]
    PI3K = x[23]
    PIP2 = x[24]
    PIP3 = x[25]
    IP3 = x[26]
    CA = x[27]
    PKC = x[28]
    TBET = x[29]
    IFNG = x[30]
    GATA3 = x[31]
    IL4 = x[32]
    FOXP3 = x[33]
    IL10 = x[34]
    TGFB = x[35]
    RORGT = x[36]
    IL21 = x[37]
    IL17 = x[38]
    BCL6 = x[39]
    IL9 = x[40]
    CD40L = x[41]
    MTORC1 = x[42]
    MTORC2 = x[43]
    LKB1 = x[44]
    AMPK = x[45]
    Glycolysis = x[46]
    OXPHOS = x[47]
    AMPATPratio = x[48]
    HIF1A = x[49]
    GLUTAMINOLISIS = x[50]
    AKG = x[51]

    S = (1 + e ** (+ 1 * (t - 20)))
    Antigen = AttAnt / (1 + e ** (+ 1 * (t - TAnt)))
    CD8086 = AttCD8086 / (1 + e ** (+ 1 * (t - TCD8086)))

    WTCR = Antigen * (1 - CTLA4DIM)
    WCD28 = CD8086 * (1 - CTLA4DIM)
    WAP1 = RASGTPR * (1 - PRED)
    WCD25 = IL2G * (1 - CTLA4DIM)
    WIL2G = NFAT * AP1 * (1 - NDRG1)
    WIL2E = IL2G
    WMTOR = (CD25 + AKT) - (CD25 * AKT)
    WZAP70 = (TCR * LCK) * (1 - CTLA4DIM) * (1 - PRED)
    WSTAT5 = CD25 * (1 - CTLA4DIM)
    WNFAT = (CA) * (1 - CS)
    WNFKB = PKC * (1 - PRED)
    WAKT = (((CD28) * (1 - CTLA4DIM)) + (PDK1)) - (((CD28) * (1 - CTLA4DIM)) * (PDK1))
    WCTLA4 = IL2G * ZAP70
    WCTLA4DIM = ((CTLA4 * CD8086) + (FOXP3 * TGFB)) - ((CTLA4 * CD8086) * (FOXP3 * TGFB))
    WBCL2 = AKT
    WNDRG1 = NFAT * (1 - AKT)
    WDAG = PLC * PIP2
    WSOS = CD28
    WRASGTPR = ((LAT * SOS * DAG) + (CD25 * DAG)) - ((LAT * SOS * DAG) * (CD25 * DAG))
    WLCK = TCR * (1 - CTLA4DIM)
    WPDK1 = (CD25 + CD28 + PIP3) - (CD25 * CD28) - (CD28 * PIP3) - (CD25 * PIP3) + (CD25 * CD28 * PIP3)
    WLAT = ZAP70
    WPLC = (ZAP70 + CD25) - (ZAP70 * CD25)
    WPI3K = (ZAP70 + CD25) - (ZAP70 * CD25)
    WPIP2 = (PI3K + PLC) - (PI3K * PLC)
    WPIP3 = PIP2
    WIP3 = PIP2 * PLC
    WCA = IP3
    WPKC = DAG
    WTBET = (IL33E * IL18E * IL12E * IL2E * IFNGE * MTORC1 * NFKB * NFAT * AP1 * TRP * AKG) * (1 - IL4) * (1 - IL10) * (1 - GATA3)
    WIFNG = (TBET * AP1 * NFAT) * (1 - GATA3)
    WGATA3 = (IL33E * IL4E * IL2E * MTORC2 * STAT5 * NFAT) * (1 - TBET) * (1 - TGFB) * (1 - IFNG) * (1 - BCL6)
    WIL4 = (GATA3) * (1 - TBET) * (1 - IFNG)
    WFOXP3 = (((TGFBE * IL10E * NFAT * STAT5 * AP1 * IL2E) + (TGFBE * IL10E * IL10 * CTLA4) + (TGFBE * TGFB)) - ((TGFBE * IL10E * NFAT * STAT5 * AP1 * IL2E) * (TGFBE * IL10E * IL10 * CTLA4)) - ((TGFBE * IL10E * IL10 * CTLA4) * (TGFBE * TGFB)) - ((TGFBE * IL10E * NFAT * STAT5 * AP1 * IL2E) * (TGFBE * TGFB)) + ((TGFBE * IL10E * NFAT * STAT5 * AP1 * IL2E) * (TGFBE * IL10E * IL10 * CTLA4) * (TGFBE * TGFB))) * (1 - IFNG) * (1 - HIF1A) * (1 - IL6E)
    WIL10 = TGFBE * FOXP3
    WTGFB = FOXP3
    WRORGT = (((IL6E * IL21E * TGFBE * AP1 * MTORC1 * TRP) + (IL21E * TGFBE * AP1 * MTORC1 * AKG) + (HIF1A)) - ((IL6E * IL21E * TGFBE * AP1 * MTORC1 * TRP) * (IL21E * TGFBE * AP1 * MTORC1 * AKG)) - ((IL21E * TGFBE * AP1 * MTORC1 * AKG) * (HIF1A)) - ((IL6E * IL21E * TGFBE * AP1 * MTORC1 * TRP) * (HIF1A)) + ((IL6E * IL21E * TGFBE * AP1 * MTORC1 * TRP) * (IL21E * TGFBE * AP1 * MTORC1 * AKG) * (HIF1A))) * (1 - TBET) * (1 - FOXP3) * (1 - GATA3)
    WIL21 = (((IL21E * RORGT) + (IL6E * BCL6)) - ((IL21E * RORGT) * (IL6E * BCL6))) * (1 - IFNG) * (1 - IL4) * (1 - IL10)
    WIL17 = RORGT
    WBCL6 = (IL6E * IL21E * AP1 * MTORC1) * (1 - RORGT) * (1 - TBET) * (1 - GATA3)
    WIL9 = BCL6
    WCD40L = BCL6
    WMTORC1 = (((MTOR * AKT) + (MTOR * AKG)) - ((MTOR * AKT) * (MTOR * AKG))) * (1 - AMPK) * (1 - RAPA)
    WMTORC2 = ((MTOR * AMPK) + (MTOR * IL4E)) - ((MTOR * AMPK) * (MTOR * IL4E))
    WLKB1 = (AKT * AMPATPratio)
    WAMPK = (LKB1 * (1 - MTORC1) + CA * AMPATPratio * (1 - MTORC1) + AKT * AMPATPratio * (1 - MTORC1) + FOXP3 + BCL6 + METF) - ((LKB1 * (1 - MTORC1) * CA * AMPATPratio * (1 - MTORC1)) - (LKB1 * (1 - MTORC1) * AKT * AMPATPratio * (1 - MTORC1)) - (LKB1 * (1 - MTORC1) * FOXP3) - (LKB1 * (1 - MTORC1) * BCL6) - (LKB1 * (1 - MTORC1) * METF) - (CA * AMPATPratio * (1 - MTORC1) * AKT * AMPATPratio * (1 - MTORC1)) - (CA * AMPATPratio * (1 - MTORC1) * FOXP3) - (CA * AMPATPratio * (1 - MTORC1) * BCL6) - (CA * AMPATPratio * (1 - MTORC1) * METF) - (AKT * AMPATPratio * (1 - MTORC1) * FOXP3) - (AKT * AMPATPratio * (1 - MTORC1) * BCL6) - (AKT * AMPATPratio * (1 - MTORC1) * METF) - (FOXP3 * BCL6) - (FOXP3 * METF) - (BCL6 * METF)) + ((LKB1 * (1 - MTORC1) * CA * AMPATPratio * (1 - MTORC1) * AKT * AMPATPratio * (1 - MTORC1)) + (LKB1 * (1 - MTORC1) * CA * AMPATPratio * (1 - MTORC1) * FOXP3) + (LKB1 * (1 - MTORC1) * CA * AMPATPratio * (1 - MTORC1) * BCL6) + (LKB1 * (1 - MTORC1) * CA * AMPATPratio * (1 - MTORC1) * METF) + (CA * AMPATPratio * (1 - MTORC1) * AKT * AMPATPratio * (1 - MTORC1) * FOXP3) + (CA * AMPATPratio * (1 - MTORC1) * AKT * AMPATPratio * (1 - MTORC1) * BCL6) + (CA * AMPATPratio * (1 - MTORC1) * AKT * AMPATPratio * (1 - MTORC1) * METF) + (AKT * AMPATPratio * (1 - MTORC1) * FOXP3 * BCL6) + (AKT * AMPATPratio * (1 - MTORC1) * FOXP3 * METF) + (FOXP3 * BCL6 * METF)) - ((LKB1 * (1 - MTORC1) * CA * AMPATPratio * (1 - MTORC1) * AKT * AMPATPratio * (1 - MTORC1) * FOXP3) - (LKB1 * (1 - MTORC1) * AKT * AMPATPratio * (1 - MTORC1) * FOXP3 * BCL6) - (LKB1 * (1 - MTORC1) * FOXP3 * BCL6 * METF) - (CA * AMPATPratio * (1 - MTORC1) * AKT * AMPATPratio * (1 - MTORC1) * FOXP3 * BCL6) - (CA * AMPATPratio * (1 - MTORC1) * FOXP3 * BCL6 * METF) - (AKT * AMPATPratio * (1 - MTORC1) * FOXP3 * BCL6 * METF)) + ((LKB1 * (1 - MTORC1) * CA * AMPATPratio * (1 - MTORC1) * AKT * AMPATPratio * (1 - MTORC1) * FOXP3 * BCL6) + (LKB1 * (1 - MTORC1) * AKT * AMPATPratio * (1 - MTORC1) * FOXP3 * BCL6 * METF) + (CA * AMPATPratio * (1 - MTORC1) * AKT * AMPATPratio * (1 - MTORC1) * FOXP3 * BCL6 * METF)) - (LKB1 * (1 - MTORC1) * CA * AMPATPratio * (1 - MTORC1) * AKT * AMPATPratio * (1 - MTORC1) * FOXP3 * BCL6 * METF)
    WGlycolysis = ((((MTORC1 * GLC) + (HIF1A * GLC)) - ((MTORC1 * GLC) * (HIF1A * GLC))) * (1 -AMPATPratio) * (1 - BCL6))
    WGLUTAMINOLISIS = GLN
    WAKG = GLUTAMINOLISIS
    WOXPHOS = AMPK * FA
    WAMPATPratio = Glycolysis * (1 - OXPHOS)
    WHIF1A = (1-O2) * AKT

    dTCRdt = 1 / (1 + e ** (-b * (WTCR - .5))) - DTCR * TCR
    dCD28dt = 1 / (1 + e ** (-b * (WCD28 - .5))) - DCD28 * CD28
    dAP1dt = 1 / (1 + e ** (-b * (WAP1 - .5))) - DAP1 * AP1
    dCD25dt = 1 / (1 + e ** (-b * (WCD25 - .5))) - DCD25 * CD25
    dIL2Gdt = 1 / (1 + e ** (-b * (WIL2G - .5))) - DIL2G * IL2G
    dIL2Edt = 1 / (1 + e ** (-b * (WIL2E - .5))) - DIL2E * IL2E
    dMTORdt = 1 / (1 + e ** (-b * (WMTOR - .5))) - DMTOR * MTOR
    dZAP70dt = 1 / (1 + e ** (-b * (WZAP70 - .5))) - DZAP70 * ZAP70
    dSTAT5dt = 1 / (1 + e ** (-b * (WSTAT5 - .5))) - DSTAT5 * STAT5
    dNFATdt = 1 / (1 + e ** (-b * (WNFAT - .5))) - DNFAT * NFAT
    dNFKBdt = 1 / (1 + e ** (-b * (WNFKB - .5))) - DNFKB * NFKB
    dAKTdt = 1 / (1 + e ** (-b * (WAKT - .5))) - DAKT * AKT
    dCTLA4dt = 1 / (1 + e ** (-b * (WCTLA4 - .5))) - DCTLA4 * CTLA4
    dCTLA4DIMdt = 1 / (1 + e ** (-b * (WCTLA4DIM - .5))) - DCTLA4DIM * CTLA4DIM
    dBCL2dt = 1 / (1 + e ** (-b * (WBCL2 - .5))) - DBCL2 * BCL2
    dNDRG1dt = 1 / (1 + e ** (-b * (WNDRG1 - .5))) - DNDRG1 * NDRG1
    dDAGdt = 1 / (1 + e ** (-b * (WDAG - .5))) - DDAG * DAG
    dSOSdt = 1 / (1 + e ** (-b * (WSOS - .5))) - DSOS * SOS
    dRASGTPRdt = 1 / (1 + e ** (-b * (WRASGTPR - .5))) - DRASGTPR * RASGTPR
    dLCKdt = 1 / (1 + e ** (-b * (WLCK - .5))) - DLCK * LCK
    dPDK1dt = 1 / (1 + e ** (-b * (WPDK1 - .5))) - DPDK1 * PDK1
    dLATdt = 1 / (1 + e ** (-b * (WLAT - .5))) - DLAT * LAT
    dPLCdt = 1 / (1 + e ** (-b * (WPLC - .5))) - DPLC * PLC
    dPI3Kdt = 1 / (1 + e ** (-b * (WPI3K - .5))) - DPI3K * PI3K
    dPIP2dt = 1 / (1 + e ** (-b * (WPIP2 - .5))) - DPIP2 * PIP2
    dPIP3dt = 1 / (1 + e ** (-b * (WPIP3 - .5))) - DPIP3 * PIP3
    dIP3dt = 1 / (1 + e ** (-b * (WIP3 - .5))) - DIP3 * IP3
    dCAdt = 1 / (1 + e ** (-b * (WCA - .5))) - DCA * CA
    dPKCdt = 1 / (1 + e ** (-b * (WPKC - .5))) - DPKC * PKC
    dTBETdt = 1 / (1 + e ** (-b * (WTBET - .5))) - DTBET * TBET
    dIFNGdt = 1 / (1 + e ** (-b * (WIFNG - .5))) - DIFNG * IFNG
    dGATA3dt = 1 / (1 + e ** (-b * (WGATA3 - .5))) - DGATA3 * GATA3
    dIL4dt = 1 / (1 + e ** (-b * (WIL4 - .5))) - DIL4 * IL4
    dFOXP3dt = 1 / (1 + e ** (-b * (WFOXP3 - .5))) - DFOXP3 * FOXP3
    dIL10dt = 1 / (1 + e ** (-b * (WIL10 - .5))) - DIL10 * IL10
    dTGFBdt = 1 / (1 + e ** (-b * (WTGFB - .5))) - DTGFB * TGFB
    dRORGTdt = 1 / (1 + e ** (-b * (WRORGT - .5))) - DRORGT * RORGT
    dIL21dt = 1 / (1 + e ** (-b * (WIL21 - .5))) - DIL21 * IL21
    dIL17dt = 1 / (1 + e ** (-b * (WIL17 - .5))) - DIL17 * IL17
    dBCL6dt = 1 / (1 + e ** (-b * (WBCL6 - .5))) - DBCL6 * BCL6
    dIL9dt = 1 / (1 + e ** (-b * (WIL9 - .5))) - DIL9 * IL9
    dCD40Ldt = 1 / (1 + e ** (-b * (WCD40L - .5))) - DCD40L * CD40L
    dMTORC1dt = 1 / (1 + e ** (-b * (WMTORC1 - .5))) - DMTORC1 * MTORC1
    dMTORC2dt = 1 / (1 + e ** (-b * (WMTORC2 - .5))) - DMTORC2 * MTORC2
    dLKB1dt = 1 / (1 + e ** (-b * (WLKB1 - .5))) - DLKB1 * LKB1
    dAMPKdt = 1 / (1 + e ** (-b * (WAMPK - .5))) - DAMPK * AMPK
    dGlycolysisdt = 1 / (1 + e ** (-b * (WGlycolysis - .5))) - DGlycolysis * Glycolysis
    dOXPHOSdt = 1 / (1 + e ** (-b * (WOXPHOS - .5))) - DOXPHOS * OXPHOS
    dAMPATPratiodt = 1 / (1 + e ** (-b * (WAMPATPratio - .5))) - DAMPATPratio * AMPATPratio
    dHIF1Adt = 1 / (1 + e ** (-b * (WHIF1A - .5))) - DHIF1A * HIF1A
    dGLUTAMINOLISISdt = 1 / (1 + e ** (-b * (WGLUTAMINOLISIS - .5))) - DGLUTAMINOLISIS * GLUTAMINOLISIS
    dAKGdt = 1 / (1 + e ** (-b * (WAKG - .5))) - DAKG * AKG

    return np.array([dTCRdt, dCD28dt, dAP1dt, dCD25dt, dIL2Gdt, dIL2Edt, dMTORdt, dZAP70dt, dSTAT5dt, dNFATdt, dNFKBdt, dAKTdt, dCTLA4dt,
            dCTLA4DIMdt, dBCL2dt, dNDRG1dt, dDAGdt, dSOSdt, dRASGTPRdt, dLCKdt, dPDK1dt,  dLATdt,
            dPLCdt, dPI3Kdt, dPIP2dt, dPIP3dt, dIP3dt, dCAdt, dPKCdt, dTBETdt, dIFNGdt, dGATA3dt, dIL4dt, dFOXP3dt, dIL10dt, dTGFBdt,
            dRORGTdt, dIL21dt, dIL17dt, dBCL6dt, dIL9dt, dCD40Ldt, dMTORC1dt, dMTORC2dt, dLKB1dt, dAMPKdt, dGlycolysisdt, dOXPHOSdt, dAMPATPratiodt, dHIF1Adt,
            dGLUTAMINOLISISdt, dAKGdt])

t = np.linspace(0, 30, 1000)
x0 = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0.2, 0, 0, 0, 0])

#def GG(y, t):
    #return np.diag([0.30, 0.30, 0.30, 0.30, 0.30, 0.30, 0.30, 0.30, 0.30, 0.30, 0.30, 0.30, 0.30, 0.30, 0.30, 0.30, 0.30, 0.30, 0.30, 0.30,
                    #0.30, 0.30, 0.30, 0.30, 0.30, 0.30, 0.30, 0.30, 0.30, 0.30, 0.30, 0.30, 0.30, 0.30, 0.30, 0.30, 0.30, 0.30, 0.30, 0.30,
                    #0.30, 0.30, 0.30, 0.30, 0.30, 0.30, 0.30, 0.30, 0.30, 0.30, 0.30, 0.30])

#def GG(y, t):
    #return np.diag([0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25,
                    #0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25,
                    #0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25])

#def GG(y, t):
    #return np.diag([0.20, 0.20, 0.20, 0.20, 0.20, 0.20, 0.20, 0.20, 0.20, 0.20, 0.20, 0.20, 0.20, 0.20, 0.20, 0.20, 0.20, 0.20, 0.20, 0.20,
                    #0.20, 0.20, 0.20, 0.20, 0.20, 0.20, 0.20, 0.20, 0.20, 0.20, 0.20, 0.20, 0.20, 0.20, 0.20, 0.20, 0.20, 0.20, 0.20, 0.20,
                    #0.20, 0.20, 0.20, 0.20, 0.20, 0.20, 0.20, 0.20, 0.20, 0.20, 0.20, 0.20])

#def GG(y, t):
    #return np.diag([0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15,
                    #0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15,
                    #0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15, 0.15])

#def GG(y, t):
    #return np.diag([0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1,
                    #0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1,
                    #0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1])


#def GG(y, t):
    #return np.diag([0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05,
                    #0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05,
                    #0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05])

def GG(y, t):
    return np.diag([0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
                    0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03,
                    0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03])

def fmain (b = 10, AttAnt = 1, TAnt = 15, AttCD8086 = 1, TCD8086 = 15, DCTLA4 = 1, DCTLA4DIM = 1, IFNGE = 0, IL12E = 0, IL18E = 0, IL33E = 0, IL4E = 0, TGFBE=0,
           IL10E = 0, IL21E = 0, IL6E = 0, GLC = 1, GLN = 1, FA = 1, TRP = 1, O2 = 1, METF = 0, RAPA = 0, PRED = 0, CS = 0):

  fig, ((ax1, ax2, ax3, ax4, ax5), (ax6, ax7, ax8, ax9, ax10)) = plt.subplots(2, 5, figsize = (16, 6), gridspec_kw={'height_ratios': [2, 2]})
  fig.subplots_adjust(left=0.2, wspace=0.5, hspace=1.2)
  fig.text(0.5, 0.05, 'Time', ha='center', fontsize=12)
  fig.text(0.15, 0.5, 'Activity level', va='center', rotation='vertical', fontsize=12)

  TbetL.clear()
  GATA3L.clear()
  BCL6L.clear()
  RORGTL.clear()
  FOXP3L.clear()

  reps = 10
  args = (b, AttAnt, TAnt, AttCD8086, TCD8086, DCTLA4, DCTLA4DIM, IFNGE, IL12E, IL18E, IL33E, IL4E, TGFBE, IL10E, IL21E, IL6E, GLC, GLN,
                                  FA, TRP, O2, METF, RAPA, PRED, CS)

  def close(func, *args):
    def newfunc(x, t):
        return func(x, t, *args)
    return newfunc

  for _ in range(reps):
    x = sdeint.itoint(close(f, *args), GG, x0, t)

    TCR = x[:, 0]
    CD28 = x[:, 1]
    AP1 = x[:, 2]
    CD25 = x[:, 3]
    IL2G = x[:, 4]
    IL2E = x[:, 5]
    MTOR = x[:, 6]
    ZAP70 = x[:, 7]
    STAT5 = x[:, 8]
    NFAT = x[:, 9]
    NFKB = x[:, 10]
    AKT = x[:, 11]
    CTLA4 = x[:, 12]
    CTLA4DIM = x[:, 13]
    BCL2 = x[:, 14]
    NDRG1 = x[:, 15]
    DAG = x[:, 16]
    SOS = x[:, 17]
    RASGTPR = x[:, 18]
    LCK = x[:, 19]
    PDK1 = x[:, 20]
    LAT = x[:, 21]
    PLC = x[:, 22]
    PI3K = x[:, 23]
    PIP2 = x[:, 24]
    PIP3 = x[:, 25]
    IP3 = x[:, 26]
    CA = x[:, 27]
    PKC = x[:, 28]
    TBET = x[:, 29]
    IFNG = x[:, 30]
    GATA3 = x[:, 31]
    IL4 = x[:, 32]
    FOXP3 = x[:, 33]
    IL10 = x[:, 34]
    TGFB = x[:, 35]
    RORGT = x[:, 36]
    IL21 = x[:, 37]
    IL17 = x[:, 38]
    BCL6 = x[:, 39]
    IL9 = x[:, 40]
    CD40L = x[:, 41]
    MTORC1 = x[:, 42]
    MTORC2 = x[:, 43]
    LKB1 = x[:, 44]
    AMPK = x[:, 45]
    Glycolysis = x[:, 46]
    OXPHOS = x[:, 47]
    AMPATPratio = x[:, 48]
    HIF1A = x[:, 49]
    GLUTAMINOLISIS = x[:, 50]
    AKG = x[:, 51]

    TbetL.append(TBET[-1])
    above_thresholdtbet = [i for i in TbetL if i > threshold]
    ptbet = (len(above_thresholdtbet)) / (len(TbetL)) * 100

    GATA3L.append(GATA3[-1])
    above_thresholdgata3 = [i for i in GATA3L if i > threshold]
    pgata3 = len(above_thresholdgata3) / len(GATA3L) * 100

    BCL6L.append(BCL6[-1])
    above_thresholdbcl6 = [i for i in BCL6L if i > threshold]
    pbcl6 = len(above_thresholdbcl6) / len(BCL6L) * 100

    RORGTL.append(RORGT[-1])
    above_thresholdrorgt = [i for i in RORGTL if i > threshold]
    prorgt = len(above_thresholdrorgt) / len(RORGTL) * 100

    FOXP3L.append(FOXP3[-1])
    above_thresholdfoxp3 = [i for i in FOXP3L if i > threshold]
    pfoxp3 = len(above_thresholdfoxp3) / len(FOXP3L) * 100

    ax1.plot('Th1', TBET[-1], 'lawngreen', marker="_", markersize=10, linestyle="")
    #ax1.plot('TH1', IFNG[-1],'lawngreen', marker="_",  markersize=10, linestyle="")
    ax1.plot('Th2', GATA3[-1], 'blueviolet', marker="_", markersize=10, linestyle="")
    #ax1.plot('TH2', IL4[-1], 'blueviolet', marker="_", markersize=10, linestyle="")
    ax1.plot('Th17', RORGT[-1], 'tab:cyan', marker="_", markersize=10, linestyle="")
    #ax1.plot('TH17', IL17[-1],  'tab:cyan',marker="_", markersize=10, linestyle="")
    #ax1.plot('TH17', IL21[-1], 'tab:cyan', marker="_", markersize=10, linestyle="")
    ax1.plot('Treg', FOXP3[-1], 'tab:red', marker="_", markersize=10, linestyle="")
    #ax1.plot('Treg', TGFB[-1], 'tab:red',marker="_", markersize=10, linestyle="")
    ax1.plot('Tfh', BCL6[-1], 'grey', marker="_", markersize=10, linestyle="")
    #ax1.plot('TFH', IL9[-1], 'grey', marker="_", markersize=10, linestyle="")
    #ax1.set_ylabel('Activity level', fontsize=10)
    ax1.tick_params(axis='x', labelsize=9)
    ax1.tick_params(axis='y', labelsize=9)
    ax1.legend([f"Th1   = {ptbet}%", f"Th2   = {pgata3}%", f"Th17 = {prorgt}%", f"Treg  = {pfoxp3}%", f"Tfh    = {pbcl6}%"], bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=1, mode="expand", borderaxespad=0., prop={'size': 8})
    ax1.set_ylim(0, 1.1)
    ax1.text(-0.2, 1.80, "A) Phenotype population", fontfamily='DejaVu Sans', fontsize=9, fontstyle='normal')
    ax1.axhline(0.2, color = 'black', ls='--', linewidth=0.5, label='Event')

    ax2.plot(t, TCR, 'lawngreen', linestyle = '-', linewidth=1, label='TCR')
    ax2.plot(t, CD28, 'blueviolet', linestyle = ':', linewidth=1, label='CD28')
    ax2.plot(t, CTLA4, 'tab:cyan', linestyle = '--', linewidth=1, label='CTLA4')
    ax2.plot(t, NDRG1, 'tab:red', linestyle = '-.', linewidth=1, label='NDRG1')
    ax2.tick_params(axis='x', labelsize=9)
    ax2.tick_params(axis='y', labelsize=9)
    ax2.legend(['TCR', 'CD28', 'CTLA4', 'NDRG1'], bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=1, mode="expand", borderaxespad=0., prop={'size': 8})
    ax2.set_ylim(0, 1.1)
    ax2.set_xlim(-0.5, 30.5)
    ax2.text(0.0, 1.80, "B) Antigen presentation", fontfamily='DejaVu Sans', fontsize=9, fontstyle='normal')

    ax3.plot(t, Glycolysis, 'lawngreen', linestyle = '-', linewidth=1, label='Glycolysis')
    ax3.plot(t, OXPHOS, 'blueviolet', linestyle = ':', linewidth=1, label='OXPHOS')
    ax3.plot(t, AMPATPratio, 'tab:cyan', linestyle = '--', linewidth=1, label='AMPATPratio')
    ax3.plot(t, AMPK, 'tab:red', linestyle = '-.', linewidth=1, label='AMPK')
    ax3.tick_params(axis='x', labelsize=9)
    ax3.tick_params(axis='y', labelsize=9)
    ax3.legend(['Glycolysis', 'OXPHOS', 'AMP/ATP ratio', 'AMPK'], bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=1, mode="expand", borderaxespad=0., prop={'size': 8})
    ax3.set_ylim(0, 1.1)
    ax3.set_xlim(-0.5, 30.5)
    ax3.text(0.0, 1.80, "C) Metabolism", fontfamily='DejaVu Sans', fontsize=9, fontstyle='normal')

    ax4.plot(t, AP1, 'lawngreen', linestyle = '-', linewidth=1, label='AP1')
    ax4.plot(t, NFAT, 'blueviolet', linestyle = ':', linewidth=1, label='NFAT')
    ax4.plot(t, NFKB, 'tab:cyan', linestyle = '--', linewidth=1, label='NFKB')
    ax4.tick_params(axis='x', labelsize=9)
    ax4.tick_params(axis='y', labelsize=9)
    ax4.legend(['AP1', 'NFAT', 'NFKB'], bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=1, mode="expand", borderaxespad=0., prop={'size': 8})
    ax4.set_ylim(0, 1.1)
    ax4.set_xlim(-0.5, 30.5)
    ax4.text(0.0, 1.80, "D) Transcription factors", fontfamily='DejaVu Sans', fontsize=9, fontstyle='normal')

    ax5.plot(t, IL2G, 'lawngreen', linestyle = '-', linewidth=1, label='IL2G')
    ax5.plot(t, MTORC1, 'blueviolet', linestyle = ':', linewidth=1, label='MTORC1')
    ax5.plot(t, MTORC2, 'tab:cyan', linestyle = '--', linewidth=1, label='MTORC2')
    ax5.tick_params(axis='x', labelsize=9)
    ax5.tick_params(axis='y', labelsize=9)
    ax5.legend(['IL2G', 'MTORC1', 'MTORC2'], bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=1, mode="expand", borderaxespad=0., prop={'size': 8})
    ax5.set_ylim(0, 1.1)
    ax5.set_xlim(-0.5, 30.5)
    ax5.text(0.0, 1.80, "E) Activation markers", fontfamily='DejaVu Sans', fontsize=9, fontstyle='normal')

    ax6.plot(t, TBET, 'lawngreen', linestyle = '-', linewidth=1, label='TBET')
    ax6.plot(t, IFNG, 'blueviolet', linestyle = ':', linewidth=1, label='IFNG')
    ax6.tick_params(axis='x', labelsize=9)
    ax6.tick_params(axis='y', labelsize=9)
    ax6.legend(['TBET', 'IFNG'], bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=1, mode="expand", borderaxespad=0., prop={'size': 8})
    ax6.set_ylim(0, 1.1)
    ax6.set_xlim(-0.5, 30.5)
    ax6.text(0.0, 1.80, "F) Th1", fontfamily='DejaVu Sans', fontsize=9, fontstyle='normal')

    ax7.plot(t, GATA3, 'lawngreen', linestyle = '-', linewidth=1, label='GATA3')
    ax7.plot(t,  IL4, 'blueviolet', linestyle = ':', linewidth=1, label='IL4')
    ax7.tick_params(axis='x', labelsize=9)
    ax7.tick_params(axis='y', labelsize=9)
    ax7.legend(['GATA3', 'IL4'], bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=1, mode="expand", borderaxespad=0., prop={'size': 7})
    ax7.set_ylim(0, 1.1)
    ax7.set_xlim(-0.5, 30.5)
    ax7.text(0.0, 1.80, "G) Th2", fontfamily='DejaVu Sans', fontsize=9, fontstyle='normal')

    ax8.plot(t, IL17, 'lawngreen', linestyle = '-', linewidth=1, label='IL17')
    ax8.plot(t, IL21, 'blueviolet', linestyle = ':', linewidth=1, label='I21')
    ax8.plot(t, RORGT, 'tab:cyan', linestyle = '--', linewidth=1, label='RORGT')
    ax8.tick_params(axis='x', labelsize=9)
    ax8.tick_params(axis='y', labelsize=9)
    ax8.legend(['IL17', 'II21', 'RORGT'], bbox_to_anchor=(0., 1.02, 1., .102), loc=4, ncol=1, mode="expand", borderaxespad=0., prop={'size': 8})
    ax8.set_ylim(0, 1.1)
    ax8.set_xlim(-0.5, 30.5)
    ax8.text(0.0, 1.80, "H) Th17", fontfamily='DejaVu Sans', fontsize=9, fontstyle='normal')

    ax9.plot(t, FOXP3, 'lawngreen', linestyle = '-', linewidth=1, label='FOXP3')
    ax9.plot(t, TGFB, 'blueviolet', linestyle = ':', linewidth=1, label='TGFB')
    ax9.plot(t, CTLA4DIM, 'tab:cyan', linestyle = '--', linewidth=1, label='CTLA4DIM')
    ax9.tick_params(axis='x', labelsize=9)
    ax9.tick_params(axis='y', labelsize=9)
    ax9.legend(['FOXP3', 'TGFB', 'CTLA4DIM'], bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=1, mode="expand", borderaxespad=0., prop={'size': 8})
    ax9.set_ylim(0, 1.1)
    ax9.set_xlim(-0.5, 30.5)
    ax9.text(0.0, 1.80, "I) Treg", fontfamily='DejaVu Sans', fontsize=9, fontstyle='normal')

    ax10.plot(t, BCL6, 'lawngreen', linestyle = '-', linewidth=1, label='BCL6')
    ax10.plot(t, IL21, 'blueviolet', linestyle = ':', linewidth=1, label='IL21')
    ax10.plot(t, CD40L, 'tab:cyan', linestyle = '--', linewidth=1, label='CD40L')
    ax10.plot(t, IL9, 'tab:red', linestyle = '-.', linewidth=1, label='IL9')
    ax10.tick_params(axis='x', labelsize=9)
    ax10.tick_params(axis='y', labelsize=9)
    ax10.legend(['BCL6', 'IL21', 'CD40L', 'IL9' ], fontsize=6, bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=1, mode="expand", borderaxespad=0., prop={'size': 8})
    ax10.set_ylim(0, 1.1)
    ax10.set_xlim(-0.5, 30.5)
    ax10.text(0.0, 1.80, "J) Tfh", fontfamily='DejaVu Sans', fontsize=9, fontstyle='normal')

  plt.savefig("main.pdf", bbox_inches='tight')
  plt.show(fig)

b = widgets.FloatSlider(value = 10.0, max = 100, step = 1, description = 'b:')
AttAnt = widgets.FloatSlider(value = 1.0, max = 1, step = 0.001, description = 'AttAnt:')
TAnt = widgets.FloatSlider(value = 15.0, max = 100, step = 1, description = 'TAnt:')
AttCD8086 = widgets.FloatSlider(value = 1.0, max = 1, step = 0.001, description = 'AttCD8086:')
TCD8086 = widgets.FloatSlider(value = 15.0, max = 100, step = 1, description = 'TCD8086:')
DCTLA4 = widgets.FloatSlider(value = 1.0, max = 1.0, step = 0.001, description = 'CTLA4 D:')
DCTLA4DIM = widgets.FloatSlider(value = 1.0, max = 1.0, step = 0.001, description = 'CTLA4DIM D:')
IFNGE = widgets.FloatSlider(value = 0.0, max = 1.0, step = 0.001, description = 'Ext IFNγ:')
IL12E = widgets.FloatSlider(value = 0.0, max = 1.0, step = 0.001, description = 'Ext IL-12:')
IL18E = widgets.FloatSlider(value = 0.0, max = 1.0, step = 0.001, description = 'Ext IL-18:')
IL33E = widgets.FloatSlider(value = 0.0, max = 1.0, step = 0.001, description = 'Ext IL-33:')
IL4E = widgets.FloatSlider(value = 0.0, max = 1.0, step = 0.001, description = 'Ext IL-4:')
TGFBE = widgets.FloatSlider(value = 0.0, max = 1.0, step = 0.001, description = 'Ext TGFβ:')
IL10E = widgets.FloatSlider(value = 0.0, max = 1.0, step = 0.001, description = 'Ext IL-10:')
IL21E = widgets.FloatSlider(value = 0.0, max = 1.0, step = 0.001, description = 'Ext IL-21:')
IL6E = widgets.FloatSlider(value = 0.0, max = 1.0, step = 0.001, description = 'Ext IL-6:')
GLC = widgets.FloatSlider(value = 1.0, max = 1.0, step = 0.001, description = 'Glucose:')
GLN = widgets.FloatSlider(value = 1.0, max = 1.0, step = 0.001, description = 'Glutamine:')
FA = widgets.FloatSlider(value = 1.0, max = 1.0, step = 0.001, description = 'Fatty acids:')
TRP = widgets.FloatSlider(value = 1.0, max = 1.0, step = 0.001, description = 'Tryptophan:')
O2 = widgets.FloatSlider(value = 1.0, max = 1.0, step = 0.001, description = 'O2:')
METF = widgets.FloatSlider(value = 0.0, max = 1.0, step = 0.001, description = 'METF:')
RAPA = widgets.FloatSlider(value = 0.0, max = 1.0, step = 0.001, description = 'RAPA:')
PRED = widgets.FloatSlider(value = 0.0, max = 1.0, step = 0.001, description = 'PRED:')
CS = widgets.FloatSlider(value = 0.0, max = 1.0, step = 0.001, description = 'CS:')
ui = VBox([b, AttAnt, TAnt, AttCD8086, TCD8086, DCTLA4, DCTLA4DIM, IFNGE, IL12E, IL18E, IL33E, IL4E, TGFBE, IL10E, IL21E, IL6E, GLC, GLN, FA, TRP, O2, METF,
         RAPA, PRED, CS])

graphicz = interactive_output(fmain, {'b':b, 'AttAnt':AttAnt, 'TAnt':TAnt, 'AttCD8086':AttCD8086, 'TCD8086':TCD8086, 'DCTLA4':DCTLA4, 'DCTLA4DIM':DCTLA4DIM,
                                      'IFNGE':IFNGE, 'IL12E':IL12E, 'IL18E':IL18E, 'IL33E':IL33E, 'IL4E':IL4E, 'TGFBE':TGFBE, 'IL10E':IL10E, 'IL21E':IL21E,
                                      'IL6E':IL6E, 'GLC':GLC, 'GLN':GLN, 'FA':FA, 'TRP':TRP, 'O2':O2, 'METF':METF, 'RAPA':RAPA, 'PRED':PRED, 'CS':CS})

display(HBox([ui,graphicz]))
