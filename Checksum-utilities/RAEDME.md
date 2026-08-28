## Checksum Utilities

### About

- Collection of Python programs for file integrity verification
- Uses MD5 hashing algorithm for checksum calculation
- Detects duplicate files and verifies file integrity
- Useful for data security and file management

### Purpose

- Learn file integrity verification using checksums
- Understand hash functions and duplicate file detection
- Learn checksum comparison techniques
- Build automated file validation scripts

### Programs Included

#### ChecksumCalculateDirectory.py

- Calculates MD5 checksum for all files in a directory
- Reads files in chunks for memory efficiency
- Uses `hashlib.md5()` for checksum calculation
- Displays filename with the corresponding checksum
- Recursively processes all subdirectories

#### ChecksumCalculateDirectoryStore.py

- Calculates checksums and stores them in a dictionary
- Detects duplicate files by comparing checksums
- Identifies files with matching checksums
- Displays duplicate file groups
- Removes duplicate files automatically
- Generates a report of deleted duplicate files

### How to Run

```bash
python ChecksumCalculateDirectory.py
python ChecksumCalculateDirectoryStore.py
```

### Key Concepts

- **Checksum** – Hash value representing file content
- **MD5 Hashing** – Cryptographic hash algorithm
- **File Integrity** – Verifying whether file content has been modified
- **Duplicate Detection** – Finding files with identical content
- **Hash Comparison** – Comparing checksum values
- **Buffer Reading** – Efficiently processing large files in chunks
- **Dictionary Storage** – Organizing checksums using a dictionary

### Technologies Used

- Python 3.x
- `hashlib` module
- `os` module
- MD5 hashing algorithm
- Dictionary data structure

### Learning Path

- Start with `ChecksumCalculateDirectory.py` for calculating file checksums
- Practice checksum calculation using `hashlib.md5()`
- Learn `ChecksumCalculateDirectoryStore.py` for storing checksums
- Understand duplicate file detection using checksum comparison
- Learn duplicate file removal
- Practice generating duplicate removal reports

### Notes

- Files are read in 1000-byte chunks for efficient processing
- Files with the same checksum may have identical content
- Duplicate files can be removed to save storage space
- Hashing allows efficient comparison of file contents
- Always create a backup before removing duplicate files
- MD5 is suitable for basic integrity checks but is not recommended for
security-sensitive cryptographic applications
