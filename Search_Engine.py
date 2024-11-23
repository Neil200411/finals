
from kivy.metrics import dp
from kivy.uix.screenmanager import Screen
from kivymd.uix.dialog import MDDialog



class DictionaryScreen(Screen):
    def __init__(self, **kwargs):
        super(DictionaryScreen, self).__init__(**kwargs)
        self.original_data = [
            ("brb", "be right back"),
            ("idk", "I don't know"),
            ("lol", "laugh out loud"),
            ("python", "a high-level programming language"),
            ("data", "facts and statistics collected together"),
            ("yeet", "to throw something with force"),
            ("sus", "suspicious or suspect")
        ]

    def on_enter(self):
        pass

    def search_term(self, search_input):
        """Search for the abbreviation and show a dialog with the meaning."""
        search_value = search_input.text.lower().strip()

        # Search for the term in the dictionary
        for abbr, meaning in self.original_data:
            if search_value == abbr.lower():
                # Show a dialog with the meaning of the term
                self.show_dialog(abbr, meaning)
                search_input.text = ""  # Clear search field after search
                return

        # If no match found, show a not found dialog
        self.show_dialog("Not Found", f"No meaning found for '{search_value}'. Please try again.")
        search_input.text = ""  # Clear search field after showing dialog

    def show_dialog(self, title, text):
        """Show a dialog with the result."""
        dialog = MDDialog(
            title=title,
            text=text,
            size_hint=(0.8, None),
            height=dp(200)
        )
        dialog.open()

