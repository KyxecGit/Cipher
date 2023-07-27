from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"Слово {cipher_direction} зашифровано результат: {end_text}")


print(logo)

should_end = False
while not should_end:

  direction = input("Введите encode для шифрования, введите decode для расшифровки:\n")
  text = input("Введите свое сообщение:\n").lower()
  shift = int(input("Введите номер смены:\n"))
  shift = shift % 26

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  restart = input("Введите да, если вы хотите повторить попытку. В противном случае введите нет.\n")
  if restart == "нет":
    should_end = True
    print("Прощайте")
    
