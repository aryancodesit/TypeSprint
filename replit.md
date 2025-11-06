# Typing Speed Test CLI

## Overview
A colorful CLI-based typing speed test platform inspired by MonkeyType with an enhanced terminal interface featuring heavy rounded borders. Built with Python using the Rich library for beautiful terminal output and loaded with 6,437+ real quotes from books, movies, songs, and literature.

## Recent Changes
- **2025-11-06 (Update 2)**: Enhanced UI and added TAB functionality
  - Integrated massive english.json database with 6,437+ quotes
  - Added "Very Long" quote category (601+ characters)
  - Implemented TAB key to skip/change quotes during typing
  - Enhanced all UI elements with HEAVY and HEAVY_HEAD border styles
  - Added quote source display in typing area header
  - Improved fallback quote system for all categories
  - Updated README with comprehensive feature documentation

- **2025-11-06 (Initial)**: Project setup
  - Created core typing test engine with real-time character tracking
  - Implemented colorful terminal UI with gradient effects
  - Added multiple quote length options (short, medium, long)
  - Built local leaderboard system with JSON persistence
  - Implemented word-by-word typing history tracking
  - Added live WPM and accuracy calculations
  - Timer now starts automatically when user begins typing

## Features
- 6,437+ quotes from real sources (books, movies, songs, literature)
- Four quote length categories: Short (0-100), Medium (101-300), Long (301-600), Very Long (601+)
- TAB key to skip quotes and get new random ones
- Enhanced UI with heavy rounded borders throughout
- Quote source attribution display
- Real-time typing feedback with color-coded characters (green=correct, red=error, yellow=cursor)
- Live WPM, accuracy, time, and progress tracking
- Word-by-word performance history (top 15 displayed)
- Local JSON-based leaderboard with category filtering
- Colorful terminal interface using Rich library
- Runs completely offline
- English language support

## Project Architecture

### Core Files
- `main.py` - Main application with enhanced UI and menu system
- `typing_engine.py` - Core typing test logic and statistics calculations
- `quotes.py` - QuoteManager for loading and categorizing quotes from JSON
- `leaderboard.py` - Leaderboard management with JSON persistence
- `english.json` - Massive quote database (6,437+ quotes)

### Dependencies
- Python 3.11
- Rich 14.2.0 (colorful terminal UI with HEAVY border styles)
- Readchar 4.2.1 (keyboard input handling including TAB detection)

### Data Storage
- `english.json` - Quote database with 6,437+ categorized quotes
- `leaderboard.json` - Persistent local score storage (auto-generated)

### Quote Database Statistics
- Total quotes: 6,437
- Short (0-100 chars): 910 quotes
- Medium (101-300 chars): 3,758 quotes
- Long (301-600 chars): 1,583 quotes
- Very Long (601+ chars): 186 quotes

## UI Design Philosophy
All UI elements use HEAVY and HEAVY_HEAD box styles from Rich library for consistent, polished appearance:
- Heavy borders create visual prominence
- Rounded corners for modern aesthetic
- Consistent styling across all panels and tables
- Color-coded elements for intuitive understanding

## User Experience Features
- Timer starts automatically on first keystroke (no pre-start key press needed)
- TAB key provides instant quote skip functionality
- Quote source displayed for context and interest
- Visual hint panel reminds users of TAB functionality
- Top 15 word history to focus on relevant performance data
- Category-filtered leaderboards for fair comparison

## User Preferences
None specified yet.
