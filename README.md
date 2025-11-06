# 🚀 Typing Speed Test CLI

A colorful, interactive command-line typing speed test platform inspired by MonkeyType, featuring a vibrant terminal UI with enhanced rounded borders and a massive quote database.

## ✨ Features

- **Enhanced UI with Heavy Borders** - Stunning terminal interface with heavy, rounded box styles
- **Massive Quote Database** - 6,437+ real quotes from books, movies, songs, and more
- **Multiple Quote Lengths** - Choose between Short (0-100 chars), Medium (101-300), Long (301-600), and Very Long (601+)
- **TAB to Skip** - Don't like a quote? Press TAB to get a new random one instantly
- **Real-time Feedback** - Character-by-character color-coded typing feedback
  - ✅ Green for correct characters
  - ❌ Red for errors with highlighted background
  - 📍 Yellow cursor indicator
- **Quote Source Display** - See the source of each quote (book, movie, song, etc.)
- **Live Statistics** - Real-time WPM, accuracy, time, and progress tracking
- **Word History** - Detailed per-word typing performance analysis (top 15 displayed)
- **Local Leaderboard** - Persistent JSON-based score tracking with filtering
- **Offline & Open Source** - Runs completely locally, no internet required

## 🎮 How to Use

1. Run the application:
   ```bash
   python main.py
   ```

2. Navigate the menu using number keys (1-5)

3. Start a typing test:
   - Press `1` to start a test
   - Begin typing immediately (timer starts on first character)
   - Press `TAB` at any time to skip and get a new quote
   - Use backspace to correct mistakes
   - Get instant visual feedback with colored characters

4. View your results:
   - WPM (Words Per Minute)
   - Accuracy percentage
   - Total errors
   - Time taken
   - Word-by-word performance history

5. Save your score to the leaderboard

## 📊 Quote Lengths

- **Short** - 0-100 characters (~15-20 words)
- **Medium** - 101-300 characters (~20-60 words)
- **Long** - 301-600 characters (~60-120 words)
- **Very Long** - 601+ characters (120+ words)

Database contains:
- 910 short quotes
- 3,758 medium quotes
- 1,583 long quotes
- 186 very long quotes

## 🎯 New Features

### TAB to Skip Quotes
Don't like the current quote? Press TAB during the test to instantly get a new random quote from the same category. Your timer will reset, so you can start fresh!

### Quote Source Attribution
Every quote displays its source (book title, movie, song, author) in the typing area header, so you know where each quote comes from.

### Enhanced Visual Design
All UI elements now use heavy border styles for a more polished, professional look that stands out in your terminal.

## 🏆 Leaderboard

- Top 50 scores automatically saved
- Filter by quote length category
- View top 15 performers per category or overall
- Persistent local storage in `leaderboard.json`
- Sort by WPM (highest first)

## 🛠️ Technical Stack

- **Python 3.11**
- **Rich** - Beautiful terminal UI with colors and formatting
- **Readchar** - Advanced keyboard input handling
- **JSON** - Local data persistence (quotes and leaderboard)

## 📁 Project Structure

```
.
├── main.py              # Main application with UI and game loop
├── quotes.py            # Quote manager with categorization
├── typing_engine.py     # Core typing test logic and calculations
├── leaderboard.py       # Score management and persistence
├── english.json         # 6,437+ quotes database
└── leaderboard.json     # Your saved scores (auto-generated)
```

## 🎨 UI Elements

All UI components use heavy border styles (HEAVY and HEAVY_HEAD) for consistent, appealing visuals:
- Menu panels
- Typing area with quote display
- Live statistics panel
- TAB hint indicator
- Results summary
- Word history table
- Leaderboard table

## 💡 Tips

- Start with Short or Medium quotes to warm up
- Use the TAB key to find quotes you enjoy typing
- Watch your accuracy - it's better to go slow and accurate than fast and error-prone
- Check the word history to see which words slow you down
- Practice regularly to improve your WPM

## 📝 License

Open source - feel free to use, modify, and distribute!

## 🚀 Future Enhancements

- Custom text input option
- Difficulty modes with punctuation/numbers
- Performance analytics and graphs
- Practice mode for specific problem areas
- Sound effects and celebrations
- Export typing statistics
