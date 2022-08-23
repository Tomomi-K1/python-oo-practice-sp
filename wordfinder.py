"""Word Finder: finds random words from a dictionary."""

from random import choice

class WordFinder:
    """
    create object from contents in other file

    Attribute
    file_path: file path to file that contains content

    >>> a = WordFinder('words.txt')
    >>> a.random() in a.file_content_list
    True


    """
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_content = open (file_path)
        self.file_content_list = self.file_into_list() 

    def __repr__(self):
        return f"{len(self.file_content_list)} words read"

    def random(self):
        """ choose random word from list of content 
        
        """
        return choice(self.file_content_list)



    def file_into_list(self):
        """ create a list contains each line item as an element """
        return [line.strip() for line in self.file_content]
        self.file_content.close()


class SpecialWordFinder(WordFinder):
    """
    create object from contents in other file but ignores comments start with "#" and blank line.

    Attribute
    file_path: file path to file that contains content

    >>> a = SpecialWordFinder('words2.txt')
    >>> a.random() in a.file_content_list
    True

    >>> a.random() is not ""
    True
    """


    def __init__(self, file_path):
        super().__init__(file_path)


    def file_into_list(self):
        """return the list of each line content except the blank line and line starts with '#' """
        return [line.strip() for line in self.file_content if (not line.startswith('#')) and (line.strip() !='')]
        self.file_content.close()

