# Base URL for Apple Arcade
site = "https://www.apple.com/apple-arcade/"

# XPath of the FAQ section header
faq_header = "//h2[contains(text(),'Questions? Answers.')]"

# Tag name for sending keyboard navigation from the body
body_tag = "body"

# Generates XPath for a FAQ toggle button by its aria-controls attribute
def faq_button_by_aria(aria_controls):
    return f"//button[@aria-controls='{aria_controls}']"

# Expected attribute value after expansion
expected_expanded_value = "true"
