"""
oec.display
~~~~~~~~~~~
"""

_ASCII_CHAR_MAP = {
    '>': 0x08,
    '<': 0x09,
    '[': 0x0a,
    ']': 0x0b,
    ')': 0x0c,
    '(': 0x0d,
    '}': 0x0e,
    '{': 0x0f,

    # 0x10 - A real space?
    '=': 0x11,
    '\'': 0x12,
    '"': 0x13,
    '/': 0x14,
    '\\': 0x15,
    '|': 0x16,
    '¦': 0x17,
    '?': 0x18,
    '!': 0x19,
    '$': 0x1a,
    '¢': 0x1b,
    '£': 0x1c,
    '¥': 0x1d,
    # 0x1e - A P/T looking symbol
    # 0x1f - A intertwined parens symbol

    '0': 0x20,
    '1': 0x21,
    '2': 0x22,
    '3': 0x23,
    '4': 0x24,
    '5': 0x25,
    '6': 0x26,
    '7': 0x27,
    '8': 0x28,
    '9': 0x29,
    'ß': 0x2a,
    '§': 0x2b,
    '#': 0x2c,
    '@': 0x2d,
    '%': 0x2e,
    '_': 0x2f,

    '&': 0x30,
    '-': 0x31,
    '.': 0x32,
    ',': 0x33,
    ':': 0x34,
    '+': 0x35,
    '¬': 0x36,
    '¯': 0x37, # ???
    '°': 0x38,
    # 0x39 - Accent?
    # 0x3a - Accent?
    # 0x3b - A tilde?  It looks more like an accent...
    '¨': 0x3c,
    # 0x3d - Accute accent?
    # 0x3e - Opposite of accute accent?
    # 0x3f - A more extreme comma?

    'a': 0x80,
    'b': 0x81,
    'c': 0x82,
    'd': 0x83,
    'e': 0x84,
    'f': 0x85,
    'g': 0x86,
    'h': 0x87,
    'i': 0x88,
    'j': 0x89,
    'k': 0x8a,
    'l': 0x8b,
    'm': 0x8c,
    'n': 0x8d,
    'o': 0x8e,
    'p': 0x8f,

    'q': 0x90,
    'r': 0x91,
    's': 0x92,
    't': 0x93,
    'u': 0x94,
    'v': 0x95,
    'w': 0x96,
    'x': 0x97,
    'y': 0x98,
    'z': 0x99,
    'æ': 0x9a,
    'ø': 0x9b,
    'å': 0x9c,
    'ç': 0x9d,
    # 0x9e - Semi colon with top line
    # 0x9f - Asterisk with top line

    'A': 0xa0,
    'B': 0xa1,
    'C': 0xa2,
    'D': 0xa3,
    'E': 0xa4,
    'F': 0xa5,
    'G': 0xa6,
    'H': 0xa7,
    'I': 0xa8,
    'J': 0xa9,
    'K': 0xaa,
    'L': 0xab,
    'M': 0xac,
    'N': 0xad,
    'O': 0xae,
    'P': 0xaf,

    'Q': 0xb0,
    'R': 0xb1,
    'S': 0xb2,
    'T': 0xb3,
    'U': 0xb4,
    'V': 0xb5,
    'W': 0xb6,
    'X': 0xb7,
    'Y': 0xb8,
    'Z': 0xb9,
    'Æ': 0xba,
    'Ø': 0xbb,
    'Å': 0xbc,
    'Ç': 0xbd,
    ';': 0xbe,
    '*': 0xbf
}

ASCII_CHAR_MAP = [_ASCII_CHAR_MAP.get(character, 0x00) for character in map(chr, range(256))]

def encode_ascii_character(character):
    """Map an ASCII character to a terminal display character."""
    if character > 255:
        return 0x00

    return ASCII_CHAR_MAP[character]

def encode_string(string, errors='replace'):
    """Map a string to terminal display characters."""
    return bytes([encode_ascii_character(character) for character
                  in string.encode('ascii', errors)])

# TODO: remove default columns
# TODO: add validation of column and data length for write() - must be inside status line
class StatusLine:
    def __init__(self, interface, columns=80):
        self.interface = interface
        self.columns = columns

    def write(self, column, data):
        self.interface.offload_write(data, address=column, restore_original_address=True)

    def write_string(self, column, string):
        self.write(column, encode_string(string))