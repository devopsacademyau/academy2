#!/bin/bash
set -ex
echo "Act"

# TO DO: Include the commands that solve the exercise here
source ${GITHUB_WORKSPACE}/exercise1/exercise1.sh

# DEBUG
echo "GITHUB_ACTION_PATH=$GITHUB_ACTION_PATH"
env
ls -la