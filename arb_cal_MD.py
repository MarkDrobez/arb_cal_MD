import streamlit as st

def calculate_arbitrage(odds1, odds2, total_bet):
    if odds1 <= 1 or odds2 <= 1:
        return None, None, None, None
    
    # Convert odds to implied probabilities
    prob1 = 1 / odds1
    prob2 = 1 / odds2
    total_prob = prob1 + prob2
    
    # Check if arbitrage exists
    if total_prob >= 1:
        return None, None, None, None  # No arbitrage opportunity
    
    # Calculate bet sizing
    stake1 = (total_bet * prob2) / total_prob
    stake2 = (total_bet * prob1) / total_prob

    # Calculate guaranteed profit
    profit = (stake1 * odds1) - total_bet
    return stake1, stake2, profit, (profit / total_bet) * 100

# Streamlit UI
st.title("🔢 Delayed Arbitrage Betting Calculator")

st.write("Enter the odds from two sportsbooks and your total bet amount to check for an arbitrage opportunity.")

# User Inputs
odds1 = st.number_input("📌 Odds from Pinnacle (or fast book)", min_value=1.01, step=0.01, format="%.2f")
odds2 = st.number_input("📌 Odds from slow book (before adjustment)", min_value=1.01, step=0.01, format="%.2f")
total_bet = st.number_input("💰 Total Bet Amount (€)", min_value=1.0, step=1.0, format="%.2f")

if st.button("🔍 Calculate Arbitrage"):
    stake1, stake2, profit, profit_percent = calculate_arbitrage(odds1, odds2, total_bet)
    
    if profit is None:
        st.error("❌ No arbitrage opportunity detected. The combined implied probability is too high.")
    else:
        st.success(f"✅ Arbitrage Opportunity Found!")
        st.write(f"**Bet €{stake1:.2f} on odds {odds1}**")
        st.write(f"**Bet €{stake2:.2f} on odds {odds2}**")
        st.write(f"**Guaranteed Profit: €{profit:.2f} ({profit_percent:.2f}%)**")

st.markdown("---")
st.markdown("⚡ **Tip:** This tool helps detect delayed arbitrage where one sportsbook adjusts odds slower than another.")
