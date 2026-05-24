# SEO Keyword Optimizer for Digital Products
def generate_seo_tags(product_name, keywords):
    """
    Cleans and formats keywords into SEO-ready tags.
    """
    clean_tags = [tag.strip().lower() for tag in keywords.split(',')]
    formatted_tags = " | ".join(clean_tags)
    return f"SEO Tags for {product_name}: {formatted_tags}"

# Example Usage:
product = "Canva Planner Template"
raw_keywords = "Digital, PLANNERS, Canva Design, Organization, minimalist"

print(generate_seo_tags(product, raw_keywords))
