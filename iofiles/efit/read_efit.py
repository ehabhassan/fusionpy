from numpy             import reshape,ceil,zeros
from os.path           import isfile,realpath
from traceback         import extract_stack

def read_efit(fpath):
   #Developed by Ehab Hassan on 2019-02-27
    if isfile(fpath) == False:
       errorFunc = extract_stack(limit=2)[-2][3]
       errorLine = extract_stack(limit=2)[-2][1]
       errorFile = extract_stack(limit=2)[-2][2]
       errMSG    = 'Call %s line %5d in file %s Failed.\n'
       errMSG   += 'Fatal: file %s not found.'
       raise IOError(errMSG %(errorFunc,errorLine,errorFile,fpath))
    
    ofh = open(fpath,'r')
    efitdata = {}
    cline = ofh.readline()
    efitdata['idum']   = int(cline[48:52])
    efitdata['RDIM']   = int(cline[52:56])
    efitdata['ZDIM']   = int(cline[56:61])
    cline = ofh.readline()
    efitdata['RLEN']   = float(cline[0:16])
    efitdata['ZLEN']   = float(cline[16:32])
    efitdata['RCTR']   = float(cline[32:48])
    efitdata['RLFT']   = float(cline[48:64])
    efitdata['ZMID']   = float(cline[64:80])
    cline = ofh.readline()
    efitdata['RMAX']   = float(cline[0:16])
    efitdata['ZMAX']   = float(cline[16:32])
    efitdata['PSIMAX'] = float(cline[32:48])
    efitdata['PSIBND'] = float(cline[48:64])
    efitdata['BCTR']   = float(cline[64:80])
    cline = ofh.readline()
    efitdata['CURNT']  = float(cline[0:16])
    efitdata['PSIMAX'] = float(cline[16:32])
    efitdata['XDUM']   = float(cline[32:48])
    efitdata['RMAX']   = float(cline[48:64])
    efitdata['XDUM']   = float(cline[64:80])
    cline = ofh.readline()
    efitdata['ZMAX']   = float(cline[0:16])
    efitdata['XDUM']   = float(cline[16:32])
    efitdata['PSIBND'] = float(cline[32:48])
    efitdata['XDUM']   = float(cline[48:64])
    efitdata['XDUM']   = float(cline[64:80])

    nlines1D = int(ceil(efitdata['RDIM']/5.0))

    efitdata['fpol'] = zeros(efitdata['RDIM'])
    for iline in range(nlines1D):
        cline = ofh.readline()
        try:
            efitdata['fpol'][iline*5+0] = float(cline[0:16])
            efitdata['fpol'][iline*5+1] = float(cline[16:32])
            efitdata['fpol'][iline*5+2] = float(cline[32:48])
            efitdata['fpol'][iline*5+3] = float(cline[48:64])
            efitdata['fpol'][iline*5+4] = float(cline[64:80])
        except:
            error = 'empty records'

    efitdata['pressure'] = zeros(efitdata['RDIM'])
    for iline in range(nlines1D):
        cline = ofh.readline()
        try:
            efitdata['pressure'][iline*5+0] = float(cline[0:16])
            efitdata['pressure'][iline*5+1] = float(cline[16:32])
            efitdata['pressure'][iline*5+2] = float(cline[32:48])
            efitdata['pressure'][iline*5+3] = float(cline[48:64])
            efitdata['pressure'][iline*5+4] = float(cline[64:80])
        except:
            error = 'empty records'

    efitdata['ffprime'] = zeros(efitdata['RDIM'])
    for iline in range(nlines1D):
        cline = ofh.readline()
        try:
            efitdata['ffprime'][iline*5+0] = float(cline[0:16])
            efitdata['ffprime'][iline*5+1] = float(cline[16:32])
            efitdata['ffprime'][iline*5+2] = float(cline[32:48])
            efitdata['ffprime'][iline*5+3] = float(cline[48:64])
            efitdata['ffprime'][iline*5+4] = float(cline[64:80])
        except:
            error = 'empty records'

    efitdata['pprime'] = zeros(efitdata['RDIM'])
    for iline in range(nlines1D):
        cline = ofh.readline()
        try:
            efitdata['pprime'][iline*5+0] = float(cline[0:16])
            efitdata['pprime'][iline*5+1] = float(cline[16:32])
            efitdata['pprime'][iline*5+2] = float(cline[32:48])
            efitdata['pprime'][iline*5+3] = float(cline[48:64])
            efitdata['pprime'][iline*5+4] = float(cline[64:80])
        except:
            error = 'empty records'

    nlines2D = int(ceil(efitdata['RDIM']*efitdata['ZDIM']/5.0))

    efitdata['psiRZ'] = zeros(efitdata['RDIM']*efitdata['ZDIM'])
    for iline in range(nlines2D):
        cline = ofh.readline()
        try:
            efitdata['psiRZ'][iline*5+0] = float(cline[0:16])
            efitdata['psiRZ'][iline*5+1] = float(cline[16:32])
            efitdata['psiRZ'][iline*5+2] = float(cline[32:48])
            efitdata['psiRZ'][iline*5+3] = float(cline[48:64])
            efitdata['psiRZ'][iline*5+4] = float(cline[64:80])
        except:
            error = 'empty records'
    efitdata['psiRZ'] = reshape(efitdata['psiRZ'],(efitdata['ZDIM'],efitdata['RDIM']))
   #efitdata['psiRZ'] = (efitdata['psiRZ']-efitdata['PSIMAX'])/(efitdata['PSIBND']-efitdata['PSIMAX'])

    efitdata['qpsi'] = zeros(efitdata['RDIM'])
    for iline in range(nlines1D):
        cline = ofh.readline()
        try:
            efitdata['qpsi'][iline*5+0] = float(cline[0:16])
            efitdata['qpsi'][iline*5+1] = float(cline[16:32])
            efitdata['qpsi'][iline*5+2] = float(cline[32:48])
            efitdata['qpsi'][iline*5+3] = float(cline[48:64])
            efitdata['qpsi'][iline*5+4] = float(cline[64:80])
        except:
            error = 'empty records'
 
    cline = ofh.readline()
    efitdata['nbound'] = int(cline[0:5])
    efitdata['nlimit'] = int(cline[5:10])

    if efitdata['nbound'] > 0:
       nlines1D = int(ceil(2*efitdata['nbound']/5.0))

       Ary1D = zeros(2*efitdata['nbound'])
       for iline in range(nlines1D):
           cline = ofh.readline()
           try:
               Ary1D[iline*5+0] = float(cline[0:16])
               Ary1D[iline*5+1] = float(cline[16:32])
               Ary1D[iline*5+2] = float(cline[32:48])
               Ary1D[iline*5+3] = float(cline[48:64])
               Ary1D[iline*5+4] = float(cline[64:80])
           except:
               error = 'empty records'

       efitdata['rbound'] = Ary1D[0::2]
       efitdata['zbound'] = Ary1D[1::2]


    if efitdata['nlimit'] > 0:
       nlines1D = int(ceil(2*efitdata['nlimit']/5.0))

       Ary1D = zeros(2*efitdata['nlimit'])
       for iline in range(nlines1D):
           cline = ofh.readline()
           try:
               Ary1D[iline*5+0] = float(cline[0:16])
               Ary1D[iline*5+1] = float(cline[16:32])
               Ary1D[iline*5+2] = float(cline[32:48])
               Ary1D[iline*5+3] = float(cline[48:64])
               Ary1D[iline*5+4] = float(cline[64:80])
           except:
               error = 'empty records'

       efitdata['rlimit'] = Ary1D[0::2]
       efitdata['zlimit'] = Ary1D[1::2]
 
    return efitdata

if __name__=='__main__':
    efit_file_path = realpath('../../testsuite/state_files/plasma_eq.efit')
    efitdata = read_efit(fpath=efit_file_path)
    print(efitdata['Jtot'])

