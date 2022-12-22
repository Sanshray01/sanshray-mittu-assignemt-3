# forming a pattern.
word = "ABCDEFGHIJK"
for i in range(0,6):
    print(" "*i + word[0:11-2*i])
    