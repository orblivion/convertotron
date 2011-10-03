import magic


class FileDetect:
    """
    FileDetect will allow us to gather information about the file that we will be trying to convert"
    """

    def __init__(self):
        pass

    def get_mimetype(self, filename):
        m = magic.Magic()
        return m.from_file(filename)

    def get_mimeencoding(self, filename):
        m = magic.Magic(mime_encoding=True)
        return m.from_file(filename)
