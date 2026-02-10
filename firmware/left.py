import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()
keyboard.modules.append(Layers())

# Pin mapping for XIAO RP2040 (Left)
keyboard.row_pins = (board.D0, board.D1, board.D2, board.D3)
keyboard.col_pins = (board.D4, board.D5, board.D6, board.D10, board.D9, board.D8)
keyboard.diode_orientation = DiodeOrientation.ROW2COL

# 4x6 matrix - Left side only
keyboard.keymap = [
    [
        KC.TAB,  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,    
        KC.ESC,  KC.A,    KC.S,    KC.D,    KC.F,    KC.G,    
        KC.LSFT, KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    
        KC.LCTL, KC.LGUI, KC.LALT, KC.MO(1),KC.SPC,  KC.NO,
    ],
    [
        # Layer 1 (Example: Numbers)
        KC.GRV,  KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,   
        KC.TRNS, KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,   
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, 
        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.NO,
    ]
]

if __name__ == '__main__':
    keyboard.go()