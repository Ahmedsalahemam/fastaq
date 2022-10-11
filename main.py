def readd(fileread):
    sequances=[]
    qualities=[]
    filee=open(fileread)
    while True:
        filee.readline()
        seq=filee.readline().rstrip();
        filee.readline()
        quality = filee.readline().rstrip();
        if len(seq)==0:
            break;
        sequances.append(seq)
        qualities.append(quality)
    return sequances,qualities;
def phred33(quality):
    return ord(quality)-33

def createhist(lq):
    hist=[0]*50;
    for strg in lq:
        for chra in strg:
            q=phred33(chra)
            hist[q]+=1;
    return hist;
#main
s1,q1=readd("gblab1.fastq")
print(q1)
h=createhist(q1)
print(h)









