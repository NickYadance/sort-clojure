import re
import fileinput
import os
import sys

require_start_pattern = re.compile("\s*\(:require.*")
require_end_pattern = re.compile(".*\)")
namespace_pattern = re.compile("\[.*]")
clj_filename_pattern = ".clj"


def get_ns_and_sort(filename):
    ns = []
    with open(filename, "r") as file:
        line = file.readline()
        while line:
            if require_start_pattern.match(line):
                while namespace_pattern.search(line):
                    ns.append(namespace_pattern.search(line).group(0))
                    if require_end_pattern.match(line):
                        break
                    else:
                        line = file.readline()
                ns.sort()
                replace(filename, ns)
                return
            line = file.readline()


def replace(filename, ns):
    newns = []
    with fileinput.FileInput(filename, inplace=True) as file:
        line = file.readline()
        while line:
            if require_start_pattern.match(line):
                ns_count = 0
                while namespace_pattern.search(line) \
                        and ns_count < len(ns):
                    newns.append(namespace_pattern.search(line).group(0))
                    replace_line = re.sub("\[.*]", ns[ns_count], line)
                    print(replace_line, end="")
                    ns_count = ns_count + 1
                    line = file.readline()
            print(line, end="")
            line = file.readline()
    d = differ(ns, newns)
    if d > 0:
        print(filename, ": rewriting [", d, "] namespaces")


def differ(ns1, ns2):
    c = 0
    for k, v in enumerate(ns1):
        if v != ns2[k]:
            c = c + 1
    return c


def handle(dirname):
    for root, _, filenames in os.walk(dirname):
        for filename in filenames:
            if clj_filename_pattern in filename:
                get_ns_and_sort(os.path.join(root, filename))


def usage():
    print("""
    Sort .clj namespaces
    example:
        python sort.py /path/to/clojure
    """)


def error(e):
    print("""
    Error:
    """, e)


def main(argv):
    if len(argv) < 2:
        usage()
        exit(-1)

    dirname = argv[1]
    if not os.path.isdir(dirname):
        error("Invalid dir")
        exit(-2)

    print("Target: ", dirname)
    handle(dirname)


if __name__ == '__main__':
    main(sys.argv)
