import pandas as pd
from datetime import datetime
import frontmatter
import os

def parse_timestamp(timestamp_str):
    """Parse timestamp from Google Forms format"""
    try:
        # Try parsing the M/D/YYYY H:M:S format
        return datetime.strptime(timestamp_str, '%m/%d/%Y %H:%M:%S')
    except ValueError:
        try:
            # Fallback for other potential formats
            return pd.to_datetime(timestamp_str).to_pydatetime()
        except:
            # If all else fails, use current date
            print(f"Warning: Could not parse timestamp '{timestamp_str}', using current date")
            return datetime.now()

def clean_yaml_string(s):
    """Clean a string for YAML single-line output"""
    if pd.isna(s):
        return ''
    # Replace newlines and multiple spaces with single space
    s = ' '.join(str(s).split())
    # If string contains special characters, wrap in quotes and escape internal quotes
    if any(char in s for char in '"\':#{}[]|>&*?!%@`'):
        s = f'"{s.replace('"', '\\"')}"'
    return s

def create_markdown(row):
    """Convert a form submission row into a markdown file"""
    # Convert submission date to proper format
    date = parse_timestamp(row['Timestamp']).strftime('%Y-%m-%d')

    # Clean all fields that go into YAML header
    clean_title = clean_yaml_string(row['Package Name'])
    clean_author = clean_yaml_string(row['Your Name'])
    clean_description = clean_yaml_string(row['Short description'])
    clean_categories = [clean_yaml_string(cat.strip()) for cat in str(row['Categories']).split(',')]
    # Convert the value to lowercase
    lowercase_language = row['Language?'].lower()
    # Use the .format() method to add literal curly braces
    formatted_language = "{{{}}}".format(lowercase_language)

    # Create the markdown content with frontmatter
    content = f"""---
title: {clean_title}
date: {date}
author: {clean_author}
categories: [{', '.join(clean_categories)}]
description: {clean_description}
---

## Problem Solved
{row['What is the package or tool useful for?']}

## Example Usage
```{formatted_language}
|# eval: false
{row['Example Code']}
```

## Additional Resources
- Source Code: [{row['Source Code Link']}]({row['Source Code Link']})

## Notes
{row['Additional Notes']}
"""

    # Create filename with .qmd extension
    filename = f"{date}-{row['Package Name'].lower().replace(' ', '-')}.qmd"

    return filename, content

def main():
    # Read the latest submission from CSV
    df = pd.read_csv('04_data/002_form_exports/discoveries_form_export.csv')
    latest = df.iloc[-1]  # Get most recent submission

    # Create the posts directory if it doesn't exist
    os.makedirs('07_dissemination/01_website/003_discoveries', exist_ok=True)

    # Process the submission
    filename, content = create_markdown(latest)

    # Write to file
    with open(f"07_dissemination/01_website/003_discoveries/{filename}", 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    main()
