# Shoptimizer

Shoptimizer is a tool that helps you improve the SEO and accessibility of our WooCommerce or Shopify store. It does this by:

- Generating vivid product descriptions based on product images
- Generating descriptive alt texts for each product image

This helps you get a higher Google listing and comply with American and European accessibility laws.

## How does it work?

Shoptimizer:

- Pulls a list of products from your store's API.
- Uploads the product images to Jina AI's [SceneXplain](https://scenex.jina.ai) to generate text strings associated with the images (e.g. short description, long description, image alt text).
- Passes that text back to your API to update the product listings in your store.

Shoptimizer uploads product images to Jina AI's [SceneXplain](https://scenex.jina.ai), along with some task-based prompts which explain what we want from the image (e.g. short description, long description, alt text). I

## Interactive demo

Use it [here](http://ec2-13-51-173-24.eu-north-1.compute.amazonaws.com:8501/)

**Note:** We suggest using the demo on a dummy store. The software is still under development and we're not using a secure connection at present.

## Getting credentials

On Shoptizer's configuration page you will need to enter:

- A [SceneXplain](https://scenex.jina.ai) account and  [API key](https://scenex.jina.ai).
- Your WooCommerce URL, [consumer key and consumer secret](https://woo.com/document/woocommerce-rest-api/#section-2).

## Run it on your machine

1. Clone this repo.
2. Edit `docker-compose.yml` to fill in your credentials.
3. In the repo's base directory, run `docker-compose up` to build and run the Docker images.
4. Access http://localhost:8501 in your web browser
