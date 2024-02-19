import os


def get_settings():
    settings = {
        "shoptimizer_backend_url": os.environ.get("SHOPTIMIZER_BACKEND_URL", ""),
        "scenex_api_key": os.environ.get("SCENEX_API_KEY", ""),
        "woocommerce_url": os.environ.get("WOOCOMMERCE_URL", ""),
        "woocommerce_key": os.environ.get("WOOCOMMERCE_KEY", ""),
        "woocommerce_secret": os.environ.get("WOOCOMMERCE_SECRET", ""),
        "shopify_shop_name": os.environ.get("SHOPIFY_SHOP_NAME", ""),
        "shopify_access_token": os.environ.get("SHOPIFY_ACCESS_TOKEN", ""),
    }

    return settings
