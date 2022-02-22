# Wordle-Solver
Helps solve wordle puzzles

```
PS C:\Users\avish\Desktop\Chris Coding Demo\Wordle> python .\wordle_solver.py
Enter guess: .....
Enter required chars: ane
Enter banned characters: cr
['admen', 'aeons', 'agene', 'agent', 'agone', 'akene', 'alane', 'alien', 'aline', 'alone', 'amend', 'amens', 'ament', 'amine', 'anele', 'anent', 'angel', 'angle', 'anile', 'anime', 'anise', 'ankle', 'annex', 'anode', 'anole', 'ansae', 'antae', 'anted', 'antes', 'apnea', 'ashen', 'aspen', 'atone', 'avens', 'awned', 'axmen', 'axone', 'azine', 'baned', 'banes', 'beano', 'beans', 'began', 'daven', 'dawen', 'deans', 'dewan', 'eaten', 'elain', 'eland', 'elans', 'enate', 'enema', 'entia', 'etnas', 
'faena', 'fanes', 'ganef', 'ganev', 'genoa', 'genua', 'glean', 'hanse', 'haven', 'henna', 'hyena', 'inane', 'janes', 'jeans', 'kanes', 'kenaf', 'knave', 'knead', 'laden', 'lanes', 'laten', 'leans', 'leant', 'leman', 'liane', 'maned', 'manes', 'mange', 'manse', 'maven', 'means', 'meant', 'meany', 'menad', 'mensa', 'menta', 'minae', 'nabes', 'naevi', 'naive', 'naked', 'naled', 'named', 'names', 'napes', 'nappe', 'nates', 'navel', 'naves', 'neaps', 'neath', 'neats', 'nemas', 'novae', 'oaken', 'oaten', 'paean', 'paeon', 'paned', 'panel', 'panes', 'panne', 'paten', 'peans', 'pekan', 'penal', 'penna', 'plane', 'plena', 'quean', 'saned', 'sanes', 'sedan', 'senna', 'sensa', 'sewan', 'skean', 'snake', 'sneak', 'sneap', 'spean', 'stane', 'taken', 'tenia', 'thane', 'tinea', 'ulnae', 'usnea', 'vaned', 'vanes', 'veena', 'vegan', 'venae', 'venal', 'waken', 'waned', 'wanes', 'waney', 'waxen', 'weans', 'xenia', 'yamen', 'yeans', 'yenta', 'zazen']
Enter guess: .....
Enter required chars: aen
Enter banned characters: gt
['admen', 'aeons', 'akene', 'alane', 'alien', 'aline', 'alone', 'amend', 'amens', 'amine', 'anele', 'anile', 'anime', 'anise', 'ankle', 'annex', 'anode', 'anole', 'ansae', 'apnea', 'ashen', 'aspen', 'avens', 'awned', 'axmen', 'axone', 'azine', 'baned', 'banes', 'beano', 'beans', 'daven', 'dawen', 'deans', 'dewan', 'elain', 'eland', 'elans', 'enema', 'faena', 'fanes', 'hanse', 'haven', 'henna', 'hyena', 'inane', 'janes', 'jeans', 'kanes', 'kenaf', 'knave', 'knead', 'laden', 'lanes', 'leans', 
'leman', 'liane', 'maned', 'manes', 'manse', 'maven', 'means', 'meany', 'menad', 'mensa', 'minae', 'nabes', 'naevi', 'naive', 'naked', 'naled', 'named', 'names', 'napes', 'nappe', 'navel', 'naves', 'neaps', 'nemas', 'novae', 'oaken', 'paean', 'paeon', 'paned', 'panel', 'panes', 'panne', 'peans', 'pekan', 'penal', 'penna', 'plane', 'plena', 'quean', 'saned', 'sanes', 'sedan', 'senna', 'sensa', 'sewan', 'skean', 'snake', 'sneak', 'sneap', 'spean', 'ulnae', 'usnea', 'vaned', 'vanes', 'veena', 'venae', 'venal', 'waken', 'waned', 'wanes', 'waney', 'waxen', 'weans', 'xenia', 'yamen', 'yeans', 'zazen']
Enter guess: .ake.
Enter required chars: n
Enter banned characters: w
['naked', 'oaken']
Enter guess:
```
Final answer was "naked" - taken from the last two provided choices.

Note that this tool does not take into account invalid positions of letters (yet).
