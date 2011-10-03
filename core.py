from formats import Formats, mapping
import subprocess, sys
from file_detect import FileDetect

def find_best_method(output_options):
    return output_options[0]

def convert(fname, output_fname, output_format = None, output_location = None, settings = None):

    #if output_location:       # "I want to play this on my iPod!" (cue from Miro)
    #    output_formats = get_format(output_location, settings) # aac, etc
    #else
    #    output_formats = [output_format]

    detector = FileDetect(fname)
    input_format = detector.detect()
    if not input_format:
        # actually these should return error codes or something, this is a core function.
        sys.stderr.write( "Input file format not detected.\n" )
    if not output_format:
        sys.stderr.write( "No (valid) output file formats specified.\n" )
    else:

        #output_options = []
        #for of in output_formats:
        #    output_options.append(get_outputs(input_format, of, options))


        conversion_methods = mapping(input_format, output_format)
        #map (check_installed,   output_options)

        best_method = find_best_method (conversion_methods)
        arguments = [arg % {"in_file": fname, "out_file": output_fname } for arg in best_method["arguments"] ]

        # Run it
        subprocess.call([best_method['program']] + arguments) 
