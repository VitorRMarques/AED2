const prompt = require("prompt-sync")()

let tarefas = []

while (true){
    let opcao = prompt(
        "\nGerenciador de Tarefas\n" +
        "1. Adicionar Tarefa\n" +
        "2. Listar Tarefas\n" +
        "3. Remover tarefa\n"+
        "4. Sair\n" +
        "Escolha uma opcao: "
    )
    if (opcao == 1) {
        let tarefa = prompt("Digite a tarefa: ")
        tarefas.push(tarefa)
        console.log(`Tarefa ${tarefa} adicionada com sucesso`)
    } else if (opcao == 2) {
        tarefas.forEach((t, i) => console.log(`${i + 1}. ${t}`))
    } else if (opcao == 3){
        let indice = Number.parseInt(prompt("Digite o indice da remover: ")) -1 
        if (indice > 0 && indice < tarefas.length) {
            tarefas.splice(indice, 1)
            console.log("Tarefa Removida com sucesso!")
        } else {
            console.log("Numero invalido")
        }
    } else if (opcao == 4){
        console.log("Saindo do programa...")
        break
    } else {
        console.log("Opcao invalida!")
    }
}