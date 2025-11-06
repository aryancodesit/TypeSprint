"""Core typing test engine with real-time feedback"""

import time
from typing import List, Tuple, Dict

class TypingEngine:
    def __init__(self, target_text: str):
        self.target_text = target_text
        self.user_input = ""
        self.start_time = None
        self.end_time = None
        self.errors = 0
        self.word_stats = []
    
    def start(self):
        """Start the typing test timer"""
        self.start_time = time.time()
    
    def end(self):
        """End the typing test timer"""
        self.end_time = time.time()
    
    def add_character(self, char: str):
        """Add a character to user input"""
        if len(self.user_input) < len(self.target_text):
            self.user_input += char
    
    def remove_character(self):
        """Remove the last character (backspace)"""
        if self.user_input:
            self.user_input = self.user_input[:-1]
    
    def is_complete(self) -> bool:
        """Check if typing test is complete"""
        return len(self.user_input) >= len(self.target_text)
    
    def get_current_char_status(self) -> List[Tuple[str, str]]:
        """Get character-by-character status (char, status)"""
        result = []
        for i, target_char in enumerate(self.target_text):
            if i < len(self.user_input):
                user_char = self.user_input[i]
                if user_char == target_char:
                    result.append((target_char, 'correct'))
                else:
                    result.append((target_char, 'incorrect'))
            else:
                result.append((target_char, 'pending'))
        return result
    
    def calculate_wpm(self) -> float:
        """Calculate words per minute"""
        if not self.start_time or not self.end_time:
            return 0.0
        
        time_elapsed = self.end_time - self.start_time
        if time_elapsed == 0:
            return 0.0
        
        words_typed = len(self.user_input.split())
        minutes = time_elapsed / 60
        return words_typed / minutes if minutes > 0 else 0.0
    
    def calculate_accuracy(self) -> float:
        """Calculate typing accuracy percentage"""
        if not self.user_input:
            return 0.0
        
        correct_chars = sum(1 for i, char in enumerate(self.user_input) 
                          if i < len(self.target_text) and char == self.target_text[i])
        return (correct_chars / len(self.user_input)) * 100
    
    def calculate_errors(self) -> int:
        """Calculate total number of errors"""
        errors = sum(1 for i, char in enumerate(self.user_input) 
                    if i < len(self.target_text) and char != self.target_text[i])
        return errors
    
    def get_word_history(self) -> List[Dict]:
        """Get per-word typing statistics"""
        target_words = self.target_text.split()
        user_words = self.user_input.split()
        
        word_history = []
        char_index = 0
        
        for i, target_word in enumerate(target_words):
            if i < len(user_words):
                user_word = user_words[i]
                correct_chars = sum(1 for j, char in enumerate(user_word) 
                                  if j < len(target_word) and char == target_word[j])
                accuracy = (correct_chars / len(target_word)) * 100 if target_word else 0
                
                word_history.append({
                    'word': target_word,
                    'typed': user_word,
                    'accuracy': round(accuracy, 1),
                    'correct': user_word == target_word
                })
            else:
                word_history.append({
                    'word': target_word,
                    'typed': '',
                    'accuracy': 0.0,
                    'correct': False
                })
            char_index += len(target_word) + 1
        
        return word_history
    
    def get_elapsed_time(self) -> float:
        """Get elapsed time in seconds"""
        if not self.start_time:
            return 0.0
        end = self.end_time if self.end_time else time.time()
        return end - self.start_time
    
    def get_live_wpm(self) -> float:
        """Calculate WPM in real-time"""
        if not self.start_time:
            return 0.0
        
        time_elapsed = time.time() - self.start_time
        if time_elapsed == 0:
            return 0.0
        
        words_typed = len(self.user_input.split())
        minutes = time_elapsed / 60
        return words_typed / minutes if minutes > 0 else 0.0
