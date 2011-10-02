# "Constants" for file format descriptions, for the purpose of lookup in the table.

WAV = "WAV"
FLAC = "FLAC"

mapping = {
    (FLAC, WAV):
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
