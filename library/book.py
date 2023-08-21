import re


class Book:
    def __init__(self, title: str, author: str, length: int):
        self.title = title
        self.author = author
        self. length = length
        
    def get_title(self) -> str:
        return self.title
    
    def get_author(self) -> str:
        return self.author
    