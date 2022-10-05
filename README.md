# delivery-sorter

This project was written to take large sets of people and sort them into local groups. It takes as input a spreadsheet with details including longitude and latitude coordinates (these can be obtained from addresses, for example, by using one of many free google sheets extensions). The spreadsheet also indicates group leaders, or 'deliverers', of which exactly one must be present in each group.

### Summary of what the modules do ###

__analysis.py:__ sorts the data into groups and shows a summary, with the option to __save the sorted data into a new spreadsheet__

__k-means.py:__ demonstrates the working of the k-means clustering algorithm by randomly generating points and sorting into k groups. The number of points and the value of k can be changed in the program

__plot.py:__ sorts data into groups as in analysis.py, but plots the points at each iteration of the grouping to show how the groups develop

__showresults.py:__ plots a scatter of all points then final results, colour coordinated to show each group

### Example demonstration ###

When run on a database containing 962 random* London addresses, the inital scatter of points is output as follows:

\**(a similar number of random adresses were selected from each London postcode, giving a spread of locations across the city)*

![scatter](https://user-images.githubusercontent.com/98184411/194065463-6bd4f787-5cf9-44a3-8e20-7c58727735c3.png)

Points were then sorted, and grouped as below:

![grouped](https://user-images.githubusercontent.com/98184411/194065562-7a98dd3d-fdba-4af1-92b2-19b95d01e945.png)

Zooming in shows more clearly how groups are divided, with the 'deliverer' for each group outlined in grey

![groups_zoomed](https://user-images.githubusercontent.com/98184411/194065606-662aeff2-f5af-4df1-9736-a61c3d33b8b7.png)
