# Simplified sample code of the tag cleanning process for the CiteULike dataset based on the work:

# Dong, H., Wang, W., & Frans, C. (2017).
# Deriving dynamic knowledge from academic social tagging data: a novel research direction.
# iConference 2017 Proceedings.

# the program will generate a pickle file, saving a dictionary type variable,
# where each key is a raw tag and each value is the standard form of the raw tag in the corresponding key.

# author: Hang Dong
# last edit: 16 July 2019

from nltk.metrics import *
from LeeLemmatizer import *
#from lee_lemmatizer_master import LeeLemmatizer
import pickle
import os
import sys
import time

# test: read the dtag_std
def test():
    with open('dtag_std.pkl', 'rb') as data_f:
        dtag_std=pickle.load(data_f)
        
    #for tag,std in dtag_std.items():
    #    if tag != std:
    #        print(tag,std)
    dict2File(dtag_std)
    
def dict2File(dtag_std):
    dstd_tags = {}
    for tag,std in dtag_std.items():
        dstd_tags[std] = (dstd_tags.get(std,'') + ' ' + tag).strip()
        
    with open(r'standard_tag_groups.txt', 'w', encoding="utf-8") as f_output:
        for std,tags in dstd_tags.items():
            f_output.write(std + ':' + tags + '\n')
        
start_time = time.time()            
# step0 : check whether the pkl file exists
if os.path.exists('dtag_std.pkl'):
    print('step0 : the pickle file, dtag_std.pkl, already exists')
    test()
    sys.exit()
else:
    print('step0 : start program')
    
# step 0.5: read dist labels
with open(r'tags.dat', encoding='latin-1') as f_content:
    tags = f_content.readlines()

tags = [x.strip() for x in tags]
##with open(r'citeulike_cleaned_tag.txt', encoding='latin-1') as f_content:
##    labelsets = f_content.readlines()
##labelsets = [x.strip() for x in labelsets]
##
##dtag_freq={}
###test_number=200
###n=0
##for labelset in labelsets:
###    if n>test_number:
###        break
##    tags = labelset.split(' ')
##    for tag in tags:
##        if dtag_freq.get(tag,None) != None:
##            dtag_freq[tag] = dtag_freq[tag] + 1
##        else:
##            dtag_freq[tag] = 0
###    n=n+1
##    
##print(len(dtag_freq)) #46390

dtag_std={} # a dictionary mapping an original tag to its standard form
            
# step1 : Specific character handling
for tag in tags:
    # dealing with colons (:)
    std = tag[tag.find(':')+1:]
    # dealing with double minuses (--)
    if tag.find('--') != -1:
        std = tag[tag.find('--')+2:]
    # dealing with minuses (-)
    std = std.replace('-','_')
    dtag_std[tag] = std

print('step1 : Specific character handling done' + '\n')

# step2.1 : Multiword tag group extraction
count = 0
for tag,std in dtag_std.items():
    count = count + 1
    if count % 1000 == 0:
        print(str(count), 'out of', str(len(dtag_std)))
    if std.find('_') != -1 and len(std) >= 8:
        # it is a multiword tag and it has a certain length,
        # we calculate the Levenshtain distance of the tag to all other *multiword* tags,
        # if distance < threshold, then we set the tag as the standard tag of the matched tags.

        # match other *multiword* tags to the current multiword tag:
        # all matched tags will be standardised as the matching tag (the first occurrence of this tag in the list).
        for tag_,std_ in dtag_std.items():
            if std_.find('_') != -1 and std != std_ and len(std_)>=5:
                if std[0] == std_[0]: 
                    dist = edit_distance(std,std_)
                    th = 1 if std[-2] == '_' else 2
                    # if the secend last char is '_', then set the dist threshold as 1 (exact matching),
                    # this will prevent matching 'vitamin_e' to 'vitamin_d'.
                    if dist<th:
                        # matched [TODO: then set the std as the one having higher frequency].
                        print(tag,std,tag_,std_)
                        dtag_std[tag_] = std
                        #if dtag_freq[tag]>=dtag_freq[tag_]:
                        #    dtag_std[tag_] = std
                        #else:
                        #    dtag_std[tag_] = std_
                        #    dtag_std[tag] = std_

print('step2.1.1 : Multiword-multiword mapping done') # now the multiword forms are standardised
print("--- The program took %s seconds so far ---" % (time.time() - start_time) + '\n')

count = 0
for tag,std in dtag_std.items():
    count = count + 1
    if count % 1000 == 0:
        print(str(count), 'out of', str(len(dtag_std)))
    if std.find('_') != -1 and len(std) >= 8:
        # it is a multiword tag and it has a certain length,
        # we calculate the Levenshtain distance of the tag to all other *single* tags,
        # if distance < threshold, then we set the tag as the standard tag of the matched tags.

        # match other *single tags* to the current multiword tag
        for tag_,std_ in dtag_std.items():
            if std_.find('_') == -1 and std != std_ and len(std_)>=5:
                if std[0] == std_[0]:
                    dist = edit_distance(std.replace('_',''),std_) #compare to the one without '_'.
                    th = 1 if std[-2] == '_' else 2
                    # if the secend last char is '_', then set the dist threshold as 1 (exact matching),
                    # this will prevent matching 'objective_c' to 'objective'.
                    if dist<th:
                        print(tag,std,tag_,std_)
                        dtag_std[tag_] = std
                
print('step2.1.1 : Multiword-single-tag mapping done')
print('step2.1 : Multiword tag group extraction done')
print("--- The program took %s seconds so far ---" % (time.time() - start_time) + '\n')

# step2.2 : Single tag group extraction
lmtsr = LeeLemmatizer()
for tag,std in dtag_std.items():
    if std.find('_') == -1:
        std_lemma = lmtsr.lemmatize(std)
        if std != std_lemma:
            print(tag,std,std_lemma)
            dtag_std[tag] = std_lemma

print('step2.2 : Single tag group extraction done')
print("--- The program took %s seconds so far ---" % (time.time() - start_time) + '\n')

# step3 : Tag selection using selected metrics
#pass

# step4 : Tag selection by languages
#pass

# store the dtag_std
with open('dtag_std.pkl', 'ab') as data_f:
    pickle.dump(dtag_std, data_f)

print('the raw-standard dictionary stored to dtag_std.pkl')
print("--- The whole program took %s seconds ---" % (time.time() - start_time) + '\n')
