import transformers 

MAX_LEN = 512
TRAIN_BATCH_SIZE = 8
VALID_BATCH_SIZE = 4
EPOCHS = 1
BERT_PATH = "C:\\Sowmya\\Personal\\PYTORCH\\Training_Sentiment_Model_Using_Bert_Pytorch\\input\\bert-base-uncased\\"
MODEL_PATH = "model.bin"
TRAINING_FILE = "C:\Sowmya\Personal\PYTORCH\Training_Sentiment_Model_Using_Bert_Pytorch\input\IMDB.csv"
TOKENIZER = transformers.BertTokenizer.from_pretrained(
    "bert-base-uncased",
    do_lower_case=True
)
DEVICE="cpu"