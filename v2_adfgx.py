import os
import io
import numpy as np
from itertools import permutations


"""
Steps for cracking ADFGX:
-  Load data by column
-  Create data storage allowing for movement of column ordering with indexing across rows
-  Turn the pairs of letters into single letters:
	-  if the number of columns is even, every column is made of the same "kind" of letter (top/side)
	-  if the number of columns is odd, every other row in each column is made of the same "kind" of letter
		-  need to separate but we don't know if the letter pairings are side-top or top-side, so we need to check both
-  Calculate the index of coincidence for the single letters; store as {columnOrder, IC}
-  Compare ICs to IC of known English (EIC - CIC_i == 0 if CIC_i ~ English) --> sort from least to greatest
"""

# Function for separating rows/cols into letter pairs
def makePairs(permMatrix, numCols, numRows ):
	"Create pairs of top/side letters and return pairs separated by columns?"

	pairs = ''
	# Go through every column and row, collecting each columns' letters row-by-row to form a single string
	for j in range(0,numRows):
		for i in range(0, numCols):
			pairs = pairs + permMatrix[i][j]

	# Separate letters in pairs string by 2s with spaces separating the pairs
	pairs = " ".join(pairs[i:i+2] for i in range(0, len(pairs), 2))

	# return the single letters generated by substitute()
	return substitute(pairs);


# Function for turning pairs of letters into single letters 
def substitute(pairs):
	"Replace pairs of letters with single letters and remove spaces"

	pairs = pairs.replace('AA', 'A')
	pairs = pairs.replace('AD', 'B')
	pairs = pairs.replace('AF', 'C')
	pairs = pairs.replace('AG', 'D')
	pairs = pairs.replace('AX', 'E')
	pairs = pairs.replace('DA', 'F')
	pairs = pairs.replace('DD', 'G')
	pairs = pairs.replace('DF', 'H')
	pairs = pairs.replace('DG', 'I')
	pairs = pairs.replace('DX', 'K')
	pairs = pairs.replace('FA', 'L')
	pairs = pairs.replace('FD', 'M')
	pairs = pairs.replace('FF', 'N')
	pairs = pairs.replace('FG', 'O')
	pairs = pairs.replace('FX', 'P')
	pairs = pairs.replace('GA', 'Q')
	pairs = pairs.replace('GD', 'R')
	pairs = pairs.replace('GF', 'S')
	pairs = pairs.replace('GG', 'T')
	pairs = pairs.replace('GX', 'U')
	pairs = pairs.replace('XA', 'V')
	pairs = pairs.replace('XD', 'W')
	pairs = pairs.replace('XF', 'X')
	pairs = pairs.replace('XG', 'Y')
	pairs = pairs.replace('XX', 'Z')
	pairs = pairs.replace(' ', '')

	return pairs;	


# Function for calculating IC
def indexOfCoincidence(letters):
	"Calculate the index of coincidence for the given letters"

	# IC = sum(Ni(Ni-1))/N(N-1)
	N = len(letters)
	alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	sumFreq = 0

	# for every possible letter in the alphabet, count the number of occurrences in the given string 
	# and calculate Ni(Ni-1), where Ni is the frequency of letter i in the string. Add all Ni(Ni-1) values for i=1:26
	for letter in alphabet:
		freq = letters.count(letter)
		sumFreq = sumFreq + freq*(freq-1)

	# return the numerator divided by the total number of letters N times N-1
	return sumFreq/float(N*(N-1));


""" 
Main function 
"""
  
# input ADFGX ciphertext
str = "XDXAGGXGXXGGFAXGXFDAAAAGDAXAXDFGDFFFGDXGFGAXXAADXFGGGGXXADDGXFAFDFXDGFXAGGGGADAAXXGFXDDGXDGFDDAGXDDGXXXGXDDFAFFDXFDGADAFAGADGDDAAGDGDGDGAGAGDDXGGGDGGGAGXFXAADFAADGAAXADDDFGFDFDXDXAAFDADFDGGGXGGGXGXXFGXADFAGDGAFGFADDGXGADGFADDDDDDDAFAFFADGDAAFGFXAAFADADGAFGXFAFDDAADGDFGAXGDAAFAGXXDFDGXDGAGGAADFAADGXGAGXFFXDFGAFGAGAXXFXADGAGAGXDAFFDXFFAXFADXAAGADAAFDADDFXDDGDAGGAFXXFAGFXAFGXFXFAXDDXDAGDXDDAAAGXAXGXFADDFAAXAGADFAGADDAGAGAGADFADDDADGFXDDGXXAGAXFAFDFAFAXFFAADAGAGDXDDXGXDAAADXAGFADDFXDXFGDGGADGAGDXAXDDGGAXDGDDFAXDFAFXDDAXGXGGDXFAFAADGXAADFGDAGFGGXGDGDDXDDGDDFXDGDDAAAFAAGDAAGFFXGXAADAFGGXFAFDADGDADGXGAFADDGFAFDAAAAXGADAFDDXAFAXGDDADGGXAXGFAAAFDADAGGAAGGFGXADGDAFAAGDAGAGXGADFFAAGDAGXFFGXAFDAGGFDGXDADDDDGGFAFAAGAXADGXFXAXXDGFAGGXADFFADAGFAGAGDDAXFGADFAAFFFGDGGDFAGAAAADFAAXGXXFFDGXDFFGGAFXFADGDADFDAGGGADFFAAGGXAGFDXDGAFDDADAFGFDGGFXGAAAXFADDXGGGDGXDFDDGXGDDGFFADDFGAADDXDGGDFDGGDXDFAAFXDFAAGXAAFFAADAXAGXDAXDAXAAGXDGDDGFDDDAFGDAGAFGGXFAGDFFDFAGFAGFGXGGGFDXGADXFGGDADADGFADDGAAGAFXFAGADDFGGXGXDAFXDAFDGAAXAXFGAAGXGFGGAXGDDAFGGDFFDDXFADAAGDFFFAFGDXDXFAXAADAFFDDGAXDGFGDAGXXDGGDXFDGAFXXXDXAGFXDDDAXGGADFFDAAAXGFADDDGXFFXFDAFAFGDADGFGXGDFDDAFDDDFGAXGDAGGXGXGFAAGXGXFXAAFDAGGXFDFGAGGGFFAFFDGFAAGXDDGFFAADGXAXDAFDDFDDGXFDDAGXDXDAFXDFADFDDAAGGFDAFXGAGADXGDGGAFXAGADDGFFXDADXFAADGFDAFADDFGDFFAFDGDGXFDADXGFAGDDDXDGAAAFDAGAADAGXGDDAFFAAGXDDDGGGGDDDFAGGGXXXGXFDAADFDAADAGGGFGFXXXGDGGFGGDFXDAGAFGGXGAFGGFFDXFXGAGAGXAFFAFAAXGFGXAADAFDGAGDGDDAGXDXGGADAADAGXDGGFFDGGGFDXADGAADAXGFFGXFFDDGDFDFFAGXGFDDFGGXADDDDXDGAGADFDAGFFAADXAADADDDDGGFGFXDDFDAFDAFDFGAXFXGDXDXADDGXFXFDAGGAGDDDGDDDAXADAGDXGXGXFDXFGDGXGAGGFDGDAAGGAXGAGXGAFFGADDADDXXFDDGAAGGDFAFDFADGAAFAXXFGGAXDFGFDAAGDDAXDDGFFXDFGGDGAGXGXGFAXAXXAAXADAFGGGGAAXAGGADGAGGADAFDXGDFGDGDFGFGGGGAGDXADXGFDXXDDDAFDAGDAXXDAADAFAAADDGGGDGFAADAGXXGDXGADAFXDFDGGXAFGAGAGAGAGXAXFADFDXDFFAGDGXGXDADXGXXFFDDDAXDXGDGXFDGFAFDDGAFDGXFXFGAAGAFXXXGXFDAXFFFXGAFGDFGGDXADGAGXGXXGFXADGDADFGGXFDFXGGGDGDGDFDDXAFGXXXGDDFGGDFAAAXGDGXGAGXFGDAGFGFXDAAFDDGFFXDGXDFFDGXFFADGGFFXDXDGGGXGDADXAGGDFFGADXGADAFGAGFAGGGGDGDAAXFFGADGFAAAFXGXFAGGAADGGXDAFDFXDDGXGFAXFXFADXGXFXGDGDGAAAAFAGDGGFDAGGGDDFGXFAFDAXAAXXGDDAADFAGXDGFDDXDGGDGAFAFAXXADFXADGXGXFXXAAGDXFDADFGADAADGGAFGGGDXDXAAFDGAADAAAXGDADDDADGAGDFXFDFAADAGFXAADDGDFFFDDFFAGFFXGAXFDDAGAAFGDAGGGADDGDFFDDDAADAGGAAAADDAFGGDFXXXDXFGAAGXGAADDAFXGAGDDAAGGFGGXFDAAAGXDAFAFAGDGFFAADGDFDXDAAGGDAAAAAGGADXDGDGXXFGDGAFXAAGADXFXXDFDFAXAFXGAAGFFFFFDGXFAAXAGAXADADAXDDADGADDDDGGDAGFAXAXFGGAGXXGADGXAAGAGXDXFADGGAFDGAGDGXXGXDGXAXDADDDGDXAAXFGAFDFFXXGDDDGDXAFAGDGDFXGAGAGDDXXF"

# Set numCols to the desired key length
numCols = 9  # number of columns = keylength

numLetters = len(str)  # total number of letters in the ciphertext
numRows = numLetters/numCols  # number of rows in each column

# Create data storage lists (make sure to have numCols letters in the transpoMatrix initialization)
transpoMatrix = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
for i in range(numCols) :
	transpoMatrix[i] = str[i*numRows : (i+1)*numRows]


# get all possible permutation orderings
permOrders = list(permutations(range(0,numCols)))

# for each permutation of rows, calculate the IC for the pairs of letters as single letters
# Note: All letters are used by makePairs(), so this might take a while to run
candidateOrders = {}
for order in permOrders:
	# Sort the matrix by the order of the permutation
	permMatrix = [x for (y,x) in sorted(zip(order, transpoMatrix), key=lambda pair: pair[0])]
	# Transform the matrix into pairs of letters and then into single letters
	letters = makePairs(permMatrix, numCols, numRows)
	# Calculate the index of coincidence for the single letters linked to this permutation
	index = indexOfCoincidence(letters)
	# Store the permutation order and IC as a dict item
	candidateOrders[order] = index

# print out the top 100 candidate orders by IC (larger is more English-like)
#print(sorted(candidateOrders.items(), key=lambda x:-x[1])[:100]) 

# Only save the candidates that are most like English (which is about 0.063)
topCandidates = {}
for k,v in candidateOrders.items():
	if v >= 0.06 :
		topCandidates[k] = v

# remove the large variables to make the program less burdensome
del candidateOrders
del permOrders

# print the total number of English-like candidates
numCandidates = len(topCandidates)
print(numCandidates)

# calculate the frequency of each column number in each position of the top candidate orders
# un-comment the initialization of candFreq that matches your key length (the order is 8, 9, 10 below)

#candFreq = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]] 
candFreq = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]] 
#candFreq = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]] 

for k in topCandidates.keys():			# for each order in the top candidates,
	for j in range(numCols):			# for each position in the transposition
		for i in range(numCols):		# for each possible column
			candFreq[i][j] += 1 if k[j] == i else 0

print(candFreq)