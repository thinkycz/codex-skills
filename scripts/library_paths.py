"""Stable inventories and local-reference resolution shared by library tools."""
import re

CACHES = {'.git', '__pycache__', '.pytest_cache', '.DS_Store', 'node_modules', '.venv'}

def source_files(directory):
    return sorted(p for p in directory.rglob('*') if p.is_file()
                  and not any(part in CACHES for part in p.relative_to(directory).parts)
                  and p.suffix not in {'.pyc', '.pyo'})

def local_links(text):
    links = re.findall(r'\[[^\]]*\]\(([^)]+)\)', text)
    links += re.findall(r'`((?:\.\.?/|references/|scripts/|assets/|agents/|templates/)[^`\s]+)`', text)
    for link in links:
        link = link.strip('<>').split('#', 1)[0]
        if link and not re.match(r'[a-zA-Z][\w+.-]*:', link):
            yield link

def resolve_link(path, link, package):
    link = link.strip('<>').split('#', 1)[0]
    if path.suffix in {'.yaml', '.yml'} and link.startswith('./assets/'):
        return (package / link).resolve()
    base = package if link.startswith(('references/', 'scripts/', 'assets/', 'agents/', 'templates/')) else path.parent
    return (base / link).resolve()
