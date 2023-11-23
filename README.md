# confirm.py

This is a simple script that helps automate the mindbogglingly dull and error-prone process of verifying the submission of student results at the University of Melbourne.

## Assumptions and prerequisites

1. You have Python 3+ installed on your computer.
2. You have access to a terminal emulator on your computer.
3. You have the CSV file with the marks that you submitted (a fictitious example is provided in this repository).
4. You have copied-and-pasted into a plain text file the student rows from the result confirmation webpage, starting just before the student id of the first student row and ending at the end of the last student row (a fictitious example of this is also provided).
5. (Not really under your control) Melbourne Uni has not changed too drastically the format of the CSV files for submitting results, nor the format of the result confirmation webpage.  This version of the script has last been checked to work for semester 2, 2023.

## What to do

If you have successfully verified assumptions 1-4 listed above, you proceed as follows.

1. Clone this repository onto your computer, or simply [download only confirm.py from this link][raw].
2. Copy the file `confirm.py`, your CSV file with the marks, and the copied-and-pasted text file, into the same directory.
3. In the terminal and the directory with these files, run
```
python confirm.py -l NAME_OF_LOCAL_CSV_FILE -r NAME_OF_REMOTE_TXT_FILE
```
Optionally, add a ```-v``` argument to have the script print all the rows as it checks them (otherwise, default behaviour is to only print conflicts, if any exist).

That's all.

I tested this on some Linux machines and a MacBook.
The code is not using anything operating-system-specific though, so it **should** work on anything capable of running Python.

[raw]: https://raw.githubusercontent.com/aghitza/unimelb-confirm-results/master/confirm.py
