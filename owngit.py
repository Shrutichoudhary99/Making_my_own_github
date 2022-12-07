import os
import cryptography
import fileinput
# initiale our git repo
def init(repo):
    # this function is to initiale a git repository
    os.mkdir(repo)
    os.mkdir(os.path.join(repo, '.fit'))
    for name in ["objects", "ref"]:
        os.mkdir(os.path.join(repo, '.fit', name))
    
    print(f"initialized empty git repo {repo}")

def add(repo):
    data = read_files(os.path.join('.'))

    return add

def HashObjects(data, onj_type, write=True):
    header = f"{onj_type} {len(data).encode()}"


def commit():
    commit_entries = []
    for entry in read_index():
        assert '/' not in entry.path, \
            "Does not include in the git directory"
        mode_path = f'{entry.mode} {entry.path.encode()} '
    
    commit_entries = mode_path + entry.sha1

    commit_entries.append(commit_entries)

    return commit()

init('fit')