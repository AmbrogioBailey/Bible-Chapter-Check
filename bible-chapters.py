from art import logo
import warnings
warnings.filterwarnings("ignore", category=SyntaxWarning)
book_names = ['genesis', 'exodus', 'leviticus', 'numbers',
              'deuteronomy', 'joshua', 'judges', 'ruth',
              '1 samuel', '2 samuel', '1 kings',
              '2 kings', '1 chronicles', '2 chronicles',
              'ezra', 'nehemiah', 'esther', 'job', 'psalms',
              'proverbs', 'ecclesiastes', 'song of solomon',
              'isaiah', 'jeremiah', 'lamentations',
              'ezekiel', 'daniel', 'hosea',
              'joel', 'amos', 'obadiah', 'jonah',
              'micah', 'nahum', 'habakkuk', 'zephaniah',
              'haggai', 'zechariah', 'malachi', 'matthew',
              'mark', 'luke', 'john', 'acts', 'romans',
              '1 corinthians', '2 corinthians', 'galatians', 'ephesians', 'philippians', 'colossians',
              '1 thessalonians', '2 thessalonians',
              '1 timothy', '2 timothy', 'titus', 'philemon',
              'hebrews', 'james', '1 peter', '2 peter', '1 john', '2 john', '3 john', 'jude', 'revelation']
def bible_chapters():
    chapters = 0
    """Gives you the amount of chapters in the Bible book you enter."""
    print(logo)
    running = True
    while running:
        book = input("Type in a book from the Bible to find out how many chapters are in it: ").lower()
        if book not in book_names:
            print("That is not a book in the Bible, make sure to check your spelling\n")
            continue
        if book == 'genesis':
            chapters = 50
            print(f"{book.title()} has {chapters} chapters")
        if book == 'exodus':
            chapters = 40
            print(f"{book.title()} has {chapters} chapters")
        if book == 'leviticus':
            chapters = 27
            print(f"{book.title()} has {chapters} chapters")
        if book == 'numbers':
            chapters = 36
            print(f"{book.title()} has {chapters} chapters")
        if book == 'deuteronomy':
            chapters = 34
            print(f"{book.title()} has {chapters} chapters")
        if book == 'joshua':
            chapters = 24
            print(f"{book.title()} has {chapters} chapters")
        if book == 'judges':
            chapters = 21
            print(f"{book.title()} has {chapters} chapters")
        if book == 'ruth':
            chapters = 4
            print(f"{book.title()} has {chapters} chapters")
        if book == '1 samuel':
            chapters = 31
            print(f"{book.title()} has {chapters} chapters")
        if book == '2 samuel':
            chapters = 24
            print(f"{book.title()} has {chapters} chapters")
        if book == '1 kings':
            chapters = 22
            print(f"{book.title()} has {chapters} chapters")
        if book == '2 kings':
            chapters = 25
            print(f"{book.title()} has {chapters} chapters")
        if book == '1 chronicles':
            chapters = 29
            print(f"{book.title()} has {chapters} chapters")
        if book == '2 chronicles':
            chapters = 36
            print(f"{book.title()} has {chapters} chapters")
        if book == 'ezra':
            chapters = 10
            print(f"{book.title()} has {chapters} chapters")
        if book == 'nehemiah':
            chapters = 13
            print(f"{book.title()} has {chapters} chapters")
        if book == 'esther':
            chapters = 10
            print(f"{book.title()} has {chapters} chapters")
        if book == 'job':
            chapters = 42
            print(f"{book.title()} has {chapters} chapters")
        if book == 'psalms':
            chapters = 150
            print(f"{book.title()} has {chapters} chapters")
        if book == 'proverbs':
            chapters = 31
            print(f"{book.title()} has {chapters} chapters")
        if book == 'ecclesiastes':
            chapters = 12
            print(f"{book.title()} has {chapters} chapters")
        if book == 'song of solomon':
            chapters = 8
            print(f"{book.title()} has {chapters} chapters")
        if book == 'isaiah':
            chapters = 66
            print(f"{book.title()} has {chapters} chapters")
        if book == 'jeremiah':
            chapters = 52
            print(f"{book.title()} has {chapters} chapters")
        if book == 'lamentations':
            chapters = 5
            print(f"{book.title()} has {chapters} chapters")
        if book == 'ezekiel':
            chapters = 48
            print(f"{book.title()} has {chapters} chapters")
        if book == 'daniel':
            chapters = 12
            print(f"{book.title()} has {chapters} chapters")
        if book == 'hosea':
            chapters = 14
            print(f"{book.title()} has {chapters} chapters")
        if book == 'joel':
            chapters = 3
            print(f"{book.title()} has {chapters} chapters")
        if book == 'amos':
            chapters = 9
            print(f"{book.title()} has {chapters} chapters")
        if book == 'obadiah':
            chapters = 1
            print(f"{book.title()} has {chapters} chapters")
        if book == 'jonah':
            chapters = 4
            print(f"{book.title()} has {chapters} chapters")
        if book == 'micah':
            chapters = 7
            print(f"{book.title()} has {chapters} chapters")
        if book == 'nahum':
            chapters = 3
            print(f"{book.title()} has {chapters} chapters")
        if book == 'habakkuk':
            chapters = 3
            print(f"{book.title()} has {chapters} chapters")
        if book == 'zephaniah':
            chapters = 3
            print(f"{book.title()} has {chapters} chapters")
        if book == 'haggai':
            chapters = 2
            print(f"{book.title()} has {chapters} chapters")
        if book == 'zechariah':
            chapters = 14
            print(f"{book.title()} has {chapters} chapters")
        if book == 'malachi':
            chapters = 4
            print(f"{book.title()} has {chapters} chapters")
        if book == 'matthew':
            chapters = 28
            print(f"{book.title()} has {chapters} chapters")
        if book == 'mark':
            chapters = 16
            print(f"{book.title()} has {chapters} chapters")
        if book == 'luke':
            chapters = 24
            print(f"{book.title()} has {chapters} chapters")
        if book == 'john':
            chapters = 21
            print(f"{book.title()} has {chapters} chapters")
        if book == 'acts':
            chapters = 28
            print(f"{book.title()} has {chapters} chapters")
        if book == 'romans':
            chapters = 16
            print(f"{book.title()} has {chapters} chapters")
        if book == '1 corinthians':
            chapters = 16
            print(f"{book.title()} has {chapters} chapters")
        if book == '2 corinthians':
            chapters = 13
            print(f"{book.title()} has {chapters} chapters")
        if book == 'galatians':
            chapters = 6
            print(f"{book.title()} has {chapters} chapters")
        if book == 'ephesians':
            chapters = 6
            print(f"{book.title()} has {chapters} chapters")
        if book == 'philippians':
            chapters = 4
            print(f"{book.title()} has {chapters} chapters")
        if book == 'colossians':
            chapters = 4
            print(f"{book.title()} has {chapters} chapters")
        if book == '1 thessalonians':
            chapters = 5
            print(f"{book.title()} has {chapters} chapters")
        if book == '2 thessalonians':
            chapters = 3
            print(f"{book.title()} has {chapters} chapters")
        if book == '1 timothy':
            chapters = 6
            print(f"{book.title()} has {chapters} chapters")
        if book == '2 timothy':
            chapters = 4
            print(f"{book.title()} has {chapters} chapters")
        if book == 'titus':
            chapters = 3
            print(f"{book.title()} has {chapters} chapters")
        if book == 'philemon':
            chapters = 1
            print(f"{book.title()} has {chapters} chapters")
        if book == 'hebrews':
            chapters = 13
            print(f"{book.title()} has {chapters} chapters")
        if book == 'james':
            chapters = 5
            print(f"{book.title()} has {chapters} chapters")
        if book == '1 peter':
            chapters = 5
            print(f"{book.title()} has {chapters} chapters")
        if book == '2 peter':
            chapters = 3
            print(f"{book.title()} has {chapters} chapters")
        if book == '1 john':
            chapters = 5
            print(f"{book.title()} has {chapters} chapters")
        if book == '2 john':
            chapters = 1
            print(f"{book.title()} has {chapters} chapters")
        if book == '3 john':
            chapters = 1
            print(f"{book.title()} has {chapters} chapters")
        if book == 'jude':
            chapters = 1
            print(f"{book.title()} has {chapters} chapters")
        if book == 'revelation':
            chapters = 22
            print(f"{book.title()} has {chapters} chapters")

        another = input("\nif you want to figure out the chapters for "
                        "another book in the Bible enter 'y', otherwise press any key to exit:  ").lower()
        if another == 'y':
            continue
        else:
            print('\nRemember John 14:27, when Jesus said '
                    '"Peace I leave with you; My peace I give to you; not as the world gives do I give to you.\n'
                    'Do not let your heart be troubled, nor let it be fearful."')
            running = False

bible_chapters()