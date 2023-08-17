# https://milliams.com/courses/intermediate_python/answer_morse_raise.html

import morse

# message = morse.encode("hello")
# print(f"morsemessage {message}")

# morsemessage = "... . -.-. .-. . - / -- . ... ... .- --. ."
# decoded_message = morse.decode(morsemessage)
# print(decoded_message)

message = "test"

code = morse.encode(message)
decode = morse.decode(code)
print(decode == message)

# import recipe

# gram = recipe.ounces_to_grams(-66)
# print(gram)
