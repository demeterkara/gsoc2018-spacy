# coding: utf8
from __future__ import unicode_literals


"""
Example sentences to test spaCy and its language models.
>>> from spacy.lang.en.examples import sentences
>>> docs = nlp.pipe(sentences)
"""


sentences = [
    "Η καταπάτηση των δικαιωμάτων των ανθρώπων είναι η χειρότερη μορφή δικτατορίας",
    "Κανείς δεν πρέπει να ξεκινάει έναν πόλεμο που δεν μπορεί να κερδίσει",
    "Οι περιπέτειες ξεκινάνε όταν δεν προγραμματίζεις το χρόνο σου και τις προτεραιότητες σου",
    "Στη Βουλή συζητήθηκε εκτενώς το θέμα της συμφωνίας σχετικά με το Μακεδονικό ζήτημα",
    "Το μουντιάλ βρίσκεται στη φάση των 16",
    "Τα παιδιά λατρεύουν τα παραμύθια και τα γλυκά",
    "Οι δασώδεις εκτάσεις του Αμαζονίου προσφέρονται για σαφάρι και εξερεύνηση του άγριου βιότοπου",
    "Η προσπέραση από τα δεξιά απαγορεύεται αυστηρώς από το νόμο",
    "Οι συναυλίες είναι για το καλοκαίρι ότι οι χιονισμένες μέρες για το χειμώνα"
]

lemmatizer_out =[
    "η καταπάτηση το δικαίωμα το άνθρωπος είμαι η κακός μορφή δικτατορία",
    "Κανείς δεν πρέπει να ξεκινάω ένας πόλεμος που δεν μπορώ να κερδίσω",
    "Ο περιπέτεια ξεκινάω όταν δεν προγραμματίζω το χρόνο μου και τη προτεραιότητα μου",
    "στη Βουλή συζητώ εκτενώς το θέμα ο συμφωνία σχετικά με το Μακεδονικό ζήτημα",
    "το μουντιάλ βρίσκομαι τη φάση ο 16",
    "το παιδί λατρεύω το παραμύθι και το γλυκό",
    "ο δασώδης έκταση το Αμαζόνιος προσφέρομαι για σαφάρι και εξερεύνηση το άγριος βιότοπος",
    "η προσπέραση από το δεξιά απαγορεύω αυστηρώς από το νόμο",
    "η συναυλία είμαι για το καλοκαίρι ότι ο χιονισμένος μέρα για το χειμώνας",

]
