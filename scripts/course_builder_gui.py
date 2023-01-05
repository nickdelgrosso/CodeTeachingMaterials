
import streamlit as st
import files
import workshop_recipe as wr


# GUI

st.title('Data Science Workshop Builder')

st.header('Workshop')
st.text_input(label='Workshop Title')
git_remote_url = st.text_input(label='GitHub Repo URL')

st.header('Sessions')
num_days = st.number_input(label="Number of Sessions", min_value=1, max_value=10)


basenames = {p.stem: p for p in files.get_notebook_paths()}
sessions = []
tabs = st.tabs([f"Session {idx}" for idx in range(1, num_days+1)])
for idx, tab in enumerate(tabs, start=1):
    title = tab.text_input(label='Session Title', key=f"title_{idx}")
    units = tab.multiselect(label='Lessons', key=f"lessons_{idx}", options=list(sorted(basenames.keys())), max_selections=6)
    unit_paths = [basenames[name] for name in units]
    unit_names = [tab.text_input(label="Lesson Filename", value=path.name) for path in unit_paths]
    session = wr.create_session(title=title, unit_paths=unit_paths, unit_names=unit_names)
    sessions.append(session)


recipe = wr.create_recipe(url=git_remote_url, sessions=session)


st.download_button(label="Download Recipe File", data=wr.serialize_recipe(recipe=recipe))
recipe