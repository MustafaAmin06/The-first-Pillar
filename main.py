from __future__ import annotations

from dataclasses import dataclass
from typing import List

import flet as ft
from flet import Colors, Icons


SOFT_GOLD = "#c29a3d"
INK_BLACK = "#000000"
CLOUD_WHITE = "#fdfbf5"
SOFT_GRAY = "#e8e6df"


@dataclass
class GuideStep:
    title: str
    description: str
    arabic: str
    transliteration: str
    translation: str
    image: str
    audio: str


@dataclass
class Guide:
    key: str
    name: str
    subtitle: str
    steps: List[GuideStep]


def build_guides() -> List[Guide]:
    placeholder_audio = "assets/audio/placeholder.mp3"

    def place_img(label: str) -> str:
        return "assets/images/placeholder.png"

    return [
        Guide(
            key="wudu",
            name="Wudu (Ablution)",
            subtitle="Purification before every salah",
            steps=[
                GuideStep(
                    title="Intention & Bismillah",
                    description="Hold the intention for purification and begin with Bismillah.",
                    arabic="بِسْمِ اللّٰهِ",
                    transliteration="Bismillāh",
                    translation="In the name of Allah",
                    image=place_img("Wudu Step 1"),
                    audio=placeholder_audio,
                ),
                GuideStep(
                    title="Wash face & arms",
                    description="Gently wash the face and forearms up to the elbows three times.",
                    arabic="اللَّهُمَّ اجْعَلْنِي مِنَ التَّوَّابِينَ",
                    transliteration="Allāhumma-jʿalnī mina-t-tawwābīn",
                    translation="O Allah, make me among those who repent",
                    image=place_img("Wudu Step 2"),
                    audio=placeholder_audio,
                ),
                GuideStep(
                    title="Wipe head & wash feet",
                    description="Pass wet hands over the head once, then wash the feet to the ankles.",
                    arabic="وَاجْعَلْنِي مِنَ الْمُتَطَهِّرِينَ",
                    transliteration="Wajʿalnī mina-l-mutaṭahhirīn",
                    translation="and make me among the purified",
                    image=place_img("Wudu Step 3"),
                    audio=placeholder_audio,
                ),
            ],
        ),
        Guide(
            key="fajr",
            name="Fajr",
            subtitle="Dawn prayer · 2 units",
            steps=[
                GuideStep(
                    title="Opening Takbir",
                    description="Raise the hands and softly say the opening takbir.",
                    arabic="اللَّهُ أَكْبَر",
                    transliteration="Allāhu akbar",
                    translation="Allah is the Greatest",
                    image=place_img("Fajr Step 1"),
                    audio=placeholder_audio,
                ),
                GuideStep(
                    title="Recitation",
                    description="Recite Surah Al-Fatiha and a short surah with presence of heart.",
                    arabic="الْحَمْدُ لِلّٰهِ رَبِّ الْعَالَمِينَ",
                    transliteration="Al-ḥamdu lillāhi rabbil-'ālamīn",
                    translation="All praise is for Allah, Lord of the worlds",
                    image=place_img("Fajr Step 2"),
                    audio=placeholder_audio,
                ),
                GuideStep(
                    title="Ruku & Sujud",
                    description="Bow with hands on knees, then prostrate with humility.",
                    arabic="سُبْحَانَ رَبِّيَ الْعَظِيم",
                    transliteration="Subḥāna rabbiyal-ʿaẓīm",
                    translation="Glory be to my Lord, the Magnificent",
                    image=place_img("Fajr Step 3"),
                    audio=placeholder_audio,
                ),
            ],
        ),
        Guide(
            key="dhuhr",
            name="Dhuhr",
            subtitle="Midday prayer · 4 units",
            steps=[
                GuideStep(
                    title="Quiet recitation",
                    description="Recite silently while focusing on the meanings.",
                    arabic="إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِين",
                    transliteration="Iyyāka naʿbudu wa-iyyāka nastaʿīn",
                    translation="You alone we worship, and You alone we ask for help",
                    image=place_img("Dhuhr Step 1"),
                    audio=placeholder_audio,
                ),
                GuideStep(
                    title="Qiyam to Ruku",
                    description="Stand with calm composure, then move into ruku when ready.",
                    arabic="سَمِعَ اللّٰهُ لِمَنْ حَمِدَه",
                    transliteration="Samiʿa llāhu liman ḥamidah",
                    translation="Allah hears those who praise Him",
                    image=place_img("Dhuhr Step 2"),
                    audio=placeholder_audio,
                ),
                GuideStep(
                    title="Tashahhud",
                    description="Sit peacefully and recite the tashahhud before salām.",
                    arabic="التَّحِيَّاتُ لِلّٰهِ",
                    transliteration="At-taḥiyyātu lillāh",
                    translation="All greetings belong to Allah",
                    image=place_img("Dhuhr Step 3"),
                    audio=placeholder_audio,
                ),
            ],
        ),
        Guide(
            key="asr",
            name="Asr",
            subtitle="Afternoon prayer · 4 units",
            steps=[
                GuideStep(
                    title="Centering breath",
                    description="Pause briefly, breathe, and enter the prayer with focus.",
                    arabic="اللَّهُ أَكْبَر",
                    transliteration="Allāhu akbar",
                    translation="Allah is the Greatest",
                    image=place_img("Asr Step 1"),
                    audio=placeholder_audio,
                ),
                GuideStep(
                    title="Measured bow",
                    description="Keep the back level in ruku and gaze softly at the place of sujud.",
                    arabic="سُبْحَانَ رَبِّيَ الْعَظِيم",
                    transliteration="Subḥāna rabbiyal-ʿaẓīm",
                    translation="Glory be to my Lord, the Magnificent",
                    image=place_img("Asr Step 2"),
                    audio=placeholder_audio,
                ),
                GuideStep(
                    title="Grateful prostration",
                    description="In sujud, whisper gratitude and supplication.",
                    arabic="سُبْحَانَ رَبِّيَ الأَعْلَى",
                    transliteration="Subḥāna rabbiyal-aʿlā",
                    translation="Glory be to my Lord, the Most High",
                    image=place_img("Asr Step 3"),
                    audio=placeholder_audio,
                ),
            ],
        ),
        Guide(
            key="maghrib",
            name="Maghrib",
            subtitle="Sunset prayer · 3 units",
            steps=[
                GuideStep(
                    title="Opening gratitude",
                    description="Begin with awareness of the day that just passed.",
                    arabic="رَبَّنَا تَقَبَّلْ مِنَّا",
                    transliteration="Rabbana taqabbal minnā",
                    translation="Our Lord, accept this from us",
                    image=place_img("Maghrib Step 1"),
                    audio=placeholder_audio,
                ),
                GuideStep(
                    title="Balanced pace",
                    description="Recite audibly yet softly in the first two rakʿat.",
                    arabic="وَلَا الضَّالِّينَ",
                    transliteration="Walā ḍ-ḍāllīn",
                    translation="and not of those who are astray",
                    image=place_img("Maghrib Step 2"),
                    audio=placeholder_audio,
                ),
                GuideStep(
                    title="Closing salām",
                    description="Turn the head right and left, offering salām to the angels.",
                    arabic="السَّلَامُ عَلَيْكُمْ وَرَحْمَةُ اللّٰهِ",
                    transliteration="As-salāmu ʿalaykum wa raḥmatullāh",
                    translation="Peace and mercy of Allah be upon you",
                    image=place_img("Maghrib Step 3"),
                    audio=placeholder_audio,
                ),
            ],
        ),
        Guide(
            key="isha",
            name="Isha",
            subtitle="Night prayer · 4 units",
            steps=[
                GuideStep(
                    title="Deep focus",
                    description="Let the stillness of the night enhance intention.",
                    arabic="قُلْ هُوَ اللّٰهُ أَحَد",
                    transliteration="Qul huwa llāhu aḥad",
                    translation="Say: He is Allah, One",
                    image=place_img("Isha Step 1"),
                    audio=placeholder_audio,
                ),
                GuideStep(
                    title="Tranquil sujud",
                    description="Stay a little longer in sujud to reflect on Allah's mercy.",
                    arabic="رَبِّ اغْفِرْ لِي",
                    transliteration="Rabbi-ghfir lī",
                    translation="My Lord, forgive me",
                    image=place_img("Isha Step 2"),
                    audio=placeholder_audio,
                ),
                GuideStep(
                    title="Witr reminder",
                    description="After Isha, consider praying Witr to seal the night.",
                    arabic="اللَّهُمَّ أَنْتَ السَّلَام",
                    transliteration="Allāhumma anta s-salām",
                    translation="O Allah, You are Peace",
                    image=place_img("Isha Step 3"),
                    audio=placeholder_audio,
                ),
            ],
        ),
    ]


INFO_MD = """
# Foundations to Remember

## Five Pillars of Islam
1. **Shahada** – Declaring that none is worthy of worship except Allah and that Muhammad ﷺ is His Messenger.
2. **Salah** – Performing the five daily prayers with presence, beginning with Fajr and ending with Isha.
3. **Zakah** – Offering a portion of one's wealth to uplift those in need.
4. **Sawm** – Fasting the month of Ramadan as an act of discipline and compassion.
5. **Hajj** – Pilgrimage to Makkah once in a lifetime for those who are able.

## Six Articles of Faith
1. **Belief in Allah** – Acknowledging His oneness, mercy, and guidance.
2. **Belief in Angels** – Recognizing the unseen creation that obeys Allah without hesitation.
3. **Belief in Revealed Books** – Qur'an, Torah, Gospel, Psalms, and scriptures sent to humanity.
4. **Belief in Messengers** – Including Adam, Nuh, Ibrahim, Musa, Isa, and Muhammad ﷺ.
5. **Belief in the Last Day** – Accountability, justice, and eternal life.
6. **Belief in Divine Decree** – Trusting Allah's perfect knowledge of all that was, is, and will be.

> *"Indeed, in the remembrance of Allah do hearts find rest."* – Qur'an 13:28
"""


class GuideApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.guides = build_guides()
        self.selected_guide = self.guides[0]
        self.step_index = 0
        self.is_playing = False

        self.audio = ft.Audio(src=self.current_step.audio, volume=0.9, balance=0.0, autoplay=False)
        self.page.overlay.append(self.audio)

        self.play_button = ft.IconButton(
            icon=Icons.PLAY_CIRCLE,
            icon_color=SOFT_GOLD,
            icon_size=36,
            tooltip="Play recitation",
            on_click=self.toggle_audio,
        )
        self.speed_selector = ft.Dropdown(
            value="1.0",
            width=90,
            dense=True,
            options=[
                ft.dropdown.Option("0.5"),
                ft.dropdown.Option("0.75"),
                ft.dropdown.Option("1.0"),
                ft.dropdown.Option("1.25"),
            ],
            on_change=self.change_speed,
        )
        self.loop_switch = ft.Switch(label="Loop", value=False, on_change=self.toggle_loop)

        self.prayers_view = ft.Column(spacing=28, expand=True)
        self.info_view = ft.Container(
            padding=ft.padding.all(20),
            bgcolor=Colors.WHITE,
            border_radius=18,
            content=ft.Markdown(
                INFO_MD,
                selectable=True,
                extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
                code_theme="atom-one-light",
            ),
        )

        self.tabs = ft.Tabs(
            animation_duration=350,
            indicator_color=SOFT_GOLD,
            selected_index=0,
            label_color=INK_BLACK,
            unselected_label_color="#555555",
            tabs=[
                ft.Tab(
                    text="Prayers",
                    content=ft.Container(padding=ft.padding.all(0), content=self.prayers_view),
                ),
                ft.Tab(text="Info", content=self.info_view),
            ],
            expand=1,
        )

        self.page.add(self.tabs)
        self.render_prayers_view()

    @property
    def current_step(self) -> GuideStep:
        return self.selected_guide.steps[self.step_index]

    def select_guide(self, guide: Guide):
        self.selected_guide = guide
        self.step_index = 0
        self.update_audio_source()
        self.render_prayers_view()

    def next_step(self, *_):
        if self.step_index < len(self.selected_guide.steps) - 1:
            self.step_index += 1
            self.update_audio_source()
            self.render_prayers_view()

    def previous_step(self, *_):
        if self.step_index > 0:
            self.step_index -= 1
            self.update_audio_source()
            self.render_prayers_view()

    def on_step_swipe(self, e: ft.DragEndEvent):
        if e.velocity_x < -300:
            self.next_step()
        elif e.velocity_x > 300:
            self.previous_step()

    def toggle_audio(self, *_):
        if not self.audio.src:
            return
        if self.is_playing:
            self.audio.pause()
            self.play_button.icon = Icons.PLAY_CIRCLE
            self.play_button.tooltip = "Play recitation"
        else:
            self.audio.play()
            self.play_button.icon = Icons.PAUSE_CIRCLE
            self.play_button.tooltip = "Pause recitation"
        self.is_playing = not self.is_playing
        self.play_button.update()

    def change_speed(self, e: ft.ControlEvent):
        try:
            rate = float(e.control.value)
        except (TypeError, ValueError):
            rate = 1.0
        self.audio.playback_rate = rate
        self.audio.update()

    def toggle_loop(self, e: ft.ControlEvent):
        self.audio.loop = bool(e.control.value)
        self.audio.update()

    def reset_audio(self, *_):
        self.audio.pause()
        self.audio.seek(0)
        self.is_playing = False
        self.play_button.icon = Icons.PLAY_CIRCLE
        self.play_button.tooltip = "Play recitation"
        self.play_button.update()

    def update_audio_source(self):
        self.audio.src = self.current_step.audio
        self.audio.loop = self.loop_switch.value
        self.audio.playback_rate = float(self.speed_selector.value)
        self.audio.update()
        self.is_playing = False
        self.play_button.icon = Icons.PLAY_CIRCLE
        self.play_button.tooltip = "Play recitation"
        self.play_button.update()

    def build_guide_cards(self) -> ft.ResponsiveRow:
        cards: List[ft.Control] = []
        for guide in self.guides:
            is_selected = guide.key == self.selected_guide.key
            cards.append(
                ft.Container(
                    col={"xs":12, "sm":6, "md":4},
                    padding=ft.padding.all(18),
                    bgcolor=Colors.WHITE,
                    border_radius=18,
                    ink=True,
                    on_click=lambda _, g=guide: self.select_guide(g),
                    border=ft.border.all(1, SOFT_GOLD if is_selected else SOFT_GRAY),
                    content=ft.Column(
                        controls=[
                            ft.Text(guide.name, weight=ft.FontWeight.BOLD, size=18, color=INK_BLACK),
                            ft.Text(guide.subtitle, color="#666666"),
                            ft.Container(
                                height=4,
                                bgcolor=SOFT_GOLD if is_selected else SOFT_GRAY,
                                border_radius=12,
                            ),
                        ],
                        spacing=6,
                    ),
                )
            )
        return ft.ResponsiveRow(columns=12, run_spacing=16, spacing=16, controls=cards)

    def build_step_detail(self) -> ft.Control:
        step = self.current_step
        total_steps = len(self.selected_guide.steps)
        triple_layout = ft.ResponsiveRow(
            columns=12,
            run_spacing=12,
            controls=[
                ft.Container(
                    col={"xs":12, "md":4},
                    padding=14,
                    bgcolor=CLOUD_WHITE,
                    border_radius=14,
                    content=ft.Column(
                        [
                            ft.Text("Arabic", size=13, color=SOFT_GOLD),
                            ft.Text(step.arabic, weight=ft.FontWeight.BOLD, size=20),
                        ]
                    ),
                ),
                ft.Container(
                    col={"xs":12, "md":4},
                    padding=14,
                    bgcolor=CLOUD_WHITE,
                    border_radius=14,
                    content=ft.Column(
                        [
                            ft.Text("Transliteration", size=13, color=SOFT_GOLD),
                            ft.Text(step.transliteration, italic=True),
                        ]
                    ),
                ),
                ft.Container(
                    col={"xs":12, "md":4},
                    padding=14,
                    bgcolor=CLOUD_WHITE,
                    border_radius=14,
                    content=ft.Column(
                        [
                            ft.Text("English", size=13, color=SOFT_GOLD),
                            ft.Text(step.translation),
                        ]
                    ),
                ),
            ],
        )

        nav_controls = ft.Row(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                ft.Text(f"Step {self.step_index + 1} of {total_steps}", weight=ft.FontWeight.BOLD),
                ft.Row(
                    spacing=10,
                    controls=[
                        ft.IconButton(
                            icon=Icons.ARROW_BACK,
                            tooltip="Previous",
                            disabled=self.step_index == 0,
                            on_click=self.previous_step,
                        ),
                        ft.FilledButton(
                            text="Next",
                            icon=Icons.ARROW_FORWARD,
                            style=ft.ButtonStyle(bgcolor=SOFT_GOLD),
                            on_click=self.next_step,
                            disabled=self.step_index == total_steps - 1,
                        ),
                    ],
                ),
            ],
        )

        audio_row = ft.ResponsiveRow(
            columns=12,
            controls=[
                ft.Container(
                    col={"xs":12, "md":6},
                    content=ft.Row(
                        spacing=12,
                        controls=[
                            self.play_button,
                            ft.TextButton("Reset", on_click=self.reset_audio, style=ft.ButtonStyle(color=INK_BLACK)),
                        ],
                    ),
                ),
                ft.Container(
                    col={"xs":12, "md":6},
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.END,
                        spacing=12,
                        controls=[
                            ft.Text("Speed"),
                            self.speed_selector,
                            self.loop_switch,
                        ],
                    ),
                ),
            ],
        )

        gesture_shell = ft.GestureDetector(
            on_pan_end=self.on_step_swipe,
            content=ft.Container(
                padding=ft.padding.all(22),
                bgcolor=Colors.WHITE,
                border_radius=26,
                content=ft.Column(
                    spacing=20,
                    controls=[
                        ft.Image(src=step.image, height=260, fit=ft.ImageFit.COVER, border_radius=20),
                        ft.Text(step.title, size=22, weight=ft.FontWeight.BOLD),
                        ft.Text(step.description, size=15, color="#444444"),
                        triple_layout,
                        audio_row,
                        nav_controls,
                    ],
                ),
            ),
        )

        return gesture_shell

    def render_prayers_view(self):
        cards_row = self.build_guide_cards()
        detail = self.build_step_detail()
        self.prayers_view.controls = [
            ft.Text("The First Pillar", size=28, weight=ft.FontWeight.BOLD, color=INK_BLACK),
            ft.Text(
                "A calm companion for every prayer. Choose a guide, swipe through steps, or tap Next.",
                color="#555555",
            ),
            cards_row,
            ft.Container(height=1, bgcolor=SOFT_GRAY),
            detail,
        ]
        self.prayers_view.update()


def main(page: ft.Page):
    page.title = "The First Pillar – Prayers"
    page.padding = ft.padding.symmetric(horizontal=30, vertical=20)
    page.bgcolor = CLOUD_WHITE
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO
    page.fonts = {
        "Poppins": "https://github.com/google/fonts/raw/main/ofl/poppins/Poppins-Regular.ttf",
        "PoppinsBold": "https://github.com/google/fonts/raw/main/ofl/poppins/Poppins-Bold.ttf",
    }
    page.theme = ft.Theme(font_family="Poppins")

    GuideApp(page)


if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)
