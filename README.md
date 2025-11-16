📖 Bible Chapters Finder

A simple and interactive Python command-line tool that tells you how many chapters are in any book of the Bible. Enter any of the 66 books and instantly get its chapter count, with clean validation and a peaceful exit message.

✨ Features

🔍 Look up any Bible book (Old & New Testament)

✔️ Input validation — detects misspellings or invalid books

🔁 Repeat mode — search multiple books in a single run

🎨 Optional ASCII-art logo (via art.py)

📜 Encouraging Scripture on exit

🐍 Lightweight Python script — no dependencies needed

📦 Requirements

Python 3.8+

A terminal or command prompt

🚀 How to Run (Terminal)

Clone the repository:

git clone https://github.com/YOUR-USERNAME/bible-chapters-finder.git


Navigate into the project folder:

cd bible-chapters-finder


Run the script:

python3 bible_chapters.py

🖥️ Example Usage
Type in a book from the Bible to find out how many chapters are in it: john
John has 21 chapters

If you want to figure out the chapters for another book enter 'y', otherwise press any key to exit: y

Type in a book from the Bible to find out how many chapters are in it: psalms
Psalms has 150 chapters

If you want to figure out the chapters for another book enter 'y', otherwise press any key to exit:
Remember John 14:27, when Jesus said "Peace I leave with you..."

📁 Project Structure
bible-chapters-finder/
│── bible_chapters.py   # Main program logic
│── art.py              # ASCII logo (optional)
└── README.md           # Project documentation

🧠 How It Works

Loads a full list of all 66 Bible books

Prompts the user to enter a book name

Checks for a valid match:

If valid → prints chapter count

If invalid → asks again

Asks if the user wants to look up another book

Exits with a Scripture message
