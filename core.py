import formats
import subprocess

def identify(fname):
    return formats.FLAC

def interaction(fname, output_fname, output_formats = None, output_location = None, settings = None):

#    if output_location:       # "I want to play this on my iPod!" (cue from Miro)
#        output_formats = get_format(output_location, settings) # aac, etc

#    # file first, then      imagemagick, gstreamer(?), ffmpeg/libavcodec
    input_format = identify(fname)


#    # research gstreamer    sources and sinks
#    output_options   ::         [ (Program, Switches/Arguments, Warnings/Features Lost, Sanity Index, Description) ]
#    # Description ex:        "This extracts your subtitles"
#    output_options = []
#    for of in output_formats:
#        output_options.append(get_outputs(input_format, of, options))
#
#    # considerations for what's installed, what the user cares to install
#    map (check_installed,   output_options)
#    best = find_best (output_options)


    conversion_method = formats.mapping[(input_format, formats.WAV)][0]
    arguments = [arg % {"in_file": fname, "out_file": output_fname } for arg in conversion_method["arguments"] ]
    subprocess.call([conversion_method['program']] + arguments) 
