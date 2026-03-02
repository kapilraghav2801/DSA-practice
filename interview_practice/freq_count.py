# s = "aab"
# #output = {'a':2, 'b':1}
# def charFreq(s):
#     freq = {}
#     for ch in s:
#         if ch in freq:
#             freq[ch] += 1
#         else:
#             freq[ch] = 1
#     return freq

# print(charFreq(s))

def charFreq(s):
    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq

print(charFreq(s="aab"))

