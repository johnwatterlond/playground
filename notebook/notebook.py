import datetime

#Counter to apply unique ids.
last_id = 0

class Note:
    """
    Represent a note in the notebook.

    Match against a string in searches.
    Store `tags` for each note.
    """
    def __init__(self, memo, tags=''):
        """
        Initialize a note with memo and optional space-separated `tags`.

        Automatically set the note's `creation_date` and (unique) `id`.
        """
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()

        global last_id
        last_id = last_id + 1
        self.id = last_id

    def contains(self, string):
        """
        Determine if note contains string in the text or tags.

        Search is case sensitive.
        """
        return string in self.memo or string in self.tags


class Notebook:
    """
    Represent a collection of notes.

    Notes can be tagged, modified, and searched.
    """
    def __init__(self):
        """Initialize a notebook with an empty list of notes."""
        self.notes = []

    def create_note(self, memo, tags=''):
        """Create a new note and add it to the list of notes."""
        self.notes.append(Note(memo, tags))

    def modify_memo(self, note_id, new_memo):
        """
        Change memo of note with id note_id to new_memo.
        """
        for note in self.notes:
            if note.id == note_id:
                note.memo = new_memo
                break

    def modify_tags(self, note_id, new_tags):
        """
        Change tags of note with id note_id to new_tags.
        """
        for note in self.notes:
            if note.id == note_id:
                note.tags = new_tags
                break

    def search(self, string):
        """
        Return a list of all notes that contain the given string.
        """
        return [note for note in self.notes if note.contains(string)]
