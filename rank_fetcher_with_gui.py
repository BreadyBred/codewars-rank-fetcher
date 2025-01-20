import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
import requests
from lxml import html
import time
from threading import Thread

class CodewarsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Codewars Rank Fetcher")
        
        # Variables
        self.username = tk.StringVar()
        self.hide_empty_ranks = tk.BooleanVar(value=True)
        self.sort_ranks = tk.BooleanVar(value=True)
        self.categories = {}  # Will store category variables
        self.file_path = "ranks.json"
        
        # Create main frame
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Username section
        ttk.Label(main_frame, text="Codewars Username:").grid(row=0, column=0, sticky=tk.W, pady=5)
        username_entry = ttk.Entry(main_frame, textvariable=self.username)
        username_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5)
        
        # Hide empty ranks checkbox
        ttk.Checkbutton(
            main_frame, 
            text="Hide empty ranks", 
            variable=self.hide_empty_ranks
        ).grid(row=1, column=0, columnspan=2, sticky=tk.W, pady=5)
        
        # Sort ranks checkbox
        ttk.Checkbutton(
            main_frame, 
            text="Sort ranks from highest to lowest", 
            variable=self.sort_ranks
        ).grid(row=2, column=0, columnspan=2, sticky=tk.W, pady=5)

        # Categories section with note
        categories_frame = ttk.LabelFrame(main_frame, text="Select Categories", padding="5")
        categories_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        # Add note about no selection
        ttk.Label(
            categories_frame,
            text="Note: If no categories are selected, all categories will be checked.",
            font=('TkDefaultFont', 9, 'italic')
        ).grid(row=0, column=0, columnspan=2, sticky=tk.W, pady=(0,5))
        
        # Create a frame with canvas for scrollable categories
        canvas_frame = ttk.Frame(categories_frame)
        canvas_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Create canvas and scrollbar
        self.canvas = tk.Canvas(canvas_frame, height=200)
        scrollbar = ttk.Scrollbar(canvas_frame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)
        
        # Configure canvas
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)
        
        # Grid layout for canvas and scrollbar
        self.canvas.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        # Load and create category checkboxes
        self.load_categories()
        
        # Status frame
        status_frame = ttk.LabelFrame(main_frame, text="Status", padding="5")
        status_frame.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        # Progress bar
        self.progress_var = tk.DoubleVar()
        self.progress = ttk.Progressbar(
            status_frame,
            variable=self.progress_var,
            maximum=100
        )
        self.progress.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=5, padx=5)
        
        # Status label
        self.status_var = tk.StringVar(value="Ready")
        self.status_label = ttk.Label(
            status_frame,
            textvariable=self.status_var,
            wraplength=400  # Allow text to wrap
        )
        self.status_label.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=2, padx=5)
        
        # Detailed status (for rank results)
        self.detailed_status = tk.Text(status_frame, height=4, wrap=tk.WORD)
        self.detailed_status.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=5, padx=5)
        self.detailed_status.config(state=tk.DISABLED)
        
        # Start button
        self.start_button = ttk.Button(
            main_frame,
            text="Fetch Ranks",
            command=self.start_fetch,
            state=tk.DISABLED
        )
        self.start_button.grid(row=5, column=0, columnspan=2, pady=10)
        
        # Bind username entry validation
        self.username.trace_add('write', self.validate_username)
        
        # Configure grid weights
        main_frame.columnconfigure(1, weight=1)
        canvas_frame.columnconfigure(0, weight=1)
        status_frame.columnconfigure(0, weight=1)
        
        # Bind mouse wheel to canvas
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)
        
    def add_status_message(self, message):
        """Add a message to the detailed status text widget"""
        self.detailed_status.config(state=tk.NORMAL)
        self.detailed_status.insert(tk.END, message + "\n")
        self.detailed_status.see(tk.END)
        self.detailed_status.config(state=tk.DISABLED)
        self.root.update_idletasks()

    def clear_status_messages(self):
        """Clear all messages from the detailed status text widget"""
        self.detailed_status.config(state=tk.NORMAL)
        self.detailed_status.delete(1.0, tk.END)
        self.detailed_status.config(state=tk.DISABLED)

    def add_codewars_rank(self, category, display_name):
        """Fetch the user's rank for a specific category."""
        self.status_var.set(f"Fetching rank for {display_name}...")
        self.root.update_idletasks()
        
        url = f"https://www.codewars.com/users/leaderboard/ranks?language={category}"

        try:
            response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
            response.raise_for_status()
            self.add_status_message(f"Data fetched for {display_name}")
        except requests.RequestException as e:
            self.add_status_message(f"Error fetching {display_name}: {str(e)}\n")
            return None

        tree = html.fromstring(response.content)
        rows = tree.xpath("//div[contains(@class, 'leaderboard')]//table//tr")

        for row in rows:
            data_username = row.get("data-username")
            if data_username == self.username.get():
                rank_cell = row.xpath(".//td[contains(@class, 'rank')]")
                if rank_cell:
                    user_rank = rank_cell[0].text_content().strip()
                    user_rank = int(user_rank.replace("#", ""))
                    self.add_status_message(
                        f"Rank for {self.username.get()} in category {display_name} is: {user_rank}\n"
                    )
                    return user_rank

        self.add_status_message(f"No rank found for {self.username.get()} in {display_name}\n")
        return None

    def fetch_ranks(self):
        """Main function to fetch all ranks."""
        try:
            self.clear_status_messages()
            self.create_json_file()
            selected_categories = [(name, info['value']) 
                                 for name, info in self.categories.items() 
                                 if info['var'].get()]
            
            # If no categories selected, use all categories
            if not selected_categories:
                self.add_status_message("No categories selected - checking all categories\n")
                selected_categories = [(name, info['value']) 
                                     for name, info in self.categories.items()]

            total_categories = len(selected_categories)
            for i, (display_name, category) in enumerate(selected_categories, 1):
                user_rank = self.add_codewars_rank(category, display_name)
                
                if self.hide_empty_ranks.get() and user_rank is None:
                    continue

                self.write_rank_in_json(display_name, user_rank)
                self.progress_var.set((i / total_categories) * 100)
                
            self.sort_json_ranks()
            self.status_var.set("Rank fetching completed!")
            self.add_status_message("Rank fetching completed!")
            messagebox.showinfo("Success", "Ranks have been fetched and saved!")
            
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
            
        finally:
            self.start_button.config(state=tk.NORMAL)
            self.progress_var.set(0)

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def load_categories(self):
        try:
            with open("data/categories.json", "r") as f:
                categories_data = json.load(f)
                
            row = 0
            col = 0
            max_rows = (len(categories_data) + 1) // 2

            for display_name, value in categories_data.items():
                var = tk.BooleanVar(value=False)
                self.categories[display_name] = {'var': var, 'value': value}
                
                ttk.Checkbutton(
                    self.scrollable_frame,
                    text=display_name,
                    variable=var
                ).grid(row=row, column=col, sticky=tk.W, padx=5, pady=2)
                
                row += 1
                if row >= max_rows:
                    row = 0
                    col += 1
        except FileNotFoundError:
            messagebox.showerror("Error", "categories.json not found in data directory")
        except json.JSONDecodeError:
            messagebox.showerror("Error", "Invalid JSON in categories.json")

    def validate_username(self, *args):
        if self.username.get().strip():
            self.start_button.config(state=tk.NORMAL)
        else:
            self.start_button.config(state=tk.DISABLED)

    def get_selected_categories(self):
        return [info['value'] for name, info in self.categories.items() 
                if info['var'].get()]

    def create_json_file(self):
        """Create or reset the ranks.json file."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

        data = {self.username.get(): {}}
        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=4)

    def write_rank_in_json(self, category, rank):
        """Write the user's rank to ranks.json."""
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as f:
                data = json.load(f)
        else:
            data = {self.username.get(): {}}

        data[self.username.get()][category] = rank

        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=4)

    def sort_json_ranks(self):
        """Sort the ranks from highest to lowest if requested."""
        if not self.sort_ranks.get():
            return

        with open(self.file_path, 'r') as f:
            data = json.load(f)

        username = self.username.get()
        sorted_ranks = sorted(
            data[username].items(),
            key=lambda x: (x[1] if x[1] is not None else float('inf'))
        )
        data[username] = dict(sorted_ranks)

        with open(self.file_path, 'w') as f:
            json.dump(data, f, indent=4)

    def start_fetch(self):
        """Start the rank fetching process in a separate thread."""
        self.start_button.config(state=tk.DISABLED)
        self.status_var.set("Starting rank fetch...")
        self.progress_var.set(0)
        
        # Start fetching in a separate thread to keep GUI responsive
        Thread(target=self.fetch_ranks, daemon=True).start()

def main():
    root = tk.Tk()
    app = CodewarsGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()