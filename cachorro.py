class Cachorro(Animal):
    def __init__(self, nome, idade, porte):
        super().__init__(nome, idade)
        self.__porte = porte  

    def get_porte(self):
        return self.__porte

    def set_porte(self, porte):
        self.__porte = porte

    def mostrar(self):
        return f"Cachorro - Nome: {self.get_nome()}, Idade: {self.get_idade()} anos, Porte: {self.get_porte()}"
