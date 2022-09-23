from plot import *

groups = create_groups()
deliverer_ids = [item.id for item in datalist if item.deliverer]
k = len(deliverer_ids) # number of groups
def run():
    # overview
    print("\nOverview of the groups: \n")
    df = pd.DataFrame([[len(groups[i]) for i in range(k)], deliverer_ids], \
        index=['Group Size', 'Deliverer ID'], columns=['Group '+str(i+1) for i in range(k)])
    print(df)

    print("\nPress Enter to continue and print a summary of up to 5 groups,\n \
    or type 'all' to print a summary for all groups: \n")
    printsummary = input()

    # dictionary of dataframes so they can be put in a spreadsheet
    dflist = {}

    # create and print dataframe summary of each delivery group
    for a in range(k):
        testlist = [[] for i in range(len(groups[a]))]
        for b in range(len(groups[a])):
            person = groups[a][b]
            testlist[b].append(person.id)
            testlist[b].append(a+1)
            testlist[b].append(person.street)
            testlist[b].append(person.house_no)
            testlist[b].append(person.postcode)
            testlist[b].append(person.status)
        df = pd.DataFrame(testlist, index=[i+1 for i in range(len(groups[a]))], columns=['ID', 'Group', 'Street', 'House No', 'Postcode', 'Deliverer?'])
        dflist[a] = df
        if a < 5 or printsummary.lower()=='all':
            print(df)
            print("\n")

    savechoice = input("Enter 'x' to save results in a spreadsheet: ")
    if savechoice.lower() == 'x':
        # create excel spreadsheet sorted into groups
        with pd.ExcelWriter('../delivery_groups_sorted.xlsx') as writer:
            for i in range(k):
                dflist[i].to_excel(writer, sheet_name='Group '+str(i+1))
        print("Spreadsheet saved as 'delivery_groups_sorted.xlsx'")

if __name__ == '__main__':
    run()