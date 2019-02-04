# File Writer

## Description
This program sends a JSON object to a server which is then extracted and written to a file. This file is read and written
in google protobuf format to another file.

A BASH script is used to execute this program from the command line.

ex: ```./bashsample.sh ```

## Quick Startup
To run this program on your machine, _FORK_ and clone [this](https://github.com/jtruelas/File-Writer.git) repo.
```
user ~ $ mkdir new_directory
user ~ $ git clone repo_url new_directory
user ~ $ cd new_directory
```
If you don't already have python go [here](https://www.python.org/downloads/) to download it. Make sure you check the box _Add python to PATH_ during the installation process.

Open your terminal and enter the following:
```
user ~ $ pip install Flask protobuf
```
When the install completes, open an additional terminal and cd to directory hosting the cloned repo, then run:

```user <repo-directory> $ ./webserver.py```

In the other terminal you should also be in the directory where the clone was made. Run the following command and follow the prompt:

```user <repo-directory> $ ./bashsample.sh```

You can view the files being written to by simply clicking on them from the file explorer.

## Testing
Some ways to make sure this program is functioning as expected. 

_If you run the bash script and press 'Enter' rather than inputting the requested data, it should repeat the request._

_The program will only continue when the requested data is entered. If you do not have any further data to add you can simply exit with ```Ctrl+C```._
