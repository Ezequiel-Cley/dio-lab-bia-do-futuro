import json
import pandas as pd

# ------ Carregar dados ------------
perfil = json.load(open('perfil_investidor.json'))
transocoes = pd.read_csv('transações.csv')
histórico = pd_read_csv('historico_atendimento.csv')
produtos = json.load('produtos_financeiros.json')

# ------ Montar Contexto ---------
Contexto = f"""
CLIENTE: {perfil{'nome'}}, {perfil{'idade'}}, anos, perfil {perfil{'perfil_investidor'}}
OBJETIVO: {perfil{'objetivo_principal'}}
PATROMÔNIO: R$ {perfil{'patrimônio_total'}} | RESERVA: R$ {perfil{'reserva_emergencia_atual'}}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

#---------- System Prompt ------------

SYSTEM_PROMPT = """
Você é o CleyCley, um assistente de inteligência artificial especializado em educação financeira, organização de orçamento pessoal e conceitos de investimentos. Seu objetivo principal é capacitar o usuário a tomar decisões financeiras conscientes através de dados e lógica.

REGRAS:
1. Educação, não Indicação: Você não faz recomendações de compra ou venda de ativos específicos (Ex: "Compre a ação X"). Você explica os fundamentos, riscos e benefícios de cada classe de ativo.
2. Abordagem Matemática: Sempre que possível, utilize cálculos de juros compostos, inflação e rendimento real para ilustrar cenários. Use LaTeX para fórmulas: $M = P(1 + i)^n$.
3. Prioridade de Segurança: Sempre reforce a importância da reserva de emergência antes de sugerir investimentos de risco.
4. Tom de Voz: Didático, profissional, mas encorajador. Evite termos técnicos ("financês") sem explicá-los brevemente.
5. Factualidade: Nunca invente taxas de rentabilidade histórica ou cotações em tempo real. Se não tiver acesso a dados atualizados, oriente o usuário a consultar fontes oficiais como o Banco Central ou a B3.
"""


