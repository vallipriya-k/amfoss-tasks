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

## Level 3: Little Garden

Returned to the `GrandLine` folder, switched to the target branch, and navigated to `Little_Garden`:

`cd ../..`
`git checkout little_garden`
`cd Little_Garden`

Navigated into `Wax_Jungle` and generated the MD5 hash of Level 2's flag:

`cd Wax_Jungle`
`echo -n "BAROQUE_DIAL{SPLIT_TIMELINE_MISDIRECTION}" | md5sum`

Searched recursively through the directories for relevant entries:

`grep -rn "BAROQUE" .`

Located and read the agent log inside the nested archive directory:

`cat ./sector_beta/outpost/watchtower/storage/archive/agent_manifest.log`

Output / Fragment I:
`PONEGLYPH_FRAGMENT_I = "KjY2MjF4bW0lKzYqNyBsIS0vbTAtJTcnL"`

---

## Level 4: Water 7

Navigated into the `Water_7` directory and listed the contents to find compressed blueprint archives:

`cd ../../..`
`cd Water_7`
`ls -la`

Extracted `puffing_tom_blueprints` using `tar`, then unzipped the nested `step1_blueprints.zip` file:

`tar -xvf puffing_tom_blueprints`
`unzip step1_blueprints.zip`

Navigated to the newly extracted `blueprints_extracted` folder and inspected `secret_link.txt`:

`cat blueprints_extracted/secret_link.txt`

Output / Fragment II:
`PONEGLYPH_FRAGMENT_II = "SwnbzptDiM3JspvFiMuJ28PJzAlJ28VIzA="`

---

## Level 5: Enies Lobby

Navigated back to `GrandLine` and checked all branches to locate the alternate timeline:

`cd ~/Terminal-Voyage-User-Edition/GrandLine`
`git branch -a`
`git checkout alternate_timeline`

Inspected commit history to locate the intact state before destruction and checked out commit `d4e7bf5`:

`git log --oneline -n 10`
`git checkout d4e7bf5`

Navigated into `Enies_Lobby` and executed the XOR decryption script using Python (`0x42` key) on both concatenated fragments:

`cd Enies_Lobby`
`python3 -c '
import base64
KEY = 0x42
code = "KjY2MjF4bW0lKzYqNyBsIS0vbTAtJTcnL" + "SwnbzptDiM3JspvFiMuJ28PJzAlJ28VIzA="
try:
    decoded = base64.b64decode(code)
    flag_bytes = bytes(b ^ KEY for b in decoded)
    print("Raw Bytes:", flag_bytes)
    print("Latin-1 Decoded:", flag_bytes.decode("latin-1"))
except Exception as e:
    print("Error:", e)
'`

Repository Unlocked:
`https://github.com/rogueone-x/Laugh-Tale-Merge-War.git`

---

## Level 6: Laugh Tale (Merge War)

Cloned the final challenge repository and navigated into it:

`git clone https://github.com/rogueone-x/Laugh-Tale-Merge-War.git`
`cd Laugh-Tale-Merge-War`

Merged `origin/pirate_king_path` into the active branch to combine the key components:

`git merge origin/pirate_king_path`

Inspected the merge conflicts inside `treasure/key_part_1.txt` and `treasure/key_part_2.txt`:

`cat treasure/key_part_1.txt`
`cat treasure/key_part_2.txt`

Resolved the conflicts to assemble the password (`TheGrandLineRemembers`), staged the resolved files, and committed the resolution:

`git add treasure/key_part_1.txt treasure/key_part_2.txt`
`git commit -m "Resolve merge conflicts for key parts"`

Executed `victory.sh` and supplied the assembled password:

`./victory.sh`

Final Output / Flag:
`FLAG{The_Grand_Line_Remembers_Your_Commit}`
