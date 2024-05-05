import tkinter as tk
import keyboard
import pyperclip

class ClipboardManager:
    def __init__(self, root):
        self.root = root
        self.last_clipboard = []
        self.label_buttons = []

        self.setup_ui()
        keyboard.add_hotkey('ctrl+c', self.handle_event)

    def handle_event(self):
        text_input = pyperclip.paste()
        self.last_clipboard.append(text_input)
        self.window_update()

    def reset_array(self):
        self.last_clipboard = []
        self.window_update()

    def copy_to_clipboard(self, text):
        pyperclip.copy(text)

    def window_update(self):
        # Usunięcie wszystkich widżetów etykiet i przycisków kopiowania
        for widget in self.label_buttons:
            widget.destroy()
        self.label_buttons.clear()
        
        # Tworzenie etykiet i przycisków kopiowania
        for i, text in enumerate(self.last_clipboard):
            label = tk.Label(self.root, text=text, padx=20, pady=5)
            label.grid(row=i, column=0, sticky="w")
            copy_button = tk.Button(self.root, text="Kopiuj", command=lambda t=text: self.copy_to_clipboard(t))
            copy_button.grid(row=i, column=1, sticky="e")
            # Dodanie referencji do utworzonych widżetów do listy
            self.label_buttons.append(label)
            self.label_buttons.append(copy_button)

    def setup_ui(self):
        self.root.title("Clipboard Manager")
        self.root.geometry("600x400+100+50")

        # Tworzenie przycisku
        button = tk.Button(self.root, text="Czyszczenie danych", command=self.reset_array)
        button.grid(row=0, columnspan=2)

        # Wywołanie funkcji aktualizującej okno
        self.window_update()

if __name__ == "__main__":
    # Tworzenie okna głównego
    root = tk.Tk()
    clipboard_manager = ClipboardManager(root)
    root.mainloop()
