# Computational thinking: lab test cheatsheet

Search this file with **Cmd+F** on Mac or **Ctrl+F** on Windows. Search the keywords below or a past-paper function name in the source map. Markdown headings also appear in most editors' Outline view. This file works offline.

Scope: Python Lab Tests 1 and 2. More space goes to Lab Test 2's file handling, dictionaries and simulation. Based on six local past papers from AY2023/24 to AY2025/26, their supporting code, and local mocks. These are observed patterns, not predictions of the next test. Snippets are reusable reference patterns, not a new practice test.

## Quick search index

| Need | Search / jump |
|---|---|
| Decide how to approach a question | [Workflow](#workflow) |
| Syntax, operators, conversion, rounding | [Python essentials](#python-essentials) |
| Thresholds, inclusive/exclusive bounds | [Conditions and ranges](#conditions-and-ranges) |
| Count, filter, transform, all/any | [Loop patterns](#loop-patterns) |
| First, last, second match; ties | [Search and best item](#search-and-best-item) |
| Slicing, reverse, split, punctuation | [Strings](#strings) |
| Copy, mutation, unique, common words | [Lists, tuples and sets](#lists-tuples-and-sets) |
| Read/write, delimiters, headers, encoded text | [Files and parsing](#files-and-parsing) |
| Frequency, grouping, nested records, averages | [Dictionaries and reports](#dictionaries-and-reports) |
| Dates, AM/PM, seconds | [Dates and times](#dates-and-times) |
| Grid, adjacency, traffic, inventory, coins | [Simulation and grids](#simulation-and-grids) |
| All combinations, all safe routes, minimum | [Search over possibilities](#search-over-possibilities) |
| Import helper, run tests, common errors | [Debugging and submission](#debugging-and-submission) |
| Locate the original question | [Source map](#source-map) |

## Workflow

1. Read the signature and write down the exact return shape, such as `dict[str, list[tuple]]`. Distinguish **return**, **print**, and **write to file**.
2. Mark the boundaries, empty-input result, no-match result, tie rule, required order and mutation restrictions. These differ between questions.
3. Identify the pattern: filter, accumulate, group, simulate or enumerate possibilities.
4. Implement the simplest part first. Reuse helper functions where required or allowed. Read each part's dependency instructions; some past questions grade later parts with correct helpers.
5. Run the supplied test script. Compare actual and expected values, including types and order. The papers say grading uses different tests, so cover the full specification.

The six inspected papers each allocate 90 minutes and 25 marks. A useful working budget is about 3 minutes per mark plus 15 minutes for checking and packaging. Adjust to the actual paper.

## Python essentials

```python
x / y                 # true division; 4 / 2 gives 2.0
x // y                # floor division
x % y                 # remainder; n % 2 == 0 means even
x ** 2                # power; ^ is NOT power
int('032')            # 32
float('12.50')        # 12.5
int(3.9)              # 3; truncates towards zero
int(-3.9)             # -3; not mathematical floor
round(62.5)           # 62; halfway cases round to even
round(3.14159, 2)      # numeric result: 3.14
f'{3.1:.2f}'          # string result: '3.10'
```

Use the requested conversion. For nonnegative rebates, `int(value)` discards the fractional dollar. Use `round` when explicitly requested. Round a final average after summing, unless the question says otherwise.

| Task | Python |
|---|---|
| Empty list / dictionary / set | `[]` / `{}` / `set()` |
| One-element tuple | `(value,)` |
| First / last element | `items[0]` / `items[-1]` |
| First and last tuple elements | `tup[0] + tup[-1]` |
| Iterate values | `for item in items:` |
| Iterate indices | `for i in range(len(items)):` |
| Index and value | `for i, item in enumerate(items):` |
| Inclusive integers 1 through n | `range(1, n + 1)` |
| Reverse indices | `range(len(items) - 1, -1, -1)` |
| Tuple unpacking | `name, age, score = record` |
| None check | `value is None` |

`None`, `0`, `''`, `[]` and `{}` are different results even though all are false in a condition. Match the question's contract.

## Conditions and ranges

Translate words carefully:

| Wording | Condition |
|---|---|
| At least / no less than | `x >= limit` |
| At most / not exceeding | `x <= limit` |
| Strictly shorter than | `len(text) < n` |
| Above a, not exceeding b | `a < x <= b` |
| Between a and b, inclusive | `a <= x <= b` |
| Lower inclusive, upper exclusive | `a <= x < b` |
| All requirements | `condition_a and condition_b` |
| Either requirement | `condition_a or condition_b` |

For a threshold table, test ordered bands with `if` / `elif` / `else`. Several independent `if` statements can overwrite an earlier result.

```python
if margin >= 0.5:
    min_stock = 3
elif margin >= 0.2:
    min_stock = 8
else:
    min_stock = 15
```

For plan costs, separate plan parameters from the formula: `base_fee + max(0, usage - quota) * extra_rate`. Use this only when the tariff charges for excess usage in that way.

Write `category == 'A' or category == 'B'`, or `category in ('A', 'B')`. The expression `category == 'A' or 'B'` is always truthy.

## Loop patterns

| Pattern | Initial state | Inside the loop | End result |
|---|---|---|---|
| Count matches | `count = 0` | If match, `count += 1` | `count` |
| Sum matching values | `total = 0` | If match, `total += value` | `total` |
| Filter records | `result = []` | If match, `result.append(record)` | `result` |
| Transform every item | `result = []` | `result.append(transformed_item)` | `result` |
| Average of matches | `total = count = 0` | Add value and increment count | `total / count`, if count > 0 |

Reset a counter inside the outer loop when the question wants one count **per string, group or city**. Keep it outside for a whole-input total.

For **all records satisfy a rule**, return `False` on the first violation, then `True` after the loop. For **any record satisfies a rule**, return `True` on the first match, then `False` after the loop. An empty input gives `True` for the first pattern and `False` for the second unless the specification overrides that behavior.

```python
def all_scores_positive(scores):
    for score in scores:
        if score <= 0:
            return False
    return True
```

`break` leaves the innermost loop. `continue` skips to its next iteration. `return` leaves the entire function. A `while` loop needs an update that moves it towards its stopping condition.

## Search and best item

- First match: return immediately on a match.
- Last match: update the saved answer on every match; return after the loop.
- Second match: increment a match counter and return when it reaches 2.
- No index found: initialize `answer = -1` if that is the required sentinel.

For maximum/minimum questions, initialize from the first valid candidate or use `None`. Starting a maximum at `0` fails when every value is negative.

```python
def longest_word(words):
    if not words:
        return None
    best = words[0]
    for word in words[1:]:
        if len(word) >= len(best):
            best = word
    return best, len(best)
```

Tie rule: `>` keeps the **first** maximum; `>=` keeps the **last** maximum. Reverse the comparisons for minimums. AY2024/25 LT1 `get_longest_string` keeps the last; AY2023/24 LT2 `get_highest_value` keeps the first.

## Strings

```python
s[start:stop]          # includes start, excludes stop
s[:3]                 # first 3 characters
s[3:]                 # everything after the first 3 characters
s[-2:]                # last 2 characters
s[:-2]                # all except last 2 characters
s[::-1]               # reversed copy
s[::2]                # indices 0, 2, 4, ...
s[1::2]               # indices 1, 3, 5, ...
ch.isalpha()          # letter?
ch.isdigit()          # digit?
ch in 'AaEeIiOoUu'    # vowel?
s.startswith('#')     # prefix check; also works on an empty string
```

Indices start at zero. Slices tolerate out-of-range endpoints; direct indexing can raise `IndexError`. Check a string is nonempty before reading `s[0]`.

| Operation | Meaning / trap |
|---|---|
| `s.split()` | Split whitespace; collapse repeated whitespace; omit empty tokens |
| `s.split(',')` | Split commas; preserve empty fields, e.g. `'a,,b'` |
| `s.rstrip('\n')` | Remove trailing newline characters; preserve spaces |
| `s.strip()` | Remove surrounding whitespace; may destroy meaningful padding |
| `s.replace('!', ' ')` | Return a new string; assign it back |
| `'#'.join(parts)` | Join strings with `#`; convert numbers to strings first |
| `s.lower()` | Use only when the question says case-insensitive |

Multiple separators: replace each permitted separator with a common delimiter, then split. If empty segments matter, use an explicit delimiter. For the revision notebook's `reverse_segments`, replacing `|`, `-`, `=` with `|` and using `.split('|')` preserves empty segments.

Alternating two strings: loop to `min(len(s1), len(s2))`, append `s1[i] + s2[i]`, then append the longer string's unconsumed suffix reversed. This also handles either string being empty.

Exact output: build a list of formatted pieces and use `separator.join(pieces)` to avoid a trailing separator. For padding, `' ' * n` produces n spaces.

## Lists, tuples and sets

```python
items.append(value)       # add ONE object, including a tuple or list
items.extend(other)       # add each element from other
items.remove(value)       # remove first equal value; error if absent
items.pop(i)              # remove and return item at index i
copy = items[:]           # new outer list; nested objects remain shared
rows_copy = [row[:] for row in rows]  # also copy each inner list
```

`append`, `extend`, `sort` and `reverse` modify a list and return `None`. Do not write `items = items.sort()`. Use `sorted(items)` for a sorted copy and `items[::-1]` for a reversed copy.

If input must remain unchanged, build a new result. Copy every mutable level you will change. A shallow copy is sufficient if you only replace outer elements or the inner elements are immutable tuples.

Unique values **in first-appearance order**:

```python
unique = []
for value in values:
    if value not in unique:
        unique.append(value)
```

Use `set(values)` when order and duplicate counts do not matter. Distinct shared words: `len(set(words_a) & set(words_b))`. Do not convert coins to a set: three coins worth 2 are three spendable coins.

Unordered pairs without pairing an item with itself:

```python
for i in range(len(records)):
    for j in range(i + 1, len(records)):
        # compare records[i] with records[j]
        pass
```

For circular adjacency, the next index is `(i + 1) % len(records)`, which includes the last-to-first pair. Check the source diagram to determine which pairs count as adjacent.

## Files and parsing

Use the supplied filename parameter. Run from the resource directory when sample files use relative paths.

```python
def read_records(filename):
    result = []
    with open(filename, 'r') as source:
        for line in source:
            name, category, amount = line.rstrip('\n').split(',')
            result.append((name, category, float(amount.lstrip('$'))))
    return result
```

Parse in layers: line → fields → subfields → converted values. Examples include `line.split('|')`, timestamp `.split(':')`, and grouped numbers `.split('#')` followed by each group's `.split()`.

Do not skip blank lines or strip every field unless the format permits it. For comma-separated empty fields, `.split(',')` preserves the missing data. The simple split pattern assumes the paper's plain delimited format; quoted commas require a CSV parser.

### Fixed-width fields and checksums

AY2025/26 LT2 `decode_potter` stores a 3-character length followed by text and irrelevant trailing data:

```python
length = int(line[:3])
sentence = line[3:3 + length]
# For the checksum variant, the last 2 characters WITHIN sentence are digits:
text = sentence[:-2]
transmitted = int(sentence[-2:])
actual = 0
for ch in text:
    if ch in 'AaEeIiOoUu':
        actual += 1
record = (text, actual, actual == transmitted)
```

Slice the field before removing the checksum. Do not count vowels in the random suffix. A length of zero gives `''` in Part A. A checksum match means this check passes; it does not prove the text is unchanged.

### Header-driven records

For a file whose first line names the fields:

```python
with open(filename) as source:
    headers = source.readline().rstrip('\n').split(',')
    rows = []
    for line in source:
        fields = line.rstrip('\n').split(',')
        record = {}
        for i in range(len(headers)):
            record[headers[i]] = fields[i]  # convert as specified
        rows.append(record)
```

AY2023/24 LT2 `load_pokedex` requires empty fields → `None`, digits → `int`, digits with one decimal point → `float`, otherwise → `str`. Apply that classification; do not hardcode header names or field count. Negative numbers and other formats need whatever rules the actual question supplies.

Projection, as in `select_fields`: create a new dictionary per record, copy requested keys only if present, and omit empty dictionaries. In that paper, requesting no fields means return all fields.

### Writing files

```python
with open(output_filename, 'w') as target:
    for count, average in report_rows:
        target.write(f'{count}: {average:.1f}\n')
```

`'w'` replaces the file; `'a'` appends. Match spaces, labels, decimal places and newlines exactly. `write` needs a string. Do not use `print` as a substitute for writing to the requested file.

## Dictionaries and reports

Choose the shape before coding:

| Need | Shape / update |
|---|---|
| Frequency | `counts[key] = counts.get(key, 0) + 1` |
| Total per category | `totals[key] = totals.get(key, 0) + value` |
| Group records by city/buyer/school | `groups[key]` holds a list |
| Lookup current stock | `stock[product]` holds the current quantity |
| Structured rows with named attributes | List of dictionaries |

Grouping preserves input order within each group's list:

```python
groups = {}
for key, record in keyed_records:
    if key not in groups:
        groups[key] = []
    groups[key].append(record)
```

Use `for key, value in data.items():` to read both. `key in data` checks keys. `data[key]` requires a present key; `data.get(key, default)` supplies a fallback. A plain assignment for an existing key replaces its old value, so append when a key can have multiple records.

For a grouped report: initialize totals **per group**, filter records, count and sum only matches, then create the output entry if the contract requires it.

```python
def weather_summary(data, start_date, end_date):
    result = {}
    for city, records in data.items():
        count = 0
        total_temp = total_rain = 0.0
        for date, high, low, rain in records:
            if start_date <= date <= end_date:
                count += 1
                total_temp += high
                total_rain += rain
        if count > 0:
            result[city] = (count, round(total_temp / count, 1),
                            round(total_rain, 1))
    return result
```

No matches: check the requested result. Weather reports omit that city; the swimming report returns `(0, 0)`; the cargo question distinguishes empty input `None` from a nonempty input with no qualifying items `0`.

## Dates and times

Dates represented as integer tuples `(year, month, day)` compare chronologically:

```python
start_date <= date <= end_date
```

Do not separately require the year, month and day each to fall within their own range. That fails across month/year boundaries. Parse numeric components first: `tuple(int(part) for part in date_text.split('-'))`.

For times, normalize everything to minutes or seconds before comparing:

```python
seconds = hour * 3600 + minute * 60 + second
hour24 = hour12 % 12
if suffix == 'PM':
    hour24 += 12
```

12 AM maps to 0; 12 PM maps to 12. If an end time is specified as `(hour, minute)` and converted to seconds, it means second 0 of that minute. Follow the stated inclusivity. An overnight interval needs separate handling only when the problem allows it.

## Simulation and grids

Write down the state, event order and update rule. Walk through one small source example by hand before coding.

- Inventory: process orders in input order. `filled = min(requested, available)`; subtract `filled` immediately, then append that order's result under its buyer. Later orders see the updated stock.
- Transactions: represent each address's coins as a list or value-to-count dictionary. Validate all inputs against a temporary copy, consuming each coin once. Commit withdrawals and outputs only if the whole transaction is valid. Invalid transactions change no state. A total balance alone cannot validate exact coin denominations.
- Traffic lights: maintain elapsed time and remaining green for each lane. If the next car needs more than the remaining green, wait the remaining green plus the red period, reset green, then process the car. Equality fits. Lanes operate in parallel; required green cycles are the maximum across lanes.
- Neighbour allocation: local constraints can propagate. For a line, left-to-right and right-to-left passes handle both slopes. For a grid, a single pass need not settle all constraints; propagate until no required increase remains.

Grid basics:

```python
board = [['-' for c in range(cols)] for r in range(rows)]
for r in range(rows):
    for c in range(cols):
        cell = board[r][c]
# A neighbour (nr, nc) is valid when:
# 0 <= nr < rows and 0 <= nc < cols
string_rows = [''.join(row) for row in board]
```

Avoid `[['-'] * cols] * rows`, which shares the same inner list across rows. Strings are immutable; use list rows while changing cells. Gravity questions usually scan a column from the bottom for its first free cell. Read whether coordinates are zero-based or one-based.

## Search over possibilities

Use this section for harder questions asking for **all valid results**, a swap satisfying several rules, or the **best among candidates**. These patterns vary more between papers than basic filtering and file reports.

For swapping one element from each of two lists: enumerate every `(i, j)`, copy both inputs, swap the selected elements, and run the validity helpers. Return according to the specified first/any/all rule. Do not leave trial mutations in the original lists.

For coin combinations, AY2024/25 LT2 explicitly suggests `itertools.combinations`:

```python
from itertools import combinations

def best_coin_choices(coins, target):
    best_total = None
    choices = set()
    for size in range(1, len(coins) + 1):
        for combo in combinations(coins, size):
            total = sum(combo)
            if total < target:
                continue
            canonical = tuple(sorted(combo))
            if best_total is None or total < best_total:
                best_total = total
                choices = {canonical}
            elif total == best_total:
                choices.add(canonical)
    return sorted(choices)
```

Equal-valued physical coins remain available separately; canonical tuples remove duplicate answers. This enumerates exponentially many subsets, so it suits small inputs. Greedily taking the largest coin does not generally minimize change or find all optimal combinations.

### All safe routes

AY2025/26 LT2 frog questions allow jumps of 1, 2 or 3 positions, rightwards in 1D and rightwards/downwards in 2D. Only the landing cell must be safe; jumping over a nest is allowed.

```python
def safe_routes(map_text):
    paths = [[] for _ in map_text]
    paths[0] = [[]]  # one route to the start: no moves yet
    for pos in range(len(map_text)):
        for path in paths[pos]:
            for jump in (1, 2, 3):
                dest = pos + jump
                if dest < len(map_text) and map_text[dest] != '*':
                    paths[dest].append(path + [jump])
    return len(paths[-1]), paths[-1]
```

`[]` means no route; `[[]]` means one route containing no moves. Use `path + [move]` to create a new path rather than modifying a shared path. For 2D, keep independent path lists per cell and use moves `(step, 'r')` and `(step, 'd')`. Right/down moves let you process cells in row order. Returning all routes can itself require exponential space; a count alone does not satisfy an all-sequences question.

## Debugging and submission

From the resource folder, run the supplied script, for example `python3 q3b_test.py`. Some supplied scripts only print expected/actual output, so successful execution does not mean every result matches.

```python
from q2a import helper_name  # call helper_name(...)
# Alternatively:
import q2a                  # call q2a.helper_name(...)
```

Use the actual function name. Keep test calls under `if __name__ == '__main__':` if needed, so imports do not run interactive code. Preserve required helpers and signatures, including optional defaults such as `swimmer_name=None`.

| Symptom | Check |
|---|---|
| `None` unexpectedly returned | Missing `return`; assigning the result of `.append()` or `.sort()` |
| Only first record handled | `return` indented inside the loop |
| Wrong average | Denominator counts all rows instead of matching rows; reset in wrong place |
| `TypeError` with numbers | Forgot `int`/`float`; mixed string and numeric data |
| `KeyError` | Group not initialized; requested field absent |
| `IndexError` | Empty input; index at length; unequal string lengths |
| Output changes in several rows | Shared inner lists or shared mutable records |
| Correct totals, wrong answer | Tuple/list shape, tie rule, order, rounding or empty-result contract |
| `FileNotFoundError` | Working directory, filename parameter, spelling |

Before packaging:

- Check empty input, no matches, exact thresholds, tied best values and repeated keys when these are allowed inputs.
- Check no forbidden input mutation, no extra debug output, and exact return types.
- Ensure every submitted Python file imports/runs without syntax errors. Keep the test files unchanged.
- Follow the actual test's name/email comments, folder naming and ZIP instructions.

Past papers allow local files and restrict communication/network access; newer papers also prohibit AI assistance during the test. Use this as an offline reference and follow your current paper's instructions.

## Source map

Links below open local source files. Page numbers refer to the PDF's printed pages. The six papers are the main evidence; local mock implementations are supporting examples and may contain student errors. Confidence is high for recurring implementation/filter/aggregate/parse patterns, and lower for the exact theme or algorithm of a future hard question.

| Source | Existing questions and relevant patterns |
|---|---|
| [AY2025/26 LT2](<Lab Test 2024 onwards/AY2025_2026_LabTest_2/LabTest-2.pdf>) | pp. 2–3 Q1 `get_specific_tuples`, `extract_words`: filter, punctuation. pp. 3–5 Q2 `decode_potter`, `decode_potter_checksum`: fixed widths, checksum. pp. 5–7 Q3 `read_weather_data`, `analyze_weather_patterns`: grouping, date filtering, averages. pp. 7–10 Q4 `help_frog_against_snakes`, `help_frog_against_snakes_2`: enumerate 1D/2D paths. |
| [AY2024/25 LT2](<Lab Test 2024 onwards/AY2024_2025_LabTest_2/LabTest-2.pdf>) | pp. 2–3 Q1 `sum_values_by_weights`, `alternate_and_reverse`: filter/sum, interleave, empty cases. pp. 3–4 Q2 `get_entry_count`, `get_swim_report`: optional filter, count/average. pp. 4–7 Q3 `manage_inventory`, `process_orders`: parse currency, thresholds, sequential state. pp. 7–11 Q4 `get_invalid_transactions`, `get_coins`: validate coin ownership, combinations. |
| [AY2023/24 LT2](<Lab Test 2024 onwards/AY2023_2024_LabTest_2/LabTest-2.pdf>) | pp. 2–4 Q1 `compute_coe_rebate`, `compute_parf_rebate`, `get_highest_value`: formulas, bands, helpers, first tie. pp. 5–6 Q2 `get_special_word_count`, `generate_loan_report`: token scans, filtering, totals. pp. 6–9 Q3 `load_pokedex`, `select_fields`: dynamic headers, types, projection. pp. 9–10 Q4 `calculate_actual_delays`: parallel-lane simulation. Older paper labelled IS111. |
| [AY2025/26 LT1](<Lab Test 2024 onwards/AY2025_2026_LabTest_1/LabTest-1.pdf>) | Q1 `is_food_safe`, `compute_plan_cost`: conditions and tariffs. Q2 `calculate_bmr`, `find_people_in_range`: formulas, helpers, formatted output. Q3 `get_counts`, `get_pokemon_info`, `get_best_avg`: category counts, best item, grouped means. Q4 `get_min_allocation`, `get_min_allocation_grid`: neighbour constraints. |
| [AY2024/25 LT1](<Lab Test 2024 onwards/AY2024_2025_LabTest_1/LabTest-1.pdf>) | Q1 formulas and category rules. Q2 `count_short_strings`, `get_longest_string`: strict bounds, last tie, `None`. Q3 `process_patient_data`: counts, averages, unique ailments in input order. Q4 `get_board_state`, `get_board_state_gravity`, `get_who_won`: boards, gravity, winner detection. |
| [AY2023/24 LT1](<Lab Test 2024 onwards/AY2023_2024_LabTest_1/LabTest-1.pdf>) | Q1 parking and rebate conditions. Q2 `get_digits_of_even_index`, `count_non_digits`: indices and nested scans. Q3 `is_partially_compliant`, `is_fully_compliant`, `make_tables_fully_compliant`: multi-rule checks, adjacency, trial swaps. Q4 `schedule_delivery`: required sorting helper and time simulation. Older paper labelled IS111. |
| [Mock LT2A resources](<Week_12/Mock_LabTest_2A_Resource/>) | `find_last_letter`, `find_second_letter`, `get_reversed_list`, `process_numbers`: searches, transformations, nested delimiters and report writing. |
| [Mock LT2B resources](<Mock_LabTest_2B_Resource/>) | `count_high_temperatures`, `check_age`, `count_emails`, `get_document_pair`: count, universal check, AM/PM/time ranges, unique shared words. |
| [Mock LT1 resources](<Week_6/Mock Test/Mock_LabTest_1_Resource/>) | `get_hashtags`, `add_first_odd_digits`, `pad_strings`: token scans, first match per item, padding. |

Revisit [Lab 7: file handling](<Week_10/Lab/Lab 7 - File Handling (v1.2).pdf>) for filtering and averages in Q2, matrices in Q5, and file output in Q6. Revisit [Lab 8: dictionaries](<Week_11/Lab/Lab 8 - Dictionaries (v1.2).pdf>) for grouping students in Q4 and word frequencies in Q5. These repeat the data-processing skills used in the past tests. [Revision notebook](<13. Revisions.ipynb>) includes `reverse_segments` for preserving empty segments.

### Two supplied-solution pitfalls

The paper's specification takes priority over a supplied implementation:

- AY2025/26 LT2 Q1A says first plus **last** tuple element. The local [solution q1a.py](<Lab Test 2024 onwards/AY2025_2026_LabTest_2/LT2-solution/q1a.py>) uses `tup[1]`; use `tup[-1]` for the last element of variable-length tuples.
- AY2025/26 LT2 Q3B permits arbitrary date ranges. The local [solution q3b.py](<Lab Test 2024 onwards/AY2025_2026_LabTest_2/LT2-solution/q3b.py>) compares year/month/day separately. Compare complete integer date tuples to handle ranges crossing months or years.
