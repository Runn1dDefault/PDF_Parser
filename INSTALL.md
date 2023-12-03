## Exe file build instructions for windows

### 1. Install Pyinstaller

```bash
pip install pyinstaller==5.3
```
---

### 2. Create a spec file template

```bash
pyinstaller --onefile --name touchtracer .\main.py
```

---

### 3. Manipulations in the spec file

> Replace variable 'a' with argument values 'hiddenimports' to ['pandas', 'tkinter']

> add multiprocessing.freeze_support() function call in main.py file  to support multiprocessing

> :warning: **required!**:
```text
# required after the line if __name__ == "__main__":
if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()
```
---

### 4. Run Build
```bash
pyinstaller .\main.spec
```

> After the build and dist folders are created
> The dist folder should contain the compiled exe file

---

#### Import errors I encountered. The solution was a simple installation

```bash
pip install opencv-python==4.6.0.66
```

```bash
pip install pyparsing==3.0.9
```

```bash
pip install pyenchant==3.2.2
```
