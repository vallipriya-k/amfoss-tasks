# Terminal Voyage - Task 01 Solutions

## Level 1: Loguetown Reef

Cloned the repository and navigated into the project directory:

`git clone https://github.com/rogueone-x/Terminal-Voyage-User-Edition`
`cd Terminal-Voyage-User-Edition`

Switched to the target branch and moved into the Level 1 directory:

`git checkout timeline`
`cd GrandLine/Loguetown_Reef`

Listed the contents using `ls` and found `eat.sh` executable. Inspected `eat.sh` using `cat` to see how it operates:

`cat eat.sh`

The script checks for executable permissions on devil fruit files. Noticed `sector_C/devil_fruit_6.txt` highlighted in green, so passed it as an argument to `eat.sh`:

`./eat.sh sector_C/devil_fruit_6.txt`

Output:
`ONE_PIECE{GITO_GITO_NO_AWAKENING}`
