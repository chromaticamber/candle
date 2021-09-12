def on_sound_loud():
    global Lit
    Lit = not (Lit)
input.on_sound(DetectedSound.LOUD, on_sound_loud)

Flicker = 0
Lit = False
Lit = True

def on_forever():
    global Flicker
    if Lit:
        basic.show_leds("""
            . # . . .
            . # # # .
            . # # # .
            . # # # .
            . # # # .
        """)
        Flicker = randint(1, 3)
        if Flicker != 1:
            led.unplot(1, 0)
            led.plot(Flicker, 0)
        basic.pause(200)
    else:
        basic.clear_screen()
basic.forever(on_forever)
