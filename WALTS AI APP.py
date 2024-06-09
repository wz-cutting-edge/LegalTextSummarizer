import tkinter as tk
#from transformers import pipeline
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
def summarize_text():
    input_text = input_box.get("1.0", "end-1c")
    summarizer = pipeline("summarization", model="aiguy68/Super_legal_text_summarizer")
    tokenizer = AutoTokenizer.from_pretrained("aiguy68/Super_legal_text_summarizer")
    inputs = tokenizer(input_text, return_tensors="pt").input_ids
    model = AutoModelForSeq2SeqLM.from_pretrained("aiguy68/Super_legal_text_summarizer")
    outputs = model.generate(inputs, max_new_tokens=142, do_sample=False)
    summary = tokenizer.decode(outputs[0], skip_special_tokens=True)
    output_box.delete("1.0", "end")
    output_box.insert("1.0", summary)

root = tk.Tk()
root.title("W.A.L.T.S AI")

input_label = tk.Label(root, text="INPUT TEXT")
input_label.pack(pady=5)

input_box = tk.Text(root, height=5, width=50)
input_box.pack(pady=5)

summarize_button = tk.Button(root, text="Summarize", command=summarize_text)
summarize_button.pack(pady=5)

output_label = tk.Label(root, text="SUMMARY")
output_label.pack(pady=5)

output_box = tk.Text(root, height=10, width=50)
output_box.pack(pady=5)

root.mainloop()