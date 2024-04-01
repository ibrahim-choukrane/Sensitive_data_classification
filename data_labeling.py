import pandas as pd
import numpy as np
import sys
import os



def tags2dict(tags):
    unique_names = []
    tags_dict = {}
    unique_names = tags["Table_Name"].unique()
    for table in unique_names:
        temp = {}
        for column,tag in zip(tags["Column_Name"],tags["Tag"]):
            temp[column] = tag
        tags_dict[table] = temp
    return tags_dict


if ( len(sys.argv) == 3 ) and ( os.path.splitext(sys.argv[1])[1] == '.csv'):
    embeddings = pd.read_csv(sys.argv[1])
    sensitivity_rules = tags2dict(pd.read_csv(sys.argv[2]))

    embeddings.index = pd.MultiIndex.from_frame(embeddings.loc[:,["Unnamed: 0","Unnamed: 1"]],names= ("Table", "Column"))
    embeddings.drop(["Unnamed: 0","Unnamed: 1"], axis=1, inplace=True)

    try:
        labels = []
        for table, column in embeddings.index:
            labels.append(sensitivity_rules[table][column])
        #labels = [sensitivity_rules[table][column] for table, column in embeddings.index]
    except KeyError :
        print(table,column)

    
    serie_labels = pd.Series(labels)
    
    embeddings['sensitivity'] = serie_labels.to_numpy()
        
    embeddings.to_csv(f"test_labeled_{os.path.splitext(sys.argv[1])[0]}.csv")

else:
    print("Please provide appropriate parameters")