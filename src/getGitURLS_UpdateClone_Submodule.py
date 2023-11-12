
import os
import re
import tkinter as tk
from tkinter import filedialog


def get_git_urls(directory):
    """
    Returns a list of git URLs found in the given directory.
    """
    urls = []
    for root, dirs, files in os.walk(directory):
        for name in files:
            if name == '.git':
                path = os.path.join(root, name)
                with open(path, 'r') as f:
                    config = f.read()
                    match = re.search(r'url\s*=\s*(.*)', config)
                    if match:
                        urls.append(match.group(1))
    return urls


def get_git_commands(urls, choice):
    """
    Returns a list of git clone or git submodule add commands for the given list of git URLs.
    """
    commands = []
    for url in urls:
        if choice == 'clone':
            commands.append(f'git clone {url}')
        elif choice == 'submodule':
            commands.append(f'git submodule add {url}')
    return commands


def get_directory():
    """
    Opens a file dialog to select a directory and returns the selected directory path.
    """
    root = tk.Tk()
    root.withdraw()
    directory = filedialog.askdirectory()
    return directory


def save_file(repo_list):
    """Save the repo list to a custom file name"""
    filename = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('Text files', '*.csv')])
    for repo in repo_list:
        with open(filename, 'a') as f:
            f.write(repo + '\n')
            print(repo)
    print('Saved to file:', filename)


def main():
    """
    Main function that calls the above functions and prints the list of git clone or git submodule add commands.
    """
    directory = get_directory()
    if not directory:
        print('No directory selected.')
        return
    choice = input('Enter "clone" or "submodule": ')
    urls = get_git_urls(directory)
    commands = get_git_commands(urls, choice)
    for command in commands:
        print(command)
    save_file(commands)


if __name__ == '__main__':
    main()
