const processarUsuarios = (usuarios = []) => {
    if (!Array.isArray(usuarios)) return []

    const usuariosValidos = usuarios.filter(user=> user?.nome && user?.idade)

    const usuariosFormatados = usuariosValidos.map(use => {
        const {
            nome = "Nome nao informado",
            idade = 0,
            endereco: {
                cidade = "Cidade Desconhecida",
                estado = "Estado Desconhecido"
            } = {}
        } = user ?? {}

        return {
            ...user, 
            nome,
            idade,
            localizacao: `${cidade} - ${estado}`
        }
    })

    const grupos = usuariosFormatados.reduce((acc, user) => {
        const {idade} = user

        let faixa = ""

        if (idade < 18) faixa = "Menor de idade";
        else if (idade < 30) faixa = "Jovem adulto";
        else if (idade < 60) faixa = "Adulto";
        else faixa = "Idoso"

        if (!acc.has(faixa)){
            acc.set(faixa, [])
        }

        acc.get(faixa).push(user)

        return acc
    }, new Map())

    return {
        usuariosFormatados,
        grupos
    }
}

const dados = [
    {
        nome: "Ana",
        idade: 25,
        endereco: { cidade: "Sao Paulo", estado: "SP"}
    },
    {
        nome: "Carlos",
        idade: 17,
        endereco: { cidade: "Rio de Janeiro", estado: "RJ"}
    },
    {
        nome: "Maria",
        idade: 30
    },
    null
]

const resultado = processarUsuarios(dados)

console.log("Formatados:", resultado.usuariosFormatados)
console.log("Grupos:", Array.from(resultado.grupos.entries()))