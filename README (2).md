## PC Assistant

A simple command-line personal assistant for Windows, written in Python. Helps you quickly launch apps, manage bookmarks, and take notes — all from your terminal.

## Features

- Runs from a simple numbered menu interface
- Supported actions:
  - **Open Websites** – launch all saved URLs in your browser at once
  - **Add Website** – save a new URL to your favorites list
  - **Open Notepad** – quickly launch Windows Notepad
  - **Open Calculator** – quickly launch the Windows Calculator
  - **Take a Note** – jot something down and save it to a text file
  - **Show Notes** – view all your previously saved notes
- No external dependencies — uses Python standard library only

## Getting Started

### Requirements

- Python 3.x
- Windows OS (uses `os.startfile` to launch Notepad and Calculator)

### Run

```bash
python assistant.py
```

Press `7` then Enter to exit.

### Configuration

Open `assistant.py` to customize behavior. You can add new menu options and their corresponding functions to extend the assistant.

Data is saved in plain text files in the same directory:

```
favorite_websites.txt   # your saved URLs (one per line)
my_notes.txt            # your saved notes (one per line)
```

These are created automatically on first use and are excluded from version control via `.gitignore`.

### Run on Startup (Optional)

To have it launch automatically when Windows starts:

1. Press `Win + R`, type `shell:startup`, hit Enter
2. Create a `.bat` file in that folder with this content:

```bat
@echo off
python "C:\full\path\to\assistant.py"
```

## Contributing

You can check [CONTRIBUTING.md](CONTRIBUTING.md) for details!
