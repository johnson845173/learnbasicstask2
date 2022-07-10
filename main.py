# import section
import pandas as pd

# Reading the iput file
#enter the name of file in terminal wwhich you want to be taken as input
df = pd.read_csv(input("Enter the name of input file without extension")+".csv")

# function to extract the names of the test from input data
def head():
    for k in headings:
        temp = (k.split('-', 1)[0].strip())
        if temp not in test_name:
            test_name.append(temp)

test_no = i = 0

# Create a List with all the test name
test_name = []

# create a  varible heading with all the column title
headings = df.head(0)

list = ['Name','Username','Chapter Tag','Test_Name','answered','correct','score','skipped','time-taken(seconds)','wrong']

head()
test_name = test_name[3:]

# Creating a new DataFrame for saving the output file
new_dict = pd.DataFrame(columns = list)

for name in df.Name:
    test_no = 0
    for tt in test_name:
        values = []
        for j in headings:
            if test_name[test_no] in j or j == 'Name' or j == 'id' or j == 'Chapter Tag' :
                values.append(df.loc[i][j])
        values.insert(3,test_name[test_no])

        if "-" not in values:
            new_dict.loc[len(new_dict.index)] = values
        test_no += 1

    i+=1

#enter the desired file name you want the file to be saved as
new_dict.to_csv(input("enter the name for the file to be saved as")+".csv")
