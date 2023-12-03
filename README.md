# PDF parser

Simple UI to start parsing selective pdf and zip files containing pdf files

> :warning: **The program is designed for certain PDF files and will not parse files that do not belong to them!**:

Running PDF parser requires:

* Python 3.11 (tested under Python 3.11.2)

--- 
### Installing Dependencies

```bash
pip install -r requirements.txt
```
---

### Running
```bash
python main.py
```

---

### Core Implementation


The program uses one main process and several child processes. The main process creates a queue and launches the UI, a process is also launched that listens to the queue and performs parsing when files are found in the queue

The UI is laid out in a simple way, you click on a button to open a file browser window and select pdf or zip files. Next, the selected files are transferred to the queue in the form of a list.

After parsing is completed, an output xlsx file with the name of today's date will appear on the desktop

The parsing process reads the text from the file and begins to separate the information at the beginning of the table by the content in the line with 'LINE', 'OPCODE', 'TECH', 'TYPE', etc.
The end of each table row is determined by the content 'PARTS', 'LABOR', 'OTHER', 'TOTAL LINE'.
And the beginning of a table row must begin with a letter and in alphabetical order.
Further, to determine the component part of the table row, the row with the deepest tabulation and containing two floating-point digits at the end is found.
After that, any information will be separated by spaces and will be matched with the found line from the table.
