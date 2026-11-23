import os
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import InMemorySaver
from ferramentas import tools


def criar_agente():

    chave = os.getenv("GROQ_API_KEY")

    if not chave:
        raise RuntimeError("GROQ_API_KEY não configurada.")

    llm = ChatOpenAI(model="openai/gpt-oss-20b", temperature=0, api_key=chave, base_url="https://api.groq.com/openai/v1")

    agente = create_agent(model=llm, tools=tools, checkpointer=InMemorySaver(), system_prompt=(
            "Você é um assistente de conta digital simulada. "
            "Utilize as ferramentas para consultar saldo e extrato. "
            "Use apenas as informações retornadas pelas ferramentas. "
            "Não invente datas, movimentações ou valores. "
            "Se alguma informação não estiver disponível, informe isso. "
            "Os dados são fictícios e apenas demonstrativos. "
            "Não realize operações bancárias reais."))

    return agente