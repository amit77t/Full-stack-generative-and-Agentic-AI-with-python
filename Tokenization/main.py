import tiktoken


enc=tiktoken.encoding_for_model("gpt-4o")


text="Hello My name is Amit Chaurasia"

tokens=enc.encode(text)


#[13225, 3673, 1308, 382, 136538, 1036, 4178, 37232]
print("Tokens : ",tokens)

decoded=enc.decode([13225, 3673, 1308, 382, 136538, 1036, 4178, 37232])
print( "Decoded : ",decoded)




