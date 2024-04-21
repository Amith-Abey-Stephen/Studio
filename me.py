from transformers import GPT2LMHeadModel, GPT2Tokenizer

class ChatGPT:
    def __init__(self):
        self.model_name = "gpt2-medium"
        self.tokenizer = GPT2Tokenizer.from_pretrained(self.model_name)
        self.model = GPT2LMHeadModel.from_pretrained(self.model_name)
    
    def generate_response(self, user_input):
        input_ids = self.tokenizer.encode(user_input, return_tensors='pt')
        response_ids = self.model.generate(input_ids, max_length=100, num_return_sequences=1, pad_token_id=self.tokenizer.eos_token_id)
        response = self.tokenizer.decode(response_ids[0], skip_special_tokens=True)
        return response

    def chat_loop(self):
        print("Hello! I'm your ChatGPT.")
        while True:
            user_input = input("You: ")
            if user_input.lower() in ('exit', 'quit'):
                print("ChatGPT: Goodbye!")
                break
            response = self.generate_response(user_input)
            print("ChatGPT:", response)


if __name__ == "__main__":
    chatbot = ChatGPT()
    chatbot.chat_loop()
