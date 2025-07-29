import os

from matplotlib.backends.backend_pdf  import PdfPages


def to_pdf(figobjs,fname='',category=''):
    if type(figobjs) not in [list,tuple]: figobjs = [figobjs]

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
    if fname[-4:].lower() == '.pdf':
       pdffigs = PdfPages(os.path.join(figurepath,fname))
    else:
       pdffigs = PdfPages(os.path.join(figurepath,'%s.pdf' % fname))

    if type(figobjs) not in [list,tuple]: figobjs = list(figobjs)
    for ifigobj in figobjs:
        pdffigs.savefig(ifigobj)
    pdffigs.close()


def to_png(figobjs,fname='',category=''):
    if type(figobjs) not in [list,tuple]: figobjs = [figobjs]

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
    if fname[-4:].lower() == '.png':
       path_to_figures = os.path.join(figurepath,fname[:-4])
    else:
       path_to_figures = os.path.join(figurepath,fname)

    for ifigobj in figobjs:
        ind = figobjs.index(ifigobj)
        ifigobj.savefig("%s_%02d.png" % (path_to_figures,ind))
