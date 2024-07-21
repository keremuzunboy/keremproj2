from transformers import Trainer, TrainingArguments, AutoModelForSequenceClassification, AutoTokenizer
from datasets import load_dataset

# Load a dataset (example: IMDb dataset)
dataset = load_dataset("imdb", split="test")

# Load the model and tokenizer
model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased")
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# Tokenize the dataset
def tokenize_function(examples):
    return tokenizer(examples["text"], padding="max_length", truncation=True)

tokenized_dataset = dataset.map(tokenize_function, batched=True)

# Define training arguments
training_args = TrainingArguments(output_dir="./results")

# Update the Trainer with the dataset
trainer = Trainer(model=model, args=training_args, eval_dataset=tokenized_dataset)

# Evaluate the model
results = trainer.evaluate()

# Print the evaluation results
print(results)