import streamlit as st
import info
import pandas as pd

st.set_page_config(page_title="Portfolio", page_icon="📄", layout="wide")

def about_me():
    st.header("About Me")
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image(info.profile_picture, width=180)
    with col2:
        st.write(info.about_me)
    st.divider()

def sidebar_links():
    st.sidebar.header("Links")
    st.sidebar.markdown(f"[LinkedIn]({info.my_linkedin_url})")
    st.sidebar.markdown(f"[GitHub]({info.my_github_url})")
    st.sidebar.markdown(f"[Email](mailto:{info.my_email_address})")

def education():
    st.header("Education")
    st.subheader(info.education_data["Degree"])
    st.write(f"**{info.education_data['Institution']}** — {info.education_data['Location']}")
    st.write(f"Graduation: {info.education_data['Graduation Date']}")
    st.write(f"GPA: {info.education_data['GPA']}")
    df = pd.DataFrame(info.course_data)
    st.dataframe(df, use_container_width=True)
    st.divider()

def professional_experience():
    st.header("Professional Experience")
    for title, (details, image) in info.experience_data.items():
        with st.expander(title):
            col1, col2 = st.columns([1, 2])
            with col1:
                st.image(image, width=220)
            with col2:
                for detail in details:
                    st.write(detail)
    st.divider()

def projects():
    st.header("Projects")
    for name, description in info.projects_data.items():
        st.subheader(name)
        st.write(description)
    st.divider()

def skills():
    st.header("Programming Skills")
    for language, level in info.programming_data.items():
        icon = info.programming_icons.get(language, "")
        st.write(f"{icon} **{language}**")
        st.progress(level)
    st.divider()

    st.header("Spoken Languages")
    for language, level in info.spoken_data.items():
        icon = info.spoken_icons.get(language, "")
        st.write(f"{icon} **{language}:** {level}")
    st.divider()

def activities():
    st.header("Leadership & Activities")
    for title, (details, image) in info.leadership_data.items():
        st.subheader(title)
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(image, width=220)
        with col2:
            for detail in details:
                st.write(detail)

    for title, details in info.activity_data.items():
        st.subheader(title)
        for detail in details:
            st.write(detail)

about_me()
sidebar_links()
education()
professional_experience()
projects()
skills()
activities()
