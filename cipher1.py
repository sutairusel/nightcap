shift=int(input("Amount to shift by:\n"))
text=list(input("\nEnter text to encrypt:\n"))
olist=list()
enc_text=""
for i in text:
  ordinal=ord(i)+shift
  if(ordinal>=127):
    ordinal=ordinal%127+32
    olist.append(ordinal)
  elif(ordinal<=31):
    ordinal=ordinal+95
    olist.append(ordinal)
  else:
    olist.append(ordinal)
for i in olist:
  enc_text=enc_text+chr(i)
print("\nYour encrypted text:\n"+enc_text+"\n")
