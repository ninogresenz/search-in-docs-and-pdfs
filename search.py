#!/usr/bin/python3

import magic
import os
import pdftotext
import sys
import re
from tabulate import tabulate

PDF_MIME = 'application/pdf'
XLS_MIME = 'application/msexcel'
XLSX_MIME = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
SUPPORTED_MIMETYPES = [PDF_MIME, XLS_MIME, XLSX_MIME]


def get_files_from_dir(directory, recursive=False):
    all_items = os.listdir(directory)
    files = []
    for item in all_items:
        file = directory + '/' + item
        if os.path.isfile(file):
            files.append(file)
    return files


def filter_by_mimetypes(list_of_files=[], supported_mimetypes=[]):
    supported_files = []
    for file in list_of_files:
        mimetype = magic.from_file(file, mime=True)
        if mimetype in supported_mimetypes:
            supported_files.append({'path': file, 'mimetype': mimetype})
    return supported_files


def get_text_from_xlsx(file_path):
    pass

#
# def get_text_from_pdf(file_path):
#     with open(file_path, 'rb') as file:
#         pdf = PyPDF2.PdfFileReader(file)
#         complete_text = ''
#         for pageNumber in range(pdf.getNumPages()):
#             page = pdf.getPage(pageNumber)
#             complete_text += page.extractText()
#         return complete_text

def get_text_from_pdf2(file_path):
    with open(file_path, 'rb') as file:
        pdf = pdftotext.PDF(file)
        complete_text = ''
        for page in pdf:
            complete_text += page
        return complete_text



def get_text(file):
    if file.get('mimetype') == PDF_MIME:
        return get_text_from_pdf2(file.get('path'))
    elif file.get('mimetype') == XLSX_MIME:
        return 'not implemented'  # todo tbd
    elif file.get('mimetype') == XLS_MIME:
        return 'not implemented'  # todo tbd
    else:
        raise Exception('mimetype: "' + file.get('mimetype') + '" is not supported.')

def print_help():
    print('Usage:')
    print('search.py [options] [regex expression] [directory to search]')
    print('')
    print('Options: # not yet suppored')
    print('  -r --recursive\t search recursively through all folders')  # todo tbd
    print('')
    print('Supported files formats:')
    print('  PDF\tyes')
    print('  XLS\tnot yet')
    print('  XLSX\tnot yet')


if __name__ == '__main__':
    debug = False
    if len(sys.argv) < 3:
        print_help()
        exit(1)
    search = str(sys.argv[1])
    path = str(sys.argv[2])

    all_files = get_files_from_dir(path)
    supported_files = filter_by_mimetypes(all_files, SUPPORTED_MIMETYPES)

    if debug:
        print('Directory: ' + path)
        print('Recursive: ' + str(False))
        print('Searching supported in {0}/{1} files ...'.format(str(len(supported_files)), str(len(all_files))))
        print('-')
        print('Result:')

    result = []
    for file in supported_files:
        text = get_text(file)
        x = re.findall(search, text)
        matches = len(x)
        if matches > 0:
            result.append([str(matches), file.get('path')])
    print(tabulate(result, headers=['Matches', 'File'], tablefmt='plain'))
