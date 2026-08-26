# File Handling

## **About**
- Collection of Python programs demonstrating file input/output operations
- Covers file modes (read, write, append) and exception handling
- Uses try-except-finally for robust file operations
- Includes seek() and tell() for file pointer manipulation

## **Purpose**
- Learn and practice file handling in Python
- Understand exception handling with files
- Master file modes and file pointer operations
- Build robust file I/O automation scripts

## **Programs Included**

**FileIO1.py**
- Basic file opening without modes
- Simple file object creation
- Foundation for file operations

**FileIOException.py**
- Demonstrates try-except-finally structure
- Handles FileNotFoundError exception
- Shows proper exception handling flow

**FileIOExceptionX.py**
- Opens file in read mode explicitly
- Uses "r" mode parameter
- Exception handling for read operations

**FileIOExceptionWrite.py**
- Opens file in write mode
- Uses "w" mode parameter
- Exception handling for write operations

**FileIOExceptionWriteX.py**
- Writes content to file
- Uses fobj.write() method
- Proper file closing with fobj.close()

**FileIOExceptionAppend.py**
- Appends data to existing file
- Uses "a" mode parameter
- Preserves existing file content

**FileIOExceptionRead.py**
- Reads entire file content
- Uses fobj.read() without parameters
- Displays complete file data

**FileOperationReadX.py**
- Reads specific number of characters
- Uses fobj.read(6) with parameter
- Partial file reading technique

**FileIOExceptionReadTell.py**
- Demonstrates tell() function
- Shows current file pointer position
- Tracks offset before and after reading

**FileIOExceptionReadSeek.py**
- Uses seek() to move file pointer
- Seeks from beginning of file
- Combines seek() and read() operations

**FileIOExceptionReadSeekXX.py**
- Advanced seek() with parameters
- Seeks from current position (mode 1)
- Alternative seek reference points

**FileIOFunctions.py**
- Demonstrates file object properties
- Uses fobj.name, fobj.mode, fobj.closed
- Shows file metadata information

**FileIOFunctionsX.py**
- File object method properties
- Uses readable(), writable(), seekable()
- Checks file capabilities

## How to Run
bash
# Run any program
python FileIO1.py
python FileIOException.py
python FileIOExceptionRead.py

# And so on...

## Key Concepts
- File modes: "r" (read), "w" (write), "a" (append)
- try-except-finally: Exception handling structure
- FileNotFoundError: Exception for missing files
- fobj.read(): Read entire or partial file content
- fobj.write(): Write content to file
- fobj.close(): Close file object
- fobj.tell(): Get current file pointer position
- fobj.seek(): Move file pointer to specific position
- File properties: name, mode, closed status

## Technologies Used
- Python 3.x
- Built-in file operations
- Exception handling
- File object methods

## Learning Path
- Start with FileIO1.py (basic file opening)
- Learn FileIOException.py (exception handling)
- Practice FileIOExceptionWrite.py (write operations)
- Master FileIOExceptionRead.py (read operations)
- Advance to FileIOExceptionReadSeek.py (pointer manipulation)
- Understand FileIOFunctions.py (file properties)

## Notes
- Always close files after use
- Use try-except for error handling
- Different modes have different behaviors
- File pointer position affects read/write operations
- Use seek() to navigate file content efficiently
