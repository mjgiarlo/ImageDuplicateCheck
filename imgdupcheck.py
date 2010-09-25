"""
author: dan coughlin
date: 2010-09-14
file: checkdupe.py
"""

import os
import glob
import Image


histogram_map = {
    # '[0, "..."]': ['file1', 'file2'],
}

def is_same_image(image1, image2):
    """ Takes two image files and compares them to see if they are the same both
    arguments expect to be created from the result of: 
    Image.open(/path/to/image.ext)
    """
    return image1.histogram() == image2.histogram()

def check_images(path, quiet=True):
    """ Takes a path to a directory and checks each file against each other to
    determine if there are any duplicates.  If so, paths to both files are 
    printed
    """
    # loop over files in directory to look at
    for filename in glob.glob(os.path.join(path, '*.*')): 
        if not quiet:
            print "Examining %s" % filename
        # get histogram to compare against the rest
        # coerce to string for easy reverse lookup
        histogram = str(Image.open(filename).histogram())
        if histogram in histogram_map:
            histogram_map[histogram].append(filename)
            if not quiet:
                print "Duplicates\n%s" % "\t".join(histogram_map[histogram])
        else:
            histogram_map[histogram] = [filename]
    if not quiet:
        for duplicates in histogram_map.values():
            print "\t".join(duplicates)
    return histogram_map.values()
        
def main():
    import optparse
    parser = optparse.OptionParser("Usage: %prog [options] /path/to/directory")
    parser.add_option("-q", dest="quiet", action="store_true", default=False,
                      help="quiet output")
    options, args = parser.parse_args()
    
    if len(args) != 1:
         parser.print_help()
         return
                          
    path = args[0]
 
    if os.path.isdir(path):
        if not options.quiet:
            print "Checking for duplicate images in:\n%s\n" % path 
        check_images(path, options.quiet)
    else:
        raise Exception("%s is not a directory" % path)
        
    if not options.quiet:
        print "done."
