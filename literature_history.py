import matplotlib.pyplot as plt
import networkx as nx

# Create a directed graph
G = nx.DiGraph()

# Add nodes and edges representing the structure of the history of the novel
novel_tree = [
    ("Novel Writing History", "Early Beginnings"),
    ("Early Beginnings", "Ancient Narratives"),
    ("Ancient Narratives", "*The Golden Ass* by Apuleius"),
    ("Ancient Narratives", "*Daphnis and Chloe* by Longus"),
    ("Early Beginnings", "Early Non-Western Novels"),
    ("Early Non-Western Novels", "*The Tale of Genji* by Murasaki Shikibu"),

    ("Novel Writing History", "Medieval and Early Modern Foundations"),
    ("Medieval and Early Modern Foundations", "Medieval Romances and Epic Poetry"),
    ("Medieval Romances and Epic Poetry", "*The Divine Comedy* by Dante"),
    ("Medieval Romances and Epic Poetry", "Arthurian Romances"),
    ("Medieval and Early Modern Foundations", "Early Modern Novels"),
    ("Early Modern Novels", "*Don Quixote* by Miguel de Cervantes"),

    ("Novel Writing History", "17th and 18th Century: The Emergence of the Novel"),
    ("17th and 18th Century: The Emergence of the Novel", "Spanish Novel"),
    ("Spanish Novel", "*Don Quixote* by Miguel de Cervantes"),
    ("17th and 18th Century: The Emergence of the Novel", "English Novel"),
    ("English Novel", "*Robinson Crusoe* by Daniel Defoe"),
    ("English Novel", "*Pamela* by Samuel Richardson"),
    ("English Novel", "*Tom Jones* by Henry Fielding"),
    ("17th and 18th Century: The Emergence of the Novel", "French Novel"),
    ("French Novel", "*Manon Lescaut* by Abbé Prévost"),

    ("Novel Writing History", "19th Century: The Golden Age of the Novel"),
    ("19th Century: The Golden Age of the Novel", "English Realism"),
    ("English Realism", "*Pride and Prejudice* by Jane Austen"),
    ("English Realism", "*Great Expectations* by Charles Dickens"),
    ("English Realism", "*Middlemarch* by George Eliot"),
    ("19th Century: The Golden Age of the Novel", "French Realism"),
    ("French Realism", "*Madame Bovary* by Gustave Flaubert"),
    ("French Realism", "*La Comédie Humaine* by Honoré de Balzac"),
    ("19th Century: The Golden Age of the Novel", "Russian Novel"),
    ("Russian Novel", "*War and Peace* by Leo Tolstoy"),
    ("Russian Novel", "*Crime and Punishment* by Fyodor Dostoevsky"),

    ("Novel Writing History", "20th Century: Experimentation and Modernism"),
    ("20th Century: Experimentation and Modernism", "Modernism"),
    ("Modernism", "*Ulysses* by James Joyce"),
    ("Modernism", "*To the Lighthouse* by Virginia Woolf"),
    ("Modernism", "*In Search of Lost Time* by Marcel Proust"),
    ("20th Century: Experimentation and Modernism", "Psychological Novel"),
    ("Psychological Novel", "*The Sound and the Fury* by William Faulkner"),
    ("Psychological Novel", "*The Trial* by Franz Kafka"),
    ("20th Century: Experimentation and Modernism", "Stream of Consciousness"),
    ("Stream of Consciousness", "*Mrs. Dalloway* by Virginia Woolf"),
    ("Stream of Consciousness", "*As I Lay Dying* by William Faulkner"),

    ("Novel Writing History", "Postmodernism and Contemporary Novels"),
    ("Postmodernism and Contemporary Novels", "Postmodernism"),
    ("Postmodernism", "*Gravity's Rainbow* by Thomas Pynchon"),
    ("Postmodernism", "*Slaughterhouse-Five* by Kurt Vonnegut"),
    ("Postmodernism and Contemporary Novels", "Magical Realism"),
    ("Magical Realism", "*One Hundred Years of Solitude* by Gabriel García Márquez"),
    ("Magical Realism", "*Midnight’s Children* by Salman Rushdie"),
    ("Postmodernism and Contemporary Novels", "Contemporary Novels"),
    ("Contemporary Novels", "*The Road* by Cormac McCarthy"),
    ("Contemporary Novels", "*Americanah* by Chimamanda Ngozi Adichie"),
]

# Add edges to the graph
G.add_edges_from(novel_tree)

# Set figure size
plt.figure(figsize=(16, 14))

# Use graphviz tree layout if available, fall back to spring layout
try:
    pos = nx.drawing.nx_agraph.graphviz_layout(G, prog='dot')
except Exception:
    pos = nx.spring_layout(G, k=0.9, iterations=50)

# Draw the graph
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightgreen", font_size=8, font_weight="bold", arrows=True,
        arrowstyle='->', arrowsize=10)

plt.title("History of Novel Writing - Tree Structure")
plt.show()

