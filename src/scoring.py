def score_position(position: str):
    """
    Pontuações simples.
    """
    if position == "above_mean":
        return 2
    elif position == "equal_to_mean":
        return 1
    elif position == "below_mean":
        return 0
    else:
        return 0


def normalize_score(raw_score, max_score):
    """
    Converte pontuação bruta para escala 0–100.
    """
    return round((raw_score / max_score) * 100, 2)


def classify_risk(score):
    """
    Classificação baseada na pontuação final.
    """
    if score >= 70:
        return "A - Baixo risco"
    elif score >= 40:
        return "B - Risco moderado"
    else:
        return "C - Alto risco"


def generate_score(benchmark_report):
    """
    benchmark_report = saída da função generate_benchmark_report()
    """

    indicators_stats = benchmark_report["sector_statistics"]

    raw_score = 0
    max_score = 0
    detailed_results = {}

    for indicator, stats in indicators_stats.items():
        pos = stats["position"]
        pts = score_position(pos)

        raw_score += pts
        max_score += 2  # max por indicador

        detailed_results[indicator] = {
            "target_value": stats["target_value"],
            "mean": stats["mean"],
            "position": pos,
            "points": pts
        }

    final_score = normalize_score(raw_score, max_score)
    risk_class = classify_risk(final_score)

    return {
        "final_score": final_score,
        "risk_class": risk_class,
        "details": detailed_results
    }


# Teste local
if __name__ == "__main__":
    from mock_data import load_mock_data
    from src.benchmark import generate_benchmark_report

    target, bench = load_mock_data()
    report_bench = generate_benchmark_report(target, bench)

    scoring = generate_score(report_bench)

    print("\nFinal score:", scoring["final_score"])
    print("Risk Class:", scoring["risk_class"])
    print("\nDetails:\n", scoring["details"])
