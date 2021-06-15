# crypto - data parser
This script takes the piped input and extracts a pattern.

## Suggested Use

### save your plottting into a log.txt file
Plotting takes some time and because of that we need to save it to a log fie first.
```bash
$ <run your command> &> logs.txt 
```

Once plotting is complete do the following

```bash
cat logs.txt | python3 stdin.py
```

- `&>` redirects the stdout and stderr to your log file
- `cat <filename>` sends the output to stdout
- `python3 stdin.py` runs the script
- `|` pipes are used to direct output as input to next command

### General overview
> pattern: `Total plot creation time was XXXXX.XX sec`

use test.txt to see this in action

```bash
$ cat test.txt | python3 stdin.py
```

### Regex used
```
^(Total plot creation time was ([0-9]{1,6}\.?[0-9]{1,2}) sec)
```

### Pre-Requisites
[python3](https://www.python.org/downloads/)