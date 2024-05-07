from optparse import OptionParser

parser = OptionParser(usage="""%prog [options]""")
parser.add_option('-i', dest='input', help="input bedgraph")
parser.add_option('-o', dest='output', help="output wiggle,variableStep wiggle")

opts, args = parser.parse_args()


def convert_bedGraph_to_variableStep_wig(bedGraph_file, output_wig_file):
    with open(bedGraph_file, 'r') as input_file, open(output_wig_file, 'w') as output_file:

        current_chrom = ""
        for line in input_file:
            # skip lines that start with '#'
            if line.startswith('#'):
                continue

            parts = line.strip().split("\t")

            chrom = parts[0]
            start = parts[1]
            end = parts[2]
            value = parts[3]

            if chrom != current_chrom:
                output_file.write("variableStep chrom=%s\n" % chrom)
                current_chrom = chrom

            output_file.write("%s\t%s\n" % (start, value))


file_in = opts.input
file_out = opts.output
convert_bedGraph_to_variableStep_wig(file_in, file_out)
