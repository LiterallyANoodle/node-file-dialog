import tkinter as tk
import tkinter.filedialog
import argparse
import sys
root = tk.Tk()
# Hide it with .withdraw
root.withdraw()
     
parser=argparse.ArgumentParser(
        description="Opens File selection dialog boxes")
parser.add_argument('-d',help="directory open prompt",action='store_true')
parser.add_argument('-o',help='file open prompt',action='store_true')
parser.add_argument('-s',help='file save prompt',action='store_true')
parser.add_argument('-f',help='multiple files open prompt',action='store_true')
parser.add_argument('-t',help='list of filetypes to search for. format as ordered strings: Label1 Extension1 Label2 Extension2 ...',nargs='+')
args=parser.parse_args()

# error if filetypes strings are not paired
if (len(args.t) % 2):
    sys.stderr.write("\nError: Filetype parameters not paired.\n")
    parser.print_help(sys.stderr)
    sys.exit(1)
if len(sys.argv)==1:
    parser.print_help(sys.stderr)
    sys.exit(1)

filetypes = [ (args.t[x*2], args.t[x*2+1]) for x in range(len(args.t) // 2) ]

if args.s:
    temp=tkinter.filedialog.asksaveasfilename(filetypes=filetypes)
    if(len(temp)==0):
        print("None")
    else:
        print(temp)
if args.o:
    temp=(tkinter.filedialog.askopenfilename(filetypes=filetypes))
    if(len(temp)==0):
        print("None")
    else:
        print(temp)

if args.d:
    temp=(tkinter.filedialog.askdirectory())
    if(len(temp)==0):
        print("None")
    else:
        print(temp)

if args.f:
    temp=(tkinter.filedialog.askopenfilenames(filetypes=filetypes))
    if(len(temp)==0):
        print("None")
    else:
        print('\n'.join(temp))

