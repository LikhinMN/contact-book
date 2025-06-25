import streamlit as st

# Initialize contacts list in session state if it doesn't exist
if 'contacts' not in st.session_state:
    st.session_state.contacts = []

def add_contact(name, phone, email):
    # Basic validation (add more as needed)
    if not name or not phone:
        st.error("Name and Phone number are required to add a contact.")
        return False
    # Check for duplicate phone number
    if any(contact['phone'] == phone for contact in st.session_state.contacts):
        st.error(f"A contact with phone number '{phone}' already exists.")
        return False

    st.session_state.contacts.append({"name": name, "phone": phone, "email": email})
    st.success(f"Contact '{name}' added successfully!")
    return True

# --- Custom Styles (Tailored to the provided dark theme UI) ---
st.markdown('''
    <style>
        /* General Body and Background - Dark Theme */
        body {
            font-family: 'Inter', sans-serif;
            background-color: #1A202C !important; /* Dark background from image */
            color: #E2E8F0; /* Light text for readability on dark background */
        }
        .stApp {
            margin: 0;
            padding: 0;
        }

        /* Adjusting Streamlit's main content area padding */
        section.main .block-container {
            padding-top: 2rem;
            padding-right: 2rem;
            padding-left: 2rem;
            padding-bottom: 2rem;
        }

        /* Navbar (Top Bar) - Simplified, mostly hidden as per new image */
        header {
            visibility: hidden; /* Hide Streamlit's default header */
            height: 0;
        }
        footer {
            visibility: hidden; /* Hide Streamlit's default footer */
            height: 0;
        }

        /* Custom Top Banner (Simulating "Contact Book" header in the image) */
        .top-banner {
            background-color: #2D3748; /* Slightly lighter dark for banner */
            padding: 1.5rem 2.5rem;
            border-radius: 8px; /* Soft rounded corners */
            margin-bottom: 2rem;
            display: flex;
            align-items: center;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2); /* Darker shadow */
            width: 100%; /* Ensure it spans */
            max-width: 800px; /* Constrain width like the example */
            margin-left: auto;
            margin-right: auto;
        }
        .top-banner-logo img {
            margin-right: 15px;
            width: 40px; /* Slightly larger icon */
            height: 40px;
        }
        .top-banner-title {
            color: #E2E8F0; /* Light text color */
            font-size: 1.8rem;
            font-weight: 700;
        }

        /* Sidebar - White background as shown in the image */
        section[data-testid="stSidebar"] {
            background-color: #FFFFFF; /* White background */
            border-right: 1px solid #E0E0E0;
            box-shadow: 2px 0 10px rgba(0,0,0,0.1); /* Soft shadow */
            padding-top: 2.5rem; /* More padding at top */
            padding-left: 1.5rem;
            padding-right: 1.5rem;
            border-radius: 0 16px 16px 0; /* Rounded right corners */
        }
        .sidebar-title {
            color: #2D3748; /* Darker text for title on light sidebar */
            font-size: 1rem;
            font-weight: 600;
            margin-bottom: 1.8rem;
            margin-left: 0.5rem;
            letter-spacing: 1px;
            text-transform: uppercase;
        }
        /* Sidebar radio buttons */
        .sidebar-radio .stRadio > div[role="radiogroup"] label {
            display: flex;
            align-items: center;
            font-size: 1.1rem !important;
            padding: 0.7rem 1.2rem;
            border-radius: 10px;
            transition: background 0.2s, color 0.2s;
            margin-bottom: 0.6rem;
            color: #2D3748;
        }
        .sidebar-radio .stRadio > div[role="radiogroup"] label:hover {
            background-color: #F0F4F7;
            color: #2D3748;
        }
        /* Style for the selected radio option - From the image, it looks like just text color changes */
        .stRadio div[role="radiogroup"] label[data-testid="stRadioInline"] > input:checked + div {
            background-color: #E2E8F0; /* Subtle background for selected */
            color: #4299E1 !important; /* Blue from image */
            font-weight: 700; /* Bolder */
        }

        /* Main Content Cards - Light background as per image */
        .main-content-area {
            max-width: 800px;
            margin: 0 auto; /* Center the content */
        }
        .content-card {
            background-color: #FFFFFF; /* White background */
            border-radius: 12px;
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
            padding: 2rem 2.5rem;
            margin-bottom: 2rem; /* Space between cards */
        }
        .content-card h1, .content-card h2, .content-card h3 {
            color: #2D3748; /* Dark text for headings */
            font-weight: 700;
            margin-bottom: 1.5rem;
        }
        .content-card .divider {
            border-top: 1px solid #E2E8F0; /* Lighter divider on white background */
            margin: 2rem 0;
        }

        /* Inputs and Buttons - styled for light background */
        .stTextInput > div > div > input {
            border-radius: 8px;
            border: 1px solid #CBD5E0; /* Light gray border */
            padding: 0.7rem 1.2rem;
            font-size: 1rem;
            color: #2D3748; /* Dark text for input */
            background-color: #F7FAFC; /* Slightly off-white background */
            transition: border-color 0.2s, box-shadow 0.2s;
        }
        .stTextInput > div > div > input:focus {
            border-color: #4299E1; /* Blue on focus */
            box-shadow: 0 0 0 3px rgba(66, 153, 225, 0.3); /* Blue focus ring */
            outline: none;
        }
        .stTextInput label {
            color: #4A5568; /* Darker label text */
            font-weight: 600;
            margin-bottom: 0.5rem;
            display: block;
        }

        .stButton > button {
            background-color: #4299E1; /* Primary blue from image */
            color: white;
            border-radius: 8px;
            padding: 0.7rem 1.8rem;
            border: none;
            font-weight: 600;
            font-size: 1rem;
            margin-top: 1.5rem;
            transition: background-color 0.2s ease, transform 0.1s ease;
            cursor: pointer;
        }
        .stButton > button:hover {
            background-color: #3182CE; /* Darker blue on hover */
            transform: translateY(-1px);
        }
        .stButton > button:active {
            background-color: #2B6CB0;
            transform: translateY(0);
        }

        /* Alert Messages - matching the light theme contrast */
        [data-testid="stAlert"] {
            border-radius: 8px;
            padding: 0.8rem 1.2rem;
            font-size: 0.95rem;
            margin-bottom: 1rem;
            background-color: #EDF2F7; /* Light background for alerts */
            color: #2D3748; /* Dark text for alerts */
        }
        [data-testid="stAlert"] > div {
            padding: 0.5rem 1rem;
        }
        /* Specific alert colors */
        [data-testid="stAlert"] > div[data-baseweb="alert"] > div:first-child { /* Info icon color */
            color: #4299E1 !important;
        }
        .stAlert.st-success {
            background-color: #EBF8FF !important; /* Light blue success */
            border: 1px solid #90CDF4;
            color: #2C5282 !important;
        }
        .stAlert.st-error {
            background-color: #FFF5F5 !important; /* Light red error */
            border: 1px solid #FEB2B2;
            color: #C53030 !important;
        }
        .stAlert.st-warning {
            background-color: #FFFAF0 !important; /* Light yellow warning */
            border: 1px solid #FBD38D;
            color: #B7791F !important;
        }

        /* Contact item display in "All Contacts" */
        .contact-item {
            background-color: #F7FAFC; /* Slightly off-white for individual contacts */
            border-radius: 8px;
            padding: 1.2rem 1.8rem;
            margin-bottom: 1rem;
            border: 1px solid #E2E8F0;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .contact-item strong {
            color: #2D3748; /* Darker name */
        }
        .contact-item span {
            color: #4A5568; /* Phone number color */
        }
        .contact-item small {
            color: #718096; /* Email color */
        }
        .contact-actions {
            margin-left: 1rem;
            display: flex;
            gap: 0.8rem; /* Space between buttons */
        }
        .contact-actions button {
            background-color: #A0AEC0; /* Muted gray for action buttons */
            font-size: 0.9rem;
            padding: 0.5rem 1rem;
            margin-top: 0; /* Remove default margin-top from stButton */
            color: white;
        }
        .contact-actions button:hover {
            background-color: #718096;
        }
        .delete-button { /* Target the delete button specifically */
            background-color: #E53E3E !important; /* Red for delete */
        }
        .delete-button:hover {
            background-color: #C53030 !important;
        }
        /* Style for the horizontal rule between contacts */
        .contact-divider {
            border: 0;
            border-top: 1px dashed #E2E8F0;
            margin: 1.5rem 0;
        }
        /* Style for the "No contacts added yet" message */
        .no-contacts-message {
            background-color: #2D3748; /* Dark background as shown in image */
            color: #E2E8F0; /* Light text */
            padding: 1.5rem;
            border-radius: 8px;
            text-align: center;
            font-size: 1.1rem;
            margin-top: 2rem;
            box-shadow: 0 2px 8px rgba(0,0,0,0.3);
        }
    </style>
''', unsafe_allow_html=True)

# --- Top Banner (Replacing Navbar for this design) ---
# This simulates the "Contact Book" header element in the main content area.
st.markdown(f"""
<div class="top-banner">
    <div class="top-banner-logo">
        <img src="https://img.icons8.com/color/48/000000/open-book--v2.png" width="40">
    </div>
    <span class="top-banner-title">Contact Book</span>
</div>
""", unsafe_allow_html=True)

# --- Main Content Area (Containers for cards) ---
st.markdown('<div class="main-content-area">', unsafe_allow_html=True)

# --- Sidebar Navigation ---
st.sidebar.markdown('<div class="sidebar-title">Menu</div>', unsafe_allow_html=True)

# Sidebar radio buttons
sidebar_options = ["All Contacts", "Add Contact"]
sidebar_icons = ["📇", "➕"]
sidebar_display = [f"{icon} {label}" for icon, label in zip(sidebar_icons, sidebar_options)]
sidebar_selected = st.sidebar.radio(
    label="Navigation",
    options=sidebar_display,
    index=0,
    key="sidebar_radio",
    label_visibility="collapsed",
    help=None,
    disabled=False,
)
sidebar_option = sidebar_options[sidebar_display.index(sidebar_selected)]

# --- Main Content based on sidebar selection ---

if sidebar_option == "All Contacts":
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.header("📇 All Contacts")
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    # Search contacts input field (white background)
    search_query = st.text_input("Search contacts", "", placeholder="Search by name or phone...", key="all_contacts_search")

    display_contacts = st.session_state.contacts

    if search_query:
        display_contacts = [
            contact for contact in st.session_state.contacts
            if search_query.lower() in contact['name'].lower() or \
               search_query.lower() in contact['phone'].lower()
        ]
        if not display_contacts:
            st.info("No contacts found matching your search.")

    if display_contacts:
        for i, contact in enumerate(display_contacts):
            # Using columns for contact details and action buttons
            col_details, col_actions = st.columns([3, 1])

            with col_details:
                st.markdown(f"""
                    <div class="contact-details">
                        <strong>{contact['name']}</strong><br>
                        <span>{contact['phone']}</span><br>
                        <small>{contact['email']}</small>
                    </div>
                """, unsafe_allow_html=True)

            with col_actions:
                # To make buttons appear on the same line, they need to be in the same column
                # or use st.columns again within col_actions if you want them side-by-side.
                # For simplicity here, let's stack them or put them close.
                st.markdown('<div class="contact-actions">', unsafe_allow_html=True)
                edit_button_col, delete_button_col = st.columns(2)
                with edit_button_col:
                    if st.button("Edit", key=f"edit_{i}"): # Unique key for each button
                        st.warning(f"Edit functionality for {contact['name']} not yet implemented.")
                with delete_button_col:
                    if st.button("Delete", key=f"delete_{i}", help="Delete this contact", type="secondary"): # Use type secondary to style it for delete
                        # Implement delete logic here
                        st.session_state.contacts = [c for c in st.session_state.contacts if c['phone'] != contact['phone']]
                        st.success(f"Contact '{contact['name']}' deleted.")
                        st.rerun() # Rerun to update the list immediately
                st.markdown('</div>', unsafe_allow_html=True)

            if i < len(display_contacts) - 1: # Add divider between contacts, but not after the last one
                st.markdown('<div class="contact-divider"></div>', unsafe_allow_html=True)

    else:
        if not search_query: # Only show "No contacts added yet" if no search query and no contacts
            st.markdown('<div class="no-contacts-message">No contacts added yet. Go to "Add Contact" to add new contacts.</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True) # Close content-card

elif sidebar_option == "Add Contact":
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.header("➕ Add a New Contact")
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    with st.form("add_contact_form", clear_on_submit=True):
        name = st.text_input("Name", key="add_name")
        phone = st.text_input("Phone", key="add_phone")
        email = st.text_input("Email (Optional)", key="add_email")

        submitted = st.form_submit_button("Save Contact")

        if submitted:
            add_contact(name, phone, email)
    st.markdown('</div>', unsafe_allow_html=True) # Close content-card

st.markdown('</div>', unsafe_allow_html=True) # Close main-content-area