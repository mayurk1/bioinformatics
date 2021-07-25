#! /usr/bin/env python

import argparse
import sys
import os
import re
import subprocess
import time

import pandas as pd

"""
Names of all the species:
Above:
Homo Sapiens
Monodelphis domestica
Gallus gallus
Anas platyrhynchos
Ornithorhynchus anatinus
Anolis carolinensis
Xenopus laevis
Xenopus tropicalis
Nanorana parkeri

Fish:
Danio rerio
Takifugu rubripes
Oryzias latipes
Lepisosteus oculatus

Below:
Rhincodon typus
Callorhinchus milii
Latimeria chalumnae
Branchiostoma belcheri
Ciona intestinalis
Strongylocentrotus purpuratus
Drosophila melanogaster
Drosophila grimshawi
Nasonia vitripennis
Trachymyrmex cornetzi
Anopheles gambiae
Apis mellifera
Pogonomyrmex barbatus
Caenorhabditis elegans
Aplysia californica
Nematostella vectensis
Hydra vulgaris


1, use e-cutoff=0.05; ranking the result based on the score.
2, find the homologs from fish species (pick up the top one from each fish species), get average score
3, find the homologs from all other species (pick up the top one)
4, if majority of species (higher than fish) are found, then keep and get average score (Hscore) for “higher than fish” homologs; otherwise put it aside;
5, if majority of species (lower than fish) are found, then keep and get average score (Lscore) for “lower than fish” homologs; otherwise put it aside;
6, if the average score of fish homologs “some number” less than average score of “lower than fish” species, then keep. This “some number” should be a number = (Hscore – Lscore)/4,
"""


def averageFish()
	summation = 0.0
	values = 0.0
	if highDr > 0.0:
		summation += highDr
		values += 1
	if highTrr > 0.0:
		summation += highTrr
		values += 1
	if highOl > 0.0:
		summation += highOl
		values += 1
	if highLo > 0.0:
		summation += highLo
		values += 1	

	average = summation/values

	return average

#Below Identifiers
def isHomo(name):
    if name in ("Homo sapiens")
        return 



def isBelow(name):
	if name in ("Callorhinchus milii", "Apis mellifer", 
				"Aplysia californica", "Branchiostoma belcheri", 
				"Caenorhabditis elegans", "Ciona intestinalis", 
				"Drosophila grimshawi", "Drosophila melanogaster",
				"Hydra vulgaris", "Latimeria chalumnae", 
				"Nanorana parkeri", "Nasonia vitripennis", 
				"Nematostella vectensis", "Pogonomyrmex barbatus", 
				"Rhincodon typus", "Strongylocentrotus purpuratus", 
				"Trachymyrmex cornetzi"):
		return True					
	else:
		return False

def blastp(sequence):
	with open("queryCurrent.fa", "w+") as q:
		q.write(str(sequence))	
	script = 'blastp -query queryCurrent.fa -db CombinedDB -out blastResult -evalue .05 -outfmt \"10 bitscore sseqid sscinames\" -num_threads 8'
	s = subprocess.call(script, shell=True)

def iterate():
	high = blasted.at[0 , 'score']
	#Above:
	Homo_Sapiens = high
	Monodelphis_domestica = 0.0
	Gallus_gallus = 0.0
	Anas_platyrhynchos = 0.0
	Ornithorhynchus_anatinus = 0.0
	Anolis_carolinensis = 0.0
	Xenopus_laevis = 0.0
	Xenopus_tropicalis = 0.0
	Nanorana_parkeri = 0.0

	#Fish
	Danio_rerio = 0.0
	Takifugu_rubripes_rubripes = 0.0
	Oryzias_latipes = 0.0
	Lepisosteus_oculatus = 0.0

	#Below
	Rhincodon_typus = 0.0
	Callorhinchus_milii = 0.0
	Latimeria_chalumnae = 0.0
	Branchiostoma_belcheri = 0.0
	Ciona_intestinalis = 0.0
	Strongylocentrotus_purpuratus = 0.0
	Drosophila_melanogaster = 0.0
	Drosophila_grimshawi = 0.0
	Nasonia_vitripennis = 0.0
	Trachymyrmex_cornetzi = 0.0
	Anopheles_gambiae = 0.0
	Apis_mellifera = 0.0
	Pogonomyrmex_barbatus = 0.0
	Caenorhabditis_elegans = 0.0
	Aplysia_californica = 0.0
	Nematostella_vectensis = 0.0
	Hydra_vulgaris = 0.0


    #Loop through BlastResult and pick up the highest species 
	x = 1
	while x < (blasted.shape[0]):	
		#Above organisms
		if blast.at[x, 'name'] == "Monodelphis domestica" and blasted.at[x, 'score'] > Monodelphis_domestica:
			Monodelphis_domestica = blasted.at[x, 'score']

		if blast.at[x, 'name'] == "Gallus gallus" and blasted.at[x, 'score'] > Gallus_gallus:
			Gallus_gallus = blasted.at[x, 'score']

		if blast.at[x, 'name'] == "Anas platyrhynchos" and blasted.at[x, 'score'] > Anas_platyrhynchos:
			Anas_platyrhynchos = blasted.at[x, 'score']
			
		if blast.at[x, 'name'] == "Ornithorhynchus anatinus" and blasted.at[x, 'score'] > Ornithorhynchus_anatinus:
			Ornithorhynchus_anatinus = blasted.at[x, 'score']	

		if blast.at[x, 'name'] == "Anolis carolinensis" and blasted.at[x, 'score'] > Anolis_carolinensis:
			Anolis_carolinensis = blasted.at[x, 'score']

		if blast.at[x, 'name'] == "Xenopus laevis" and blasted.at[x, 'score'] > Xenopus_laevis:
			Xenopus_laevis = blasted.at[x, 'score']

		if blast.at[x, 'name'] == "Xenopus tropicalis" and blasted.at[x, 'score'] > Xenopus_tropicalis:
			Xenopus_tropicalis = blasted.at[x, 'score']
			
		if blast.at[x, 'name'] == "Nanorana parkeri" and blasted.at[x, 'score'] > Nanorana_parkeri:
			Nanorana_parkeri = blasted.at[x, 'score']


		#Fish
		if blast.at[x, 'name'] == "Danio rerio" and blasted.at[x, 'score'] > Danio_rerio:
			Danio_rerio = blasted.at[x, 'score']

		if blast.at[x, 'name'] == "Takifugu rubripes" and blasted.at[x, 'score'] > Takifugu_rubripes_rubripes:
			Takifugu_rubripes_rubripes = blasted.at[x, 'score']

		if blast.at[x, 'name'] == "Oryzias latipes" and blasted.at[x, 'score'] > Oryzias_latipes:
			Oryzias_latipes = blasted.at[x, 'score']
			
		if blast.at[x, 'name'] == "Lepisosteus oculatus" and blasted.at[x, 'score'] > Lepisosteus_oculatus:
			Lepisosteus_oculatus = blasted.at[x, 'score']	


		#Below organisms
		if blast.at[x, 'name'] == "Rhincodon typus" and blasted.at[x, 'score'] > Rhincodon_typus:
			Rhincodon_typus = blasted.at[x, 'score']

		if blast.at[x, 'name'] == "Callorhinchus milii" and blasted.at[x, 'score'] > Callorhinchus_milii:
			Callorhinchus_milii = blasted.at[x, 'score']

		if blast.at[x, 'name'] == "Latimeria chalumnae" and blasted.at[x, 'score'] > Latimeria_chalumnae:
			Latimeria_chalumnae = blasted.at[x, 'score']
			
		if blast.at[x, 'name'] == "Branchiostoma belcheri" and blasted.at[x, 'score'] > Branchiostoma_belcheri:
			Branchiostoma_belcheri = blasted.at[x, 'score']	

		if blast.at[x, 'name'] == "Anolis carolinensis" and blasted.at[x, 'score'] > Anolis_carolinensis:
			Anolis_carolinensis = blasted.at[x, 'score']

		if blast.at[x, 'name'] == "Ciona intestinalis" and blasted.at[x, 'score'] > Ciona_intestinalis:
			Ciona_intestinalis = blasted.at[x, 'score']

		if blast.at[x, 'name'] == "Strongylocentrotus purpuratus" and blasted.at[x, 'score'] > Strongylocentrotus_purpuratus:
			Strongylocentrotus_purpuratus = blasted.at[x, 'score']
			
		if blast.at[x, 'name'] == "Drosophila melanogaster" and blasted.at[x, 'score'] > Drosophila_melanogaster:
			Drosophila_melanogaster = blasted.at[x, 'score']				

		if blast.at[x, 'name'] == "Drosophila grimshawi" and blasted.at[x, 'score'] > Drosophila_grimshawi:
			Drosophila_grimshawi = blasted.at[x, 'score']

		if blast.at[x, 'name'] == "Nasonia vitripennis" and blasted.at[x, 'score'] > Nasonia_vitripennis:
			Nasonia_vitripennis = blasted.at[x, 'score']

		if blast.at[x, 'name'] == "Trachymyrmex cornetzi" and blasted.at[x, 'score'] > Trachymyrmex_cornetzi:
			Trachymyrmex_cornetzi = blasted.at[x, 'score']
			
		if blast.at[x, 'name'] == "Anopheles gambiae" and blasted.at[x, 'score'] > Anopheles_gambiae:
			Anopheles_gambiae = blasted.at[x, 'score']	

		if blast.at[x, 'name'] == "Apis mellifera" and blasted.at[x, 'score'] > Apis_mellifera:
			Apis_mellifera = blasted.at[x, 'score']
			
		if blast.at[x, 'name'] == "Pogonomyrmex barbatus" and blasted.at[x, 'score'] > Pogonomyrmex_barbatus:
			Pogonomyrmex_barbatus = blasted.at[x, 'score']
			
		if blast.at[x, 'name'] == "Caenorhabditis elegans" and blasted.at[x, 'score'] > Caenorhabditis_elegans:
			Caenorhabditis_elegans = blasted.at[x, 'score']
			
		if blast.at[x, 'name'] == "Aplysia californica" and blasted.at[x, 'score'] > Aplysia_californica:
			Aplysia_californica = blasted.at[x, 'score']
			
		if blast.at[x, 'name'] == "Nematostella vectensis" and blasted.at[x, 'score'] > Nematostella_vectensis:
			Nematostella_vectensis = blasted.at[x, 'score']
			
		if blast.at[x, 'name'] == "Hydra vulgaris" and blasted.at[x, 'score'] > Hydra_vulgaris:
			Hydra_vulgaris = blasted.at[x, 'score']						
		
		x+=1	
			
queryNumbers = 1
hitsList = []

#parse fasta sequences using Pandas DataTable
query = pd.read_csv("query.csv", header=None, names=['ref', 'sequence'])

for seq in range(query.shape[0]):
	print ("Analyzing: " + str(query.at[seq, 'ref']))
	blastp(query.at[seq, 'sequence'])
	#Open blastpresult file, formatted as: "10 bitscore sseqid sscinames"
	blasted = pd.read_csv("blastResult", header=None, names=['score', 'ass', 'name'])
	time.sleep(1)
	iterate()
	sys.stdout.write("Analyzed " + str(queryNumbers) + " sequences. \n \n")
	queryNumbers += 1
	sys.stdout.flush()

#Create output file
hits = open('hits', 'w+')	

for item in hitsList:
	hits.write("%s\n" % item)	

hits.close()

