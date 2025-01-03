

# GREEK DEITIES GENETIC RISKS
# -- Capstone Greek and Roman History Unit Project
# Author: Yongqing Grace Yu
# Last updated 11 November 2021




print('''


# Greek Deities Genetic Risks
Capstone Greek and Roman History Unit Project (schoolwork)

Author: Yongqing Grace Yu
Last updated 11 November 2021
This project is licensed under the terms of the MIT license.


## Research Question
- How do genetic illnesses pass down the incestuous Greek mythological family tree in Hesiod's Theogony? Specifically, if one or more primordial deities are genetically defective, how much genetic risks would their posterities suffer?


## Program Objectives
- To calculate the expected genetic composition of 310 Greek gods/mortals based on user-designated primordial god/mortal genotypes;
- To provide contextual interpretations of these data, such as on the expressed phenotype and genetic legacy of different genotype probability distributions, in order to provide a satisfactory answer to the research question for a general audience;
- To spur an interest in and enhance the understanding of Greek mythological figures for the reader;
- To spur an interest in and enhance the understanding of evolutionary biology for the reader;
- To discourage the reader from marrying their relatives.


## Invented Abbreviations
- `deity` (plural, deities): refers to all mythological figures, both gods and mortals, in the Theogony family tree
- `primor` (plural, primors): "deities" whose parents are not included in the family tree, i.e., primordial gods + mortals of ungodly descent (highlighted yellow in the [spreadsheet](https://github.com/yyu1230/High-School/blob/main/greek_deities_genetic_risks/greek_deities_pedigree.xlsx); genotype designated directly by the user)
- `posterity` (plural, posterities): all non-"primor" figures in the family tree


## Program Procedures
- You will be prompted to designate a value for the genotype (nn, nd, or dd; where n designates the normal allele and d the defective) of the concerned genetic character for each "primor."
- You can then enter the names of any "deities" (there will be a [list](https://github.com/yyu1230/High-School/blob/main/greek_deities_genetic_risks/greek_deities_pedigree.xlsx)), and the program will return their probabilities of having genotypes nn, nd, and dd, and interpret these results in the contexts of the genetic illness being autosomal recessive, dominant, co-dominant, or incompletely dominant.
- Finally, when you enter "quit," the program will exit with *thoughtful advice (you are welcome!)* on why it is not a good idea to marry your relatives.


## "Deities" Included
- Primordial gods: Chaos, Gaea, Tartaros, Eros
- Mortals of ungodly descent:
  + Cadmus (founder of Thebes, Harmonia's lover, Semele's father),
  + Alkmene (Zeus' lover, Heracles' mother),
  + Iasion (hero, Demeter's husband),
  + Tithonus (Eos' lover, Mnemnon/Emathion's father),
  + Jason (hero of the Golden Fleece, Medea's husband),
  + Asopus (actually a river god of unknown descent, Metope's husband, Aegina's father, Aiakos' maternal grandfather),
  + Metope's mother (Ladon's lover),
  + Endeïs (Aiakos' wife, Peleus' mother, Achilles' paternal grandmother),
  + Anchises (Trojan nobleman, Aphrodite's lover, Aineias' father),
  + Odysseus (hero of the Odyssey and the Trojan War)

There are 310 total "deities."

Note: When you enter the names of "deities," please use the same spelling as in the Pedigree Spreadsheet (e.g., Heracles instead of Hercules). Unfortunately, the author is not sufficiently competent to make the program understand the nuances of spelling when she hardly understands Greek-Latin translation herself.


## Pedigree Spreadsheet
I made a [Greek deities pedigree Excel spreadsheet](https://github.com/yyu1230/High-School/blob/main/greek_deities_genetic_risks/greek_deities_pedigree.xlsx) based on [Zaffron Steam's YouTube video](https://youtu.be/XWyH1YhO9dY) (see [References](https://github.com/yyu1230/High-School/tree/main/greek_deities_genetic_risks#references)) and Wikipedia/Britannica where Zaffron Steam's record is incomplete. The spreadsheet details
- "deities" in the family tree
- their biological parents (identical entries if born parthenogenetically)
- their gender
- their personification/role(s)
- possible controversies
- additional notes


## Python Program
- The [program](https://github.com/yyu1230/High-School/blob/main/greek_deities_genetic_risks/greek_deities_genetic_risks.py) is written in [Python](https://www.python.org/) (specifically, Python 3), so you may have to download it before the program can run successfully. Alternatively, you can find an online compiler/interpreter.
- The program imports the [xlrd module](https://xlrd.readthedocs.io/en/latest/) to read Excel files, so you may have to install it on your machine before the program can run successfully. Alternatively, you can find an online compiler/interpreter that supports xlrd.


## Additional Comments
- As I designed the algorithm, it occurred to me to question whether these probabilities could be adjusted to become metrics for the extent of inbreeding within a population. When I searched online, I found that the "coefficient of relationship" measures just that. Perhaps it would be interesting to include this indicator in future expansions of the project (if any), as it provides insights into which individuals in the family tree are most affected by the incestuous practice.
- Another potential update in future expansions (if any) could be to calculate "how much" of each "primor" is in the pedigree (i.e., relative fitness but across all generations since gods don't die; being another deity's parent +1/2, parthenogenetic double parent +1, grandparent +1/4, etc.). This information could be useful in calculating the coefficient of relationship for each "deity" as well as predicting the future gene pool. Plus, wouldn't it be fascinating to find out which "deities" are the most reproductively successful?
- An additional potential update (yep, I continue to think of weird stuff as I proofread what I wrote) could be to allow users to enter probabilities instead of definite genotypes for the "primors." In fact, this is extremely easy to do and could be useful for other potential updates, but the author is just too lazy/busy at the moment :P
- Just noticed that the primordial god Eros, the personification of love and desire, is the only "primor" to never reproduce. How ironic!


## Limitations
- Mutations are not considered because the author of this project is not sufficiently adept in biology to fully understand how, why, when, or how likely mutations occur.
- Pleiotropy, polygenetic inheritance, epigenetic inheritance, linked genes, or sex-linked genetic illnesses are not considered because their added complexity mentally overwhelms the already-exhausted author.
- This project is heavily based on [Zaffron Steam's YouTube video on Hesiod's Theogony](https://youtu.be/XWyH1YhO9dY) and Wikipedia content on Greek mythology, neither of which is a typical scholarly source. Additionally, even within a specific translation of Hesiod's Theogony, there exist errors (made by Hesiod), such as when he named 51 Nereids despite claiming earlier that there are only 50, and when he attributed the origin of the Moirai to different parents in different parts of the book. Any mistake made by any one of Hesiod, his translator, Zaffron Steam, Wikipedia, or the author of this project could result in inaccuracies in the program results. ~~But this is pseudo-history/science anyway.~~
- There are monsters in the family tree... Perhaps it would be interesting to investigate which arrangement(s) of genetic illnesses would provide the closest results to these anomalies. However, the author is too preoccupied with other urgent/important matters such as college applications to further delve into the matter. So this will be left as an exercise for the reader :P


## References
- Powell, B. B. (2017). The Poems of Hesiod: Theogony, Works and Days, and The Shield of Herakles (1st ed.). University of California Press. http://www.jstor.org/stable/10.1525/j.ctv1xxt93
- Zaffron Steam. https://www.youtube.com/channel/UCMSRDiMHGx-L. (2020, August 18). Hesiod’s Theogony - The Greek God Family Tree (partially) Animated \[Video]. YouTube. https://youtu.be/XWyH1YhO9dY


## Acknowledgements
- First and foremost, I would like to thank my Capstone Greek and Roman History instructor Mr. Westbay for providing me with vital resources such as the digital copy of the Theogony, for referring me to Zaffron Steam's exhaustive lecture on the deity family tree, and for his enlightening lectures on Greek mythologies. His emotional support for my quirky proposal was also invaluable in my research process.
- I would also like to thank my Honors Biology instructor Mr. Lotus for his exceptional lectures on biological inheritance which laid the foundation for my research. In the past, he had also encouraged me to combine my interests in mathematics and computer science with biology, which is exactly what I did in this project.
- I would like to thank the security guard of our local library who provided me with a face mask when I forgot to bring one. He had done so not out of professional or moral obligation but out of kindness and concern. Without his help, I would not have been able to enter the library and thus would not have had as peaceful a working environment, which could impact the quality of this work.
- I would like to thank my parents for not committing filicide when they learned that their daughter had spent an entire weekend studying the sexual encounters of Greek mythological figures instead of working on her college application essays as she should. Ultimately, it had been their magnanimity that enabled me to complete this project.
- Finally, I would like to thank you, the reader, for not reporting me when it became apparent that I, an underage teenager, have accessed content that is possibly classified as adult-only since it concerns the incestuous sexual relationships of people and gods. Additionally, as an Animalia Chordata Mammalia Primates Haplorhini Simiiformes Hominidae Homininae Hominini Homo Sapien (i.e., human being), I apologize for any mistakes I may have made and of which I am not currently aware. In the event that you notice any such errors, please let me know via the contact details shared on my profile.


********************************************************************************


Let's start!


''')




### INITIALIZATION

import xlrd

path = 'greek_deities_pedigree.xls'
book = xlrd.open_workbook(path)
sheet = book.sheet_by_index(0)

pedigree = {}; deities = []
# pedigree{} - deity: [parent1, parent2, nn, nd, dd]

for i in range (310):
    deity = sheet.cell_value(i+2, 1)
    parent1 = sheet.cell_value(i+2, 2)
    parent2 = sheet.cell_value(i+2, 3)
    pedigree[deity] = [parent1, parent2, -1, -1, -1]
    deities.append(deity)




### PRIMORS - USER INPUT

primors = ['Chaos', 'Gaea', 'Tartaros', 'Eros', 'Cadmus', 'Alkmene', 'Iasion',
          'Tithonus', 'Jason', 'Asopus', 'Metope\'s mother', 'Endeïs',
          'Anchises', 'Odysseus']

str1 = 'Designate the genotype of ' #deity
str2 = ' (nn, nd, dd): '

for deity in primors:
    allele = input(str1+deity+str2)
    if allele == 'nn':
        pedigree[deity][2], pedigree[deity][3], pedigree[deity][4] = 1, 0, 0
    elif allele == 'nd':
        pedigree[deity][2], pedigree[deity][3], pedigree[deity][4] = 0, 1, 0
    elif allele == 'dd':
        pedigree[deity][2], pedigree[deity][3], pedigree[deity][4] = 0, 0, 1
    else:
        print('Invalid input. Treated as "nn."')
        pedigree[deity][2], pedigree[deity][3], pedigree[deity][4] = 1, 0, 0
    deities.remove(deity)

# Current Values
# primors: all "primors," list['string']
# deities: all "posterities," list['string']
# primors + deities: all "deities," list['string']




### PROBABILITY CALCULATION FUNCTION & IMPLEMENTATION

def calculate(deity):
    parent1, parent2 = pedigree[deity][0], pedigree[deity][1]
    nn1, nn2 = pedigree[parent1][2], pedigree[parent2][2]
    nd1, nd2 = pedigree[parent1][3], pedigree[parent2][3]
    dd1, dd2 = pedigree[parent1][4], pedigree[parent2][4]
    pedigree[deity][2] = nn1*nn2 + nn1*nd2/2 + nd1*nn2/2 + nd1*nd2/4
    pedigree[deity][3] = nn1*nd2/2 + nn1*dd2 + nd1*nn2/2 + nd1*nd2/2 \
                         + nd1*dd2/2 + dd1*nn2 + dd1*nd2/2
    pedigree[deity][4] = nd1*nd2/4 + nd1*dd2/2 + dd1*nd2/2 + dd1*dd2

for deity in deities: calculate(deity)




### PROVIDE ANSWERS - USER INPUT AND PRINT

str1 = 'The probability that ' #deity
str2 = ' has alleles "nn" is ' #pedigree[deity][2]
str3 = '\nThe probability that ' #deity
str4 = ' has alleles "nd" is ' #pedigree[deity][3]
str5 = '\nThe probability that ' #deity
str6 = ' has alleles "dd" is ' #pedigree[deity][4]

while True:
    try:
        deity = input('''
Which god/goddess\' genetic composition would you like to check?
Please refer to https://github.com/yyu1230/High-School/blob/main/greek_deities_
genetic_risks/greek_deities_pedigree.xlsx for a list of deities and spelling.
Please enter "quit" if you want to quit the program.
''')
        if deity == 'quit': break

        print(str1+deity+str2+str(pedigree[deity][2])+str3+deity+str4\
              +str(pedigree[deity][3])+str5+deity+str6+str(pedigree[deity][4]))
        print('''
What does this mean?
Having alleles "nn" means that
  - the deity *expresses healthy traits* in the genetic character concerned;
  - the deity *passes down a healthy allele* to each of his/her children.
    If the deity's sexual partner also has alleles "nn,"
    then all of their children will be healthy with alleles "nn."
Having alleles "dd" means that
  - the deity *expresses defective traits* in the genetic character concerned;
  - the deity *passes down a defective allele* to each of his/her children.
    If the deity's sexual partner also has alleles "dd,"
    then all of their children will be defective with alleles "dd."
Having alleles "nd" means that
  - the deity *passes down a healthy or defective allele* to each of his/her
    children with equal probability;
  - if the genetic illness in question is *autosomal recessive*, then the deity
    *expresses healthy traits* in the genetic character concerned;
  - if the genetic illness in question is *autosomal dominant*, then the deity
    *expresses defective traits* in the genetic character concerned;
  - if the genetic illness in question is *autosomal codominant*, then the deity
    *expresses both healthy and defective traits* in the genetic character
    concerned (e.g., sickle cell disease);
  - if the genetic illness in question is *autosomal incompletely dominant*,
    then the deity *expresses in-between healthy and defective traits* in the
    genetic character concerned (e.g., Tay-Sachs disease).
''')

    except: print('Invalid input. Please try again.')




### THOUGHTFUL NOTE

print('''

Here comes the much-anticipated thoughtful note advising the reader why they
should not marry their relatives! ;)

Running the program a few times, you may notice that the percentage of defective
alleles in the gene pool does not change over generations of incest -- from
that, it is tempting to conclude that perhaps inbreeding is not so bad after
all!

But wait! Examining the percentage of "dd" genotypes in the population, you will
see that it increases significantly over generations -- this is the primary
reason why inbreeding is bad. Most genetic illnesses are autosomal recessive,
so defective traits are only expressed in individuals with "dd" genotypes, and
children can only have "dd" if both parents have defective alleles -- much more
likely in relatives, who share similar genes, than in unrelated couples.

You may be thinking... "But I don't have any genetic diseases and nor do my
siblings! Does that mean it would be fine for us to marry?"
Nope! Although you don't have any *expressed* genetic defects, you are probably
a carrier of various defective alleles. For relatives, these "hidden defects"
tend to occur in similar places, so when they combine, oh no! Your children may
get genotype "dd" and *express* defects for some genetic characters. However,
for unrelated couples, "hidden defects" tend to occur in different places, so
when their genes combine, offsprings are likely to inherit mostly "nn" or "nd"
genotypes, thus not *expressing* any genetic diseases. Hoorah!

Moral of the story? Don't marry your relatives! In fact, you probably cannot
legally do that anyway!


''')



