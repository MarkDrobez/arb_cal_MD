import streamlit as st

def calculate_minimum_odds(odds1, bet1, target_profit=0.002):
    if odds1 <= 1 or bet1 <= 0:
        return None  # Invalid input
    
    # Solve for minimum odds2 required to achieve at least 0.2% arbitrage
    min_odds2 = (bet1 * odds1) / (bet1 * (1 + target_profit))
    return min_odds2

def calculate_stake(odds1, bet1, odds2):
    if odds2 <= 1:
        return None  # Invalid odds2
    
    # Calculate the stake needed for odds2 to complete arbitrage
    stake2 = (bet1 * odds1) / odds2
    return stake2

# Streamlit UI
st.title("🔢 Delayed Arbitrage Betting Calculator")

st.write("Step 1: Enter the first bet details. Step 2: Enter the second odds to calculate the required bet size for arbitrage.")

# Step 1: User inputs first bet
odds1 = st.number_input("📌 Odds from Pinnacle (or fast book)", min_value=1.01, step=0.01, format="%.2f")
bet1 = st.number_input("💰 Bet Amount (€) on first odds", min_value=1.0, step=1.0, format="%.2f")

# Step 1 Output: Minimum required odds for arbitrage
min_odds2 = calculate_minimum_odds(odds1, bet1)
if min_odds2:
    st.info(f"ℹ️ Minimum required odds for at least 0.2% arbitrage: **{min_odds2:.2f}**")

# Step 2: User inputs second odds
odds2 = st.number_input("📌 Second Odds (Slower Bookmaker)", min_value=1.01, step=0.01, format="%.2f")

if st.button("🔍 Calculate Second Bet Amount"):
    stake2 = calculate_stake(odds1, bet1, odds2)
    
    if stake2 is None:
        st.error("❌ Invalid second odds. Please enter valid values.")
    else:
        st.success(f"✅ To complete the arbitrage, place a bet of **€{stake2:.2f}** on the second odds.")

st.markdown("---")
st.markdown("⚡ **Tip:** Use this tool to determine both the required second odds and the stake to guarantee a profitable arbitrage opportunity.")
