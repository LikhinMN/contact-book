import streamlit as st
import os
import re
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)

if 'user' not in st.session_state:
    st.session_state.user = None

st.title("📇 Contact Book")

if st.session_state.user is None:
    st.subheader("🔐 Login / Sign Up")

    auth_mode = st.radio("Select option:", ["Login", "Sign Up"])
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if auth_mode == "Login":
        if st.button("Login"):
            try:
                res = supabase.auth.sign_in_with_password({"email": email, "password": password})
                st.session_state.user = res.user
                st.success(f"✅ Logged in as {res.user.email}")
                st.experimental_rerun()
            except Exception as e:
                st.error(f"Login failed: {e}")

    elif auth_mode == "Sign Up":
        if st.button("Sign Up"):
            try:
                if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                    st.warning("⚠️ Please enter a valid email address.")
                else:
                    res = supabase.auth.sign_up({"email": email, "password": password})
                    st.success("✅ Check your email to confirm your account!")
            except Exception as e:
                st.error(f"Sign Up failed: {e}")

else:
    user = st.session_state.user
    st.sidebar.success(f"✅ Logged in: {user.email}")

    if st.sidebar.button("Logout"):
        st.session_state.user = None
        st.experimental_rerun()

    st.sidebar.title("📚 Menu")
    menu = st.sidebar.radio(
        "Choose an action",
        ("➕ Add New Contact", "📋 View & Manage Contacts")
    )

    for field in ["name", "phone", "email_input", "address"]:
        if field not in st.session_state:
            st.session_state[field] = ""

    if menu == "➕ Add New Contact":
        if "clear_form" in st.session_state and st.session_state.clear_form:
            for field in ["name", "phone", "email_input", "address"]:
                st.session_state[field] = ""
            st.session_state.clear_form = False

        with st.form("add_contact"):
            name = st.text_input("Name", key="name")
            phone = st.text_input("Phone", key="phone")
            email_input = st.text_input("Email", key="email_input")
            address = st.text_area("Address", key="address")

            submitted = st.form_submit_button("Add Contact")

            if submitted:
                name = name.strip()
                phone = phone.strip()
                email_input = email_input.strip()
                address = address.strip()

                if not name or not phone:
                    st.warning("⚠️ Name and Phone are required!")
                elif len(name) > 50:
                    st.warning("⚠️ Name too long! Max 50 characters.")
                elif len(phone) > 20:
                    st.warning("⚠️ Phone too long! Max 20 characters.")
                elif not phone.isdigit():
                    st.warning("⚠️ Phone must contain digits only!")
                elif email_input and not re.match(r"[^@]+@[^@]+\.[^@]+", email_input):
                    st.warning("⚠️ Invalid email address!")
                else:
                    existing = supabase.table("contacts").select("*") \
                        .eq("user_id", user.id) \
                        .eq("phone", phone).eq("name", name).execute()

                    if existing.data:
                        st.warning("⚠️ Contact already exists with same name and phone.")
                    else:
                        response = supabase.table("contacts").insert({
                            "name": name,
                            "phone": phone,
                            "email": email_input,
                            "address": address,
                            "user_id": user.id
                        }).execute()

                        if response.data:
                            st.success(f"✅ Contact '{name}' added!")
                            st.session_state.clear_form = True
                            st.experimental_rerun()
                        else:
                            st.error("❌ Failed to add contact. Please check your database.")

    elif menu == "📋 View & Manage Contacts":
        st.subheader("View & Manage Contacts")

        search_query = st.text_input("🔍 Search by name")

        contacts = supabase.table("contacts").select("*") \
            .eq("user_id", user.id).order("name").execute()

        if contacts.data:
            filtered = [
                c for c in contacts.data if search_query.lower() in c["name"].lower()
            ]

            if filtered:
                for contact in filtered:
                    with st.expander(f"{contact['name']}"):
                        st.write(f"📞 **Phone:** {contact['phone']}")
                        st.write(f"📧 **Email:** {contact['email']}")
                        st.write(f"🏠 **Address:** {contact['address']}")

                        with st.form(f"edit_{contact['id']}"):
                            new_name = st.text_input(
                                "Name", value=contact["name"], key=f"name_{contact['id']}"
                            )
                            new_phone = st.text_input(
                                "Phone", value=contact["phone"], key=f"phone_{contact['id']}"
                            )
                            new_email = st.text_input(
                                "Email", value=contact["email"], key=f"email_{contact['id']}"
                            )
                            new_address = st.text_area(
                                "Address", value=contact["address"], key=f"address_{contact['id']}"
                            )

                            col1, col2 = st.columns(2)
                            with col1:
                                update = st.form_submit_button("✏️ Update")
                            with col2:
                                delete = st.form_submit_button("🗑️ Delete")

                            if update:
                                new_name = new_name.strip()
                                new_phone = new_phone.strip()
                                new_email = new_email.strip()
                                new_address = new_address.strip()

                                if not new_name or not new_phone:
                                    st.warning("⚠️ Name and Phone are required!")
                                elif len(new_name) > 50:
                                    st.warning("⚠️ Name too long! Max 50 characters.")
                                elif len(new_phone) > 20:
                                    st.warning("⚠️ Phone too long! Max 20 characters.")
                                elif not new_phone.isdigit():
                                    st.warning("⚠️ Phone must contain digits only!")
                                elif new_email and not re.match(r"[^@]+@[^@]+\.[^@]+", new_email):
                                    st.warning("⚠️ Invalid email address!")
                                else:
                                    supabase.table("contacts").update({
                                        "name": new_name,
                                        "phone": new_phone,
                                        "email": new_email,
                                        "address": new_address
                                    }).eq("id", contact["id"]).eq("user_id", user.id).execute()
                                    st.success(f"✅ Contact '{new_name}' updated!")
                                    st.experimental_rerun()

                            if delete:
                                supabase.table("contacts").delete() \
                                    .eq("id", contact["id"]).eq("user_id", user.id).execute()
                                st.warning(f"🗑️ Contact '{contact['name']}' deleted.")
                                st.experimental_rerun()
            else:
                st.info("No contacts found for that search.")
        else:
            st.info("No contacts found.")
