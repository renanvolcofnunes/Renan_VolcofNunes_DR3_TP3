# TP3 - Assistente de Conta Digital Simulada

## 1. Descrição do projeto

Aplicação educacional desenvolvida em Python utilizando LangChain, um agente ReAct, ferramentas personalizadas e memória conversacional.

O projeto simula consultas a uma conta digital por meio de perguntas em linguagem natural.

Todos os dados financeiros são fictícios. A aplicação não acessa instituições bancárias nem realiza operações financeiras reais.

## 2. Problema de negócio

Usuários de contas digitais precisam consultar saldos e movimentações financeiras.

A aplicação busca simplificar essas consultas, permitindo que o usuário converse com um assistente em vez de navegar por diferentes opções de um aplicativo.

## 3. Objetivo

Desenvolver um agente inteligente capaz de interpretar perguntas, selecionar ferramentas, consultar dados simulados e manter o contexto da conversa.

## 4. Público-alvo

Usuários de contas digitais interessados em consultar informações financeiras de maneira simples e intuitiva.

## 5. Funcionalidades

- Consultar saldo disponível.
- Consultar extrato financeiro.
- Identificar despesas registradas.
- Responder perguntas relacionadas ao histórico da conversa.
- Utilizar duas ferramentas em uma mesma solicitação.
- Interagir pelo terminal.

## 6. Tecnologias utilizadas

- Python 3.14.0
- LangChain 1.5.2
- LangChain OpenAI 1.8.5
- LangGraph 1.2.24
- Groq API no plano Free
- Modelo openai/gpt-oss-20b
- Visual Studio Code
- Git e GitHub

## 7. Ferramentas do agente

### consultar_saldo

Consulta o saldo disponível da conta digital simulada.

Saldo cadastrado: R$ 1.200,00.

### consultar_extrato

Consulta as movimentações financeiras simuladas:

- Saldo inicial: R$ 1.000,00.
- Pix recebido: +R$ 500,00.
- Supermercado: -R$ 180,00.
- Conta de energia: -R$ 120,00.

Saldo final: R$ 1.200,00.

## 8. Funcionamento do agente

O agente utiliza LangChain com o padrão ReAct para selecionar ferramentas conforme a pergunta.

Fluxo:

1. O usuário envia uma pergunta pelo terminal.
2. O agente interpreta a solicitação.
3. O agente decide quais ferramentas utilizar.
4. As ferramentas retornam os dados simulados.
5. O agente utiliza os resultados para gerar a resposta.
6. A memória conversacional mantém o contexto da sessão.

A memória é implementada com InMemorySaver e identificada por thread_id.

O histórico fica disponível durante a execução do programa. Não existe persistência permanente entre reinicializações.

## 9. Estrutura do projeto

- main.py: interface de linha de comando.
- agente.py: configuração do modelo, agente e memória.
- ferramentas.py: implementação das ferramentas.
- requirements.txt: dependências do projeto.
- README.md: documentação.
- .gitignore: arquivos excluídos do Git.

## 10. Instruções de execução

Criar o ambiente virtual:

    py -m venv venv

Ativar o ambiente no PowerShell:

    .\venv\Scripts\Activate.ps1

Instalar as dependências:

    python -m pip install -r requirements.txt

Configurar a variável de ambiente GROQ_API_KEY com uma chave própria do Groq.

A chave não deve ser colocada no código, no README ou no GitHub.

Executar a aplicação:

    python main.py

Para encerrar, digitar:

    sair

O uso do modelo requer conexão com a internet e está sujeito aos limites do plano contratado. O projeto foi desenvolvido utilizando o plano Free.

## 11. Casos de uso e resultados observados

### Teste 1 - Consulta de saldo

Pergunta: Qual é meu saldo?

Resultado: R$ 1.200,00.

Ferramenta utilizada: consultar_saldo.

Situação: aprovado.

### Teste 2 - Consulta de extrato

Pergunta: Mostre meu extrato.

Resultado: apresentação das movimentações fictícias e saldo final de R$ 1.200,00.

Ferramenta utilizada: consultar_extrato.

Situação: aprovado.

### Teste 3 - Identificação da maior despesa

Pergunta: Qual foi minha maior despesa?

Resultado: supermercado, R$ 180,00.

Situação: aprovado.

### Teste 4 - Memória conversacional

Pergunta seguinte: E quanto foi essa despesa?

Resultado: R$ 180,00, referente ao supermercado.

O agente manteve o contexto da pergunta anterior.

Situação: aprovado.

### Teste 5 - Utilização das duas ferramentas

Pergunta: Qual é meu saldo e quais são minhas últimas movimentações? Consulte as duas ferramentas para confirmar os dados.

Resultado: saldo de R$ 1.200,00 e apresentação das movimentações.

Ferramentas utilizadas: consultar_saldo e consultar_extrato.

Situação: aprovado.

## 12. Comparação com uma abordagem manual

Sem o agente, o usuário precisaria consultar o saldo e o extrato separadamente, identificar os valores e comparar as informações.

Com o agente, o usuário pode fazer perguntas em linguagem natural. O sistema seleciona as ferramentas necessárias, recupera os dados e apresenta uma resposta organizada.

A memória permite compreender perguntas relacionadas a interações anteriores, sem exigir que o usuário repita todas as informações.

## 13. Limitações

- Os dados financeiros são fictícios e definidos no código.
- Não há integração com contas bancárias reais.
- O saldo e o extrato não são alterados durante a conversa.
- Não são realizadas transferências ou pagamentos.
- O histórico de memória não persiste após o encerramento do programa.
- As respostas dependem do modelo de linguagem e podem apresentar imprecisões.
- A execução depende de conexão e da disponibilidade da API Groq.

## 14. Boas práticas

O código foi organizado em arquivos separados para interface, agente e ferramentas.

Foram utilizados nomes descritivos, funções específicas e tratamento de exceções na interface.

A chave de API é obtida por variável de ambiente e não deve ser versionada.

## 15. Referências e ferramentas utilizadas

- Material didático da disciplina Desenvolvimento de Data-Driven Apps com Python, Infnet.
- Aulas 11, 12 e 13, ministradas por Tiago Xavier.
- Slides da Etapa 4 - Introdução ao framework LangChain.
- Slides da Etapa 5 - Tarefas complexas com Chains e LLMs.
- Groq: serviço utilizado para executar o modelo de linguagem durante os testes.

Os resultados descritos foram obtidos durante a execução e conferência prática da aplicação.