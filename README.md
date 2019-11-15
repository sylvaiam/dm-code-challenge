You can run the file by doing:

`python viscode_filter svdose_filter ecs_filter_out`

Which will create and open a pie chart of the data in t2_registry 20190619.csv, then filter the data and output it in results.csv.
The filter will be viscodes that match viscode_filter, svdoses that match svdose_filter, and ecss that do not match ecs_filter_out.

To test, open this directory in a command line and type `pytest`
