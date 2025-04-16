import markdown
import os
from pathlib import Path

def convert_markdown_to_html(markdown_file):
    # Read the markdown file
    with open(markdown_file, 'r', encoding='utf-8') as f:
        markdown_content = f.read()
    
    # Create markdown instance with extensions
    md = markdown.Markdown(extensions=['tables', 'fenced_code', 'nl2br'])
    
    # Convert markdown to HTML
    html_content = md.convert(markdown_content)
    
    # Process image paths
    html_content = process_image_paths(html_content)
    
    # Create complete HTML document
    html_document = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Converted Markdown</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <main>
        {html_content}
    </main>
</body>
</html>"""
    
    # Write the HTML file
    with open('converted.html', 'w', encoding='utf-8') as f:
        f.write(html_document)

def process_image_paths(html_content):
    # Replace relative image paths with img folder path
    import re
    pattern = r'<img src="([^"]+)"'
    
    def replace_path(match):
        path = match.group(1)
        # If path doesn't start with 'img/', add it
        if not path.startswith('img/'):
            path = os.path.join('img', os.path.basename(path))
        return f'<img src="{path}"'
    
    return re.sub(pattern, replace_path, html_content)

if __name__ == '__main__':
    # Get the markdown file from command line argument or use a default
    import sys
    markdown_file = sys.argv[1] if len(sys.argv) > 1 else 'blog/casca.md'
    
    if not os.path.exists(markdown_file):
        print(f"Error: File '{markdown_file}' not found.")
        sys.exit(1)
    
    convert_markdown_to_html(markdown_file)
    print(f"Conversion complete! Check 'converted.html' for the result.")