from bert import Ner

model = Ner("out_base/")

output = model.predict("Благодарим Вас за то , что Вы приобрели отопительный , водогрейный , электрический котел КОВ-68 "

print(output)
