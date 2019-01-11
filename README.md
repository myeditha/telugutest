# User Instructions

Thank you for agreeing to help us tag this data :) 

Below are the instructions on how to use the tagging script. You may also choose to not use the tagger script if you choose (see below)

## Tagging Instructions

### Tagger Script Instructions

To use the tagger script, run `./tagger.py output_.txt outputaug_.txt`, where `_` should be replaced with your assigned number. 

You will have the opportunity to classify each word in every sentence sequentially. Once the script is run, you will see each sentence with the current word you're trying to classify written immediately underneath. The classifications you should put for each word should be `eng` for English, `tel` for Telugu, and `other` for other. See instructions below on how to tag each word for how to do this.

In case you make a mistake while tagging each word in a sentence, you also have the capability of going back and fixing each incorrect word. Once you finish tagging a sentence, you will be prompted to indicate whether or not your tags are correct. If you answer `y` or `yes`, then you move on to the next sentence; otherwise, you enter editor mode. In editor mode, you are given the opportunity to specify which words you determined have an incorrect classification, separated by space, and then correct the classifications of these words. If you would like to exit editor mode at any time, just type `end`, and if you would like to skip the current word you're editing the classification of, type `skip`. 

### Non-tagger Script Instructions

If you don't want to use the tagger script, you can simply create a document of the format `outputaug_.txt`, where `_` should be substituted for your assigned number.

Copy and paste each sentence from `output_.txt`, where `_` is your assigned number. Then as you classify each word `w` with some label `c`, replace `w` with `w\c` (i.e. `alage` would have classification tel, so you would replace `alage` with `alage\tel`)

## How to Tag Each Word

`eng`: tag a word with this if you believe that the word is English, and can be found in Webster's Dictionary or Merriam-Webster Dictionary (i.e. is English in a formal register).

`tel`: tag a word with this if you believe that the word is Telugu, and if transliterated into Telugu script would be understandable.

`other`: tag a word with this if the word is slang, an abbreviation, punctuation, or otherwise unclear.
