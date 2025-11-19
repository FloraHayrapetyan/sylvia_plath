#!/usr/bin/env python3
"""
A simple script that prints random stanzas from "Mad Girl's Love Song" by Sylvia Plath.
"""

import random

# stanzas from "Mad Girl's Love Song"
stanzas = [
    [
        "I shut my eyes and all the world drops dead;",
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


def print_random_stanza():
    """Selects and prints a random stanza from the poem."""
    stanza = random.choice(stanzas)
    for line in stanza:
        print(line)


if __name__ == "__main__":
    print_random_stanza()

