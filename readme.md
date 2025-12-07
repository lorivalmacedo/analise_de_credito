# 📊 Análise de Crédito Automatizada — Case CERC

Este projeto é uma prova de conceito (POC) desenvolvida para o processo seletivo da **CERC**, demonstrando como automatizar atividades analíticas típicas de um analista de crédito, especialmente considerando o aumento de volume decorrente da **duplicata escritural**.

O objetivo é mostrar **como ganhar escala**, **reduzir a carga manual** e fornecer **pareceres automáticos de crédito**, combinando:

- Python  
- Cálculo de indicadores financeiros (ratios)  
- Benchmark com empresas do setor  
- Scoring automatizado  
- (Opcional) Geração de parecer técnico via IA Generativa  

---
## Objetivos do Projeto

1. **Automatizar três tarefas do O\*NET**, conforme solicitado no case:
   - Gerar indicadores financeiros (ratios)
   - Comparar a empresa com outras do mesmo setor/geografia
   - Preparar um relatório contendo o grau de risco da operação

2. **Criar um pipeline de análise ponta a ponta**, capaz de:
   - Carregar dados (mockados conforme orientado no case)
   - Calcular indicadores
   - Gerar benchmark com 20 empresas comparáveis
   - Atribuir score e classificação de risco
   - (Opcional) Criar parecer técnico via IA

3. **Demonstrar ganho real de eficiência**, eliminando trabalho manual antes realizado por um analista.

---
## Arquitetura da Solução
mock_data → ratios → benchmark → scoring → (IA)