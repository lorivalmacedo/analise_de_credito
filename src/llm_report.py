import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def build_prompt(score_report, benchmark_report):
    """
    Monta um prompt claro para o modelo gerar um parecer técnico.
    """

    final_score = score_report["final_score"]
    risk_class = score_report["risk_class"]
    details = score_report["details"]

    # Criar texto de indicadores
    indicators_text = ""
    for ind, data in details.items():
        indicators_text += (
            f"\n- {ind}: valor da empresa = {data['target_value']:.4f}, "
            f"média setor = {data['mean']:.4f}, posição = {data['position']}"
        )

    prompt = f"""
Você é um analista de crédito especializado em risco financeiro baseado em duplicatas e recebíveis.

Com base nos dados abaixo, gere um parecer profissional, claro, objetivo e técnico sobre o risco de crédito da empresa analisada.

--- SCORE FINAL ---
Score: {final_score}
Classificação: {risk_class}

--- INDICADORES ANALISADOS ---
{indicators_text}

--- INSTRUÇÕES ---
1. Explique os pontos fortes da empresa.
2. Explique os pontos fracos.
3. Diga claramente como a empresa se posiciona no setor.
4. Justifique objetivamente a classificação de risco recebida.
5. Dê uma recomendação final (ex: risco aceitável / atenção / alto risco).

Gere um texto com tom técnico, direto e bem estruturado.
"""

    return prompt


def generate_credit_report(score_report, benchmark_report, model="gpt-4.1"):
    """
    Envia o prompt ao modelo e retorna o parecer textual.
    """

    prompt = build_prompt(score_report, benchmark_report)

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "Você é um analista de crédito sênior."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message["content"]

# Teste local
if __name__ == "__main__":
    print("Teste manual — configure OPENAI_API_KEY para usar.")