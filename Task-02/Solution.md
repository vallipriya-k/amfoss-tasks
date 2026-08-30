I set up the workspace by creating and entering the Task-02 directory (mkdir -p Task-02 and cd Task-02).

I cloned the target repository and navigated into the project root using git clone [https://github.com/Rufine777/ghost-in-the-machine.git](https://github.com/Rufine777/ghost-in-the-machine.git) followed by cd ghost-in-the-machine.

I audited the workspace structure and contents using ls -la to check hidden files and find . -maxdepth 2 -type f | sort to map top-level project files.

I verified the installed environment binaries by checking system versions via rustc --version and cargo --version.

I inspected the build definitions and backup files using cat Cargo.toml and cat Cargo.toml.bak.

I analyzed the repository commit history, branch structure, and tree visualization using git log --oneline --all --decorate --graph.

I initiated the build process and piped both stdout and stderr streams directly to a log file using cargo build 2>&1 | tee initial-build.txt.
