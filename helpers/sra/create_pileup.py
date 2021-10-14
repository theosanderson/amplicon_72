import pysam
import glob
import sys


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


bam_files_locator = "/mnt/d/bam/*.sorted.bam"
# Get list of all BAMs
bam_files = glob.glob(bam_files_locator)
for file in bam_files:
    filename = file.split("/")[-1]
    #print(filename)
    try:
        samfile = pysam.AlignmentFile(file, "rb")
        eprint("Successfully processing file: " + filename)
    except ValueError:
        eprint("File is not a BAM file")
        continue
    for pileupcolumn in samfile.pileup("NC_045512.2", 21985, 21989):
        if pileupcolumn.pos in [21986]:

            for pileupread in pileupcolumn.pileups:
                if not pileupread.is_del and not pileupread.is_refskip:
                    # query position is None if is_del or is_refskip is set.
                    print("\t".join([
                        filename,
                        str(pileupcolumn.pos),
                        str(pileupread.alignment.query_sequence[
                            pileupread.query_position]),
                        str(pileupread.alignment.reference_start),
                        str(pileupread.alignment.reference_end)
                    ]))

    samfile.close()
