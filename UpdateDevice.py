import csv
with open('device.csv', 'w') as csvfile:
	fieldnames = ['hostname', 'user', 'password',]
	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
	writer.writeheader()
	writer.writerow({'hostname':'router1','user':'Joe','password':'passw0rd1#'})
	writer.writerow({'hostname':'router1','user':'Fred','password':'passw0rd1#'})
	writer.writerow({'hostname':'router1','user':'Sam','password':'passw0rd1#'})
	writer.writerow({'hostname':'router1','user':'Lou','password':'passw0rd1#'})