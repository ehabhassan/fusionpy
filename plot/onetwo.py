import sys
import matplotlib.pyplot as plt

from plot.savefig   import to_pdf
from iofiles.onetwo import to_instate, read_state_file,read_iterdb_file
from iofiles.onetwo import read_onetwo_file

def plot_state_file(fname):
    reportpath = os.path.join(os.path.abspath("."),"fastran_report")
    if not os.path.isdir(reportpath):
       os.system('mkdir %s' % reportpath)

    onetwopath = os.path.join(reportpath,"ONETWO")
    if not os.path.isdir(onetwopath):
       os.system('mkdir %s' % onetwopath)

    figurepath = os.path.join(onetwopath,"Figures")
    if not os.path.isdir(figurepath):
       os.system('mkdir %s' % figurepath)

    ONETWOfigs = PdfPages(os.path.join(figurepath,'onetwo_plots.pdf'))

    onetwo = read_state_file(fname)

    rho  = (onetwo['rho_grid']['data']     - onetwo['rho_grid']['data'][0])
    rho /= (onetwo['rho_grid']['data'][-1] - onetwo['rho_grid']['data'][0])

    fields = []
    fields.extend(['Te', 'Ti', 'ene', 'press','pressb','q_value'])
    fields.extend(['p_flux_elct','p_flux_ion'])
    fields.extend(['e_fluxe','e_fluxe_conv','e_fluxi','e_fluxi_conv'])

    for ifield in fields:
        fg = plt.figure(onetwo[ifield]['name'])
        ax = fg.add_subplot(111)
        ax.plot(rho,onetwo[ifield]['data'])
        ax.set_title(onetwo[ifield]['name'])
        ax.set_xlabel("$\\rho$")
        ax.set_ylabel("%s ($%s$)" % (onetwo[ifield]['name'], onetwo[ifield]['unit']))
        ONETWOfigs.savefig(fg)
        plt.close(fg)

    fields = []
    fields.extend(['enion','p_flux_conv','p_flux'])

    for ifield in fields:
        fg = plt.figure(onetwo[ifield]['name'])
        fg.suptitle(onetwo[ifield]['name'])
        ax = fg.add_subplot(111)
        for ind in range(onetwo['nion']['data']):
            if onetwo['namep']['data'][0,ind].decode('utf-8').strip() != '': 
                figlabel = "ion: %s" % onetwo['namep']['data'][0,ind].decode('utf-8')
                ax.plot(rho,onetwo[ifield]['data'][ind,:],label=figlabel)
        ax.set_xlabel("$\\rho$")
        ax.set_ylabel("%s ($%s$)" % (onetwo[ifield]['name'], onetwo[ifield]['unit']))
        ax.legend()
        ONETWOfigs.savefig(fg)
        plt.close(fg)

    fields = []
    fields.extend(['enion','p_flux_conv','p_flux'])

    for ifield in fields:
        fg = plt.figure(onetwo[ifield]['name'])
        fg.suptitle(onetwo[ifield]['name'])
        ax = fg.add_subplot(111)
        for ind in range(onetwo['nion']['data']):
            if onetwo['namep']['data'][0,ind].decode('utf-8').strip() != '': 
                figlabel = "ion: %s" % onetwo['namep']['data'][0,ind].decode('utf-8')
                ax.plot(rho,onetwo[ifield]['data'][ind,:],label=figlabel)
        ax.set_xlabel("$\\rho$")
        ax.set_ylabel("%s ($%s$)" % (onetwo[ifield]['name'], onetwo[ifield]['unit']))
        ax.legend()
        ONETWOfigs.savefig(fg)
        plt.close(fg)

    ONETWOfigs.close()

def compare_data(fpathlist):
    if type(fpathlist) == str:
        fpathlist = [fpathlist]

    figs = []

    fig01 = plt.figure(1)
    ax011 = fig01.add_subplot(221)
    ax012 = fig01.add_subplot(222)
    ax013 = fig01.add_subplot(223)
    ax014 = fig01.add_subplot(224)
        
    fig02 = plt.figure(2)
    ax021 = fig02.add_subplot(221)
    ax022 = fig02.add_subplot(222)
    ax023 = fig02.add_subplot(223)
    ax024 = fig02.add_subplot(224)
        
    fig03 = plt.figure(3)
    ax031 = fig03.add_subplot(321)
    ax032 = fig03.add_subplot(322)
    ax033 = fig03.add_subplot(323)
    ax034 = fig03.add_subplot(324)
    ax035 = fig03.add_subplot(325)
    ax036 = fig03.add_subplot(326)
        
    fig04 = plt.figure(4)
    ax041 = fig04.add_subplot(321)
    ax042 = fig04.add_subplot(322)
    ax043 = fig04.add_subplot(323)
    ax044 = fig04.add_subplot(324)
    ax045 = fig04.add_subplot(325)
        
    fig05 = plt.figure(5)
    ax051 = fig05.add_subplot(321)
    ax052 = fig05.add_subplot(322)
    ax053 = fig05.add_subplot(323)
    ax054 = fig05.add_subplot(324)
    ax055 = fig05.add_subplot(325)
    ax056 = fig05.add_subplot(326)
        
    fig06 = plt.figure(6)
    ax061 = fig06.add_subplot(321)
    ax062 = fig06.add_subplot(322)
    ax063 = fig06.add_subplot(323)
    ax064 = fig06.add_subplot(324)
    ax065 = fig06.add_subplot(325)
    ax066 = fig06.add_subplot(326)
        
    fig07 = plt.figure(7)
    ax071 = fig07.add_subplot(321)
    ax072 = fig07.add_subplot(322)
    ax073 = fig07.add_subplot(323)
    ax074 = fig07.add_subplot(324)
    ax075 = fig07.add_subplot(325)
    ax076 = fig07.add_subplot(326)
        
    fig08 = plt.figure(8)
    ax081 = fig08.add_subplot(321)
    ax082 = fig08.add_subplot(322)
    ax083 = fig08.add_subplot(323)
    ax084 = fig08.add_subplot(324)
    ax085 = fig08.add_subplot(325)
    ax086 = fig08.add_subplot(326)
        
    fig09 = plt.figure(9)
    ax091 = fig09.add_subplot(321)
    ax092 = fig09.add_subplot(322)
    ax093 = fig09.add_subplot(323)
    ax094 = fig09.add_subplot(324)
    ax095 = fig09.add_subplot(325)
    ax096 = fig09.add_subplot(326)
        
    fig10 = plt.figure(10)
    ax101 = fig10.add_subplot(321)
    ax102 = fig10.add_subplot(322)
    ax103 = fig10.add_subplot(323)
    ax104 = fig10.add_subplot(324)
    ax105 = fig10.add_subplot(325)
    ax106 = fig10.add_subplot(326)
        
    fig11 = plt.figure(11)
    ax111 = fig11.add_subplot(321)
    ax112 = fig11.add_subplot(322)
    ax113 = fig11.add_subplot(323)
    ax114 = fig11.add_subplot(324)
    ax115 = fig11.add_subplot(325)
    ax116 = fig11.add_subplot(326)
        
    fig12 = plt.figure(12)
    ax121 = fig12.add_subplot(321)
    ax122 = fig12.add_subplot(322)
    ax123 = fig12.add_subplot(323)
    ax124 = fig12.add_subplot(324)
    ax125 = fig12.add_subplot(325)
    ax126 = fig12.add_subplot(326)
        
    fig13 = plt.figure(13)
    ax131 = fig13.add_subplot(221)
    ax132 = fig13.add_subplot(222)
    ax133 = fig13.add_subplot(223)
    ax134 = fig13.add_subplot(224)
        
    figs.append(fig01)
    figs.append(fig02)
    figs.append(fig03)
    figs.append(fig04)
    figs.append(fig05)
    figs.append(fig06)
    figs.append(fig07)
    figs.append(fig08)
    figs.append(fig09)
    figs.append(fig10)
    figs.append(fig11)
    figs.append(fig12)
    figs.append(fig13)

    fields01 = ['ene','enion','Te','Ti']
    fields02 = ['press','pressb','q_value','zeff']
    fields03 = ['curden','curpar','curohm','curboot','curbeam','currf']
    fields04 = ['fcap','gcap','hcap','rbp','angrot']
    fields05 = ['sion','srecom','scx','sbcx','stsource','dudtsv']
    fields06 = ['enbeam','enn','ennw','ennv','volsn','storqueb'] 
    fields07 = ['sbeame','sbeam','chieinv','chiinv','dpedt','dpidt']
    fields08 = ['qconde','qcondi','qconve','qconvi','qrad','qohm']
    fields09 = ['xkineo','qbeame','qdelt','qbeami','qrfe','qrfi']
    fields10 = ['qione','qioni','qcx','qe2d','qi2d','qmag']
    fields11 = ['qfuse','qfusi','qbfuse','qbfusi','qsawe','qsawi']
    fields12 = ['rmajavnpsi','rminavnpsi','psivolpnpsi','elongxnpsi','triangnpsi_u','pindentnpsi']
    fields13 = ['sfareanpsi','cxareanpsi','grho1npsi','grho2npsi']

    for ifpath in fpathlist:
        onetwodata = read_onetwo_file(ifpath)
        if onetwodata['file_type'] == 'state':
            fpstate_flag = True
            fiterdb_flag = False
        elif onetwodata['file_type'] == 'iterdb':
            fpstate_flag = False
            fiterdb_flag = True

        if fpstate_flag:
            ax011.plot(onetwodata['psir_grid']['data'], onetwodata[fields01[0]]['data'],    label='pstate', linestyle='-')
            ax012.plot(onetwodata['psir_grid']['data'], onetwodata[fields01[1]]['data'][0], label='pstate', linestyle='-')
            ax013.plot(onetwodata['psir_grid']['data'], onetwodata[fields01[2]]['data'],    label='pstate', linestyle='-')
            ax014.plot(onetwodata['psir_grid']['data'], onetwodata[fields01[3]]['data'],    label='pstate', linestyle='-')

        elif fiterdb_flag:
            ax011.plot(onetwodata['psir_grid']['data'], onetwodata[fields01[0]]['data'],    label='iterdb', linestyle='--')
            ax012.plot(onetwodata['psir_grid']['data'], onetwodata[fields01[1]]['data'][0], label='iterdb', linestyle='--')
            ax013.plot(onetwodata['psir_grid']['data'], onetwodata[fields01[2]]['data'],    label='iterdb', linestyle='--')
            ax014.plot(onetwodata['psir_grid']['data'], onetwodata[fields01[3]]['data'],    label='iterdb', linestyle='--')
            
        if fpstate_flag:
            ax021.plot(onetwodata['psir_grid']['data'], onetwodata[fields02[0]]['data'], label='pstate', linestyle='-')
            ax022.plot(onetwodata['psir_grid']['data'], onetwodata[fields02[1]]['data'], label='pstate', linestyle='-')
            ax023.plot(onetwodata['psir_grid']['data'], onetwodata[fields02[2]]['data'], label='pstate', linestyle='-')
            ax024.plot(onetwodata['psir_grid']['data'], onetwodata[fields02[3]]['data'], label='pstate', linestyle='-')

        elif fiterdb_flag:
            ax021.plot(onetwodata['psir_grid']['data'], onetwodata[fields02[0]]['data'], label='iterdb', linestyle='--')
            ax022.plot(onetwodata['psir_grid']['data'], onetwodata[fields02[1]]['data'], label='iterdb', linestyle='--')
            ax023.plot(onetwodata['psir_grid']['data'], onetwodata[fields02[2]]['data'], label='iterdb', linestyle='--')
            ax024.plot(onetwodata['psir_grid']['data'], onetwodata[fields02[3]]['data'], label='iterdb', linestyle='--')
            
        if fpstate_flag:
            ax031.plot(onetwodata['psir_grid']['data'], onetwodata[fields03[0]]['data'], label='pstate', linestyle='-')
            ax032.plot(onetwodata['psir_grid']['data'], onetwodata[fields03[1]]['data'], label='pstate', linestyle='-')
            ax033.plot(onetwodata['psir_grid']['data'], onetwodata[fields03[2]]['data'], label='pstate', linestyle='-')
            ax034.plot(onetwodata['psir_grid']['data'], onetwodata[fields03[3]]['data'], label='pstate', linestyle='-')
            ax035.plot(onetwodata['psir_grid']['data'], onetwodata[fields03[4]]['data'], label='pstate', linestyle='-')
            ax036.plot(onetwodata['psir_grid']['data'], onetwodata[fields03[5]]['data'], label='pstate', linestyle='-')

        elif fiterdb_flag:
            ax031.plot(onetwodata['psir_grid']['data'], onetwodata[fields03[0]]['data'], label='iterdb', linestyle='--')
            ax032.plot(onetwodata['psir_grid']['data'], onetwodata[fields03[0]]['data'], label='iterdb', linestyle='--')
            ax033.plot(onetwodata['psir_grid']['data'], onetwodata[fields03[2]]['data'], label='iterdb', linestyle='--')
            ax034.plot(onetwodata['psir_grid']['data'], onetwodata[fields03[3]]['data'], label='iterdb', linestyle='--')
            ax035.plot(onetwodata['psir_grid']['data'], onetwodata[fields03[4]]['data'], label='iterdb', linestyle='--')
            ax036.plot(onetwodata['psir_grid']['data'], onetwodata[fields03[5]]['data'], label='iterdb', linestyle='--')
            
        if fpstate_flag:
            ax041.plot(onetwodata['psir_grid']['data'], onetwodata[fields04[0]]['data'], label='pstate', linestyle='-')
            ax042.plot(onetwodata['psir_grid']['data'], onetwodata[fields04[1]]['data'], label='pstate', linestyle='-')
            ax043.plot(onetwodata['psir_grid']['data'], onetwodata[fields04[2]]['data'], label='pstate', linestyle='-')
            ax044.plot(onetwodata['psir_grid']['data'], onetwodata[fields04[3]]['data'], label='pstate', linestyle='-')
            ax045.plot(onetwodata['psir_grid']['data'], onetwodata[fields04[4]]['data'], label='pstate', linestyle='-')

        elif fiterdb_flag:
            ax041.plot(onetwodata['psir_grid']['data'], onetwodata[fields04[0]]['data'], label='iterdb', linestyle='--')
            ax042.plot(onetwodata['psir_grid']['data'], onetwodata[fields04[1]]['data'], label='iterdb', linestyle='--')
            ax043.plot(onetwodata['psir_grid']['data'], onetwodata[fields04[2]]['data'], label='iterdb', linestyle='--')
            ax044.plot(onetwodata['psir_grid']['data'], onetwodata[fields04[3]]['data'], label='iterdb', linestyle='--')
            ax045.plot(onetwodata['psir_grid']['data'], onetwodata[fields04[4]]['data'], label='iterdb', linestyle='--')
            
        if fpstate_flag:
            ax051.plot(onetwodata['psir_grid']['data'], onetwodata[fields05[0]]['data'][0,:], label='pstate', linestyle='-')
            ax052.plot(onetwodata['psir_grid']['data'], onetwodata[fields05[1]]['data'][0,:], label='pstate', linestyle='-')
            ax053.plot(onetwodata['psir_grid']['data'], onetwodata[fields05[2]]['data'][0,:], label='pstate', linestyle='-')
            ax054.plot(onetwodata['psir_grid']['data'], onetwodata[fields05[3]]['data'][0,:], label='pstate', linestyle='-')
            ax055.plot(onetwodata['psir_grid']['data'], onetwodata[fields05[4]]['data'][0,:], label='pstate', linestyle='-')
            ax056.plot(onetwodata['psir_grid']['data'], onetwodata[fields05[5]]['data'][0,:], label='pstate', linestyle='-')

        elif fiterdb_flag:
            ax051.plot(onetwodata['psir_grid']['data'], onetwodata[fields05[0]]['data']   ,   label='iterdb', linestyle='--')
            ax052.plot(onetwodata['psir_grid']['data'], onetwodata[fields05[1]]['data'][0,:], label='iterdb', linestyle='--')
            ax053.plot(onetwodata['psir_grid']['data'], onetwodata[fields05[2]]['data'][0],   label='iterdb', linestyle='--')
            ax054.plot(onetwodata['psir_grid']['data'], onetwodata[fields05[3]]['data'],      label='iterdb', linestyle='--')
            ax055.plot(onetwodata['psir_grid']['data'], onetwodata[fields05[4]]['data'][0,:], label='iterdb', linestyle='--')
            ax056.plot(onetwodata['psir_grid']['data'], onetwodata[fields05[5]]['data'][0,:], label='iterdb', linestyle='--')
            
        if fpstate_flag:
            ax061.plot(onetwodata['psir_grid']['data'], onetwodata[fields06[0]]['data'][0,:], label='pstate', linestyle='-')
            ax062.plot(onetwodata['psir_grid']['data'], onetwodata[fields06[1]]['data'][0,:], label='pstate', linestyle='-')
            ax063.plot(onetwodata['psir_grid']['data'], onetwodata[fields06[2]]['data'][0,:], label='pstate', linestyle='-')
            ax064.plot(onetwodata['psir_grid']['data'], onetwodata[fields06[3]]['data'][0,:], label='pstate', linestyle='-')
            ax065.plot(onetwodata['psir_grid']['data'], onetwodata[fields06[4]]['data'][0,:], label='pstate', linestyle='-')
            ax066.plot(onetwodata['psir_grid']['data'], onetwodata[fields06[5]]['data']     , label='pstate', linestyle='-')

        elif fiterdb_flag:
            ax061.plot(onetwodata['psir_grid']['data'], onetwodata[fields06[0]]['data'][0,:], label='iterdb', linestyle='--')
            ax062.plot(onetwodata['psir_grid']['data'], onetwodata[fields06[1]]['data'][0,:], label='iterdb', linestyle='--')
            ax063.plot(onetwodata['psir_grid']['data'], onetwodata[fields06[2]]['data'][0,:], label='iterdb', linestyle='--')
            ax064.plot(onetwodata['psir_grid']['data'], onetwodata[fields06[3]]['data'][0,:], label='iterdb', linestyle='--')
            ax065.plot(onetwodata['psir_grid']['data'], onetwodata[fields06[4]]['data'][0,:], label='iterdb', linestyle='--')
            ax066.plot(onetwodata['psir_grid']['data'], onetwodata[fields06[5]]['data']     , label='iterdb', linestyle='--')
            
        if fpstate_flag:
            ax071.plot(onetwodata['psir_grid']['data'], onetwodata[fields07[0]]['data'], label='pstate', linestyle='-')
            ax072.plot(onetwodata['psir_grid']['data'], onetwodata[fields07[1]]['data'][0,:], label='pstate', linestyle='-')
            ax073.plot(onetwodata['psir_grid']['data'], onetwodata[fields07[2]]['data'], label='pstate', linestyle='-')
            ax074.plot(onetwodata['psir_grid']['data'], onetwodata[fields07[3]]['data'], label='pstate', linestyle='-')
            ax075.plot(onetwodata['psir_grid']['data'], onetwodata[fields07[4]]['data'], label='pstate', linestyle='-')
            ax076.plot(onetwodata['psir_grid']['data'], onetwodata[fields07[5]]['data'][0,:], label='pstate', linestyle='-')

        elif fiterdb_flag:
            ax071.plot(onetwodata['psir_grid']['data'], onetwodata[fields07[0]]['data'], label='iterdb', linestyle='--')
            ax072.plot(onetwodata['psir_grid']['data'], onetwodata[fields07[1]]['data'], label='iterdb', linestyle='--')
            ax073.plot(onetwodata['psir_grid']['data'], onetwodata[fields07[2]]['data'], label='iterdb', linestyle='--')
            ax074.plot(onetwodata['psir_grid']['data'], onetwodata[fields07[3]]['data'], label='iterdb', linestyle='--')
            ax075.plot(onetwodata['psir_grid']['data'], onetwodata[fields07[4]]['data'], label='iterdb', linestyle='--')
            ax076.plot(onetwodata['psir_grid']['data'], onetwodata[fields07[5]]['data'], label='iterdb', linestyle='--')
            
        if fpstate_flag:
            ax081.plot(onetwodata['psir_grid']['data'], onetwodata[fields08[0]]['data'], label='pstate', linestyle='-')
            ax082.plot(onetwodata['psir_grid']['data'], onetwodata[fields08[1]]['data'], label='pstate', linestyle='-')
            ax083.plot(onetwodata['psir_grid']['data'], onetwodata[fields08[2]]['data'], label='pstate', linestyle='-')
            ax084.plot(onetwodata['psir_grid']['data'], onetwodata[fields08[3]]['data'], label='pstate', linestyle='-')
            ax085.plot(onetwodata['psir_grid']['data'], onetwodata[fields08[4]]['data'], label='pstate', linestyle='-')
            ax086.plot(onetwodata['psir_grid']['data'], onetwodata[fields08[5]]['data'], label='pstate', linestyle='-')

        elif fiterdb_flag:
            ax081.plot(onetwodata['psir_grid']['data'], onetwodata[fields08[0]]['data'], label='iterdb', linestyle='--')
            ax082.plot(onetwodata['psir_grid']['data'], onetwodata[fields08[1]]['data'], label='iterdb', linestyle='--')
            ax083.plot(onetwodata['psir_grid']['data'], onetwodata[fields08[2]]['data'], label='iterdb', linestyle='--')
            ax084.plot(onetwodata['psir_grid']['data'], onetwodata[fields08[3]]['data'], label='iterdb', linestyle='--')
            ax085.plot(onetwodata['psir_grid']['data'], onetwodata[fields08[4]]['data'], label='iterdb', linestyle='--')
            ax086.plot(onetwodata['psir_grid']['data'], onetwodata[fields08[5]]['data'], label='iterdb', linestyle='--')
            
        if fpstate_flag:
            ax091.plot(onetwodata['psir_grid']['data'], onetwodata[fields09[0]]['data'], label='pstate', linestyle='-')
            ax092.plot(onetwodata['psir_grid']['data'], onetwodata[fields09[1]]['data'], label='pstate', linestyle='-')
            ax093.plot(onetwodata['psir_grid']['data'], onetwodata[fields09[2]]['data'], label='pstate', linestyle='-')
            ax094.plot(onetwodata['psir_grid']['data'], onetwodata[fields09[3]]['data'], label='pstate', linestyle='-')
            ax095.plot(onetwodata['psir_grid']['data'], onetwodata[fields09[4]]['data'], label='pstate', linestyle='-')
            ax096.plot(onetwodata['psir_grid']['data'], onetwodata[fields09[5]]['data'], label='pstate', linestyle='-')

        elif fiterdb_flag:
            ax091.plot(onetwodata['psir_grid']['data'], onetwodata[fields09[0]]['data'], label='iterdb', linestyle='--')
            ax092.plot(onetwodata['psir_grid']['data'], onetwodata[fields09[1]]['data'], label='iterdb', linestyle='--')
            ax093.plot(onetwodata['psir_grid']['data'], onetwodata[fields09[2]]['data'], label='iterdb', linestyle='--')
            ax094.plot(onetwodata['psir_grid']['data'], onetwodata[fields09[3]]['data'], label='iterdb', linestyle='--')
            ax095.plot(onetwodata['psir_grid']['data'], onetwodata[fields09[4]]['data'], label='iterdb', linestyle='--')
            ax096.plot(onetwodata['psir_grid']['data'], onetwodata[fields09[5]]['data'], label='iterdb', linestyle='--')
            
        if fpstate_flag:
            ax101.plot(onetwodata['psir_grid']['data'], onetwodata[fields10[0]]['data'], label='pstate', linestyle='-')
            ax102.plot(onetwodata['psir_grid']['data'], onetwodata[fields10[1]]['data'], label='pstate', linestyle='-')
            ax103.plot(onetwodata['psir_grid']['data'], onetwodata[fields10[2]]['data'], label='pstate', linestyle='-')
            ax104.plot(onetwodata['psir_grid']['data'], onetwodata[fields10[3]]['data'], label='pstate', linestyle='-')
            ax105.plot(onetwodata['psir_grid']['data'], onetwodata[fields10[4]]['data'], label='pstate', linestyle='-')
            ax106.plot(onetwodata['psir_grid']['data'], onetwodata[fields10[5]]['data'], label='pstate', linestyle='-')

        elif fiterdb_flag:
            ax101.plot(onetwodata['psir_grid']['data'], onetwodata[fields10[0]]['data'], label='iterdb', linestyle='--')
            ax102.plot(onetwodata['psir_grid']['data'], onetwodata[fields10[1]]['data'], label='iterdb', linestyle='--')
            ax103.plot(onetwodata['psir_grid']['data'], onetwodata[fields10[2]]['data'], label='iterdb', linestyle='--')
            ax104.plot(onetwodata['psir_grid']['data'], onetwodata[fields10[3]]['data'], label='iterdb', linestyle='--')
            ax105.plot(onetwodata['psir_grid']['data'], onetwodata[fields10[4]]['data'], label='iterdb', linestyle='--')
            ax106.plot(onetwodata['psir_grid']['data'], onetwodata[fields10[5]]['data'], label='iterdb', linestyle='--')
            
        if fpstate_flag:
            ax111.plot(onetwodata['psir_grid']['data'], onetwodata[fields11[0]]['data'], label='pstate', linestyle='-')
            ax112.plot(onetwodata['psir_grid']['data'], onetwodata[fields11[1]]['data'], label='pstate', linestyle='-')
            ax113.plot(onetwodata['psir_grid']['data'], onetwodata[fields11[2]]['data'], label='pstate', linestyle='-')
            ax114.plot(onetwodata['psir_grid']['data'], onetwodata[fields11[3]]['data'], label='pstate', linestyle='-')
            ax115.plot(onetwodata['psir_grid']['data'], onetwodata[fields11[4]]['data'], label='pstate', linestyle='-')
            ax116.plot(onetwodata['psir_grid']['data'], onetwodata[fields11[5]]['data'], label='pstate', linestyle='-')

        elif fiterdb_flag:
            ax111.plot(onetwodata['psir_grid']['data'], onetwodata[fields11[0]]['data'], label='iterdb', linestyle='--')
            ax112.plot(onetwodata['psir_grid']['data'], onetwodata[fields11[1]]['data'], label='iterdb', linestyle='--')
            ax113.plot(onetwodata['psir_grid']['data'], onetwodata[fields11[2]]['data'], label='iterdb', linestyle='--')
            ax114.plot(onetwodata['psir_grid']['data'], onetwodata[fields11[3]]['data'], label='iterdb', linestyle='--')
            ax115.plot(onetwodata['psir_grid']['data'], onetwodata[fields11[4]]['data'], label='iterdb', linestyle='--')
            ax116.plot(onetwodata['psir_grid']['data'], onetwodata[fields11[5]]['data'], label='iterdb', linestyle='--')
            
        if fpstate_flag:
            ax121.plot(onetwodata['psivalnpsi']['data'], onetwodata[fields12[0]]['data'], label='pstate', linestyle='-')
            ax122.plot(onetwodata['psivalnpsi']['data'], onetwodata[fields12[1]]['data'], label='pstate', linestyle='-')
            ax123.plot(onetwodata['psivalnpsi']['data'], onetwodata[fields12[2]]['data'], label='pstate', linestyle='-')
            ax124.plot(onetwodata['psivalnpsi']['data'], onetwodata[fields12[3]]['data'], label='pstate', linestyle='-')
            ax125.plot(onetwodata['psivalnpsi']['data'], onetwodata[fields12[4]]['data'], label='pstate', linestyle='-')
            ax126.plot(onetwodata['psivalnpsi']['data'], onetwodata[fields12[5]]['data'], label='pstate', linestyle='-')

        elif fiterdb_flag:
            ax121.plot(onetwodata['psir_grid']['data'],  onetwodata[fields12[0]]['data'], label='iterdb', linestyle='--')
            ax122.plot(onetwodata['psir_grid']['data'],  onetwodata[fields12[1]]['data'], label='iterdb', linestyle='--')
            ax123.plot(onetwodata['psir_grid']['data'],  onetwodata[fields12[2]]['data'], label='iterdb', linestyle='--')
            ax124.plot(onetwodata['psir_grid']['data'],  onetwodata[fields12[3]]['data'], label='iterdb', linestyle='--')
            ax125.plot(onetwodata['psir_grid']['data'],  onetwodata[fields12[4]]['data'], label='iterdb', linestyle='--')
            ax126.plot(onetwodata['psir_grid']['data'],  onetwodata[fields12[5]]['data'], label='iterdb', linestyle='--')
            
        if fpstate_flag:
            ax131.plot(onetwodata['psivalnpsi']['data'], onetwodata[fields13[0]]['data'], label='pstate', linestyle='-')
            ax132.plot(onetwodata['psivalnpsi']['data'], onetwodata[fields13[1]]['data'], label='pstate', linestyle='-')
            ax133.plot(onetwodata['psivalnpsi']['data'], onetwodata[fields13[2]]['data'], label='pstate', linestyle='-')
            ax134.plot(onetwodata['psivalnpsi']['data'], onetwodata[fields13[3]]['data'], label='pstate', linestyle='-')

        elif fiterdb_flag:
            ax131.plot(onetwodata['psir_grid']['data'],  onetwodata[fields13[0]]['data'], label='iterdb', linestyle='--')
            ax132.plot(onetwodata['psir_grid']['data'],  onetwodata[fields13[1]]['data'], label='iterdb', linestyle='--')
            ax133.plot(onetwodata['psir_grid']['data'],  onetwodata[fields13[2]]['data'], label='iterdb', linestyle='--')
            ax134.plot(onetwodata['psir_grid']['data'],  onetwodata[fields13[3]]['data'], label='iterdb', linestyle='--')
        
    ax011.legend()
    ax021.legend()
    ax031.legend()
    ax041.legend()
    ax051.legend()
    ax061.legend()
    ax071.legend()
    ax081.legend()
    ax091.legend()
    ax101.legend()
    ax111.legend()
    ax121.legend()
    ax131.legend()
        
    ax011.set_ylabel(fields01[0])
    ax012.set_ylabel(fields01[1])
    ax013.set_ylabel(fields01[2])
    ax014.set_ylabel(fields01[3])
        
    ax021.set_ylabel(fields02[0])
    ax022.set_ylabel(fields02[1])
    ax023.set_ylabel(fields02[2])
    ax024.set_ylabel(fields02[3])
        
    ax031.set_ylabel(fields03[0])
    ax032.set_ylabel(fields03[1])
    ax033.set_ylabel(fields03[2])
    ax034.set_ylabel(fields03[3])
    ax035.set_ylabel(fields03[4])
    ax036.set_ylabel(fields03[5])
        
    ax041.set_ylabel(fields04[0])
    ax042.set_ylabel(fields04[1])
    ax043.set_ylabel(fields04[2])
    ax044.set_ylabel(fields04[3])
    ax045.set_ylabel(fields04[4])
        
    ax051.set_ylabel(fields05[0])
    ax052.set_ylabel(fields05[1])
    ax053.set_ylabel(fields05[2])
    ax054.set_ylabel(fields05[3])
    ax055.set_ylabel(fields05[4])
    ax056.set_ylabel(fields05[5])
        
    ax061.set_ylabel(fields06[0])
    ax062.set_ylabel(fields06[1])
    ax063.set_ylabel(fields06[2])
    ax064.set_ylabel(fields06[3])
    ax065.set_ylabel(fields06[4])
    ax066.set_ylabel(fields06[5])
        
    ax071.set_ylabel(fields07[0])
    ax072.set_ylabel(fields07[1])
    ax073.set_ylabel(fields07[2])
    ax074.set_ylabel(fields07[3])
    ax075.set_ylabel(fields07[4])
    ax076.set_ylabel(fields07[5])
        
    ax081.set_ylabel(fields08[0])
    ax082.set_ylabel(fields08[1])
    ax083.set_ylabel(fields08[2])
    ax084.set_ylabel(fields08[3])
    ax085.set_ylabel(fields08[4])
    ax086.set_ylabel(fields08[5])
        
    ax091.set_ylabel(fields09[0])
    ax092.set_ylabel(fields09[1])
    ax093.set_ylabel(fields09[2])
    ax094.set_ylabel(fields09[3])
    ax095.set_ylabel(fields09[4])
    ax096.set_ylabel(fields09[5])
        
    ax101.set_ylabel(fields10[0])
    ax102.set_ylabel(fields10[1])
    ax103.set_ylabel(fields10[2])
    ax104.set_ylabel(fields10[3])
    ax105.set_ylabel(fields10[4])
    ax106.set_ylabel(fields10[5])
        
    ax111.set_ylabel(fields11[0])
    ax112.set_ylabel(fields11[1])
    ax113.set_ylabel(fields11[2])
    ax114.set_ylabel(fields11[3])
    ax115.set_ylabel(fields11[4])
    ax116.set_ylabel(fields11[5])
        
    ax121.set_ylabel(fields12[0])
    ax122.set_ylabel(fields12[1])
    ax123.set_ylabel(fields12[2])
    ax124.set_ylabel(fields12[3])
    ax125.set_ylabel(fields12[4])
    ax126.set_ylabel(fields12[5])
        
    ax131.set_ylabel(fields13[0])
    ax132.set_ylabel(fields13[1])
    ax133.set_ylabel(fields13[2])
    ax134.set_ylabel(fields13[3])
        
    ax033.set_xticks([])
    ax034.set_xticks([])
    
    ax043.set_xticks([])
   #ax044.set_xticks([])
    
    ax053.set_xticks([])
    ax054.set_xticks([])
    
    ax063.set_xticks([])
    ax064.set_xticks([])
    
    ax073.set_xticks([])
    ax074.set_xticks([])
    
    ax083.set_xticks([])
    ax084.set_xticks([])
    
    ax093.set_xticks([])
    ax094.set_xticks([])
    
    ax103.set_xticks([])
    ax104.set_xticks([])
    
    ax113.set_xticks([])
    ax114.set_xticks([])
    
    ax123.set_xticks([])
    ax124.set_xticks([])
    
    ax011.xaxis.tick_top(); ax011.xaxis.set_label_position('top')
    ax012.xaxis.tick_top(); ax012.xaxis.set_label_position('top')
    
    ax021.xaxis.tick_top(); ax021.xaxis.set_label_position('top')
    ax022.xaxis.tick_top(); ax022.xaxis.set_label_position('top')
    
    ax031.xaxis.tick_top(); ax031.xaxis.set_label_position('top')
    ax032.xaxis.tick_top(); ax032.xaxis.set_label_position('top')
    
    ax041.xaxis.tick_top(); ax041.xaxis.set_label_position('top')
    ax042.xaxis.tick_top(); ax042.xaxis.set_label_position('top')
    
    ax051.xaxis.tick_top(); ax051.xaxis.set_label_position('top')
    ax052.xaxis.tick_top(); ax052.xaxis.set_label_position('top')
    
    ax061.xaxis.tick_top(); ax061.xaxis.set_label_position('top')
    ax062.xaxis.tick_top(); ax062.xaxis.set_label_position('top')
    
    ax071.xaxis.tick_top(); ax071.xaxis.set_label_position('top')
    ax072.xaxis.tick_top(); ax072.xaxis.set_label_position('top')
    
    ax081.xaxis.tick_top(); ax071.xaxis.set_label_position('top')
    ax082.xaxis.tick_top(); ax072.xaxis.set_label_position('top')
    
    ax012.yaxis.tick_right(); ax012.yaxis.set_label_position('right')
    ax014.yaxis.tick_right(); ax014.yaxis.set_label_position('right')
    
    ax022.yaxis.tick_right(); ax022.yaxis.set_label_position('right')
    ax024.yaxis.tick_right(); ax024.yaxis.set_label_position('right')
    
    ax032.yaxis.tick_right(); ax032.yaxis.set_label_position('right')
    ax034.yaxis.tick_right(); ax034.yaxis.set_label_position('right')
    ax036.yaxis.tick_right(); ax036.yaxis.set_label_position('right')
    
    ax042.yaxis.tick_right(); ax042.yaxis.set_label_position('right')
    ax044.yaxis.tick_right(); ax044.yaxis.set_label_position('right')
    
    ax052.yaxis.tick_right(); ax052.yaxis.set_label_position('right')
    ax054.yaxis.tick_right(); ax054.yaxis.set_label_position('right')
    ax056.yaxis.tick_right(); ax056.yaxis.set_label_position('right')
    
    ax062.yaxis.tick_right(); ax062.yaxis.set_label_position('right')
    ax064.yaxis.tick_right(); ax064.yaxis.set_label_position('right')
    ax066.yaxis.tick_right(); ax066.yaxis.set_label_position('right')
    
    ax072.yaxis.tick_right(); ax072.yaxis.set_label_position('right')
    ax074.yaxis.tick_right(); ax074.yaxis.set_label_position('right')
    ax076.yaxis.tick_right(); ax076.yaxis.set_label_position('right')
    
    ax082.yaxis.tick_right(); ax082.yaxis.set_label_position('right')
    ax084.yaxis.tick_right(); ax084.yaxis.set_label_position('right')
    ax086.yaxis.tick_right(); ax086.yaxis.set_label_position('right')
    
    ax092.yaxis.tick_right(); ax092.yaxis.set_label_position('right')
    ax094.yaxis.tick_right(); ax094.yaxis.set_label_position('right')
    ax096.yaxis.tick_right(); ax096.yaxis.set_label_position('right')
    
    ax102.yaxis.tick_right(); ax102.yaxis.set_label_position('right')
    ax104.yaxis.tick_right(); ax104.yaxis.set_label_position('right')
    ax106.yaxis.tick_right(); ax106.yaxis.set_label_position('right')
    
    ax112.yaxis.tick_right(); ax112.yaxis.set_label_position('right')
    ax114.yaxis.tick_right(); ax114.yaxis.set_label_position('right')
    ax116.yaxis.tick_right(); ax116.yaxis.set_label_position('right')
    
    ax122.yaxis.tick_right(); ax122.yaxis.set_label_position('right')
    ax124.yaxis.tick_right(); ax124.yaxis.set_label_position('right')
    ax126.yaxis.tick_right(); ax126.yaxis.set_label_position('right')
    
    ax132.yaxis.tick_right(); ax132.yaxis.set_label_position('right')
    ax134.yaxis.tick_right(); ax134.yaxis.set_label_position('right')
    
    fig01.tight_layout(rect=[0.0, 0.0, 1.0, 1.0])
    fig01.subplots_adjust(wspace=0,hspace=0)
    
    fig02.tight_layout(rect=[0.0, 0.0, 1.0, 1.0])
    fig02.subplots_adjust(wspace=0,hspace=0)
    
    fig03.tight_layout(rect=[0.0, 0.0, 1.0, 1.0])
    fig03.subplots_adjust(wspace=0,hspace=0)
    
    fig04.tight_layout(rect=[0.0, 0.0, 1.0, 1.0])
    fig04.subplots_adjust(wspace=0,hspace=0)
    
    fig05.tight_layout(rect=[0.0, 0.0, 1.0, 1.0])
    fig05.subplots_adjust(wspace=0,hspace=0)
    
    fig06.tight_layout(rect=[0.0, 0.0, 1.0, 1.0])
    fig06.subplots_adjust(wspace=0,hspace=0)
    
    fig07.tight_layout(rect=[0.0, 0.0, 1.0, 1.0])
    fig07.subplots_adjust(wspace=0,hspace=0)
    
    fig08.tight_layout(rect=[0.0, 0.0, 1.0, 1.0])
    fig08.subplots_adjust(wspace=0,hspace=0)
        
    fig09.tight_layout(rect=[0.0, 0.0, 1.0, 1.0])
    fig09.subplots_adjust(wspace=0,hspace=0)
        
    fig10.tight_layout(rect=[0.0, 0.0, 1.0, 1.0])
    fig10.subplots_adjust(wspace=0,hspace=0)
        
    fig11.tight_layout(rect=[0.0, 0.0, 1.0, 1.0])
    fig11.subplots_adjust(wspace=0,hspace=0)
        
    fig12.tight_layout(rect=[0.0, 0.0, 1.0, 1.0])
    fig12.subplots_adjust(wspace=0,hspace=0)
        
    fig13.tight_layout(rect=[0.0, 0.0, 1.0, 1.0])
    fig13.subplots_adjust(wspace=0,hspace=0)
        
    to_pdf(figs)

    return True

if __name__ == "__main__":
   #iterdbfname = []
   #iterdbfname.append("statefile_2.026000E+00.nc")
   #iterdbfname.append("iterdb.150139")
    iterdbfname = "iterdb.150139"
    compare_data(iterdbfname)

sys.exit()
