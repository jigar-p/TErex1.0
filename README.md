# TErex1.0 - A tool brought to you by CSE 180's final project 
### By Jenny Lee, Jigar Patel, Lowan Kim, and Arya Kaul


**Objective**
Given an input query, TErex1.0 identifies all the transposable elements within it through
an alignment method that uses the Dfam database.

**Significance**
Transposon annotation is an important tool because of the significance of transposable
elements. Transposons are elements that move, or “jump around,” from one position to
another within the genome, and they’re found abundantly in nearly all prokaryotes and
eukaryotes. Consequently, transposable elements can lead to mutations, and recently,
they’ve found a few transposons in cancer-related genes, indicating disease
development. Because of their ability to “jump around,” transposons drive genomic
evolution and gene regulation by enabling translocation, exon shuffling, and increasing
diversity, among its many effects. Their genetic influence makes transposons important
elements to identify and study.

## Installation
1. Clone the repository wherever you want to install the tools
2. Run the following command to see if everything has been installed correctly!

```
python main.py --tester
```

Feel free to explore what our options do by running:

```
python main.py -h
```

## Dependencies
Here's a list of dependencies that TErex requires to run!

1. Python2.7 


2. Python package Numpy


3. nhmmer through hmmer3.1


4. perl

If you would like to download the whole Dfam database locally, you may use the link found here:
```
http://dfam.org/web_download/Current_Release/Dfam.hmm.gz
```
