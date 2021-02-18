# Grabify-Spammer
Simple python application that utilises tor to flood an ip grabber with tor addresses, and rotates after every request. Uses the requests and stem modules

Prerequsites:
Tor

Instructions/Setup:

1. Setup the torrc file to enable the controller and the hashpassword
eg.
ControlPort 9051
HashedControlPassword 16:05834BCEDD478D1060F1D7E2CE98E9C13075E8D3061D702F63BCD674DE
(that hashed password is "password" which is NOT reccomended for use as hacking goes brrt, If you are unaware of how to generate a password look here:

2. start tor, either through the browser and having that start up the proxy, or through the tor executable.
(Note, you will need to remove the service and reinstall again if previously installed, shown below

3. edit the script and enter the link url, and header if needed.

4. Run and watch requests flood in


At current rate its around 3 requests per second, however this can vary on connection speeds.
