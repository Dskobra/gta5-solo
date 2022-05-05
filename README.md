# gta5-solo
Creates a solo lobby for gta 5 on pc

# Quick summary

Just a quick and poorly written bash/python script that times your gta 5 online session out long enough to be in your own lobby.
Personally I find it easier to simply run a command that pauses/resumes the game rather then right clicking the process in my desktops
process manager.

# Requirements
- GNU/Linux only
- Fedora 35 (tested)

Should work on any distro that includes python 3 and standard unix commands (awk, grep, ps, kill).

https://en.wikipedia.org/wiki/List_of_Unix_commands

# How to use
Simply run solo.sh from a terminal and wait for completion. It should pause gta 5 and once done you should see everybody left the lobby.

Simply rerun if you find it putting other people in your empty lobby or merged you into another lobby.

Sometimes counting to the default value of 1000000 isn't long enough to time out a session. Just change the timewaster variable
to a higher value. Something like 7000000 which has been working better for myself lately.


# Important notes

- You may need to run solo.sh a couple times as for whatever reason sometimes it doesn't split you off into your own lobby.
- I've only tested this on Fedora (my main distro) with steam version of gta 5.
- The code may or may not work with rdo if you replace "GTA5.exe" with the rdo binary filename. Haven't bothered to play rdo
for more then 5 min before I got bored.