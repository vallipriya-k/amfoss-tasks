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

## Level 2: Whiskey Peak

Returned to the `GrandLine` directory and navigated into `Whiskey_Peak`:

`cd ~/Terminal-Voyage-User-Edition/GrandLine/Whiskey_Peak`

Inspected the directory contents and read `feast_manifest.txt`:

`ls -la`
`cat feast_manifest.txt`

Checked for hidden branches using `git branch -a`. The output revealed a hidden remote branch: `remotes/origin/whiskey_peak_investigation`. Switched to it:

`git checkout whiskey_peak_investigation`

Inspected the updated contents to find new files and hidden directories:

`ls -la`
`cat intercepted_report.txt`

The branch switch revealed the hidden directory `.baroque_works_cache`. Navigated into it and listed the contents:

`cd .baroque_works_cache`
`ls -la`

Exported the signature flag from Level 1, executed the vault unlock script, and compared the generated log files using `diff`:

`export AWAKENING_SIGNATURE="ONE_PIECE{GITO_GITO_NO_AWAKENING}"`
`./unlock_vault.sh`
`diff marine_intercept.log bounty_hunter_feed.log`

Output / Flag:
`BAROQUE_DIAL{SPLIT_TIMELINE_MISDIRECTION}`
