__author__ = 'Nico'

## FOR DEBUGGING
#import pdb
#pdb.set_trace()

import btk
import Tkinter, tkFileDialog
import os
import argparse

def convert_and_write(from_c3d_filename, to_c3d_filename):


    # Makes reader from filename
    reader = btk.btkAcquisitionFileReader()
    reader.SetFilename(from_c3d_filename)
    reader.Update()
    acq=reader.GetOutput()
    points=acq.GetPoints()
    n_points=points.GetItemNumber()

    print '\n \n Updating values in c3d object'
    n=0
    for f in xrange(acq.GetPointFrameNumber()):
        for i in xrange(n_points):
            point=acq.GetPoint(i)
            data=point.GetValues()[f,:]
            point.SetDataSlice(f, *[1000*x for x in data])
        if not f%5000:
            n=n+1
            print '\n So far updated {} frames'.format(n*5000)

    writer = btk.btkAcquisitionFileWriter()
    writer.SetInput(acq)
    writer.SetFilename(to_c3d_filename)
    writer.Update()
    print '\n Converted c3d file from: \n {}'.format(from_c3d_filename)
    print '\n Wrote converted c3d file to: \n {}'.format(to_c3d_filename)


def gui_load_c3d_filenames():
        root = Tkinter.Tk()
        root.withdraw()
        c3d_filenames_u=tkFileDialog.askopenfilename(title='Choose a c3d file to convert: ',
                                                    filetypes=[('motive c3d tracking files', '*.c3d')],
                                                    multiple=True)
        c3d_filenames=[f.encode('ascii') for f in c3d_filenames_u]
        root.quit()
        return c3d_filenames


def gui_save_c3d_directory():
        root = Tkinter.Tk()
        root.withdraw()
        save_dir = (tkFileDialog.askdirectory(title='Choose a directory to save to: ')).encode('ascii')
        root.quit()
        return save_dir


if __name__ == '__main__':

    # Parse Command-Line Arguments
    parser = argparse.ArgumentParser(description="This script converts a c3d file as exported by motive to a vicon readable c3d file.",
                                 epilog="If no arguments are given, the script first opens a window to let you choose a c3d file or a directory of c3d files to convert. \n")

    parser.add_argument('-i', action='store', dest='c3d_file', default='',
                        help='name of the c3d file to convert or name of the folder which contains c3d files to convert')

    parser.add_argument('-R', action='store_true', dest='c3d_folder', default=False, help='when this flag is set files are taken from a c3d_folder')

    parser.add_argument('-o', action='store', dest='write_c3d_folder', default='',
                        help='folder where converted c3d files will be written to')

    parser.add_argument('--append', action='store', dest='save_filename_append', default='_vicon',
                       help='string to append to new files')

    args = parser.parse_args()


    # Get Filenames
    if args.c3d_file:
        if os.path.isdir(args.c3d_file):
            assert args.c3d_folder, "When -R flag is not set, files are taken from a c3d_file NOT c3d_folder!"
            filenames=[]
            for c3d_file in os.listdir(args.c3d_file):
                if c3d_file.endswith(".c3d"):
                    filenames.append(os.path.join(args.c3d_file,c3d_file))

        else:
            assert not args.c3d_folder, "When -R flag is set, files are taken from a c3d_folder NOT c3d_file!"
            filenames=[args.c3d_file]

    else:
        filenames = gui_load_c3d_filenames()


    # Get Destination Directory (Save Directory)
    if args.write_c3d_folder:
        if not os.path.exists(args.write_c3d_folder):
            os.makedirs(args.write_c3d_folder)
        save_dir = args.write_c3d_folder
    else:
        save_dir = gui_save_c3d_directory()

    # Convert and Write to Each File
    for name in filenames:
        load_dir, base_name = os.path.split(name)
        base, ext = os.path.splitext(base_name)
        save_filename=os.path.join(save_dir, base+args.save_filename_append+ext)
        convert_and_write(name,save_filename)



