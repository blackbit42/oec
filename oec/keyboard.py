"""
oec.keyboard
~~~~~~~~~~~~
"""

from enum import IntEnum, IntFlag, unique, auto
from collections import namedtuple

class KeyboardModifiers(IntFlag):
    """Keyboard modifiers."""
    LEFT_SHIFT = auto()
    RIGHT_SHIFT = auto()

    LEFT_ALT = auto()
    RIGHT_ALT = auto()

    CAPS_LOCK = auto()

    NONE = 0

    def is_shift(self):
        """Is either SHIFT key pressed?"""
        return bool(self & (KeyboardModifiers.LEFT_SHIFT | KeyboardModifiers.RIGHT_SHIFT))

    def is_alt(self):
        """Is either ALT key pressed?"""
        return bool(self & (KeyboardModifiers.LEFT_ALT | KeyboardModifiers.RIGHT_ALT))

    def is_caps_lock(self):
        """Is CAPS LOCK toggled on?"""
        return bool(self & KeyboardModifiers.CAPS_LOCK)

@unique
class Key(IntEnum):
    """Keyboad key."""

    # Modifiers
    LEFT_SHIFT = 256
    RIGHT_SHIFT = 257
    LEFT_ALT = 258
    RIGHT_ALT = 259
    CAPS_LOCK = 260

    # Cursor Movement
    SPACE = ord(' ')
    BACKSPACE = 261
    TAB = ord('\t')
    BACKTAB = 262
    NEWLINE = 263
    INSERT = 264
    DELETE = 265

    LEFT = 266
    UP = 267
    RIGHT = 268
    DOWN = 269
    ROLL_UP = 270
    ROLL_DOWN = 271
    HOME = 272

    DUP = 273
    BLANK_4 = 274
    JUMP = 275 # Alt + BLANK_4
    SWAP = 276 # Alt + BACKTAB

    # Function
    PF1 = 277
    PF2 = 278
    PF3 = 279
    PF4 = 280
    PF5 = 281
    PF6 = 282
    PF7 = 283
    PF8 = 284
    PF9 = 285
    PF10 = 286
    PF11 = 287
    PF12 = 288
    PF13 = 289
    PF14 = 290
    PF15 = 291
    PF16 = 292
    PF17 = 293
    PF18 = 294
    PF19 = 295
    PF20 = 296
    PF21 = 297
    PF22 = 298
    PF23 = 299
    PF24 = 300

    # Control
    ENTER = 301
    FIELD_EXIT = 302
    RESET = 303
    QUIT = 304

    SYS_RQ = 305
    ATTN = 306
    BLANK_1 = 307
    CLEAR = 308  # Alt + BLANK_1
    BLANK_2 = 309
    ERASE_INPUT = 310
    PRINT = 311
    HELP = 312
    HEX = 313  # Alt + HELP
    BLANK_3 = 314
    PLAY = 315
    TEST = 316 # Alt + PLAY
    SET_UP = 317
    RECORD = 318
    PAUSE = 319 # Alt + RECORD

    FIELD_MARK = 401
    CURSOR_SELECT = 402
    CURSOR_BLINK = 403
    ERASE_EOF = 404
    VOLUME = 405
    ALT_CURSOR = 406
    IDENT = 407

    PA1 = 408
    PA2 = 409

    # Number Pad
    NUMPAD_BLANK_1 = 320
    NUMPAD_BLANK_2 = 321
    NUMPAD_BLANK_3 = 322
    NUMPAD_BLANK_4 = 323
    NUMPAD_SEVEN = 324
    NUMPAD_EIGHT = 325
    NUMPAD_NINE = 326
    NUMPAD_FIELD_MINUS = 327
    NUMPAD_FOUR = 328
    NUMPAD_FIVE = 329
    NUMPAD_SIX = 330
    NUMPAD_BLANK_5 = 331
    NUMPAD_ONE = 332
    NUMPAD_TWO = 333
    NUMPAD_THREE = 334
    NUMPAD_FIELD_PLUS = 335
    NUMPAD_ZERO = 336
    NUMPAD_PERIOD = 337

    # Latin
    BACKTICK = ord('`')
    TILDE = ord('~')
    ONE = ord('1')
    BAR = ord('|')
    TWO = ord('2')
    AT = ord('@')
    THREE = ord('3')
    HASH = ord('#')
    FOUR = ord('4')
    DOLLAR = ord('$')
    FIVE = ord('5')
    PERCENT = ord('%')
    SIX = ord('6')
    NOT = ord('¬')
    SEVEN = ord('7')
    AMPERSAND = ord('&')
    EIGHT = ord('8')
    ASTERISK = ord('*')
    NINE = ord('9')
    LEFT_PAREN = ord('(')
    ZERO = ord('0')
    RIGHT_PAREN = ord(')')
    MINUS = ord('-')
    UNDERSCORE = ord('_')
    EQUAL = ord('=')
    PLUS = ord('+')

    LOWER_Q = ord('q')
    UPPER_Q = ord('Q')
    LOWER_W = ord('w')
    UPPER_W = ord('W')
    LOWER_E = ord('e')
    UPPER_E = ord('E')
    LOWER_R = ord('r')
    UPPER_R = ord('R')
    LOWER_T = ord('t')
    UPPER_T = ord('T')
    LOWER_Y = ord('y')
    UPPER_Y = ord('Y')
    LOWER_U = ord('u')
    UPPER_U = ord('U')
    LOWER_I = ord('i')
    UPPER_I = ord('I')
    LOWER_O = ord('o')
    UPPER_O = ord('O')
    LOWER_P = ord('p')
    UPPER_P = ord('P')
    CENT = ord('¢')
    EXCLAMATION = ord('!')
    BACKSLASH = ord('\\')
    BROKEN_BAR = ord('¦')

    LOWER_A = ord('a')
    UPPER_A = ord('A')
    LOWER_S = ord('s')
    UPPER_S = ord('S')
    LOWER_D = ord('d')
    UPPER_D = ord('D')
    LOWER_F = ord('f')
    UPPER_F = ord('F')
    LOWER_G = ord('g')
    UPPER_G = ord('G')
    LOWER_H = ord('h')
    UPPER_H = ord('H')
    LOWER_J = ord('j')
    UPPER_J = ord('J')
    LOWER_K = ord('k')
    UPPER_K = ord('K')
    LOWER_L = ord('l')
    UPPER_L = ord('L')
    SEMICOLON = ord(';')
    COLON = ord(':')
    SINGLE_QUOTE = ord('\'')
    DOUBLE_QUOTE = ord('"')
    LEFT_BRACE = ord('{')
    RIGHT_BRACE = ord('}')

    LESS = ord('<')
    GREATER = ord('>')
    LOWER_Z = ord('z')
    UPPER_Z = ord('Z')
    LOWER_X = ord('x')
    UPPER_X = ord('X')
    LOWER_C = ord('c')
    UPPER_C = ord('C')
    LOWER_V = ord('v')
    UPPER_V = ord('V')
    LOWER_B = ord('b')
    UPPER_B = ord('B')
    LOWER_N = ord('n')
    UPPER_N = ord('N')
    LOWER_M = ord('m')
    UPPER_M = ord('M')
    COMMA = ord(',')
    # APOSTOPHE?
    PERIOD = ord('.')
    CENTER_PERIOD = ord('·')
    SLASH = ord('/')
    QUESTION = ord('?')

KEY_UPPER_MAP = {
    Key.LOWER_A: Key.UPPER_A,
    Key.LOWER_B: Key.UPPER_B,
    Key.LOWER_C: Key.UPPER_C,
    Key.LOWER_D: Key.UPPER_D,
    Key.LOWER_E: Key.UPPER_E,
    Key.LOWER_F: Key.UPPER_F,
    Key.LOWER_G: Key.UPPER_G,
    Key.LOWER_H: Key.UPPER_H,
    Key.LOWER_I: Key.UPPER_I,
    Key.LOWER_J: Key.UPPER_J,
    Key.LOWER_K: Key.UPPER_K,
    Key.LOWER_L: Key.UPPER_L,
    Key.LOWER_M: Key.UPPER_M,
    Key.LOWER_N: Key.UPPER_N,
    Key.LOWER_O: Key.UPPER_O,
    Key.LOWER_P: Key.UPPER_P,
    Key.LOWER_Q: Key.UPPER_Q,
    Key.LOWER_R: Key.UPPER_R,
    Key.LOWER_S: Key.UPPER_S,
    Key.LOWER_T: Key.UPPER_T,
    Key.LOWER_U: Key.UPPER_U,
    Key.LOWER_V: Key.UPPER_V,
    Key.LOWER_W: Key.UPPER_W,
    Key.LOWER_X: Key.UPPER_X,
    Key.LOWER_Y: Key.UPPER_Y,
    Key.LOWER_Z: Key.UPPER_Z
}

KEY_LOWER_MAP = {upper_key: lower_key for lower_key, upper_key in KEY_UPPER_MAP.items()}

KEY_MODIFIER_MAP = {
    Key.LEFT_SHIFT: KeyboardModifiers.LEFT_SHIFT,
    Key.RIGHT_SHIFT: KeyboardModifiers.RIGHT_SHIFT,
    Key.LEFT_ALT: KeyboardModifiers.LEFT_ALT,
    Key.RIGHT_ALT: KeyboardModifiers.RIGHT_ALT,
    Key.CAPS_LOCK: KeyboardModifiers.CAPS_LOCK
}

Keymap = namedtuple('Keymap', ['name', 'default', 'shift', 'alt', 'modifier_release'])

class Keyboard:
    """Keyboard state and key mapping."""

    def __init__(self, keymap):
        if keymap is None:
            raise ValueError('Keymap is required')

        self.keymap = keymap

        self.modifiers = KeyboardModifiers.NONE

    def get_key(self, scan_code):
        """Map a scan code to key and update modifiers state."""
        key = self.keymap.default.get(scan_code)

        if self._apply_modifiers(scan_code, key):
            return (key, self.modifiers, True)

        if self.modifiers.is_shift():
            key = self.keymap.shift.get(scan_code)
        elif self.modifiers.is_alt():
            key = self.keymap.alt.get(scan_code)

        if key is None:
            return (None, self.modifiers, False)

        if self.modifiers.is_caps_lock():
            if not self.modifiers.is_shift():
                key = KEY_UPPER_MAP.get(key, key)
            else:
                key = KEY_LOWER_MAP.get(key, key)

        return (key, self.modifiers, False)

    def _apply_modifiers(self, scan_code, key):
        if scan_code in self.keymap.modifier_release:
            released_key = self.keymap.modifier_release[scan_code]

            modifier = KEY_MODIFIER_MAP.get(released_key)

            if modifier is None:
                return False

            # Ignore the release of the caps lock key as it acts as a toggle.
            if modifier.is_caps_lock():
                return False

            self.modifiers &= ~modifier

            return True

        if key in KEY_MODIFIER_MAP:
            modifier = KEY_MODIFIER_MAP[key]

            if modifier.is_caps_lock():
                self.modifiers ^= KeyboardModifiers.CAPS_LOCK
            else:
                self.modifiers |= modifier

            return True

        return False

def get_ascii_character_for_key(key):
    """Map a key to ASCII character."""
    if not key:
        return None

    value = int(key)

    if value > 255:
        return None

    return chr(value)