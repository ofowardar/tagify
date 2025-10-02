from typing import List

class Note:
    """
    Notes Class
    """
    _id_counter = 1
    def __init__(self,content:str,owner:str,tags: List[str]):
        self.id = Note._id_counter
        Note._id_counter += 1
        self.content = content
        self.tags = tags
        self.owner = owner

    def add_tag(self,tag:str):
        if tag not in self.tags:
            self.tags.append(tag)


    def to_dict(self):
        """

        Convert to dict for API response.

        """

        return {
            "id":self.id,
            "content":self.content,
            "owner": self.owner,
            "tags":self.tags
        }
    


class User:

    """
    User Class 
    """
    def __init__(self,username:str,password_hash:str):
        self.username = username
        self.password_hash = password_hash
        
    
    def to_dict(self):
        """
        Convert to dict for JSON registers 
        """
        return {
            "username": self.username,
            "password_hash": self.password_hash
        }
