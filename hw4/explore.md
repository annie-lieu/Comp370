# Exploration with Command Line Tools

## Q1: How big is the dataset?
Using `wc -l clean_dialog.csv`, we see that the file has 36860 lines or 36859 entries.

## Q2: What’s the structure of the data?
Using `head -n 2 clean_dialog.csv` reveals there are 4 features: "title", "writer", "pony", and "dialog". The "title" column contains the episode name of the respective dialogue line. The "writer" column contains the name of the writer for the episode. The "pony" column contains the name of the character who spoke the line. The "dialog" column contains the transcript line, including the action cues, for the character.

## Q3: How many episodes does it cover?
Using `csvtool col 1 clean_dialog.csv | tail +2 | uniq -c | wc -l`, we learn the dataset covers 197 episodes.

## Q4: What are some potential issues with the dataset that can complicate the analysis phase?
When scanning the dataset with `more`, some character's lines can be significantly longer than others. When determining how much a character speaks, we go by the number of lines rather than word count, so a character that speaks a few words at a time across multiple lines is considered more chatty than a character that monologues in one line.


## Task 4: Analyze Speaker Frequency
To count the number of lines each main character has, I used `csvtool col 3 clean_dialog.csv | grep "CHARACTER NAME" | wc -l`. I then calculated the percentage of lines each character has over the whole dataset and formatted the results in `Line_percentages.csv`
