import streamlit as st

def calculate_minimum_odds(odds1, bet1, target_profit=0.002):
    if odds1 <= 1 or bet1 <= 0:
        return None  # Invalid input
    
    # Solve for minimum odds2 required to achieve at least 0.2% arbitrage
    min_odds2 = (bet1 * odds1) / (bet1 * (1 + target_profit))
    return min_odds2

# Streamlit UI
st.title("🔢 Delayed Arbitrage Betting Calculator")

st.write("Enter the odds from the first bookmaker and your bet amount to calculate the minimum required odds on the other side for arbitrage.")

# User Inputs
odds1 = st.number_input("📌 Odds from Pinnacle (or fast book)", min_value=1.01, step=0.01, format="%.2f")
bet1 = st.number_input("💰 Bet Amount (€)", min_value=1.0, step=1.0, format="%.2f")

if st.button("🔍 Calculate Minimum Required Odds"):
    min_odds2 = calculate_minimum_odds(odds1, bet1)
    
    if min_odds2 is None:
        st.error("❌ Invalid input. Please enter valid odds and bet amount.")
    else:
        st.success(f"✅ To achieve at least 0.2% arbitrage, the second odds must be **{min_odds2:.2f}** or higher.")

st.markdown("---")
st.markdown("⚡ **Tip:** Use this tool to determine the necessary odds on the slower bookmaker to secure a profitable arbitrage opportunity.")
