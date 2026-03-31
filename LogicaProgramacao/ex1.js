const prompt = require("prompt-sync")()

let numeroSecreto = Math.floor(Math.random()* 100) + 1
let tentativa = 0
let palpite


do{
    palpite = parseInt(prompt("Digite um numero (entre 1 e 100) para palpite: "))
    tentativa++

    if (palpite < numeroSecreto) {
        console.log("Tente um numero maior")
    } else if (palpite > numeroSecreto) {
        console.log("Tente um numero menor")
    } else {
        console.log(`Parabens, voce acertou em ${tentativa} tentativas.`)
    }

} while( palpite !== numeroSecreto)