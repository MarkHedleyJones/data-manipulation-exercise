#! /usr/bin/env python

# Normally don't need a CSV library but because the input CSV is complex, for
# example it contains quoted fields and unicode characters, its much easier to
# use this library to help deal with it.
import csv

out = []

# Define the order we want to spit things out into the output CSV
required_headers = [
    'FULL NAME',
    'BORN',
    'AGE',
    'DIED',
    'PHYSICAL',
    'POSITION'
]

header = None

# Read all the data in and store it in an output friendly format
with open('./players_sample.csv', 'rb') as f:
    rows = csv.reader(f, delimiter=',', quotechar='"')
    for row in rows:
        if row[0] == 'FULL NAME':
            header = row
        else:
            # Assume this row is a data field since it doesn't start with 'FULL_NAME'
            # Also assume that the correct header row for this data is now loaded
            # into the header variable.

            # Zip the two rows together:
            # was ['name', 'age'] and ['Mark', '24']
            # now [('name', 'Mark'), ('age', '24')]

            # Turn the zipped rows into a dictionary so we can access each element
            # using its title
            data = dict(zip(header, row))
            temp = []
            # Step over each field we defined at the top of this file and add
            # either the data or a blank depending if present in the data
            for required_header in required_headers:
                if required_header in data:
                    if required_header == 'PHYSICAL':
                        physical_components = data[required_header].split(',')
                        if len(physical_components) > 1:
                            temp.append(physical_components[1].replace('\xc2\xa0', ""))
                        else:
                            temp.append('')
                    else:
                        temp.append(data[required_header])
                else:
                    temp.append('')
            out.append(temp)

# Now write it all out to a CSV again
with open('./players_processed.csv', 'w') as f:
    writer = csv.writer(f, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(required_headers)
    for row in out:
        writer.writerow(row)

print("Done")
