import streamlit as st
from strength_rules import check_strength
from breach_checker import check_pwned
from hash_generator import generate_hashes

st.set_page_config(page_title="Password Security Analyzer", layout="centered")

st.title("🔐 Password Security Analyzer")
password = st.text_input("Enter a password to analyze", type="password")

if st.button("Analyze"):
    if not password:
        st.warning("⚠️ Please enter a password.")
    else:
        # Strength check
        score, feedback = check_strength(password)
        st.subheader("1️⃣ Password Strength")
        st.success(f"Score: {score}/6")
        if feedback:
            st.info("Suggestions:")
            for item in feedback:
                st.markdown(f"- {item}")
        else:
            st.markdown("✅ Your password is strong!")

        # Breach check
        st.subheader("2️⃣ Data Breach Check")
        breached, count = check_pwned(password)
        if breached:
            st.error(f"⚠️ This password has been found {count} times in public data breaches!")
        else:
            st.success("✅ This password has NOT been found in known breaches.")

        # Hash output
        st.subheader("3️⃣ Hash Representations")
        hashes = generate_hashes(password)
        for algo, hash_val in hashes.items():
            st.code(f"{algo}: {hash_val}")
