import os

def createFile(finalModel, dir = '/'):
    if dir == '/':
        dir = os.getcwd()#Capta o diretorio atual se nada for digitado
        with open('README.md', 'w', encoding='utf8') as f:
            f.write(finalModel)
    else:
        fullDirectory = os.path.join(dir, "README.md")
        with open(fullDirectory, 'w', encoding='utf8') as f:
            f.write(finalModel)