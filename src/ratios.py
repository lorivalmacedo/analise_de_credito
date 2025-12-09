def safe_division(a, b):
    """Evitar divisão por zero retornando None."""
    try:
        return a / b if b != 0 else None
    except:
        return None


# Cálculos dos principais indicadores financeiros
def calculate_liquidity_ratios(fin):
    """Indicadores de liquidez."""
    return {
        "current_ratio": safe_division(fin["assets_current"], fin["liabilities_current"])
    }

def calculate_leverage_ratios(fin):
    """Indicadores ligados à estrutura de capital."""
    return {
        "debt_ratio": safe_division(fin["liabilities_total"], fin["assets_total"]),
        "equity_ratio": safe_division(fin["equity"], fin["assets_total"])
    }

def calculate_profitability_ratios(fin):
    """Indicadores de lucratividade."""
    revenue = fin["revenue"]
    net_income = fin["net_income"]
    assets_total = fin["assets_total"]
    equity = fin["equity"]

    return {
        "profit_margin": safe_division(net_income, revenue),
        "return_on_assets": safe_division(net_income, assets_total),
        "return_on_equity": safe_division(net_income, equity)
    }


# Função principal
def calculate_all_ratios(company_data):
    fin = company_data["financials"]

    ratios = {}
    ratios.update(calculate_liquidity_ratios(fin))
    ratios.update(calculate_leverage_ratios(fin))
    ratios.update(calculate_profitability_ratios(fin))

    return ratios


# Teste local
if __name__ == "__main__":
    sample = {
        "financials": {
            "assets_current": 500000,
            "liabilities_current": 300000,
            "assets_total": 900000,
            "liabilities_total": 600000,
            "equity": 300000,
            "revenue": 1200000,
            "net_income": 120000
        }
    }

    print(calculate_all_ratios(sample))