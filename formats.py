# "Constants" for file format descriptions, for the purpose of lookup in the table.

# just a namespace. useful to group them together so we can say getattr(Formats, formatname)
class Formats():

    @classmethod
    def get(cls, name):
        return getattr(Formats, name, None)

    WAV = "WAV"
    FLAC = "FLAC"

mapping = {
    (Formats.FLAC, Formats.WAV):
    [
        {
         "program":"flac",
         "arguments": ["%(in_file)s", '-o', "%(out_file)s"],
         "sanity": 0.9 ,# how likely does the user mean this sort of conversion
         "quality": 0.9, # the general quality of the conversion
         "details": "Converts a flac file to an mp3 file."
        },
    ]
}
