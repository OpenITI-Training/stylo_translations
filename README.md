# Translated novels datasets for stylo

This dataset contains Arabic translations of 58 stories by 3 authors (Arthur Conan Doyle, HG Wells, and Edward Page Mitchell), translated by 9 different
translators, each of whom translated work from at least two of these authors. 

| Translator | Wells | Mitchell | Doyle |
|------------|-------|----------|-------|
| Callam | 1 | 2 | 6 |
| Catif | 1 | 1 | 8 |
| Ghanim | 0 | 2 | 1 |
| Ghurab | 0 | 3 | 6 |
| Miftah | 0 | 2 | 3 |
| Mukhtar | 0 | 5 | 1 |
| Radan | 0 | 1 | 6 |
| Sabri | 6 | 0 | 1 |
| Sadiq | 1 | 0 | 1 |

The dataset is meant to investigate whether stylometry can detect the 
stylistic signal of the original author in a translation, 
and/or the signal of the translator.

The repo contains 5 different versions of this dataset:

1. raw texts, not cleaned:

- author_first: file names have the format author_translator_title.txt. Use this to experiment with finding the author signal in the translations.
- transl_first: file names have the format translator_author_title.txt. Use this to experiment with finding the translator signal in the translations.

2. cleaned texts (using the clean.py script): no file headers, page numbers, 
milestones, section headings, normalization of final ya/alif maqsura, 
different hamzas, final ha/ta marbuta. 

- author_first_cleaned: author_translator_title.txt. Use this to experiment with finding the author signal in the translations.
- transl_first_cleaned: translator_author_title.txt. Use this to experiment with finding the translator signal in the translations.
- transl-author_cleaned: translator-author_title.txt (the combination of translator and author will be given the same color in the stylo output graphs)

