import os
from table_bert import Table, Column
from table_bert import TableBertModel
import pandas as pd

tables = []
columns = []
data = []
embedding_data = []

for i in os.listdir("./"):
    if os.path.splitext(i)[1] == ".csv" and i not in ['tabbie_embeddings.csv', 'labeled_tabbie_embeddings.csv', 'fasttext_embeddings.csv','labeled_fasttext_embeddings.csv' ,"dev.csv", "Glove_embeddings.csv", "labeled_data.csv", "labeled.csv", "elmo_embeddings.csv", "labeled_elmo_embeddings.csv", "labeled_bert_embeddings.csv" , "labeled_tabert_embeddings.csv", "tabert_embeddings.csv", "bert_embeddings.csv"]:
    # if os.path.splitext(i)[1] == ".csv" and i in ["agences.csv"]:
        tables.append(i)

model = TableBertModel.from_pretrained(
        './TaBERT/tabert_base_k1/model.bin',
)

for tab in tables:
    # Read data using pandas
    df = pd.read_csv(tab)

    for column in df:
        columns.append((os.path.splitext(tab)[0], column))
        
    # Extract header and data from DataFrame
    header = df.columns.tolist()
    data = df.values.tolist()

    columns_bert = [Column(col, 'text', sample_value=df[col][0]) for col in header]
    
    # Create Table object
    table = Table(
        id=os.path.splitext(tab)[0],
        header=columns_bert,  # Convert header to Column objects
        data=[row.to_list() for _, row in df.iterrows() ]
    ).tokenize(model.tokenizer)
    
    # model takes batched, tokenized inputs
    context_encoding, column_encoding, info_dict = model.encode(
        contexts=[model.tokenizer.tokenize(" ")],
        tables=[table]
    )
    for col_emb in column_encoding.reshape(-1,768):
        embedding_data.append(list(col_emb.detach().numpy()))

    print(column_encoding.shape)
    print(len(embedding_data))

index = pd.MultiIndex.from_tuples(columns)

data = pd.DataFrame(embedding_data, index = index)

data.to_csv("tabert_embeddings.csv")

    
