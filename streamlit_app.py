import streamlit as st
from streamlit_option_menu import option_menu

# --- Page Setup ---
home_page = st.Page(
    page = "pages/home.py",
    title = "Home",
    icon = ":material/house:",
    
)
projects_page = st.Page(
    page = "pages/projects.py",
    title = "Projects", 
    icon = ":material/rocket_launch:",
)
values_page = st.Page(
    page = "pages/values.py",
    title = "The Jemena Values",
    icon = ":material/diversity_2:",
)
stakeholders_page = st.Page(
    page = "pages/stakeholders.py",
    title = "Our stakeholders",
    icon = ":material/communication:",
)
zinfra_page = st.Page(
    page = "pages/zinfra.py",
    title = "Zinfra",
    icon = ":material/engineering:",
)


# --- Nav setup ---
pg = st.navigation(
    {
        # pages = [home_page, projects_page, values_page]
        "Electricity": [home_page, projects_page, values_page],
        "Assets and Operations": [stakeholders_page, zinfra_page],
    }
)

# --- Run nav ---
pg.run()

# --- Logo (all pages) ---
st.logo(r"C:\Users\eylim\OneDrive - onlineeportal\Documents\GitHub\Internship-2025\assets\Jemena_BrandMark_RGB_000.png", link = "https://www.jemena.com.au/")

