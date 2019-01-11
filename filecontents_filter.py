import re

def exclude_line_data_has_regex(file_in=None, regex=None):
    with open(file_in, mode='r') as fi:
        for line in fi:
            if not re.match(regex, line.strip()):
                yield line.strip()

with open('out.txt', mode='w') as fo:
    for line in exclude_line_data_has_regex(file_in=r'C:\Users\22222\Desktop\YE\BIN_SITE_DUT.txt', regex='.*0x0000010000.*'):
        fo.write('{}\n'.format(line))
