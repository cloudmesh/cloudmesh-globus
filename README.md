# Cloudmesh Globus

This program is a better globus command line client that allows to
transfer millions of files and automatically conduct the transfer through tar 
files if desired.

We observed this program is needed as in the endpoints that I use
and accesses a Globus server the service gets interrupted but does not fail. 
Hence, the transfer never finishes. With this commandline tool 
the issue could be solved.

Please take a look at our example.

## Installation

### Mac/Linux

```bash
python3.10 -m venv ~/GLOBUS
source ~/GLOBUS/bin/activate
pip install cloudmesh-globus
cms help
cms globus help
```

Calling the command cms help directly after the pip install
is very important as it sets up some directories and files


### Windows

This will work on windows, but the creation of the venv is different.
let us know how you do it as I do not have a Windows machine available.


## Usage

```
cms help
cms help globus
cms globus login FROM_EP TO_EP
cms globus transfer FROM_EP TO_EP DIR FROM TO [--mkdir=no] [--tar] [--force] [--dryrun]
cms globus transfer FROM_EP TO_EP DIR --file=FILE TO [--mkdir=no] [--run=1:100] [--tar] [--force] [--dryrun]

Arguments:
FROM_EP   the globus endpoint to transfer the file from
TO_EP     the globus endpoint to transfer the file to
DIR       the base directory from which to transfer. All transfers
are done relative to this DIR and the new remote directory
will not have the prefix DIR.
FROM      a relative directory to transfer files from
TO        the directory to transfer the relative directory FROM
FILE      a file that contains files or directories to transfer

Options:
--file=FILE  specify the file that contains the transfers
--tar        transfer the data in a tar file
--mkdir=no   assume the remote directory to place the file in is
             already created This can speed up the transfer in
             case you have many transfers to execute.  So create
             the file tree first. It also helps in case a transfer
             failed and you need to redo it, but the directories
             are already created.
--force      in case force is not specified and the tar file already 
    exists on the remote, the transfer will be not conducted.
    With force the transfer will be done.
--run=1:10   Only execute the transfers in the lines 1 to 10 
            

Description:

cms globus transfer FROM_EP TO_EP DIR FROM TO [--mkdir=no] [--tar]

This command is a convenience wrapper for the globus command
allowing the transfer of relative directories towards a source
directory. The program creates on the destination the same
directory tree as on the source starting from the base directory
specified with DIR. The FROM directory locates at DIR/FROM is
then copied to TO without the prefix DIR.

If you specify the --mkdir=no the destination directory is assumed to
exist and is not explicitly created. If it does not exist the program
will be terminated.

bookmarks

bookmarks can be stored in a file called
`~/.cloudmesh/globus.yaml`

let us assume the file contains

bookmark:
  uva: c4d80096-7612-11e7-8b5e-22000b9923ef
  laptop: 1a1a1a1--7612-11e7-8b5e-22000b9923ef

then you can use the keyword uva for an endpoint in the command

Examples:

Transfer via multiple globus tasks

cd mydir
ls -1 > file.txt
cat -n file.txt

cms globus transfer mars uva `pwd` --file=files.txt /remotedir --mkdir=no --run=13:18 --tar

This command will from the file transfer the files in the lines 13 to 18 contained in files.txt.
Each line will be handled as a separate transfer and the data will be placed in a tar file. that
tar file will then be transferred. On the remote machine the tar file will not be untarred. This
you do have to do by loggin into the machine such as with ssh abd untar the file. T
```
