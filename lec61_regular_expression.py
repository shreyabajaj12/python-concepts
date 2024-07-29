# r refers to raw string
import re
# pattern=r"[A-Z]+hina"
# pattern=r"\d{6}"
pattern=r"\(\d{3}\)-\d{3}-\d{3}"   #since brackets has its own special meaning.
text='''India, officially the Republic of India (ISO: Bhārat Gaṇarājya),[21] is a country in South Asia. It is the seventh-largest country by area; the most populous country as of June 2023;[22][23] and from the time of its independence in 1947, the world's most populous democracy.[24][25][26] Bounded by the Indian Ocean on the south, the Arabian Sea on the southwest, and the Bay of Bengal on the southeast, it shares land borders with Pakistan to the west;[j] China, Whina, Nepal, and Bhutan to the north; and Bangladesh and Myanmar to the east. In the Indian Ocean, India is in the vicinity of Sri Lanka and the Maldives; its Andaman and Nicobar Islands share a maritime border with Thailand, Myanmar, and Indonesia.

Modern humans arrived on the Indian (999)-333-555 subcontinent from Africa 123456 no later than 55,000 years ago.[27][28][29] Their long occupation, initially in varying forms of isolation as hunter-gatherers, has made the region highly diverse, second only to Africa in human genetic diversity.[30] Settled life emerged on the subcontinent in the western margins of the Indus river basin 9,000 years ago, evolving gradually into the Indus Valley Civilisation of the third millennium BCE.[31] By 1200 BCE, an archaic form of Sanskrit, an Indo-European language, had diffused into India from the northwest.[32][33] Its evidence today is found in the hymns of the Rigveda. Preserved by an oral tradition that was resolutely vigilant, the Rigveda records the dawning of Hinduism in India.'''

match=re.search(pattern,text)  #used to wait for just 1st match only and then it stops
print(match)

# matches= re.finditer(pattern,text)
# for match in matches:
#      print(match)