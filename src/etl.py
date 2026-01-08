
print("🚀 SCRIPT INICIADO")


import pandas as pd
from pathlib import Path

# =========================
# CONFIGURAÇÕES
# =========================
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

INPUT_FILE = DATA_DIR / "usuarios.csv"
OUTPUT_FILE = DATA_DIR / "mensagens_geradas.csv"

# =========================
# EXTRACT
# =========================
def extract():
    print("🔹 Extraindo dados do CSV...")
    return pd.read_csv(INPUT_FILE)

# =========================
# TRANSFORM
# =========================
def transform(df):
    print("🔹 Transformando dados...")

    def gerar_mensagem(row):
        return (
            f"Olá {row['nome']}! 👋 "
            f"Sua conta {row['conta']} está ativa. "
            f"Cartão final {row['cartao']}. "
            f"Obrigado por ser nosso cliente!"
        )

    df["mensagem"] = df.apply(gerar_mensagem, axis=1)
    return df

# =========================
# LOAD
# =========================
def load(df):
    print("🔹 Salvando dados processados...")
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"✅ Arquivo gerado em: {OUTPUT_FILE}")

# =========================
# PIPELINE
# =========================
def main():
    df = extract()
    df = transform(df)
    load(df)

if __name__ == "__main__":
    main()
