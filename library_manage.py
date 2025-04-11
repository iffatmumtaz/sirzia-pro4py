import streamlit as st
import pandas as pd

st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
        padding: 20px;
        border-radius: 10px;
    }
    .title {
        color: #4a4a4a;
        font-size: 36px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)




# Initialize session state for books
if "books" not in st.session_state:
    st.session_state.books = []

# App Title
st.title("📚 Library Management System By Iffat Mumtaz")

# Navigation
menu = ["Add Book", "View Books", "Search Book", "Delete Book"]
choice = st.sidebar.selectbox("Menu", menu)

# Add Book
if choice == "📕 Add Book":
    st.subheader("Add New Book")
    book_name = st.text_input("Book Name")
    author = st.text_input("Author")
    year = st.number_input("Published Year", min_value=1000, max_value=2100, step=1)

    if st.button("Add Book"):
        st.session_state.books.append({"Book": book_name, "Author": author, "Year": year})
        st.success(f"'{book_name}' added to library!")

# View Books
elif choice == "View Books":
    st.subheader("All Books")
    if st.session_state.books:
        df = pd.DataFrame(st.session_state.books)
        st.dataframe(df)
    else:
        st.info("No books available yet.")

# Search Book
elif choice == "Search Book":
    st.subheader("Search Book")
    search_term = st.text_input("Enter book name or author")
    if st.button("Search"):
        results = [book for book in st.session_state.books if search_term.lower() in book["Book"].lower() or search_term.lower() in book["Author"].lower()]
        if results:
            st.write(pd.DataFrame(results))
        else:
            st.warning("No matching books found.")

# Delete Book
elif choice == "Delete Book":
    st.subheader("Delete Book")
    if st.session_state.books:
        book_titles = [book["Book"] for book in st.session_state.books]
        book_to_delete = st.selectbox("Select book to delete", book_titles)
        if st.button("Delete"):
            st.session_state.books = [book for book in st.session_state.books if book["Book"] != book_to_delete]
            st.success(f"'{book_to_delete}' has been deleted.")
    else:
        st.info("No books to delete.")
