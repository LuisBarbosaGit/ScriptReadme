import questionary

#Função para concatenar linguagens e tecnologias utilizadas
def formatScript(tech):
    i = 0
    for names in tech:
        tech[i] = f"{i + 1}-{names}"
        i+=1
    return tech

#Função para formatar o texto como MarkDown
def readmeModel(title, description, techusage, functions= ""):
    readMe = f"""
#{title}

#{description}
#Tecnologias Utilizadas
{techusage}

#Funcionalidades:
{functions}
    """
    return readMe

#Função principal para realizar o questionario
def makeQuestionary():
    RepositoryName = questionary.text("Qual o Nome do seu repositorio ?\n", multiline=False).ask()
    Description = questionary.text("Digite uma descrição para seu repositorio\n", multiline=True).ask()
    TechUsage =  questionary.checkbox(
        'Selecione Linguagens Utilizadas',
            choices=[
                'Python',
                'Javascript',
                'Typescript'
            ]).ask()
    
    ReadmePath = questionary.path(
        "Qual o Diretorio que deseja Salvar o Read.Me ?",
    ).ask()
    listTechUsage = "\n".join(formatScript(TechUsage))
    finalModel = readmeModel(RepositoryName, Description, listTechUsage)
    return (finalModel, ReadmePath)


    
