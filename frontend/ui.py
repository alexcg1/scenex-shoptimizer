import streamlit as st
from rich.console import Console

console = Console(tab_size=2)

help_markdown = """
Alt Texter automatically adds alt tags to all the images (including featured images) on your blog using [SceneXplain](https://scenex.jina.ai).

### How does it work?

Alt Texter will:

- Download each content item from whatever platform you're using
- Check each image to see if it has alt text:
    - If yes, skip that image
    - If no, create an alt text using SceneXplain and write that to the content data
- Check if the content has new alt texts:
    - If yes, update the content
    - If no, skip update
"""

st.set_page_config(page_title="Shoptimizer", layout="wide")
st.warning(
    "Shoptimizer is still under heavy development. Back up your data before using it!"
)

st.title("Shoptimizer")

st.markdown(
    "##### Use AI to write compelling SEO-friendly product descriptions and optimize your SEO by generating alt texts for your images"
)

st.markdown(
    "### Get started\n\nTo get started you'll need to fill in your SceneXplain and store credentials on the [configuration page](./Configuration)"
)

st.page_link(page="./pages/Configuration.py", label=":gear: Configure Shoptimize")

st.markdown(
    "Then you can [view your products and their alt texts and descriptions](./Products) (which count towards SEO), or [optimize your products](./Optimize_products) using SceneXplain"
)

col1, col2, col3 = st.columns([1, 1, 6])

with col1:
    st.page_link(label=":shirt: View products", page="./pages/1_Products.py")
with col2:
    st.page_link(
        label=":rocket: Optimize products", page="./pages/2_Optimize products.py"
    )
