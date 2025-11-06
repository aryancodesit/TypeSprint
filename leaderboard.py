"""Leaderboard management for typing test"""

import json
import os
from datetime import datetime
from typing import List, Dict

LEADERBOARD_FILE = "leaderboard.json"

class Leaderboard:
    def __init__(self):
        self.scores = self._load_scores()
    
    def _load_scores(self) -> List[Dict]:
        """Load scores from JSON file"""
        if os.path.exists(LEADERBOARD_FILE):
            try:
                with open(LEADERBOARD_FILE, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return []
        return []
    
    def _save_scores(self):
        """Save scores to JSON file"""
        try:
            with open(LEADERBOARD_FILE, 'w') as f:
                json.dump(self.scores, f, indent=2)
        except IOError:
            pass
    
    def add_score(self, name: str, wpm: float, accuracy: float, quote_length: str):
        """Add a new score to the leaderboard"""
        score_entry = {
            "name": name,
            "wpm": round(wpm, 2),
            "accuracy": round(accuracy, 2),
            "quote_length": quote_length,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.scores.append(score_entry)
        self.scores.sort(key=lambda x: x['wpm'], reverse=True)
        self.scores = self.scores[:50]
        self._save_scores()
    
    def get_top_scores(self, limit: int = 10, quote_length: str | None = None) -> List[Dict]:
        """Get top scores, optionally filtered by quote length"""
        if quote_length:
            filtered = [s for s in self.scores if s['quote_length'] == quote_length]
            return filtered[:limit]
        return self.scores[:limit]
