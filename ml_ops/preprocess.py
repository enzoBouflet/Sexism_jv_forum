from ml_ops.encoder import tokenize , label
def preprocess(data):
    #get the data and preprocess it by throwing it into the encoder


    data = data.map(tokenize, batched=True)

    # !!!!!! il faut changer le nom des colonnes a removes pour coller a nos data !!!!
    remove_columns = ['id', 'text', 'type']

    data = data.map(label, remove_columns=remove_columns)

    return data

def train_val_test_split(data):
    train_dataset = data['train'].shuffle(seed=10).select(range(5875))
    eval_dataset = data['train'].shuffle(seed=10).select(range(5875, 7593))
    test_dataset = data['train'].shuffle(seed=10).select(range(7593, 8593))
    return train_dataset , eval_dataset, test_dataset
