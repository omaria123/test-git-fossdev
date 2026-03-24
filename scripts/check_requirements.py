#!/usr/bin/env python3
import ast
import sys
from pathlib import Path

def extract_imports(file_path):
    imports = set()
    with open(file_path, 'r', encoding='utf-8') as f:
        tree = ast.parse(f.read())
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.add(alias.name.split('.')[0])
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.add(node.module.split('.')[0])
    return imports

def main():
    src_dir = Path("src")
    req_file = Path("requirements.txt")
    
    # собираем все имплрты
    all_imports = set()
    for py_file in src_dir.glob("*.py"):
        all_imports.update(extract_imports(py_file))
    
    # читаем requirements.txt
    with open(req_file, 'r') as f:
        requirements = set()
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                pkg_name = line.split('==')[0].split('>=')[0].split('<=')[0].strip()
                requirements.add(pkg_name)
    
    # стандартные библиотеки Python
    stdlib = {'sys', 'os', 're', 'json', 'pathlib', 'typing', 'ast'}
    
    # проверяем
    missing = []
    for imp in all_imports:
        if imp in stdlib:
            continue
        if imp not in requirements:
            missing.append(imp)
    
    if missing:
        print("Missing dependencies:")
        for m in missing:
            print(f"  - {m}")
        sys.exit(1)
    else:
        print("All imports match requirements.txt")
        sys.exit(0)

if __name__ == "__main__":
    main()