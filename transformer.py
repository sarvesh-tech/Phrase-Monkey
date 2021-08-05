import torch
from sentence_splitter import SentenceSplitter
from transformers import PegasusForConditionalGeneration, PegasusTokenizer

model_name = 'tuner007/pegasus_paraphrase'
torch_device = 'cuda' if torch.cuda.is_available() else 'cpu'
tokenizer = PegasusTokenizer.from_pretrained(model_name)
model = PegasusForConditionalGeneration.from_pretrained(model_name).to(torch_device)


def get_response(input_text, num_return_sequences, num_beams):
    batch = tokenizer([input_text], truncation=True, padding='longest', max_length=60, return_tensors="pt").to(
        torch_device)
    translated = model.generate(**batch, max_length=60, num_beams=num_beams, num_return_sequences=num_return_sequences,
                                temperature=1.5)
    tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
    return tgt_text


# Paragraph of text
def paraphrase_text(context):
    # Takes the input paragraph and splits it into a list of sentences
    splitter = SentenceSplitter(language='en')

    sentence_list = splitter.split(context)

    # Do a for loop to iterate through the list of sentences and paraphrase each sentence in the iteration
    paraphrase = []

    for i in sentence_list:
        a = get_response(i, 1, 10)
        paraphrase.append(a)

    # paraphrased text
    paraphrase2 = [' '.join(x) for x in paraphrase]

    # Combines paraphrase2 into a paragraph
    paraphrase3 = [' '.join(x for x in paraphrase2)]
    paraphrased_text = str(paraphrase3).strip('[]').strip("'")

    return paraphrased_text


# Comparison of the original (context variable) and the paraphrased version (paraphrase3 variable)
# context = "In this video, I will be showing you how to build a stock price web application in Python using the Streamlit and yfinance library. The app will be able to retrieve company information as well as the stock price data for S and P 500 companies. All of this in less than 50 lines of code."
# print(paraphrase_text(context))
