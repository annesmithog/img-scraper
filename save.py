import os

def make_folder(folder: str) -> None:
    """フォルダを作成する"""
    if not os.path.exists(folder):
        os.makedirs(folder)