import streamlit as st

# Configure the page
st.set_page_config(page_title="Streamlit App with Navbar", layout="wide")

# Navbar items
def navbar():
    st.markdown(
        """
        <style>
            .navbar {
                background-color: #2E86C1;
                padding: 10px;
                font-size: 18px;
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: space-between;
                align-items: center;
                color: white;
            }
            .navbar a {
                text-decoration: none;
                color: white;
                margin: 0 15px;
            }
            .navbar a:hover {
                text-decoration: underline;
            }
        </style>
        <div class="navbar">
            <div>
                <a href="/?page=home">Home</a>
                <a href="/?page=about">About</a>
                <a href="/?page=services">Services</a>
                <a href="/?page=contact">Contact</a>
            </div>
            <div>
                <a href="/?page=login">Login</a>
                <a href="/?page=signup">Signup</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Define the content for each page
def home_page():
    st.title("Welcome to My Streamlit App")
    st.write("This is the **Home** page.")
    st.write("Explore the other sections using the navigation links above.")

def about_page():
    st.title("About Us")
    st.write("""
        ### About This App
        This app is built using **Streamlit**, a powerful Python framework for creating interactive web apps.
        
        **Features:**
        - Simple and responsive navbar.
        - Dedicated sections for home, about, services, and contact.
        - Fully customizable and lightweight.

        **Technologies Used:**
        - Python
        - Streamlit
        - HTML/CSS for styling

        We aim to make web apps simple and accessible to everyone!
    """)
    st.image("https://placekitten.com/800/400", caption="Streamlit makes web development fun!")

def services_page():
    st.title("Our Services")
    st.write("This is the **Services** page. Here you can describe what services you offer.")

def contact_page():
    st.title("Contact Us")
    st.write("This is the **Contact** page. Add your contact details here.")

# Router to manage pages
def router():
    query_params = st.experimental_get_query_params()
    page = query_params.get("page", ["home"])[0]

    # Render the selected page
    if page == "home":
        home_page()
    elif page == "about":
        about_page()
    elif page == "services":
        services_page()
    elif page == "contact":
        contact_page()
    else:
        st.error("Page not found!")

# Main function to render the app
def main():
    navbar()
    router()

if __name__ == "__main__":
    main()
