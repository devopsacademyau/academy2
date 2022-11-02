#!/bin/bash
set -ex
# ALL OUTPUT goes to markdown

git grep -r -e 'SUPERSECRET' $(git rev-list --all) > out.txt || true

if [ -s out.txt ]
then
        echo ":x: # FAILED - EXERCISE 2" 

else
        echo ":white_check_mark: # PASSED - EXERCISE 2"
fi