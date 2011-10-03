import magic
from formats import Formats


class FileDetect:
    """
    FileDetect will allow us to gather information about the file that we will be trying to convert"
    """

    def __init__(self, filename):
        self.filename = filename

    def get_mimetype(self):
        m = magic.Magic()
        return m.from_file(self.filename)

    def get_mimeencoding(self):
        m = magic.Magic(mime_encoding=True)
        return m.from_file(self.filename)




    # I don't know how you prefer to do this, feel free to make it however you want
    # but in the end there this module should have a function that takes in the file somehow and outputs
    # a format from our list
    def detect(self):
        if self.get_mimetype().startswith("FLAC "):
            return Formats.FLAC
