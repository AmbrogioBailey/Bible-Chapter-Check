📖 Bible Chapters Finder

A simple, interactive Python CLI tool that tells you how many chapters are in any book of the Bible. Users can type a book name, get the chapter count instantly, and continue searching for as many books as they want.

The program includes input validation, clean looping logic, and a closing Scripture encouragement.

✨ Features

🔍 Search by any Bible book (Old or New Testament)

✔️ Input validation — catches misspellings or non-Bible books

🔁 Repeat mode — look up multiple books in the same run

📜 Full 66-book list included

🙏 Encouraging verse on exit

🎨 Custom ASCII logo support (via art module import)

📦 Tech Stack
Tool	Purpose
Python 3	CLI-based input/output
warnings module	Suppresses syntax warnings
Custom art module	Displays ASCII banner/logo
▶️ How It Works

Program loads a list of all 66 Bible book names.

User types a book (e.g., Genesis, John, 1 Samuel).

Script checks if the book exists:

If valid, prints the chapter count.

If invalid, displays an error message.

User chooses whether to search again.

Program exits with John 14:27.

🖥️ Running the Program
python3 bible_chapters.py


When prompted, type any Bible book name, such as:

Type in a book from the Bible to find out how many chapters are in it: john
John has 21 chapters

📚 Example Session
Type in a book from the Bible to find out how many chapters are in it: psalms
Psalms has 150 chapters

If you want to figure out the chapters for another book enter 'y', otherwise press any key to exit: y

Type in a book from the Bible to find out how many chapters are in it: zephaniah
Zephaniah has 3 chapters

If you want to figure out the chapters for another book enter 'y', otherwise press any key to exit:
Remember John 14:27, when Jesus said "Peace I leave with you..."

🧩 Code Structure
project/
│── art.py            # Contains ASCII logo printed at startup
│── bible_chapters.py # Main logic and loop
└── README.md         # Project documentation
