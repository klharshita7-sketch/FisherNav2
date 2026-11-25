import streamlit as st

st.set_page_config(
    page_title="FisherNav",
    page_icon="🚤",
    layout="wide"
)

st.title("🚤 FisherNav")
st.subheader("Fishing Boat Route and Safety Advisor")

st.write(
    "Welcome! Your assistant for fishing trip "
    "preparation and boating safety awareness."
)

st.divider()

menu = st.sidebar.selectbox(
    "Choose a feature",
    [
        "Home",
        "Weather Awareness",
        "Boat Safety",
        "Trip Preparation",
        "AI Assistant"
    ]
)

if menu == "Home":
    st.header("Welcome to FisherNav")
    st.info("Explore boating safety and trip preparation.")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Project", "FisherNav")
        st.write("🌦️ Weather awareness")

    with col2:
        st.metric("Version", "1.0")
        st.write("🛟 Boat safety guidance")

elif menu == "Weather Awareness":
    st.header("🌦️ Weather Awareness")
    st.warning(
        "Always check official marine forecasts "
        "and warnings before travelling."
    )

    st.write("Important weather factors:")
    st.write("- Wind conditions")
    st.write("- Wave conditions")
    st.write("- Rain and visibility")
    st.write("- Official marine warnings")

elif menu == "Boat Safety":
    st.header("🛟 Boat Safety Checklist")

    items = [
        "Life jackets",
        "Communication equipment",
        "Emergency supplies",
        "First aid kit",
        "Boat condition",
        "Emergency contact information"
    ]

    for item in items:
        st.checkbox(item)

elif menu == "Trip Preparation":
    st.header("🛥️ Trip Preparation")

    captain = st.text_input("Captain name")
    date = st.date_input("Trip date")

    if st.button("Prepare Trip"):
        st.success("Trip preparation form completed.")
        st.write("Captain:", captain)
        st.write("Date:", date)

elif menu == "AI Assistant":
    st.header("🤖 FisherNav Assistant")

    question = st.text_input(
        "Ask a boating safety question"
    )

    if st.button("Get Answer"):
        if question.strip():
            st.info(
                "This is the initial demo assistant. "
                "AI integration will be added in the next stage."
            )
        else:
            st.warning("Please enter a question.")

st.divider()

st.caption(
    "FisherNav | Educational prototype. "
    "Not a substitute for official navigation, "
    "marine forecasts or emergency services."
)
