class Transacao:
    def __init__(self, valor: float):
        self.valor = valor


class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao: Transacao):
        self.transacoes.append(transacao)


class Conta:
    def __init__(self, limite: float, numero: int):
        self.limite = limite
        self.numero = numero
        self.saldo = 0.0
        self.historico = Historico()

    def realizar_transacao(self, transacao: Transacao) -> bool:
        if isinstance(transacao, Saque):
            return self.sacar(transacao.valor)
        elif isinstance(transacao, Deposito):
            return self.depositar(transacao.valor)
        return False

    def sacar(self, valor: float) -> bool:
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
            self.historico.adicionar_transacao(Transacao(-valor))
            return True
        return False

    def depositar(self, valor: float) -> bool:
        self.saldo += valor
        self.historico.adicionar_transacao(Transacao(valor))
        return True


class Cliente:
    def __init__(self, endereco: str):
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta: Conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, cpf: str, endereco: str):
        super().__init__(endereco)
        self.cpf = cpf


class Saque(Transacao):
    pass


class Deposito(Transacao):
    pass


# Exemplo de uso
cliente1 = PessoaFisica(cpf="123.456.789-00", endereco="Rua Exemplo, 123")
conta1 = Conta(limite=500.0, numero=1)

cliente1.adicionar_conta(conta1)

# Realizando um depósito
conta1.depositar(1000.0)

# Realizando um saque
saque = Saque(valor=200.0)
conta1.realizar_transacao(saque)

print(f"Saldo da conta {conta1.numero}: {conta1.saldo}")