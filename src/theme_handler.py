from enum import Enum
from palette import theme

class Theme(Enum):
    DARK = "dark"
    LIGHT = "light"

class ThemeHandler:
    def __init__(self, default_theme: Theme = Theme.DARK):
        self.current_theme = default_theme # Default theme
        self.run_when_changed:dict[Theme, list[callable]] = {
            Theme.DARK: [],
            Theme.LIGHT: []
        }
        
    def toggle_theme(self):
        if self.current_theme == Theme.DARK:
            self.current_theme = Theme.LIGHT
        else:
            self.current_theme = Theme.DARK
    
        for func in self.run_when_changed[self.current_theme]:
            func()
            
    def on_theme_change(self, theme: Theme, func: callable):
        self.run_when_changed[theme].append(func)
        
    def get_theme(self) -> Theme:
        return self.current_theme
    
    def get_theme_str(self) -> str:
        return self.current_theme.value
    
    def get_theme_color(self, token: str) -> str:
        if token not in theme[self.current_theme.value]:
            raise KeyError(f"Token '{token}' not found in theme '{self.current_theme.value}'")
        return theme[self.current_theme.value][token]
        
    
    def update(self):
        for func in self.run_when_changed[self.current_theme]:
            func()

    def set_theme(self, theme: Theme):
        if self.current_theme != theme:
            self.current_theme = theme
            self.update()