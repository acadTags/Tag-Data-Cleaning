# Data Cleaning workflow for social tags

The program provides a simplied implementation of data cleaning workflow for noisy user-generated social tagging data, such as Bibsonomy, CiteULike, MovieLens, etc.

The repository also contains the supplementary material for the paper:
* Deriving Dynamic Knowledge from Academic Social Tagging Data: A Novel Research Direction, iConference 2017 ([paper](https://www.ideals.illinois.edu/bitstream/handle/2142/96693/3.13_170_Dong-Deriving%20Dynamic%20Knowledge%20from%20Academic%20Social%20Tagging%20Data.pdf?sequence=1&isAllowed=y), [poster](http://cgi.csc.liv.ac.uk/~hang/ppt/iConference%20Poster%20pptx%20Deriving%20Dynamic%20Knowledge%20from%20Academic%20Social%20Tagging%20Data.pdf)).

The [Lee-Lemmatizer](https://github.com/qingxiang-jia/lee-lemmatizer), contained in the repository, is applied for lemmatisation of single-word tags.

The supplementary material contains the extracted multiword and single-word tag groups from the Bibsonomy data, the specification of treatment of special characters and further explanation on the data format. For details, see the description file.

A simplified code implementated in Python is also provided, which applies the data cleaning steps for the CiteULike-a dataset; the code does not implement all steps described in the paper, but most of the ideas are retained.

# Acknowledgement
* Thanks to the Lee-Lemmatizer, under the license of GNU GPL v3, license information in [lee-lemmatizer google code repository](https://code.google.com/archive/p/lee-lemmatizer/).