import streamlit as st
import instaloader

# Streamlit UI
st.set_page_config(page_title="Instagram Reel Caption Extractor", layout="centered")

st.title("📸 Instagram Reel Caption Extractor")
st.write("Enter the Instagram Reel URL to extract its caption.")

# Input URL
post_url = st.text_input("🔗 Paste Instagram Reel URL here:")

# Function to extract caption
def get_instagram_caption(url):
    loader = instaloader.Instaloader()

    try:
        shortcode = url.split("/")[-2]  # Extract shortcode
        post = instaloader.Post.from_shortcode(loader.context, shortcode)
        return post.caption
    except Exception as e:
        return f"⚠️ Error!!!!!\n\nError Details: {e}"

# Button to fetch caption
if st.button("📥 Extract Caption"):
    if post_url:
        caption = get_instagram_caption(post_url)
        st.subheader("📝 Extracted Caption:")
        st.success(caption if caption else "No caption found!")
    else:
        st.warning("⚠️ Please enter a valid Instagram Reel URL.")
