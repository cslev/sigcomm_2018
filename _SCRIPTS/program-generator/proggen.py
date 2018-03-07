
def proggen(worksheet, values, outdir):
    """
    TODO: could use some template engine here instead of just writing out the html/php .. 
    but the page is pretty simple, so this should do.
    """
    output = os.path.join(outdir, worksheet + '.php')
    print("Generating prog %s ..."%(output))

    f = codecs.open(output, mode='w', encoding='ascii', errors='html_replace')

    f.write("""  <div id="%s-program" class="%s-program">\n""" % (worksheet, worksheet))

    f.write("""    <ul class="program" data-role="listview" data-filter="true" data-inset="true" data-theme="d" data-dividertheme="a" placeholder="Filter program...">\n<?php\n""")
    progdate = ""
    for i,row in enumerate(values):
        if (len(row)<1):
            continue
        row = [item.strip() for item in row]
        line = None

        type = row[COL_TYPE]



        elif ((type == 'poster' or type == 'demo' or type == 'paper') and len(row)>=4):






        if (line != None):
            f.write(line)

    f.write("""?>\n    </ul>\n  </div>\n""")
    f.close()

