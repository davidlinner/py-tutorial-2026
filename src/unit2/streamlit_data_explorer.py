import streamlit as st
import pandas as pd

scores = pd.DataFrame(
    {
        "name": ["Ada", "Bob", "Charly", "Dora", "Eve"],
        "group": ["A", "A", "B", "B", "A"],
        "score": [18, 12, 15, 9, 20],
    }
)

st.title("Mini Data Explorer")
minimum_score = st.slider("Minimum score", 0, 20, 12)
selected_group = st.selectbox("Group", ["All"] + sorted(scores["group"].unique().tolist()))

filtered = scores[scores["score"] >= minimum_score]
if selected_group != "All":
    filtered = filtered[filtered["group"] == selected_group]

st.subheader("Filtered table")
st.dataframe(filtered, use_container_width=True)
st.metric("Average score", round(filtered["score"].mean(), 2) if not filtered.empty else "n/a")
