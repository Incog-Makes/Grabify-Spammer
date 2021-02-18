# Grabify-Spammer
Simple python application that utilises tor to flood an ip grabber with tor addresses, and rotates after every request. Uses the requests and stem modules. I made this to expermiment with how python can interact with tor and also for people should they expose their ip via a ip grabber to ruin the persons day by spamming pages of junk ip's, and hiding yours in the process.

Prerequsites:
Tor

Instructions/Setup:

1. Edit the torrc file to enable the controller and the hashpassword
eg.
ControlPort 9051
HashedControlPassword 16:05834BCEDD478D1060F1D7E2CE98E9C13075E8D3061D702F63BCD674DE
(that hashed password is "password" which is NOT reccomended for use as hacking goes brrt, If you are unaware of how to generate a password, open a cmd prompt in the tor executable directory and enter tor --hash-password "<new_password>" replace <new_password> with the one you want.)

2. start tor, either through the browser and having that start up the proxy, or through the tor executable.
(Note, you will need to remove the service and reinstall again if previously installed, shown below:)
tor --service remove
tor --service install -options ControlPort 9051
tor --service restart

3. edit the script and enter the link url, and header if needed.

4. Run and watch requests flood in


At current rate its around 3 requests per second for me, however this can vary on connection speeds.
Tested on windows and python3.8, compatability for linux is likely but untested.
