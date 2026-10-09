# System dependencies

Name the runtimes, system commands, and bootstrap inputs that a fresh
worktree needs. Supply exact bootstrap commands and their expected cost.
Do not symlink shared mutable state from the main checkout.

The kit's scaffolding tools require Git, jq, and Python 3.9 or later. Interactive
scaffolding also requires gum. These are kit tool requirements. The target
project's requirements must be supplied when the run is instantiated.
