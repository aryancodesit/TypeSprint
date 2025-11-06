"""Quote database for typing test"""

import json
import random
from typing import Dict, List
from dataclasses import dataclass

@dataclass
class Quote:
    """Quote data structure"""
    text: str
    source: str
    length: int
    id: int

class QuoteManager:
    """Manages loading and categorizing quotes"""
    
    def __init__(self, json_file="english.json"):
        self.quotes_by_category: Dict[str, List[Quote]] = {
            "short": [],
            "medium": [],
            "long": [],
            "very_long": []
        }
        self._load_quotes(json_file)
    
    def _load_quotes(self, json_file: str):
        """Load and categorize quotes from JSON file"""
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            for quote_data in data.get('quotes', []):
                quote = Quote(
                    text=quote_data['text'],
                    source=quote_data.get('source', 'Unknown'),
                    length=quote_data.get('length', len(quote_data['text'])),
                    id=quote_data.get('id', 0)
                )
                
                if quote.length <= 100:
                    self.quotes_by_category["short"].append(quote)
                elif quote.length <= 300:
                    self.quotes_by_category["medium"].append(quote)
                elif quote.length <= 600:
                    self.quotes_by_category["long"].append(quote)
                else:
                    self.quotes_by_category["very_long"].append(quote)
        
        except FileNotFoundError:
            print(f"Warning: {json_file} not found, using fallback quotes")
            self._load_fallback_quotes()
        except json.JSONDecodeError as e:
            print(f"Warning: Error parsing {json_file}: {e}, using fallback quotes")
            self._load_fallback_quotes()
    
    def _load_fallback_quotes(self):
        """Fallback quotes if JSON file is not available"""
        short_quotes = [
            Quote("The quick brown fox jumps over the lazy dog.", "Pangram", 46, 0),
            Quote("Practice makes perfect.", "Proverb", 23, 0),
            Quote("Time flies when you're having fun.", "Proverb", 34, 0),
        ]
        medium_quotes = [
            Quote("The only way to do great work is to love what you do. If you haven't found it yet, keep looking. Don't settle.", "Steve Jobs", 115, 0),
            Quote("In the middle of difficulty lies opportunity. Success is not final, failure is not fatal: it is the courage to continue that counts.", "Winston Churchill", 134, 0),
        ]
        long_quotes = [
            Quote("It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife. However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered the rightful property of some one or other of their daughters.", "Pride and Prejudice", 367, 0),
        ]
        very_long_quotes = [
            Quote("To be, or not to be, that is the question: whether 'tis nobler in the mind to suffer the slings and arrows of outrageous fortune, or to take arms against a sea of troubles and by opposing end them. To die, to sleep, no more; and by a sleep to say we end the heart-ache and the thousand natural shocks that flesh is heir to: 'tis a consummation devoutly to be wished. To die, to sleep, perchance to dream: ay, there's the rub, for in that sleep of death what dreams may come, when we have shuffled off this mortal coil, must give us pause. There's the respect that makes calamity of so long life.", "Hamlet - To Be or Not to Be", 614, 0),
        ]
        self.quotes_by_category["short"] = short_quotes
        self.quotes_by_category["medium"] = medium_quotes
        self.quotes_by_category["long"] = long_quotes
        self.quotes_by_category["very_long"] = very_long_quotes
    
    def get_random_quote(self, category: str = "medium") -> Quote:
        """Get a random quote from the specified category"""
        if category not in self.quotes_by_category or not self.quotes_by_category[category]:
            category = "medium"
        
        if not self.quotes_by_category[category]:
            return Quote("No quotes available", "System", 21, 0)
        
        return random.choice(self.quotes_by_category[category])
    
    def get_quote_count(self, category: str | None = None) -> int:
        """Get count of quotes in a category or total"""
        if category:
            return len(self.quotes_by_category.get(category, []))
        return sum(len(quotes) for quotes in self.quotes_by_category.values())

quote_manager = QuoteManager()

def get_random_quote(category: str = "medium") -> Quote:
    """Get a random quote from the specified category"""
    return quote_manager.get_random_quote(category)
