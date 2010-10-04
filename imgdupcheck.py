"""
author: dan coughlin
date: 2010-09-14
file: checkdupe.py
"""

import os
import glob
import Image


def is_same_image(image1, image2):
    """ Takes two image files and compares them to see if they are the same
    arguments should each be an Image instance
    """
    return image1.histogram() == image2.histogram()


def check_images(path, quiet=True, recursive=False):
    """ Takes a path to a directory and checks each file against each other to
    determine if there are any duplicates.  If so, paths to both files are
    printed
    """
    histogram_map = {
        # '[0, "..."]': ['file1', 'file2'],
        }
    # loop over files in directory to look at
    if recursive:
        fileset = []
        for root, dirs, files in os.walk(path):
            if files:
                for f in files:
                    fileset.append(os.path.join(root, f))
    else:
        fileset = glob.glob(os.path.join(path, '*.*'))

    for filename in fileset:
        # get histogram to compare against the rest
        # coerce to string for easy reverse lookup
        try:
            histogram = str(Image.open(filename).histogram())
        except IOError:
            # not an Image -- skip it
            continue
        if histogram in histogram_map:
            histogram_map[histogram].append(filename)
        else:
            histogram_map[histogram] = [filename]
    duplicates = [l for l in histogram_map.values() if len(l) > 1]
    if not quiet:
        for duplicate in duplicates:
            print "\t".join(duplicate)
    return duplicates


def main():
    import optparse
    parser = optparse.OptionParser("Usage: %prog [options] /path/to/directory")
    parser.add_option("-q", dest="quiet", action="store_true", default=False,
                      help="quiet output")
    parser.add_option("-r", dest="recursive", action="store_true",
                      default=False, help="recursively search for images")
    options, args = parser.parse_args()

    if len(args) != 1:
        parser.print_help()
        return

    path = args[0]

    if os.path.isdir(path):
        check_images(path, options.quiet, options.recursive)
    else:
        raise Exception("%s is not a directory" % path)
