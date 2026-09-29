# French Flashcard App 🇫🇷

A desktop flashcard app built with Python and Tkinter to help learn the most
frequently used French words. Cards start showing the French word, flip
automatically after 3 seconds to reveal the English translation, and track
which words you've already learned across sessions.

## Features

- Interactive flashcards with a front (French) and back (English) view
- Auto-flip after 3 seconds using Tkinter's non-blocking timer system
- Mark words as known (✓) or unknown (✗)
- Known words are removed from the deck and won't reappear
- Progress is saved to `data/words_to_learn.csv`, so your deck picks up
  where you left off next time you run the app
- Graceful "Done!" screen once every word has been learned

## Built With

- Python 3
- Tkinter — GUI
- pandas — reading/writing word data (CSV)

## How It Works

1. On launch, the app tries to load `data/words_to_learn.csv` (your
   in-progress deck). If that file doesn't exist yet, it falls back to the
   full word list in `data/french_words.csv`.
2. A random word is chosen and displayed on the front of the card.
3. After 3 seconds, the card flips to show the English translation.
4. Click ✓ if you knew it — the word is removed from the deck and saved.
5. Click ✗ if you didn't — a new random word is shown, but the current one
   stays in the deck for review later.

## Running the App

```bash
pip install pandas
python main.py
```

## Project Structure

├── main.py
├── data/
│ └── french_words.csv
├── images/
│ ├── card_front.png
│ ├── card_back.png
│ ├── right.png
│ └── wrong.png


## Future Improvements

- A "reset progress" button to start over from the full word list
- Support for additional languages
- Spaced repetition scheduling instead of pure random selection
