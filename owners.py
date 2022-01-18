def group_by_owners(files):
    
    result = {}
    for file,owner in files.items():
        result[owner] = result.get(owner, [] + [file])
    return result

if __name__ == "__main__":
    files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }
    print(group_by_owners(files))