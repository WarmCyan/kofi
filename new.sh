#!/bin/bash

filename=$(python -c "import util; print(util.get_uuid())")

#tmux new-session -d -s k

touch cache/$filename

nvim cache/$filename
