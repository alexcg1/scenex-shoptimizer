import os

import streamlit as st
from rich.console import Console
from helper import get_settings

console = Console(tab_size=2)

settings = get_settings()

# scenex
SCENEX_API_KEY = os.environ.get("SCENEX_API_KEY", "")

# woocommerce
WOOCOMMERCE_URL = os.environ.get("WOOCOMMERCE_URL", "")
WOOCOMMERCE_KEY = os.environ.get("WOOCOMMERCE_KEY", "")
WOOCOMMERCE_SECRET = os.environ.get("WOOCOMMERCE_SECRET", "")

# shopify
SHOPIFY_SHOP_NAME = os.environ.get("SHOPIFY_SHOP_NAME", "")
SHOPIFY_ACCESS_TOKEN = os.environ.get("SHOPIFY_ACCESS_TOKEN", "")

st.set_page_config(page_title="Shoptimizer", layout="wide")

st.title("Configure Shoptimizer")
st.markdown(
    "API keys, URLs, and more. For optimization settings, check the 'Optimize Products' page."
)

PLATFORMS = ["WooCommerce", "Shopify"]

st.markdown("#### SceneXplain")

scenex_api_key = st.text_input(
    label="SceneXplain API key",
    type="password",
    value=settings["scenex_api_key"],
    help="Get on SceneXplain's [API page](https://scenex.jina.ai)",
)


st.markdown("#### Your shop")

platform = st.selectbox(label="Platform", options=PLATFORMS)
platform_settings = st.container(border=True)

if platform == "WooCommerce":
    woocommerce_url = platform_settings.text_input(
        label="WooCommerce URL", value=settings["woocommerce_url"]
    )
    woocommerce_consumer_key = platform_settings.text_input(
        label="WooCommerce consumer key", value=settings["woocommerce_key"]
    )
    woocommerce_consumer_secret = platform_settings.text_input(
        label="WooCommerce consumer secret",
        type="password",
        value=settings["woocommerce_secret"],
    )

elif platform == "Shopify":
    shopify_shop_name = platform_settings.text_input(
        label="Shopify shop name", value=settings["shopify_shop_name"]
    )
    shopify_access_token = platform_settings.text_input(
        label="Shopify access token",
        type="password",
        value=settings["shopify_access_token"],
    )


with st.expander("Advanced"):
    scenex_url = st.text_input(label="SceneXplain URL", value=settings["scenex_url"])
    shoptimizer_backend_url = st.text_input(
        label="Shoptimizer backend URL", value=settings["shoptimizer_backend_url"]
    )

save_button = st.button("Save")
if save_button:
    # st.session_state["scenex_api_key"] = scenex_api_key
    os.environ["SCENEX_API_KEY"] = scenex_api_key
    os.environ["SCENEX_URL"] = scenex_url
    if platform == "WooCommerce":
        os.environ["WOOCOMMERCE_URL"] = woocommerce_url
        os.environ["WOOCOMMERCE_KEY"] = woocommerce_consumer_key
        os.environ["WOOCOMMERCE_SECRET"] = woocommerce_consumer_secret

    # shopify
    elif platform == "Shopify":
        os.environ["SHOPIFY_SHOP_NAME"] = shopify_shop_name
        os.environ["SHOPIFY_ACCESS_TOKEN"] = shopify_access_token

    os.environ["SHOPTIMIZER_BACKEND_URL"] = shoptimizer_backend_url

    st.toast("Settings saved!", icon="💾")
