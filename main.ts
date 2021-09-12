input.onSound(DetectedSound.Loud, function () {
    Lit = !(Lit)
})
let Flicker = 0
let Lit = false
Lit = true
basic.forever(function () {
    if (Lit) {
        basic.showLeds(`
            . # . . .
            . # # # .
            . # # # .
            . # # # .
            . # # # .
            `)
        Flicker = randint(1, 3)
        if (Flicker != 1) {
            led.unplot(1, 0)
            led.plot(Flicker, 0)
        }
        basic.pause(200)
    } else {
        basic.clearScreen()
    }
})
