import re

# Load the original XML file
file_path = './SG.xml'
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# Escape problematic characters in the XML
# For instance, replace '&' with '&amp;' if it’s not part of a valid XML entity
content = re.sub(r'&(?!amp;|lt;|gt;|quot;|apos;)', '&amp;', content)

# Save the sanitized content back to the XML file for parsing
sanitized_file_path = './SG.xml'
with open(sanitized_file_path, 'w', encoding='utf-8') as file:
    file.write(content)
