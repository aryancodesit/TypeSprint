#!/usr/bin/env python3
"""Colorful CLI Typing Speed Test - MonkeyType Style"""

import sys
import readchar
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from rich.layout import Layout
from rich.live import Live
from rich import box
from rich.align import Align

from quotes import get_random_quote, Quote
from typing_engine import TypingEngine
from leaderboard import Leaderboard

console = Console()

class TypingTest:
    def __init__(self):
        self.leaderboard = Leaderboard()
        self.quote_length = "medium"
        self.current_quote = None
    
    def show_banner(self):
        """Display colorful banner with rounded corners"""
        banner = Panel(
            Text("⚡ TYPING SPEED TEST ⚡", style="bold yellow", justify="center"),
            border_style="bold cyan",
            box=box.HEAVY,
            padding=(0, 2)
        )
        console.print(Align.center(banner))
        console.print()
    
    def show_menu(self):
        """Display main menu with enhanced UI"""
        console.clear()
        self.show_banner()
        
        menu_content = Text()
        menu_content.append("1. ", style="bold yellow")
        menu_content.append("Start Typing Test\n", style="green")
        menu_content.append("2. ", style="bold yellow")
        menu_content.append("View Leaderboard\n", style="magenta")
        menu_content.append("3. ", style="bold yellow")
        menu_content.append("Change Quote Length ", style="blue")
        menu_content.append(f"(Current: {self.quote_length})\n", style="dim")
        menu_content.append("4. ", style="bold yellow")
        menu_content.append("Exit", style="red")
        
        menu_panel = Panel(
            menu_content,
            title="[bold cyan]Menu[/]",
            border_style="bright_blue",
            box=box.HEAVY_HEAD,
            padding=(1, 2)
        )
        
        console.print(Align.center(menu_panel))
        console.print()
        console.print(Align.center("[dim]Press 1-4 to select[/]"))
    
    def select_quote_length(self):
        """Let user select quote length"""
        console.clear()
        self.show_banner()
        
        menu_content = Text()
        menu_content.append("1. ", style="bold yellow")
        menu_content.append("Short ", style="green")
        menu_content.append("(0-100 chars)\n", style="dim")
        menu_content.append("2. ", style="bold yellow")
        menu_content.append("Medium ", style="blue")
        menu_content.append("(101-300 chars)\n", style="dim")
        menu_content.append("3. ", style="bold yellow")
        menu_content.append("Long ", style="magenta")
        menu_content.append("(301-600 chars)\n", style="dim")
        menu_content.append("4. ", style="bold yellow")
        menu_content.append("Very Long ", style="red")
        menu_content.append("(601+ chars)", style="dim")
        
        menu_panel = Panel(
            menu_content,
            title="[bold green]Select Quote Length[/]",
            border_style="bright_green",
            box=box.HEAVY_HEAD,
            padding=(1, 2)
        )
        
        console.print(Align.center(menu_panel))
        console.print()
        console.print(Align.center("[dim]Press 1-4 to select[/]"))
        
        while True:
            try:
                choice = readchar.readchar()
                if choice == '1':
                    self.quote_length = "short"
                    break
                elif choice == '2':
                    self.quote_length = "medium"
                    break
                elif choice == '3':
                    self.quote_length = "long"
                    break
                elif choice == '4':
                    self.quote_length = "very_long"
                    break
            except:
                pass
    
    def display_typing_area(self, engine: TypingEngine, quote: Quote):
        """Display the typing area with colored characters"""
        char_status = engine.get_current_char_status()
        
        text = Text()
        cursor_pos = len(engine.user_input)
        
        for i, (char, status) in enumerate(char_status):
            if i == cursor_pos:
                text.append(char, style="bold black on yellow")
            elif status == 'correct':
                text.append(char, style="bold green")
            elif status == 'incorrect':
                text.append(char, style="bold white on red")
            else:
                text.append(char, style="dim white")
        
        title = f"[bold cyan]Type the text below[/]  [dim]│[/]  [italic magenta]{quote.source}[/]"
        
        return Panel(
            text,
            title=title,
            border_style="bright_blue",
            box=box.HEAVY,
            padding=(1, 2)
        )
    
    def display_stats(self, engine: TypingEngine):
        """Display live statistics"""
        wpm = engine.get_live_wpm()
        accuracy = engine.calculate_accuracy()
        elapsed = engine.get_elapsed_time()
        progress = (len(engine.user_input) / len(engine.target_text)) * 100 if engine.target_text else 0
        
        stats_text = Text()
        stats_text.append("WPM: ", style="dim cyan")
        stats_text.append(f"{wpm:.1f}", style="bold cyan")
        stats_text.append("  │  ", style="dim")
        stats_text.append("Accuracy: ", style="dim yellow")
        stats_text.append(f"{accuracy:.1f}%", style="bold yellow")
        stats_text.append("  │  ", style="dim")
        stats_text.append("Time: ", style="dim green")
        stats_text.append(f"{elapsed:.1f}s", style="bold green")
        stats_text.append("  │  ", style="dim")
        stats_text.append("Progress: ", style="dim magenta")
        stats_text.append(f"{progress:.0f}%", style="bold magenta")
        
        return Panel(
            Align.center(stats_text),
            border_style="bright_green",
            box=box.HEAVY_HEAD,
            padding=(0, 1)
        )
    
    def display_hint(self):
        """Display hint for TAB key"""
        hint = Text()
        hint.append("💡 Tip: Press ", style="dim")
        hint.append("TAB", style="bold yellow")
        hint.append(" to skip this quote and get a new one", style="dim")
        
        return Panel(
            Align.center(hint),
            border_style="dim",
            box=box.HEAVY_HEAD,
            padding=(0, 1)
        )
    
    def run_typing_test(self):
        """Run the actual typing test with TAB to skip"""
        console.clear()
        self.show_banner()
        
        self.current_quote = get_random_quote(self.quote_length)
        engine = TypingEngine(self.current_quote.text)
        
        timer_started = False
        
        with Live(console=console, refresh_per_second=10) as live:
            while not engine.is_complete():
                layout = Layout()
                layout.split_column(
                    Layout(self.display_typing_area(engine, self.current_quote), size=12),
                    Layout(self.display_stats(engine), size=4),
                    Layout(self.display_hint(), size=3)
                )
                live.update(layout)
                
                try:
                    key = readchar.readchar()
                    
                    if key == readchar.key.CTRL_C:
                        console.print("\n[red]Test cancelled![/]")
                        return
                    elif key == '\t':
                        self.current_quote = get_random_quote(self.quote_length)
                        engine = TypingEngine(self.current_quote.text)
                        timer_started = False
                    elif key == readchar.key.BACKSPACE or key == '\x7f':
                        engine.remove_character()
                    elif key == readchar.key.ENTER or key == '\r' or key == '\n':
                        pass
                    elif len(key) == 1 and key.isprintable():
                        if not timer_started:
                            engine.start()
                            timer_started = True
                        engine.add_character(key)
                except:
                    pass
        
        engine.end()
        self.show_results(engine)
    
    def show_results(self, engine: TypingEngine):
        """Display test results with enhanced UI"""
        console.clear()
        self.show_banner()
        
        wpm = engine.calculate_wpm()
        accuracy = engine.calculate_accuracy()
        errors = engine.calculate_errors()
        time_taken = engine.get_elapsed_time()
        
        results_content = Text()
        results_content.append("Words Per Minute: ", style="cyan")
        results_content.append(f"{wpm:.2f}\n", style="bold yellow")
        results_content.append("Accuracy: ", style="cyan")
        results_content.append(f"{accuracy:.2f}%\n", style="bold yellow")
        results_content.append("Total Errors: ", style="cyan")
        results_content.append(f"{errors}\n", style="bold yellow")
        results_content.append("Time Taken: ", style="cyan")
        results_content.append(f"{time_taken:.2f}s\n", style="bold yellow")
        results_content.append("Quote Length: ", style="cyan")
        results_content.append(self.quote_length.capitalize(), style="bold yellow")
        
        results_panel = Panel(
            results_content,
            title="[bold green]🎉 Test Results 🎉[/]",
            border_style="bright_green",
            box=box.HEAVY,
            padding=(1, 3)
        )
        
        console.print(Align.center(results_panel))
        console.print()
        
        self.show_word_history(engine)
        
        console.print(Align.center("[cyan]Save to leaderboard? (y/n)[/]"))
        try:
            choice = readchar.readchar()
            if choice.lower() == 'y':
                console.print("[yellow]Enter your name:[/] ", end="")
                sys.stdout.flush()
                name = input().strip()
                if name:
                    self.leaderboard.add_score(name, wpm, accuracy, self.quote_length)
                    console.print(f"[green]✓ Score saved for {name}![/]")
        except:
            pass
        
        console.print("\n[dim]Press any key to return to menu...[/]")
        readchar.readchar()
    
    def show_word_history(self, engine: TypingEngine):
        """Display word-by-word typing history"""
        word_history = engine.get_word_history()
        
        if not word_history:
            return
        
        history_table = Table(
            box=box.HEAVY,
            show_header=True,
            header_style="bold magenta",
            border_style="bright_blue"
        )
        history_table.add_column("#", justify="right", style="dim", width=4)
        history_table.add_column("Target Word", style="cyan", width=20)
        history_table.add_column("You Typed", style="yellow", width=20)
        history_table.add_column("Accuracy", justify="right", width=10)
        history_table.add_column("✓/✗", justify="center", width=5)
        
        for i, word_stat in enumerate(word_history[:15], 1):
            status = "✓" if word_stat['correct'] else "✗"
            status_style = "green" if word_stat['correct'] else "red"
            
            history_table.add_row(
                str(i),
                word_stat['word'][:20],
                word_stat['typed'][:20] if word_stat['typed'] else "[dim]skipped[/]",
                f"{word_stat['accuracy']:.0f}%",
                f"[{status_style}]{status}[/]"
            )
        
        history_panel = Panel(
            history_table,
            title="[bold cyan]Word History (Top 15)[/]",
            border_style="bright_blue",
            box=box.HEAVY_HEAD,
            padding=(0, 1)
        )
        
        console.print(history_panel)
        
        if len(word_history) > 15:
            console.print(f"[dim center]... and {len(word_history) - 15} more words[/]")
    
    def show_leaderboard(self):
        """Display leaderboard with enhanced UI"""
        console.clear()
        self.show_banner()
        
        filter_content = Text()
        filter_content.append("Filter by quote length:\n\n", style="bold yellow")
        filter_content.append("1. ", style="bold yellow")
        filter_content.append("All\n", style="cyan")
        filter_content.append("2. ", style="bold yellow")
        filter_content.append("Short\n", style="green")
        filter_content.append("3. ", style="bold yellow")
        filter_content.append("Medium\n", style="blue")
        filter_content.append("4. ", style="bold yellow")
        filter_content.append("Long\n", style="magenta")
        filter_content.append("5. ", style="bold yellow")
        filter_content.append("Very Long", style="red")
        
        filter_panel = Panel(
            filter_content,
            border_style="bright_yellow",
            box=box.HEAVY_HEAD,
            padding=(1, 2)
        )
        
        console.print(Align.center(filter_panel))
        
        filter_length = None
        try:
            choice = readchar.readchar()
            if choice == '2':
                filter_length = "short"
            elif choice == '3':
                filter_length = "medium"
            elif choice == '4':
                filter_length = "long"
            elif choice == '5':
                filter_length = "very_long"
        except:
            pass
        
        console.clear()
        self.show_banner()
        
        scores = self.leaderboard.get_top_scores(limit=15, quote_length=filter_length)
        
        if not scores:
            no_scores_panel = Panel(
                Text("No scores yet! Be the first to set a record!", style="yellow", justify="center"),
                border_style="bright_yellow",
                box=box.HEAVY,
                padding=(1, 2)
            )
            console.print(Align.center(no_scores_panel))
        else:
            title = f"[bold green]🏆 Top Scores"
            if filter_length:
                title += f" ({filter_length.replace('_', ' ').capitalize()})"
            title += " 🏆[/]"
            
            leaderboard_table = Table(
                show_header=True,
                box=box.HEAVY,
                border_style="bright_green",
                header_style="bold magenta"
            )
            leaderboard_table.add_column("Rank", justify="center", style="bold yellow", width=6)
            leaderboard_table.add_column("Name", style="cyan", width=15)
            leaderboard_table.add_column("WPM", justify="right", style="bold green", width=8)
            leaderboard_table.add_column("Accuracy", justify="right", style="bold blue", width=10)
            leaderboard_table.add_column("Length", justify="center", style="magenta", width=10)
            leaderboard_table.add_column("Date", style="dim", width=18)
            
            for i, score in enumerate(scores, 1):
                rank_emoji = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else str(i)
                leaderboard_table.add_row(
                    rank_emoji,
                    score['name'][:15],
                    f"{score['wpm']:.1f}",
                    f"{score['accuracy']:.1f}%",
                    score['quote_length'][:8],
                    score['timestamp']
                )
            
            leaderboard_panel = Panel(
                leaderboard_table,
                title=title,
                border_style="bright_green",
                box=box.HEAVY_HEAD,
                padding=(0, 1)
            )
            
            console.print(leaderboard_panel)
        
        console.print("\n[dim center]Press any key to return to menu...[/]")
        readchar.readchar()
    
    def run(self):
        """Main application loop"""
        while True:
            self.show_menu()
            
            try:
                choice = readchar.readchar()
                
                if choice == '1':
                    self.run_typing_test()
                elif choice == '2':
                    self.show_leaderboard()
                elif choice == '3':
                    self.select_quote_length()
                elif choice == '4':
                    console.clear()
                    goodbye_panel = Panel(
                        Text("Thanks for typing! Keep practicing! 🚀", style="bold green", justify="center"),
                        border_style="bright_green",
                        box=box.HEAVY,
                        padding=(1, 2)
                    )
                    console.print(Align.center(goodbye_panel))
                    break
            except KeyboardInterrupt:
                console.clear()
                console.print("\n[red]Goodbye![/]")
                break
            except Exception as e:
                console.print(f"[red]Error: {e}[/]")
                console.print("[dim]Press any key to continue...[/]")
                try:
                    readchar.readchar()
                except:
                    pass

def main():
    """Entry point"""
    try:
        app = TypingTest()
        app.run()
    except KeyboardInterrupt:
        console.print("\n[red]Goodbye![/]")
        sys.exit(0)

if __name__ == "__main__":
    main()
