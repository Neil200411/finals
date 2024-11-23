from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.properties import NumericProperty, ListProperty, StringProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.screenmanager import Screen, FallOutTransition, FadeTransition


class SplashScreen(Screen):
    def on_enter(self):
        # Schedule the transition after 10 seconds
        Clock.schedule_once(self.change_screen, 10)
        self.manager.transition = FadeTransition(duration=0.3, clearcolor=(1,1,1,1))
        self.play_background_music()


    def change_screen(self, *args):
        # Change to MainScreen after 10 seconds
        self.manager.current = "main"
        self.stop_background_music()

    def play_background_music(self):
        # Load and play the audio file (replace with your audio path)
        self.sound = SoundLoader.load('Sounds/BG.mp3')
        if self.sound:
            self.sound.loop = True  # Loop the music
            self.sound.play()
        else:
            print("Failed to load sound")

    def stop_background_music(self):
        if hasattr(self, 'sound') and self.sound:
            self.sound.stop()


class CircularProgressBar(AnchorLayout):
    set_value = NumericProperty(0)
    value = NumericProperty(100)  # The maximum value to reach
    bar_color = ListProperty([1, 0, 100 / 255])
    bar_width = NumericProperty(10)
    text = StringProperty("0%")
    counter = 0
    duration = NumericProperty(7)  # Total duration for the progress to complete

    def __init__(self, **kwargs):
        super(CircularProgressBar, self).__init__(**kwargs)
        Clock.schedule_once(self.animate, 0)

    def animate(self, *args):
        interval = self.duration / self.value
        Clock.schedule_interval(self.percent_counter, interval)

    def percent_counter(self, *args):
        if self.counter < self.value:
            self.counter += 1
            self.text = f"{self.counter}%"
            self.set_value = self.counter
        else:
            Clock.unschedule(self.percent_counter)