import re
import xml.etree.cElementTree as et


def strip_markdown(text):
    # Remove headers
    text = re.sub(r'(?m)^#{1,6}\s*', '', text)
    # Remove emphasis (bold, italic)
    text = re.sub(r'(\*\*|__)(.*?)\1', r'\2', text)
    text = re.sub(r'(\*|_)(.*?)\1', r'\2', text)
    # Remove inline code
    text = re.sub(r'`([^`]+)`', r'\1', text)
    # Remove links and images
    text = re.sub(r'!\[.*?\]\(.*?\)', '', text)  # remove images
    text = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', text)  # keep link text
    # Remove blockquotes
    text = re.sub(r'(?m)^>\s?', '', text)
    # Remove horizontal rules
    text = re.sub(r'(?m)^-{3,}$', '', text)
    # Remove unordered and ordered list markers
    text = re.sub(r'(?m)^(\s*[-+*]|\s*\d+\.)\s+', '', text)
    # Remove remaining backticks
    text = text.replace('`', '')
    return text.strip()


