class ContaBancaria:
    def __init__(self):
        self.saldo = 0
        self.depositos = []
        self.saques = []
        self.saques_realizados = 0

    def depositar(self, valor):
        self.saldo += valor
        self.depositos.append(valor)
        print(f"Depósito de R${valor:.2f} realizado com sucesso.")

    def sacar(self, valor):
        if self.saques_realizados >= 3:
            print("Limite de saques diários atingido.")
            return
        if valor > 1500:
            print("Valor máximo de saque permitido é R$1500.")
            return
        if valor > self.saldo:
            print("Saldo insuficiente.")
            return
        self.saldo -= valor
        self.saques.append(valor)
        self.saques_realizados += 1
        print(f"Saque de R${valor:.2f} realizado com sucesso.")

    def extrato(self):
        print("#" * 7 + " Extrato " + "#" * 7)
        print("Depósitos:")
        for deposito in self.depositos:
            print(f" - R${deposito:.2f}")
        print("Saques:")
        for saque in self.saques:
            print(f" - R${saque:.2f} (Saque)")
        print(f"Saldo atual: R${self.saldo:.2f}")

    def mostrar_menu(self):
        print("### Menu ###")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Extrato")
        print("4. Sair")

    def executar_opcao(self, opcao):
        if opcao == 1:
            valor = float(input("Digite o valor a ser depositado: "))
            self.depositar(valor)
        elif opcao == 2:
            valor = float(input("Digite o valor a ser sacado: "))
            self.sacar(valor)
        elif opcao == 3:
            self.extrato()
        elif opcao == 4:
            print("Saindo...")
            return False
        else:
            print("Opção inválida.")
        return True


# Exemplo de uso do sistema:
conta = ContaBancaria()
continuar = True
while continuar:
    conta.mostrar_menu()
    opcao = int(input("Escolha uma opção: "))
    continuar = conta.executar_opcao(opcao)



