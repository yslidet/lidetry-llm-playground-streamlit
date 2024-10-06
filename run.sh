# >> Activate conda ENV
#conda activate llm-mac-intel

# >> Setup $PYTHONPATH
# cd [project_dir]
#export PYTHONPATH="$PWD"
### ------ SETUP:end ------

streamlit run run.py --server.port=8001 --server.address=127.0.0.1
#streamlit run run.py --server.port=8001 --server.address=localhost