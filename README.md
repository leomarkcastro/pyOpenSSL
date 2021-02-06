# pyOpenSSL
School project where the aim is to use openssl by accessing it on a programming language

This program implements the following algorithms

- aes
- sha
- rsa
- ecdsa

To run this program, first, install openssl and make sure you can run openssl in your command prompt by typing 'openssl'
  - In case you haven't installed openssl on windows, you can download an installer in this site. -> https://slproweb.com/products/Win32OpenSSL.html
  
Then, you should have Python installed on your computer atleast version 3.6
  - Download an installer here. -> https://www.python.org/downloads/

After you installed OpenSSL and Python on your computer, you can run the app in two ways:
  - If you want to run the python as is and use OpenSSL everywhere, you should add "C:\Program Files\OpenSSL-Win64\bin" on the path variables on your PC's environment variables -> https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/
    -> On the first run, you should run first_run.py first
    -> Then run the program by clicking run.py
    
  - Else you can run the program as is without touching anything at the environment variables. 
    -> On your first run, run "first_run.bat" {.bat files are console command scripts, they are not viruses haha)
    -> Then run the program by running 'run.bat'
  
