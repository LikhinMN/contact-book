# 📇 Contact Book

A simple web-based contact book built with Streamlit and Supabase. This app allows you to securely add, view, edit, and delete your personal contacts from anywhere.

## Features

- 🔐 User authentication (sign up, login, logout)
- ➕ Add new contacts (name, phone, email, address)
- 📋 View, search, update, and delete contacts
- ☁️ Data stored securely in Supabase
- 🖥️ Easy-to-use Streamlit interface

## Demo

Try it live: [https://contactbook.streamlit.app/](https://contactbook.streamlit.app/)

## Getting Started

### Prerequisites

- Python 3.8+
- A [Supabase](https://supabase.com/) project (for database and authentication)

### Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/contact-book.git
    cd contact-book
    ```

2. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Set up environment variables:**
    - Create a `.env` file in the project root:
      ```
      SUPABASE_URL=your_supabase_url
      SUPABASE_KEY=your_supabase_anon_key
      ```

4. **Run the app locally:**
    ```sh
    streamlit run [app.py](http://_vscodecontentref_/0)
    ```

### Deployment

You can deploy this app for free on [Streamlit Cloud](https://streamlit.io/cloud) or any cloud platform that supports Python.

## File Structure

- `app.py` — Main Streamlit app
- `requirements.txt` — Python dependencies
- `.env` — Environment variables (not committed)
- `README.md` — Project documentation

## License

MIT License

---

**Made with ❤️ using