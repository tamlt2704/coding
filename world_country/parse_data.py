from collections import defaultdict

d = defaultdict(list)
def get_ccode(x):
    return x[0]

with open('data/countries.csv', 'r') as f:
    f.readline()
    for line in f:
        # get country name and country code
        cname = ''.join(line.split(',')[:-1]).strip()
        ccode = line.split(',')[-1].strip()
        d[ccode[0]].append((ccode, cname))

with open('output.txt', 'w') as f:
    for ccode in sorted(d.keys()):
        f.write('{}\n'.format(ccode))
        for country in sorted(d[ccode], key=get_ccode):
            f.write('\t{:2s}\t{}\n'.format(country[0], country[1]))
