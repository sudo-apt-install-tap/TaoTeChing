import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()
keyboard.modules.append(Layers())

# Pin mapping for XIAO RP2040 (Right)
keyboard.row_pins = (board.D0, board.D1, board.D2, board.D3)
keyboard.col_pins = (board.D4, board.D5, board.D6, board.D10, board.D9, board.D8)
keyboard.diode_orientation = DiodeOrientation.ROW2COL

# 4x6 matrix - Right side only
keyboard.keymap = [
    [
        KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    KC.BSPC,
        KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, KC.QUOT,
        KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH, KC.ENT,
        KC.NO,   KC.SPC,  KC.MO(1),KC.RALT, KC.RGUI, KC.RCTL,
    ],
    [
        # Layer 1 (Example: Navigation)
        KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.DEL,
        KC.TRNS, KC.LEFT, KC.DOWN, KC.UP,   KC.RGHT, KC.TRNS,
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
        KC.NO,   KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
    ]
]

if __name__ == '__main__':
    keyboard.go()