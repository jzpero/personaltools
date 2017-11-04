import PyPDF2
import argeparse

parser = argeparse.ArgumentParser(description='Merges PDFs together.')
parser.add_argument('filename', nargs='+',type=argparse.FileType('r'), help='PDF files to merge together.')
args = parser.parse_args()

def main():
	print args

if __name__ == '__main__':
	main()