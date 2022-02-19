import argparse,os,sys

ls_parser=argparse.ArgumentParser(
    prog='pyls', # Setting the Name of the Program
    usage='%(prog)s [options] path', # Displaying a Custom Program Usage Help: where the [-h] option has been replaced by a generic [options] token.
    description='Script to display files and sub-directories for a given directory.', # for the text that is shown before the help text
    epilog='Have a pythonic day.', # for the text shown after the help text
    # prefix_chars='/', # Customizing the Allowed Prefix Chars :: now in place of '-' '/' is used in arguments and help text:: specially useful when developing script for windows
    fromfile_prefix_chars='@', # Setting Prefix Chars for Files That Contain Arguments to Be Included
)

ls_parser.add_argument(
    'Path',
    metavar='path', # ??
    type=str,
    help='Path of the target direcctory.'
)

parsed_ls=ls_parser.parse_args()

input_dir_path=parsed_ls.Path

if not os.path.isdir(input_dir_path): # check wether input is dir or not
    print('Input path is not a directory.')
    sys.exit()

print('\n'.join(os.listdir(input_dir_path)))