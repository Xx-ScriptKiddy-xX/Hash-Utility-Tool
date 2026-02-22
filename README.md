# Hash Utility Tool

<img width="600" alt="Hash Utility Tool Icon" src="https://github.com/user-attachments/assets/16720c74-c3ca-43e0-b4a0-2d7589681120" />

**Hash Utility Tool** is a lightweight command-line application for calculating and verifying file hashes. Built with Python and Tkinter, it allows users to quickly generate hashes, compare files for integrity, and verify data authenticity using multiple algorithms.

---

## Key Features

- Hash Calculation – Generate cryptographic hashes for any file.
- Hash Comparison – Compare a file’s hash against a known value to verify integrity.
- Multiple Algorithms – Supports SHA256, MD5, and SHA1.
- File Selection Dialog – Select files using a built-in file browser.
- Drag-and-Drop Support – Accepts files passed via command line.
- Error Handling – Detects invalid files, missing paths, and unsupported algorithms.
- Console-Based Interface – Simple terminal-based menu system.
- Cross-Platform – Works on Windows and other supported systems.

---

## Built With

- Python
- Tkinter – File dialog interface
- hashlib – Cryptographic hashing
- os / sys – System and file handling

---

## Usage

1. Launch the program.
2. Drag and drop a file onto the executable (optional).
3. Choose an option from the menu:
   - M – Compare a file hash
   - C – Calculate a file hash
   - Q – Quit
4. Enter the required hash and algorithm when prompted.
5. View the results in the console.
<img width="840" height="470" alt="Tutorial" src="https://github.com/user-attachments/assets/f8f441c0-bedf-40ef-8802-2e308eea6585" />


---

## Notes

- Both the compiled executable and source code are available in this repository and in the Releases tab.
- Supports common cryptographic verification workflows.

---

## License

This project is open source under the MIT License.
