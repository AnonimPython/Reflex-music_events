import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""

    ...

def music_event_card(
    date: str = "Today",
    time: str = "10:00",
    card_bg: str = "#f7dad4",
    heading_text: str = "Swiftogeddon - The Taylor Swift Club Night",
    text: str = "Bla bla bla bla bla bla bla bla",
    
)-> rx.Component:
    return rx.box(
        rx.hstack(
            rx.box(
                rx.text(date),
                rx.text(time,font_size="30px",weight="bold"),
                text_align="center",
                align_items="center",
                align_self="center",
                width="150px",
                background_color=card_bg,
                padding="15px",
                border_radius="10px",
                margin="10px",
            ),
            rx.box(
                rx.heading(heading_text,font_size="1em"),
                rx.text(text,font_size="15px"),
                padding="15px",
                max_width="555px",
                align_self="center",
                height="110px",
            ),
            rx.box(
                rx.link(
                    rx.text("Buy a ticket"),
                    color="white",
                    _hover={"color": card_bg}
                ),
                background_color="black",
                border_radius="5px",
                padding="10px",
                align_items="center",
                align_self="center",
                margin="10px",
            ),
        ),
        background_color="white",
        width="100%",
        height="120px",
        border_radius="10px",
    )

def index() -> rx.Component:
    return rx.container(
        
        rx.box(
            #* Title
            rx.heading("Music events", font_size="40px"),
            rx.text("in London, United Kingdom", font_size="20px",margin="10px 0px 20px 0px"),
            #* date | name group | description | tickets
            rx.box(
                rx.vstack(
                    music_event_card(
                        date="Today",
                        time="10:00",
                        card_bg="#f7dad4",
                        heading_text="Swiftogeddon - The Taylor Swift Club Night",
                        text="Swiftogeddon is a night dedicated to worshipping at the altar of Taylor Swift: non-stop Swifty all night: deep cuts, extended mixes, fan favourites..."
                    ),
                    music_event_card(
                        date="17 December",
                        time="22:00",
                        card_bg="#edf7d4",
                        heading_text="Lana Del Rave",
                        text="Launching the first ever 'Lana Del Rave' at Heaven Nightclub. Join us for a night devoted to the Queen of Alternative as well as favourites"
                    ),
                    music_event_card(
                        date="19 December",
                        time="18:30",
                        card_bg="#d0e7f6",
                        heading_text="MASSAOKE: XMAS LIVE at the Electric Ballroom",
                        text="Featuring all your favourite festive hits from WHAM, SLADE, MARIAH, WIZZARD, THE POGUES and many more - as well as hairbrush anthems"
                    ),
                    music_event_card(
                        date="22 December",
                        time="19:00",
                        card_bg="#e0d3f7",
                        heading_text="Eleni Tsaligopoulou full-band",
                        text="Eleni Tsaligopoulou is one of the most popular and beloved Greek singers with a wide range of repertoire and timeless hits. During her 30 year..."
                    ),
                    gap="20px",
                ),  
            ),
            
            margin_top="10%",
        ),
        
        
        background_color="#ebf2ff",
        height="100vh",
        margin="auto"
    )


app = rx.App(
    style={
        "font_family": "Ubuntu, sans-serif"
    },
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Ubuntu:ital,wght@0,300;0,400;0,500;0,700;1,300;1,400;1,500;1,700&display=swap"
    ]
)
app.add_page(index)
