import random

# Configurações gerais do projeto
NUM_BENCHMARK_COMPANIES = 20
SECTOR = "Comércio"
LOCATION = "SP"

# Empresa Alvo (dados fixos)
def generate_target_company():
    return {
        "company_id": "C0001",
        "name": "Comercial Alfa LTDA",
        "sector": SECTOR,
        "location": LOCATION,
        "financials": {
            "assets_current": 712450,
            "liabilities_current": 438920,
            "assets_total": 1248930,
            "liabilities_total": 798310,
            "equity": 450620,
            "revenue": 2860450,
            "net_income": 214370
        },
        "receivables": {
            "total_registered": 985340,
            "average_ticket": 3120,
            "buyers_concentration": {
                "top1": 0.37,
                "top3": 0.68
            },
            "receivables_default_rate": 0.021
        },
        "credit_history": {
            "delinquencies_last_year": 2,
            "avg_payment_delay_days": 9
        }
    }

# Empresas de benchmark
def generate_benchmark_company(index: int):
    """
    Gera uma empresa comparável com pequenas variações
    realistas nos valores financeiros e de recebíveis.
    """
    base_assets_current = random.randint(450000, 900000)
    base_liabilities_current = int(base_assets_current * random.uniform(0.55, 0.85))

    assets_total = base_assets_current + random.randint(450000, 650000)
    liabilities_total = int(assets_total * random.uniform(0.55, 0.80))
    equity = assets_total - liabilities_total

    revenue = random.randint(1800000, 3600000)
    net_income = int(revenue * random.uniform(0.05, 0.12))

    total_registered = random.randint(600000, 1200000)
    average_ticket = random.randint(2500, 3800)

    return {
        "company_id": f"C{1000 + index}",
        "sector": SECTOR,
        "location": LOCATION,
        "financials": {
            "assets_current": base_assets_current,
            "liabilities_current": base_liabilities_current,
            "assets_total": assets_total,
            "liabilities_total": liabilities_total,
            "equity": equity,
            "revenue": revenue,
            "net_income": net_income
        },
        "receivables": {
            "total_registered": total_registered,
            "average_ticket": average_ticket,
            "buyers_concentration": {
                "top1": round(random.uniform(0.30, 0.50), 2),
                "top3": round(random.uniform(0.55, 0.78), 2)
            },
            "receivables_default_rate": round(random.uniform(0.015, 0.035), 3)
        },
        "credit_history": {
            "delinquencies_last_year": random.randint(0, 4),
            "avg_payment_delay_days": random.randint(5, 15)
        }
    }

# Funções públicas para acessar os dados
def load_mock_data():
    """
    Retorna:
    - empresa alvo
    - lista de empresas benchmark
    """
    target = generate_target_company()
    benchmark = [generate_benchmark_company(i) for i in range(NUM_BENCHMARK_COMPANIES)]
    return target, benchmark


# Execução de teste (opcional)
if __name__ == "__main__":
    t, b = load_mock_data()
    print("Empresa alvo:", t)
    print("\nQtde benchmark:", len(b))
    print("\nPrimeira empresa benchmark:", b[0])
