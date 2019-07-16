# Data Cleaning workflow for social tags

The program provides a simplied implementation of data cleaning workflow for noisy user-generated social tagging data, such as Bibsonomy, CiteULike, MovieLens, etc.

The repository also contains the supplementary material for the paper:
* Deriving Dynamic Knowledge from Academic Social Tagging Data: A Novel Research Direction, iConference 2017 ([paper](https://www.ideals.illinois.edu/bitstream/handle/2142/96693/3.13_170_Dong-Deriving%20Dynamic%20Knowledge%20from%20Academic%20Social%20Tagging%20Data.pdf?sequence=1&isAllowed=y), [poster](http://cgi.csc.liv.ac.uk/~hang/ppt/iConference%20Poster%20pptx%20Deriving%20Dynamic%20Knowledge%20from%20Academic%20Social%20Tagging%20Data.pdf)).

The [Lee-Lemmatizer](https://github.com/qingxiang-jia/lee-lemmatizer), contained in the repository, is applied for lemmatisation of single-word tags.

The supplementary material contains the [readme files (we recommend you to read this first)](https://github.com/acadTags/tag-data-cleaning/blob/master/readme%20supplementary%20files.pdf), the extracted multiword tag groups ([Material 2](https://github.com/acadTags/tag-data-cleaning/blob/master/Material%202_Full%20multiword%20tag%20groups%20after%20step%204.txt)) and single-word tag groups ([Material 3](https://github.com/acadTags/tag-data-cleaning/blob/master/Material%203_Full_single%20tag%20groups%20after%20step%204.txt)) from the Bibsonomy data, the specification of treatment of special characters ([Material 1](https://github.com/acadTags/tag-data-cleaning/blob/master/Material%201_Table%20for%20handling%20specific%20characters.pdf)). For details, see the description file.

A simplified code implementated in Python is also provided, [```tag-cleaning.py```](https://github.com/acadTags/tag-data-cleaning/blob/master/tag-cleanning.py), which applies the data cleaning steps for the CiteULike-a dataset; the code does not implement all steps described in the paper, but most of the ideas are retained. The program inputs the whole user-generated tag set from the CiteULike-a dataset and output a list of tag groups which standard tags.

# Acknowledgement
* Thanks to the [Lee-Lemmatizer](https://github.com/qingxiang-jia/lee-lemmatizer) by Qingxiang Jia, under the license of GNU GPL v3, license information in [lee-lemmatizer google code repository](https://code.google.com/archive/p/lee-lemmatizer/).
* The CiteULike-a dataset file, [```tag.dat```](https://github.com/acadTags/tag-data-cleaning/blob/master/tags.dat) is from *Collaborative topic regression with social regularization for tag recommendation* (Wang, Chen, and Li, 2013, [link](https://sites.cs.ucsb.edu/~binyichen/IJCAI13-400.pdf)).
