#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Paste file to paste.ubuntu.com"""

from sys import argv
from os.path import splitext
from urllib import request, parse


POSTER = 'yungkcx'  # This is my ID, use yours

SYNTAXES = [
    'text', 'Cucumber', 'abap', 'ada', 'ahk', 'antlr', 'antlr-as',
    'antlr-cpp', 'antlr-csharp', 'antlr-java', 'antlr-objc', 'antlr-perl',
    'antlr-python', 'antlr-ruby', 'apacheconf', 'applescript', 'as', 'as3',
    'aspx-cs', 'aspx-vb', 'asy', 'basemake', 'bash', 'bat', 'bbcode',
    'befunge', 'blitzmax', 'boo', 'c', 'c-objdump', 'cfm', 'cfs', 'cheetah',
    'clojure', 'cmake', 'coffee-script', 'common-lisp', 'console',
    'control', 'cpp', 'cpp-objdump', 'csharp', 'css', 'css+django',
    'css+erb', 'css+genshitext', 'css+mako', 'css+myghty', 'css+php',
    'css+smarty', 'cython', 'd', 'd-objdump', 'delphi', 'diff', 'django',
    'dpatch', 'duel', 'dylan', 'erb', 'erl', 'erlang', 'evoque', 'factor',
    'felix', 'fortran', 'gas', 'genshi', 'genshitext', 'glsl', 'gnuplot',
    'go', 'gooddata-cl', 'groff', 'haml', 'haskell', 'html', 'html+cheetah',
    'html+django', 'html+evoque', 'html+genshi', 'html+mako', 'html+myghty',
    'html+php', 'html+smarty', 'html+velocity', 'hx', 'hybris', 'ini', 'io',
    'ioke', 'irc', 'jade', 'java', 'js', 'js+cheetah', 'js+django', 'js+erb',
    'js+genshitext', 'js+mako', 'js+myghty', 'js+php', 'js+smarty', 'jsp',
    'lhs', 'lighty', 'llvm', 'logtalk', 'lua', 'make', 'mako', 'maql',
    'mason', 'matlab', 'matlabsession', 'minid', 'modelica', 'modula2',
    'moocode', 'mupad', 'mxml', 'myghty', 'mysql', 'nasm', 'newspeak',
    'nginx', 'numpy', 'objdump', 'objective-c', 'objective-j', 'ocaml',
    'ooc', 'perl', 'php', 'postscript', 'pot', 'pov', 'prolog', 'properties',
    'protobuf', 'py3tb', 'pycon', 'pytb', 'python', 'python3', 'ragel',
    'ragel-c', 'ragel-cpp', 'ragel-d', 'ragel-em', 'ragel-java', 'ragel-objc',
    'ragel-ruby', 'raw', 'rb', 'rbcon', 'rconsole', 'rebol', 'redcode',
    'rhtml', 'rst', 'sass', 'scala', 'scaml', 'scheme', 'scss', 'smalltalk',
    'smarty', 'sourceslist', 'splus', 'sql', 'sqlite3', 'squidconf', 'ssp',
    'tcl', 'tcsh', 'tex', 'trac-wiki', 'v', 'vala', 'vb.net',
    'velocity', 'vim', 'xml', 'xml+cheetah', 'xml+django', 'xml+erb',
    'xml+evoque', 'xml+mako', 'xml+myghty', 'xml+php', 'xml+smarty',
    'xml+velocity', 'xquery', 'xslt', 'yaml'
]

EXT_TO_SYNTAX = {
    'js': 'js', 'scm': 'scheme', 'sql': 'sql', 'vim': 'vim', 'gas': 'gas',
    'erb': 'erb', 'vimscript': 'vim', 'm': 'matlab', 'php': 'php', 'java':
    'java', 'css': 'css', 'sh': 'bash', 'ada': 'ada', 'mysql': 'mysql',
    'erl': 'erl', 'list': 'sourceslist', 'yaml': 'yaml', 'c': 'c', 'jsp':
    'jsp', 'diff': 'diff', 'scala': 'scala', 'pl': 'perl', 'pot': 'pot',
    'xhtml': 'xhtml', 'tex': 'tex', 'go': 'go', 'vb': 'vn.net', 'i': 'c',
    'ps': 'postscript', 'bat': 'bat', 'rb': 'rb', 'tcl': 'tcl', 'irc': 'irc',
    'perl': 'perl', 'lua': 'lua', '.cc': 'cpp', 'mxml': 'mxml', 'lhs':
    'lhs', 'html': 'html', 'cpp': 'cpp', 'sass': 'sass', 'hs': 'haskell',
    'pof': 'pof', 'coffee': 'coffee-script', 'py': 'python', 'pas': 'delphi',
    'clisp': 'common-lisp', 'prolog': 'prolog', 'pm': 'perl', 'cxx': 'cpp',
    'as': 'as', 'cs': 'csharp', 'as3': 'as3', 'xml': 'xml', 'scss': 'scss'
}


def usage():
    """print usage and exit"""
    print('Usage: pasteubuntu filename[.suffix] [syntax]')
    exit(1)


def error(message):
    """print error message and exit"""
    print('Error: ' + message + '!')
    exit(2)


def get_syntax(filename):
    """return syntax by suffix of the filename or plain"""
    syntax = 'text'
    _, ext = splitext(filename)
    ext = ext.lstrip('.')
    if ext in EXT_TO_SYNTAX:
        syntax = EXT_TO_SYNTAX[ext]
    return syntax


def main():
    """post"""
    file_content = ''
    url = 'http://paste.ubuntu.com/'
    syntax = ''
    if len(argv) < 2 or len(argv) > 3:
        usage()
    elif len(argv) == 3:
        if argv[2] not in SYNTAXES:
            error('invalid syntax option')
        syntax = argv[2]
    else:
        syntax = get_syntax(argv[1])
    print('use syntax: ' + syntax)
    with open(argv[1], 'r', encoding='utf-8') as file:
        file_content = file.read()
    data = {
        'poster': POSTER,
        'syntax': syntax,
        'content': file_content
    }
    data = parse.urlencode(data).encode('utf-8')
    resp = request.urlopen(url=url, data=data)
    if resp.code != 200:
        error('status code ' + resp.code)
    elif len(resp.url[24:]) < 8:
        error('paste failed')
    print(resp.url)


if __name__ == '__main__':
    main()

