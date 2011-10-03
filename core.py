import formats
import subprocess

def identify(fname):
    return formats.FLAC

def find_best_method(output_options):
    return output_options[0]

def convert(fname, output_fname, output_formats = None, output_location = None, settings = None):

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


    conversion_methods = formats.mapping[(input_format, formats.WAV)]
#    map (check_installed,   output_options)

    best_method = find_best_method (conversion_methods)
    arguments = [arg % {"in_file": fname, "out_file": output_fname } for arg in best_method["arguments"] ]

    # Run it
    subprocess.call([best_method['program']] + arguments) 
