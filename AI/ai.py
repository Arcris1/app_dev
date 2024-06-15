from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load pre-trained GPT-2 model and tokenizer
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

prompt = input("Ask me what you want: ")

# Generate responses to prompts
# Tokenize input prompt
input_ids = tokenizer.encode(prompt, return_tensors="pt")

# Generate response from model
output = model.generate(input_ids, max_length=250, num_return_sequences=1, do_sample=True, pad_token_id=tokenizer.eos_token_id)

# Decode generated response
response = tokenizer.decode(output[0], skip_special_tokens=True)

# Print conversation
print("User:", prompt)
print("Bot:", response)
