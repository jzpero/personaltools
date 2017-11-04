import PyPDF2
import argparse
import re

parser = argparse.ArgumentParser(description='Merges PDFs together.')
parser.add_argument('filenames', nargs='+',type=str, help='PDF files to merge together.')
parser.add_argument('-r',type=str,nargs='+',dest='ranges', help="Ranges (Python slicing notation)")
parser.add_argument('-a',action='store_true')
parser.add_argument('-o', dest='outfilename', type=str, help="output filename")
args = parser.parse_args()

alternate = False
if args.a:
    alternate = True

def main():
    print args
    merger = PyPDF2.PdfFileMerger()
    with open(args.outfilename,'w') as file:
        for idx,inputfile in enumerate(args.filenames):
            with open(inputfile, 'r') as inputpdf:
                if args.ranges:
                    curr_range = args.ranges[idx]
                    num_list = re.split('[\[:\]]',curr_range)
                    num_list = map(int,filter(None,num_list))
                    range_tuple = tuple(num_list)
                    merger.append(inputpdf,pages=range_tuple,import_bookmarks=False)
                else:
                    merger.append(inputpdf,import_bookmarks=False)
        merger.write(file)
    merger.close()

if __name__ == '__main__':
	main()