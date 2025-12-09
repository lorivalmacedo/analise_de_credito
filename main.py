import os

from mock_data import load_mock_data
from src.benchmark import generate_benchmark_report
from src.scoring import generate_score

# A importação da IA é opcional 
try:
    from src.llm_report import generate_credit_report
    LLM_AVAILABLE = True
except Exception:
    LLM_AVAILABLE = False


def run_pipeline():
    # 1. Carregar dados mock
    target_company, benchmark_companies = load_mock_data()

    print("=== EMPRESA ALVO ===")
    print(target_company["name"])
    print(f"Setor: {target_company['sector']} | Localização: {target_company['location']}")
    print()

    # 2. Gerar benchmark
    benchmark_report = generate_benchmark_report(target_company, benchmark_companies)

    print("=== RATIOS DA EMPRESA ALVO ===")
    for k, v in benchmark_report["target_ratios"].items():
        print(f"{k}: {v:.4f}")
    print()

    # 3. Gerar score
    score_report = generate_score(benchmark_report)

    print("=== SCORE FINAL ===")
    print("Score:", score_report["final_score"])
    print("Classificação de risco:", score_report["risk_class"])
    print()

    print("=== DETALHES POR INDICADOR ===")
    for ind, data in score_report["details"].items():
        print(
            f"{ind} | valor: {data['target_value']:.4f} | "
            f"média setor: {data['mean']:.4f} | posição: {data['position']} | "
            f"pontos: {data['points']}"
        )
    print()

    # 4. Parecer via IA
    openai_key = os.getenv("OPENAI_API_KEY")

    if LLM_AVAILABLE and openai_key:
        print("=== PARECER GERADO VIA IA ===\n")
        try:
            report_text = generate_credit_report(score_report, benchmark_report)
            print(report_text)
        except Exception as e:
            print("Falha ao gerar parecer via IA:")
            print(e)
    else:
        print("=== PARECER VIA IA NÃO GERADO ===")
        if not LLM_AVAILABLE:
            print("- Módulo src.llm_report não disponível ou dependências não instaladas.")
        if not openai_key:
            print("- Variável de ambiente OPENAI_API_KEY não configurada.")
        print("Mesmo assim, o pipeline de análise (dados, benchmark e score) está completo.")


if __name__ == "__main__":
    run_pipeline()
