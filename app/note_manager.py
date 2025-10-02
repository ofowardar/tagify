import json
from pathlib import Path
from .models import Note
from .tagger import TagExtractor
from typing import List

class NoteManager:
    def __init__(self,file_path:str = "notes.json"):
        self.file_path = Path(file_path)
        if not self.file_path.exists():
            self.file_path.write_text("[]",encoding="utf-8")
        self.notes = self.load_notes()

    def load_notes(self) -> List[Note]:
        with open(self.file_path,"r",encoding="utf-8") as file:
            data = json.load(file)
        return [Note(n["content"],n['owner'],n["tags"]) for n in data]
    
    def save_notes(self):
        with open(self.file_path,"w",encoding="utf-8") as file:
            json.dump([n.to_dict() for n in  self.notes],file,indent=4,ensure_ascii=False)

    def create_note(self,content:str,owner:str,tagger:TagExtractor):
        tags = tagger.extract(content)
        note = Note(content=content,owner=owner,tags=tags)
        self.notes.append(note)
        self.save_notes()
        return note
    
    def get_notes_for_user(self,owner:str) -> List[Note]:
        return [n for n in self.notes if n.owner == owner]
    



        