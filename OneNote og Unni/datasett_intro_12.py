"""Tips: Bruk replace all og erstatt linjeskift og mellomrom med ingenting"""
txt = "The Zen of Python, by Tim PetersBeautiful is better than ugly.Explicit is better than implicit.Simple is better than complex.Complex is better than complicated.Flat is better than nested.Sparse is better than dense.Readability counts.Special cases aren't special enough to break the rules.Although practicality beats purity.Errors should never pass silently.Unless explicitly silenced.In the face of ambiguity, refuse the temptation to guess.There should be one-- and preferably only one --obvious way to do it.Although that way may not be obvious at first unless you're Dutch.Now is better than never.Although never is often better than *right* now.If the implementation is hard to explain, it's a bad idea.If the implementation is easy to explain, it may be a good idea.Namespaces are one honking great idea -- let's do more of those!"

#hei = "	The Zen of Python, by Tim PetersBeautiful is better than ugly.Explicit is better than implicit.Simple is better than complex.Complex is better than complicated.Flat is better than nested.Sparse is better than dense.Readability counts.Special cases aren't special enough to break the rules.Although practicality beats purity.Errors should never pass silently.Unless explicitly silenced.In the face of ambiguity, refuse the temptation to guess.There should be one-- and preferably only one --obvious way to do it.Although that way may not be obvious at first unless you're Dutch.Now is better than never.Although never is often better than *right* now.If the implementation is hard to explain, it's a bad idea.If the implementation is easy to explain, it may be a good idea.Namespaces are one honking great idea -- let's do more of those!

bokstaver_i_tekst = []
for tegn in txt:
    if tegn.lower() not in bokstaver_i_tekst:
        bokstaver_i_tekst.append(tegn.lower())

print(sorted(bokstaver_i_tekst))

ordbok = {}
for tegn1 in sorted(bokstaver_i_tekst):
    count = 0
    for tegn2 in txt:
        if tegn1==tegn2.lower():
            count +=1
    ordbok[tegn1] = count
print(ordbok)