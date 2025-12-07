import numpy as np
from src.ratios import calculate_all_ratios

# Função para calcular estatísticas do setor para cada indicador
def compute_statistics(values):
    """Retorna média, desvio padrão e percentis."""
    arr = np.array(values)
    return {
        "mean": float(np.mean(arr)),
        "std": float(np.std(arr)),
        "p25": float(np.percentile(arr, 25)),
        "p50": float(np.percentile(arr, 50)),
        "p75": float(np.percentile(arr, 75)),
    }

# Função principal do benchmark
def generate_benchmark_report(target_company, benchmark_list):
    """
    Calcula:
      - ratios do alvo
      - ratios das empresas benchmark
      - estatísticas agregadas
      - posição do alvo
    """

    # 1. Ratios do alvo
    target_ratios = calculate_all_ratios(target_company)

    # 2. Ratios do benchmark
    benchmark_ratios_list = [calculate_all_ratios(c) for c in benchmark_list]

    # Organizar por indicador
    indicators = target_ratios.keys()
    stats = {}

    for ind in indicators:
        values = [b[ind] for b in benchmark_ratios_list if b[ind] is not None]

        stats[ind] = compute_statistics(values)

        # posição do alvo no setor
        target_value = target_ratios[ind]
        if target_value is None:
            position = "N/A"
        else:
            mean = stats[ind]["mean"]
            if target_value > mean:
                position = "above_mean"
            elif target_value < mean:
                position = "below_mean"
            else:
                position = "equal_to_mean"

        stats[ind]["target_value"] = target_value
        stats[ind]["position"] = position

    return {
        "target_ratios": target_ratios,
        "sector_statistics": stats
    }

# Teste local
if __name__ == "__main__":
    from mock_data import load_mock_data

    target, bench = load_mock_data()
    report = generate_benchmark_report(target, bench)

    print("\nTarget Ratios:\n", report["target_ratios"])
    print("\nSector Stats (ex: current_ratio):\n", report["sector_statistics"]["current_ratio"])
