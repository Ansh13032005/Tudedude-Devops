# Linux Commands Assignment

This repository contains the solution for the Linux Commands Assignment.  
The assignment demonstrates basic Linux file management, file viewing, searching, compression, downloading files, permissions, and environment variables.

## Assignment Tasks

### 1. Creating and Renaming Files/Directories

#### Commands Used
```bash
mkdir test_dir
cd test_dir
touch example.txt
mv example.txt renamed_example.txt
```

#### Explanation
- `mkdir test_dir` → Creates a new directory named `test_dir`.
- `cd test_dir` → Moves into the directory.
- `touch example.txt` → Creates an empty file.
- `mv example.txt renamed_example.txt` → Renames the file.

---

### 2. Viewing File Contents

#### Commands Used
```bash
cat /etc/passwd
head -5 /etc/passwd
tail -5 /etc/passwd
```

#### Explanation
- `cat /etc/passwd` → Displays complete file contents.
- `head -5 /etc/passwd` → Displays first 5 lines.
- `tail -5 /etc/passwd` → Displays last 5 lines.

---

### 3. Searching for Patterns

#### Command Used
```bash
grep "root" /etc/passwd
```

#### Explanation
- Searches for all lines containing the word `root` in `/etc/passwd`.

---

### 4. Zipping and Unzipping

#### Commands Used
```bash
cd ..
zip -r test_dir.zip test_dir
mkdir unzipped_dir
unzip test_dir.zip -d unzipped_dir
```

#### Explanation
- `zip -r` → Compresses directory recursively.
- `unzip -d` → Extracts zip file into a target directory.

---

### 5. Downloading Files

#### Command Used
```bash
wget https://raw.githubusercontent.com/EbookFoundation/free-programming-books/main/LICENSE
```

#### Explanation
- Downloads a file using `wget`.

---

### 6. Changing Permissions

#### Commands Used
```bash
touch secure.txt
chmod 444 secure.txt
ls -l secure.txt
```

#### Explanation
- `touch secure.txt` → Creates a file.
- `chmod 444 secure.txt` → Makes the file read-only for everyone.
- `ls -l secure.txt` → Verifies permissions.

---

### 7. Working with Environment Variables

#### Commands Used
```bash
export MY_VAR="Hello, Linux!"
echo $MY_VAR
```

#### Explanation
- `export` → Creates an environment variable.
- `echo $MY_VAR` → Displays its value.

---

## Repository Structure

```plaintext
linux-assignment/
│── screenshots/
│   ├── step1.png
│   ├── step2.png
│   ├── step3.png
│   ├── ...
│── assignment.docx
│── README.md
```

## Screenshots
Screenshots of all commands and outputs are included in the `screenshots` folder.

## Tools Used
- Linux Terminal (Ubuntu)
- Git & GitHub

## Author
**Ansh Parikh**