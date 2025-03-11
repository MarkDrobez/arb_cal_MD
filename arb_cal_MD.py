import streamlit as st

def calculate_minimum_odds(odds1, target_profit=0.002):
    if odds1 <= 1:
        return None  # Invalid input
    
    # Correct formula for minimum required odds to achieve at least 0.2% arbitrage
    min_odds2 = 1 / (1 - (1 / odds1 + target_profit))
    return min_odds2

def calculate_stake(odds1, bet1, odds2):
    if odds2 <= 1:
        return None  # Invalid odds2
    
    # Calculate the stake needed for odds2 to complete arbitrage
    stake2 = (bet1 * odds1) / odds2
    return stake2

def calculate_arbitrage_profit(odds1, bet1, odds2, stake2):
    if stake2 is None:
        return None, None  # Invalid input
    
    payout1 = bet1 * odds1
    payout2 = stake2 * odds2
    total_bet = bet1 + stake2
    profit = min(payout1, payout2) - total_bet
    profit_percent = (profit / total_bet) * 100
    return profit, profit_percent

# Streamlit UI
st.title("🔢 Delayed Arbitrage Betting Calculator")

st.write("Step 1: Enter the first bet details. Step 2: Enter the second odds to calculate the required bet size for arbitrage.")

# Step 1: User inputs first bet
odds1 = st.number_input("📌 Odds from Pinnacle (or fast book)", min_value=1.01, step=0.01, format="%.2f")
bet1 = st.number_input("💰 Bet Amount (€) on first odds", min_value=1.0, step=1.0, format="%.2f")

# Step 1 Output: Minimum required odds for arbitrage
min_odds2 = calculate_minimum_odds(odds1)
if min_odds2:
    st.info(f"ℹ️ Minimum required odds for at least 0.2% arbitrage: **{min_odds2:.2f}**")

# Step 2: User inputs second odds
odds2 = st.number_input("📌 Second Odds (Slower Bookmaker)", min_value=1.01, step=0.01, format="%.2f")

if st.button("🔍 Calculate Second Bet Amount & Profit"):
    stake2 = calculate_stake(odds1, bet1, odds2)
    profit, profit_percent = calculate_arbitrage_profit(odds1, bet1, odds2, stake2)
    
    if stake2 is None:
        st.error("❌ Invalid second odds. Please enter valid values.")
    else:
        st.success(f"✅ To complete the arbitrage, place a bet of **€{stake2:.2f}** on the second odds.")
        if profit is not None:
            st.success(f"💰 Expected Arbitrage Profit: **€{profit:.2f} ({profit_percent:.2f}%)**")

st.markdown("---")
st.markdown("⚡ **Tip:** Use this tool to determine both the required second odds and the stake to guarantee a profitable arbitrage opportunity.")
