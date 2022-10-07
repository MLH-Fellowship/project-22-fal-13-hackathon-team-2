#!/bin/bash

tmux kill-server
tmux new-session -d -s portfolio_tmux
tmux send 'cd MLH_SRE_Portfolio' ENTER;
tmux send 'git fetch && git reset origin/main --hard' ENTER;
tmux send 'python -m venv python3-virtualenv' ENTER;
tmux send 'source python3-virtualenv/bin/activate' ENTER;
tmux send 'pip install -r requirements.txt' ENTER;
tmux send 'flask run --host=0.0.0.0' ENTER;
