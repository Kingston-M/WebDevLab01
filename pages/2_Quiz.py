import streamlit as st

st.set_page_config(page_title="Music Producer Quiz", page_icon="🎛️")

st.title("🎛️ What Type of Music Producer Are You?")
st.write("Answer five questions to discover the production style that best matches you.")

st.image("Images/download (1).webp", caption="Start your producer journey")

melody = 0
rhythm = 0
experimental = 0

st.header("1. What part of producing interests you most?")
q1 = st.radio(
    "Choose one:",
    ["Melodies and chords", "Drums and grooves", "Sound design and unusual textures"]
) 
if q1 == "Melodies and chords":
    melody += 2
elif q1 == "Drums and grooves":
    rhythm += 2
else:
    experimental += 2

st.header("2. Which genres do you enjoy?")
q2 = st.multiselect(  #NEW
    "Choose any that apply:",
    ["Hip-hop", "R&B", "Pop", "Rock", "Electronic"]
)  
if "R&B" in q2 or "Pop" in q2:
    melody += 1
if "Hip-hop" in q2 or "Rock" in q2:
    rhythm += 1
if "Electronic" in q2:
    experimental += 1

st.image("Images/OIP (5).webp", caption="Rhythm, movement, and groove")

st.header("3. How important is experimentation to you?")

q3 = st.slider("Rate experimentation from 1 to 10:", 1, 10, 5)  #NEW
if q3 >= 8:
    experimental += 3
elif q3 >= 5:
    experimental += 1
else:
    melody += 1

st.header("4. How many years have you been interested in music?")
q4 = st.number_input("Enter a number:", min_value=0, max_value=50, value=1, step=1)  #NEW
if q4 >= 5:
    melody += 1
    rhythm += 1
else:
    experimental += 1

st.image("Images/OIP (6).webp", caption="Creative ideas and experimentation")

st.header("5. What would you create first?")
q5 = st.selectbox(
    "Choose one:",
    ["A chord progression", "A drum pattern", "A new sound"]
) 
if q5 == "A chord progression":
    melody += 2
elif q5 == "A drum pattern":
    rhythm += 2
else:
    experimental += 2

if st.button("Show My Result"):  
    scores = {
        "Melody Producer": melody,
        "Rhythm Producer": rhythm,
        "Experimental Producer": experimental
    }

    result = max(scores, key=scores.get)

    st.divider()
    st.header("Your Result")

    if result == "Melody Producer":
        st.success("🎹 You are a Melody Producer!")
        st.write("You focus on chords, melodies, harmony, and the musical ideas that shape a track.")
    elif result == "Rhythm Producer":
        st.success("🥁 You are a Rhythm Producer!")
        st.write("You focus on drums, grooves, timing, and the energy of a track.")
    else:
        st.success("🎛️ You are an Experimental Producer!")
        st.write("You focus on unusual sounds, experimentation, and creative textures.")

    st.write(f"Melody score: {melody}")
    st.write(f"Rhythm score: {rhythm}")
    st.write(f"Experimental score: {experimental}")

