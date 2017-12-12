# Software
The official repository for software at Olin Electric Motorsports



# Running the CAN data visualization flask app:
Currently, all of the flask app content comes from the program visualization.py
It might be nice in the future to have some central "web" program; it could
render HTML templates or something fancy like that. For now though, this works.


To run the flask app in a browser, clone the repo, install flask, and then 
run these two commands in the terminal.
`export FLASK_APP=visualization.py
python -m flask run '
