#cezarova sifra
def sifra(text, posun):
  sifra_=""
  for znak in text:
    if znak.islower():
      sifra_+=chr(((ord(znak)+ posun - 97) % 26 + 97))
    else:
      sifra_ += znak
  return sifra_
  
sprava="ahoj"
zasifrovana_sprava = sifra(sprava, 3)
print(zasifrovana_sprava)