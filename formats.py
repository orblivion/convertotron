# "Constants" for file format descriptions, for the purpose of lookup in the table.

# just a namespace. useful to group them together so we can say getattr(Formats, formatname)
class Formats():

    @classmethod
    def get(cls, name):
        return getattr(Formats, name, None)

    WAV = "WAV"
    FLAC = "FLAC"

def mapping(input_format, output_format):
    return basic_cli_mapping[(input_format, output_format)]

basic_cli_mapping = {
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

# Other Mappings:

# Non-basic CLI mappings will include things like situations where we can specify options for
# a set of input formats and options for a set of output formats, where we know the two are
# completely independent

# Library based mappings. Things that don't need a CLI because they're already mapped.
