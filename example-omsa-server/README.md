# Example OMSA Server

This server is a small, easy to extend example webserver that implements a part of the OMSA API.

## Install

This example requires Python, install this. We use version 3.13.2.  
run `pip install -r .\requirements.txt` to install the required libraries for the webserver.

## Start

run `py .\webserver.py` in a terminal to start the webserver. It runs on port 5000.

## Details

You can easily extend this example by providing additional files for the meta-parts. The format of the files is always {action}-{subject}.{language}.(html|json) for the processes. Provide both files to make it OGC compatible.

The output of the data endpoints (like /processes/claim-refund-option/execute) is for now in code ...
