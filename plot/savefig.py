import os

from matplotlib.backends.backend_pdf  import PdfPages


def to_pdf(figobjs,fname='',category=''):

    reportpath = os.path.join(os.path.abspath("."),"fusionpy_report")
    if not os.path.isdir(reportpath):
       os.system('mkdir %s' % reportpath)

    if not category: category = "FUSIONPY"
    categorypath = os.path.join(reportpath,category.upper())
    if not os.path.isdir(categorypath):
       os.system('mkdir %s' % categorypath)
    
    figurepath = os.path.join(categorypath,"FIGURES")
    if not os.path.isdir(figurepath):
       os.system('mkdir %s' % figurepath)
    
    if not fname: fname = "fusionpy_plots"
    pdffigs = PdfPages(os.path.join(figurepath,'%s.pdf' % fname))


    if type(figobjs) not in [list,tuple,set]: figobjs = list(figobjs)
    for ifigobj in figobjs:
        pdffigs.savefig(ifigobj)
    pdffigs.close()
