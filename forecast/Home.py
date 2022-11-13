import streamlit as st
import leafmap.foliumap as leafmap


st.set_page_config(layout="wide")


def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://img.freepik.com/premium-photo/financial-business-chart-with-diagrams-stock-numbers-showing-profits-losses_273081-4.jpg?w=2000");
             background-attachment: fixed;
             background-size: cover
         }}
         .css-af4qln span
         {{
            text-align:center;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 


# Customize the sidebar
markdown = """

GitHub Repository: <https://github.com/ujju0906/MORKET-RESEARCH_SOFTWARE>
"""
name1 = """
Taher B Dossaji (PES1UG20CS457)
"""
name2=""" 
Tarun Senthilnathan (PES1UG20CS464)
"""
name3=""" 
Ujwal KV (PES1UG20CS475) """
name4=""" 
V Himadhith (PES1UG20CS478)"""
st.sidebar.title("About")
st.sidebar.info(name1)
st.sidebar.info(name2)
st.sidebar.info(name3)
st.sidebar.info(name4)
st.sidebar.info(markdown)
logo = "https://img.freepik.com/free-vector/buy-sell-concept-design-showing-bull-bear_1017-13716.jpg?w=2000"
st.sidebar.image(logo)

# Customize page title
st.title("💹Morket Research Software 📈")

st.markdown(
    """
    This multipage app demonstrates various interactive web apps created using [streamlit] which enables the user to get an in depth
    and comprehensive infomatics about the trading world. Moreover it not only enables them to make educated sales in the relm but 
    also makes sure it is a profitable one (subject to market risk)"""
)

st.header("Features")

markdown = """
1. Fundamental Analysis
2. Sentimental Analysis
3. Stock Prediction 
4. Stock Visualise 
"""

st.markdown(markdown)

