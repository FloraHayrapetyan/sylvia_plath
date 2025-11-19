#!/usr/bin/env python3
"""
A simple script that prints random stanzas from "Mad Girl's Love Song" by Sylvia Plath.
"""

import random
from typing import List

# Constants
POEM_TITLE = "Mad Girl's Love Song"
POET_NAME = "Sylvia Plath"

# Stanzas from "Mad Girl's Love Song"
STANZAS: List[List[str]] = [
    [
        "I shut my eyes and all the world drops drops dead;",
        "I lift my lids and all is born again.",
        "(I think I made you up inside my head.)",
        ""
    ],
    [
        "The stars go waltzing out in blue and red,",
        "And arbitrary blackness gallops in:",
        "I shut my eyes and all the world drops dead.",
        ""
    ],
    [
        "I dreamed that you bewitched me into bed",
        "And sung me moon-struck, kissed me quite insane.",
        "(I think I made you up inside my head.)",
        ""
    ],
    [
        "God topples from the sky, hell's fires fade:",
        "Exit seraphim and Satan's men:",
        "I shut my eyes and all the world drops dead.",
        ""
    ],
    [
        "I fancied you'd return the way you said,",
        "But I grow old and I forget your name.",
        "(I think I made you up inside my head.)",
        ""
    ],
    [
        "I should have loved a thunderbird instead;",
        "At least when spring comes they roar back again.",
        "I shut my eyes and all the world drops dead.",
        "(I think I made you up inside my head.)"
    ]
]


def get_random_stanza() -> List[str]:
    """Selects and returns a random stanza from the poem."""
    return random.choice(STANZAS)


def format_stanza(stanza: List[str]) -> str:
    """Formats a stanza as a single string with newlines."""
    return '\n'.join(stanza)


def print_random_stanza(intro_message: str = None):
    """Selects and prints a random stanza from the poem.
    
    Args:
        intro_message: Optional introductory message to print before the stanza.
    """
    if intro_message:
        print(intro_message)
    
    stanza = get_random_stanza()
    print(format_stanza(stanza))


if __name__ == "__main__":
    # Prompt the user for an intro message
    intro_message = input("Enter your intro message: ")
    print()
    print_random_stanza("Here is the stanza you requested:" + "\n")

