from langchain.tools import tool

@tool(description="Consulta o saldo disponível de uma conta digital simulada.")
def consultar_saldo() -> str:

    saldo = "R$ 1.200,00"

    return f"Saldo disponível da conta simulada: {saldo}"


@tool(description="Consulta as últimas movimentações de uma conta digital simulada.")
def consultar_extrato() -> str:

    extrato = (
        "Saldo inicial: R$ 1.000,00\n"
        "Pix recebido: +R$ 500,00\n"
        "Supermercado: -R$ 180,00\n"
        "Conta de energia: -R$ 120,00"
    )

    return f"Extrato da conta simulada:\n{extrato}"

tools = [consultar_saldo, consultar_extrato]
