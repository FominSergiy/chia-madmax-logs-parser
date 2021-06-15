import sys
import re
from datetime import datetime as dt

# use this to find out more https://regex101.com/
# https://regex101.com/r/G2o0h9/1
PATTERN = r'^(Total plot creation time was ([0-9]{1,6}\.?[0-9]{1,2}) sec)'
TODAY = dt.now().strftime('%Y-%m-%d %H:%M:%S.%f')

# create placeholder for files
total_plot_logs = open(f'logging {TODAY}.txt', 'w')
numbers_only = open(f'total_plots_time {TODAY}.txt', 'w')
base_str = ''

# read piped inputs and save them into a base string
# to be used to extract the pattern
for line in sys.stdin:
    base_str = base_str + '\n' + line

# returns an array of tuples
# elem at index 0 contains full string
# elem at index 1 contains only num of secs
all_matches = re.findall(PATTERN, base_str, flags=re.MULTILINE)
total_matches = len(all_matches)

# save totals
total_plot_logs.write(f'Total Number Of Matches: {total_matches}\n\n')
numbers_only.write(f'Total Number Of Matches: {total_matches}\n\n')

# write each find into .txt file
for match in all_matches:
    total_plot_logs.write(match[0] + '\n')
    numbers_only.write(match[1] + '\n')

# close files when everything is written
total_plot_logs.close()
numbers_only.close()
