import argparse
import subprocess
import csv


parser = argparse.ArgumentParser(description='Description for -h flag')
parser.add_argument('-p', '--path', type=str, metavar='', required=True, help='Path to directory')
args = parser.parse_args()

try:
    results = []
    subprocess.run(r"find " + str(args.path) + r" -type f | awk -F. '{print $NF}' | grep -v / | sort | uniq > extensions_with_loc.txt", shell=True)
    with open(r'extensions_with_loc.txt', 'r', newline='', encoding='utf-8') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for i in spamreader:
            dict_with_results = {
                'extension' : i[0],
                'loc' : int(subprocess.check_output(r"find " + str(args.path) + r" -name '*'." + str(i[0]) + " -exec cat {} ; | wc -l", shell=True)) + 1} # + 1 cause function counting '\n'
            results.append(dict_with_results)
    with open(r'extensions_with_loc.txt', 'w', newline='', encoding='utf-8') as csvfile:
        field_names = ['extension','loc']
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        headers = csv.writer(csvfile, delimiter=",")
        headers.writerow(('extension','loc'))
        for i in results:
            writer.writerow(i)
            
except Exception as error:
    print(error)