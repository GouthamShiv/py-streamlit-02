from typing import Sequence
import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image

image = Image.open('app/dna_image.jpg')
st.image(image, use_column_width=True)

st.write("""
# DNA Nucleotide Count App

#### This app counts this nucleotide composition of query DNA!
""")

st.header('Enter DNA sequence')
st.subheader('First line will be ignored')
sequence_input = '>DNA Query\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT'

sequence = st.text_area('Sequence Input', sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:] # Skips the sequence name (first line)
sequence = ''.join(sequence) # Concatenate the list to string

st.write("""
***
""")

st.header('Input (DNA Query)')
st.text(sequence)

st.header('Output (DNA Nucleotide Count)')

st.subheader('1. Print Dictionary')
def DNA_nucleotide_count(seq):
    d = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C')),
    ])
    return d

X = DNA_nucleotide_count(sequence)
X
# X_label = list(X)
# X_values = list(X.values())

st.subheader('2. Print Text')
st.write('There are ' + str(X['A']) + ' adenine (A)')
st.write('There are ' + str(X['T']) + ' thymine (T)')
st.write('There are ' + str(X['G']) + ' Guanine (G)')
st.write('There are ' + str(X['C']) + ' Cytosine (C)')

st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'Count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index' : 'Nucleotide'})
st.write(df)

st.subheader('4. Display Bar Chart')
p = alt.Chart(df).mark_bar().encode(
    x='Nucleotide',
    y='Count'
)

p = p.properties(
    width=alt.Step(80)
)

st.write(p)