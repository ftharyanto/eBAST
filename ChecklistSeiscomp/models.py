from django.db import models

seismograph_list = ['ACBM', 'ALTI', 'AAFM', 'AAI', 'AAII', 'ABJI', 'ABSM', 'ACJM', 'ALKI', 'AMPM', 'APSI', 'ARMI', 'ARPI', 'ATNI', 'BAJI', 'BAKI', 'BASI', 'BATI', 'BBBCM', 'BBCI', 'BBCM', 'BBJI', 'BBJM', 'BBSI', 'BDBI', 'BDCM', 'BESI', 'BESM', 'BGCI', 'BGCM', 'BHCM', 'BKB', 'BKJI', 'BKNI', 'BKSI', 'BLCM', 'BLJI', 'BLSM', 'BMBNG', 'BMSI', 'BNDI', 'BNSI', 'BNTI', 'BOJI', 'BOSM', 'BPMJM', 'BPSM', 'BSI', 'BSMI', 'BSSI', 'BTCM', 'BTJI', 'BUJI', 'BUKI', 'BUSI', 'BWJI', 'BYJI', 'BYLI', 'CASI', 'CBJI', 'CBJM', 'CCJM', 'CGJI', 'CIJI', 'CIJM', 'CMJI', 'CNJI', 'CSJI', 'CSJM', 'CTJI', 'CWJM', 'DBJI', 'DBKI', 'DBNFM', 'DDSI', 'DNP', 'DOCM', 'DYPI', 'EDFI', 'EGSI', 'ESNI', 'ERPI', 'FAKI', 'FKMPM', 'GBJI', 'GEJI', 'GENI', 'GESM', 'GGJM', 'GHMI', 'GKJM', 'GMJI', 'GPSM', 'GRJI', 'GSI', 'GTJI', 'GTOI', 'GTSI', 'GUJM', 'IATSM', 'IBTI', 'IGBI', 'IHMI', 'IHRSI', 'IWPI', 'JAGI', 'JASI', 'JAY', 'JBJI', 'JBJM', 'JCJI', 'JHMI', 'JMSI', 'JPJI', 'JPSI', 'JSBFM', 'JTJM', 'JWJM', 'KAPI', 'KBBI', 'KBJM', 'KBKI', 'KDI', 'KGCM', 'KHK', 'KJCM', 'KKKI', 'KKMI', 'KKSI', 'KLI', 'KLJI', 'KLNI', 'KLSI', 'KLSM', 'KMBFM', 'KMMI', 'KMNI', 'KMPI', 'KMSI', 'KPJI', 'KPJM', 'KRAI', 'KRJI', 'KRSI', 'KSI', 'KTMI', 'KTTI', 'KUKI', 'KUSI', 'KWJI', 'LASI', 'LBFI', 'LBNFM', 'LDSI', 'LEM', 'LESM', 'LHMI', 'LHSM', 'LISM', 'LJPI', 'LKCI', 'LKSM', 'LKUCM', 'LLSI', 'LLSM', 'LMNI', 'LMTI', 'LOCM', 'LPCM', 'LPSM', 'LRTI', 'LSCM', 'LSNI', 'LTNI', 'LTSM', 'LUCM', 'LUJI', 'LUWI', 'MASM', 'MBBI', 'MBJI', 'MBPI', 'MBSM', 'MDSI', 'MGAI', 'MIPI', 'MKBI', 'MKJM', 'MKSM', 'MLJI', 'MLJM', 'MMCI', 'MMRI', 'MMSI', 'MNAI', 'MNI', 'MNSI', 'MPSI', 'MPSM', 'MRSI', 'MSAI', 'MSCM', 'MTAI', 'MTCM', 'MTKI', 'MTSI', 'MTSM', 'MWPI', 'NBMI', 'NBPI', 'NGJI', 'NJBM', 'NKBI', 'NKKI', 'NSBMM', 'OBMI', 'OMBFM', 'ONSM', 'PABI', 'PAKI', 'PAFM', 'PBCI', 'PBJI', 'PBKI', 'PBLI', 'PBSI', 'PBNI', 'PCI', 'PCJI', 'PCJM', 'PDLI', 'PDSI', 'PGJM', 'PICM', 'PKCI', 'PKJI', 'PKJM', 'PKSI', 'PLAI', 'PLJI', 'PLSI', 'PLSM', 'PMBI', 'PMCI', 'PMMI', 'PMSI', 'POCI', 'PPCM', 'PPI', 'PPJI', 'PPLI', 'PPSI', 'PPSM', 'PRJI', 'PRSI', 'PSI', 'PSJCM', 'PSJM', 'PSLI', 'PSSI', 'PSSM', 'PTJI', 'PTSM', 'PWCM', 'PWJI', 'RASM', 'RDCM', 'RGRI', 'RHRSI', 'RKCM', 'RKPI', 'RLSI', 'RMSM', 'RNFM', 'RONI', 'RRSI', 'RSSM', 'RTBI', 'RSNI', 'SANI', 'SASI', 'SASM', 'SAUI', 'SBBM', 'SBJI', 'SBJM', 'SBNI', 'SBSM', 'SCJI', 'SCJM', 'SDCI', 'SDSI', 'SDSM', 'SEJI', 'SEMI', 'SGKI', 'SGSI', 'SIJI', 'SIJM', 'SIRSI', 'SISM', 'SJPM', 'SKJI', 'SKPM', 'SKSI', 'SKSM', 'SLBFM', 'SLSI', 'SLSM', 'SMKI', 'SMPI', 'SMRI', 'SMSI', 'SMSM', 'SNBI', 'SNJI', 'SNSI', 'SOEI', 'SPSI', 'SPSJM', 'SPSM', 'SRBI', 'SRMI', 'SRPI', 'SRSI', 'SSJM', 'SSKI', 'SSMI', 'SSSI', 'SSSM', 'STSI', 'SUSM', 'SWCM', 'SWI', 'SWJI', 'SWPM', 'SYJI', 'TAMI', 'TARAI', 'TASI', 'TBCM', 'TBJI', 'TBKI', 'TBMCM', 'TDNI', 'TGCM', 'TKSM', 'TLCM', 'TLE2', 'TMSI', 'TMSM', 'TMTMM', 'TNG', 'TNGI', 'TNTI', 'TOCM', 'TOJI', 'TOLI2', 'TPCI', 'TPI', 'TPRI', 'TPSI', 'TPTI', 'TRIYO', 'TRPI', 'TSI', 'TSJM', 'TSPI', 'TTSI', 'TTSM', 'TUJI', 'UGM', 'UKCM', 'ULSM', 'USFM', 'USTI', 'UTSI', 'UTSM', 'UWJI', 'WAMI', 'WBMI', 'TSNI', 'WBNI', 'WBSI', 'WEFM', 'WFTFM', 'WGJM', 'WHMI', 'WKCM', 'WLFM', 'WLJI', 'WLTFM', 'WMCM', 'WOJI', 'WRJI', 'WSI', 'WSJM', 'WSTMM', 'WUPCM', 'WWCI', 'WWPI', 'YOGI', 'BBLSI', 'BUMSI', 'KASAI', 'KKKKI', 'KKTKI', 'PBMSI', 'PRLJI', 'RHRRI', 'TTPSI', 'UTUS'] 

def remove_accelerograph(data):
    for item in data:
        if item not in seismograph_list:
            data.remove(item)
    return data

# Create your models here.
KELOMPOK = (
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5),
)

WAKTU = (
    ('12:00 WIB', '12:00 WIB'),
    ('00:00 WIB', '00:00 WIB')
)

class ChecklistSeiscompModel(models.Model):
 
    # fields of the model
    tanggal = models.DateField()
    jam = models.CharField(max_length=20, choices=WAKTU, default='12:00 WIB')
    kelompok = models.IntegerField(choices=KELOMPOK, default=1)
    operator = models.TextField(null=True,)
    gaps = models.CharField(max_length=500, null=True, blank=True)
    spikes = models.CharField(max_length=500, null=True, blank=True)
    blanks = models.CharField(max_length=500, null=True, blank=True)
    slmon = models.PositiveIntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # Modify the group field here\
        if self.gaps:
            self.gaps = self.gaps.upper()
            self.gaps = remove_accelerograph(self.gaps.split())
        if self.spikes:
            self.spikes = self.spikes.upper()
            self.spikes = remove_accelerograph(self.spikes.split())
        if self.blanks:
            self.blanks = self.blanks.upper()
            self.blanks = remove_accelerograph(self.blanks.split())

        super().save(*args, **kwargs)

    def __str__(self):
        return self.tanggal
    
class OperatorModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class StationListModel(models.Model):
    kode = models.CharField(max_length=10)
    lokasi = models.CharField(max_length=200)
    tipe = models.CharField(max_length=50)

    def __str__(self):
        return self.kode
