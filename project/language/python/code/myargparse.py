import argparse
parse = argparse.ArgumentParser(
    prog='myprogram',
    description='my test parse',
    epilog= 'not konw what this is'
)
# add parse
parse.add_argument('--filename' , default= 'myfilename')
args = parse.parse_args()
print(args.filename)