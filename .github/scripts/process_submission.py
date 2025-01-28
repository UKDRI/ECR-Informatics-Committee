import pandas as pd
import frontmatter
from datetime import datetime
from dateutil import parser
import os

def create_markdown(row):
    """Convert a form submission row into a markdown file"""
    # Convert submission date to proper format
    date = parser.parse(row['Timestamp']).strftime('%Y-%m-%d')
    
    # Create the frontmatter content
    metadata = {
        'title': row['Package Name'],
        'date': date,
        'author': row['Your Name'],
        'categories': [cat.strip() for cat in row['Categories'].split(',')],
        'description': row['Short description']
    }
    
    # Create the markdown content
    content = f"""
## Problem Solved
{row['What is the package or tool useful for?']}

## Example Usage
```{row['Language?']}
{row['Example Code']}
```

## Additional Resources
- Source Code: {row['Source Code Link']}

## Notes
{row['Additional Notes']}
"""
    
    # Combine into a proper markdown file with frontmatter
    post = frontmatter.Post(content, **metadata)
    
    # Create filename from date and package name
    filename = f"{date}-{row['Package Name'].lower().replace(' ', '-')}.qmd"
    
    return filename, post

def main():
    # Read the latest submission from CSV
    df = pd.read_csv('04_data/002_form_exports/discoveries_form_export.csv')
    latest = df.iloc[-1]  # Get most recent submission
    
    # Create the posts directory if it doesn't exist
    os.makedirs('07_dissemination/01_website/003_discoveries', exist_ok=True)
    
    # Process the submission
    filename, post = create_markdown(latest)
    
    # Write to file
    with open(f"07_dissemination/01_website/003_discoveries/{filename}", 'wb') as f:
        frontmatter.dump(post, f)

if __name__ == "__main__":
    main()
