def cap(c):
    if 'A' <= c <= 'Z':
        return chr(ord(c) + 32)
    return c

def count_chr(txt):
    res_list = [0]*26
    for c in txt:
        if 'a' <= c <= 'z' or 'A' <= c <= 'Z':
            res_list[letter_list.index(cap(c))] += 1
    return res_list

def bubbling(nList, indexList):
    for a in range(len(nList)-1):
        flag = 0
        for i in range(len(nList)-1-a):
            if nList[i] < nList[i+1]:
                nList[i], nList[i+1] = nList[i+1], nList[i]
                indexList[i], indexList[i+1] = indexList[i+1], indexList[i]
                flag = 1        
        if flag == 0:
            return nList, indexList
        
         
# ----data init----
txt = """
A lifetime on and in front of the television, that hurried medium, trained Donald Trump in the art of the compressed jibe. Next to “low energy” and “little Marco”, however, “lyin’ Ted” was a dud. It took supplemental strikes on Ted Cruz’s wife and father to sting the Texas senator, who called Mr Trump a “snivelling coward” in 2016.
On Monday, Mr Trump campaigned for Mr Cruz in Houston. There have been similar reconciliations with senators Rand Paul, who once called the president an “orange-faced windbag”, and Lindsey Graham, who, with Beckettian economy, went with “jackass”.
At this point, the done thing is to regret the moral capitulation of these one-time resisters. Less examined is the other side of the rapprochement. How easily Mr Trump comes to an understanding. For enemies, the price of re-admittance to his fold is the odd dose of flattery and votes for things they would have voted for anyway. Because he looks and talks like an immovable man, we miss evidence to the contrary.
The lesson here is not for Washington’s careerists. It is for allied nations. After they steadied gingerly from the savage shock of his election, countries were left with a practical question: how to manage this strange phase in relations with the US? How, at a stretch, to gain from it? Some, such as Germany, went into unofficial opposition. Others (Britain more than most) tried too hard to please him.
Neither has it right. Mr Trump can be worked with, or at least neutralised. And it can be done without total self-abasement. The president is not a driver of particularly hard bargains. He can live with symbolic gestures of concession: what some have called “tweetable wins”.
A minor renegotiation was enough to settle his decades-old grievance with Nafta. It also softened his more recent feud with Canada. Last year, he described Nato as “no longer obsolete” after assurances from Jens Stoltenberg, the secretary-general, about its work against terrorism. He was further defanged in his hostility to the alliance by a round of European military spending that mostly predates his presidency. As recently as April, he seemed (for a while) open to re-joining the Trans-Pacific Partnership on revised terms.
There is Trumpism as analysis: the US as gull, bearing burdens as liberty-taking foreigners giggle behind their hands. And there is Trumpism as action: small tweaks to the status quo, usually entailing a cosmetic financial sop to Washington. Perhaps he never believed the analysis in the first place. Perhaps he does not understand the smallness of the changes.
More plausible than either Mr Trump-as-fake or Mr Trump-as-fool is Mr Trump-as-politician. With re-election two years away, he wants diplomatic successes to parade. To that end, he plays up whatever he negotiates, intuiting that his voters crave the righteous momentum of America First as much as its precise detail.
Saudi Arabia supplies the most topical example of his susceptibility to economic gestures. Washington has reasons to preserve its alliance with the kingdom even after the alleged murder of dissident Jamal Khashoggi. But Mr Trump, who could mention Saudi counter-terror intelligence or usefulness against Iran, zeroes in on bilateral arms sales. Even if he is right to rate them at $110bn over time, they amount to a rounding error in the near-$20tn US economy. In other words, a veneer of munificence — “memorandums of intent” to buy American kit — has saved the Saudis from what might have been a breakdown of relations under another president.
The point is not to gloat at Mr Trump’s quickness to accommodate. (Would we rather that he was as stubborn as his image?) The point is to flag its usefulness to allies. He will lead the foremost power on Earth for two, perhaps six more years. Countries must find a modus vivendi with him. His pattern of behaviour implies that he is negotiable on much, and at affordable cost.
Although diplomats often resent mercantile foreign policy as a vulgarisation of their rarefied craft it has the blessing of clarity. There is no mistaking what a nation with such a policy wants.
What Mr Trump seems to want is a sense of restitution for monies diddled out of American coffers through such black magic as trade and collective security. Not always the substance: the sense. Knowing this, canny allies have somewhat stabilised relations with him through less-than-ruinous concessions, and let him have his day on Twitter. He means it when he calls himself a dealmaker. The mistake is to assume that he is a tough one.
"""

letter_list = []
for i in range(97, 123):
    letter_list.append(chr(i))


# ----main----
count_list = count_chr(txt)
count_list, letter_list = bubbling(count_list, letter_list)
print(count_list, letter_list)





