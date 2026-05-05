# User Ranking & Inversion Counter

A utility designed to analyze user preferences for movies and calculate their similarity based on the number of inversions compared to a target user.

## Overview

The program reads user movie rankings from an input file, takes a target user ID from the terminal, and calculates the "distance" between users using an inversion counting algorithm. The results are then saved to an output file, sorted by the level of similarity.

## Input File Format

The input file (e.g., `input.txt`) should follow this structure:

1.  **First line:** Two integers `U` (number of users) and `M` (number of movies).
2.  **Subsequent lines:** User ID followed by `M` integers representing movie rankings.

**Example Input:**
    10 5
    1 5 2 1 3 4
    2 3 2 4 1 5
    3 4 5 3 2 1
    4 5 1 4 3 2
    5 1 2 5 4 3
    6 2 5 4 1 3
    7 2 4 5 3 1
    8 5 3 1 4 2
    9 4 5 2 3 1
    10 3 1 2 4 5

## Usage

1. **Run the application.**
2. **Specify the target user:** When prompted in the terminal, enter the `User ID (X)` you wish to compare others against.
3. **Execution:** The program processes the rankings and calculates inversions for every other user relative to user `X`.

## Output File Format

The results are written to `inupt_out.txt`:

1.  **First line:** The target User ID `X`.
2.  **Subsequent lines:** Two columns: `User ID` and `Inversion Count`.
3.  **Sorting:** The list is sorted in ascending order by the **second column** (amount of inversions).

**Example Output (for X = 6):**
    6
    3 3
    2 4
    7 4
    9 4
    5 5
    1 7
    4 7
    8 7
    10 8
    6

