from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    #A is a knight or a knave but not both
    Or(Aknight, Aknave),
    Implication(AKnight, Not(AKnave)),
    Implication(AKnave, Not(AKnight)),
    #If A tells the truth, and therefore is a knight, then he is both a knight and a knave.
    Biconditional(AKnight, And(AKnight, AKnave))
    )

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    #They are either a knight or a knave but not bothOr(AKnight, AKnave),
    Or(AKnight, AKnave),
    Implication(AKnight, Not(AKnave)),
    Implication(AKnave, Not(AKnight)),
    Or(BKnight, BKnave),
    Implication(BKnight, Not(BKnave)),
    Implication(BKnave, Not(BKnight))
    #If what A says is truth, and there for he is knight, they are both knaves.
    Biconditional(AKnight, And(Aknight, Bknight))
    )

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # They are either a knight or a knave but not bothOr(AKnight, AKnave),
    Or(AKnight, AKnave),
    Implication(AKnight, Not(AKnave)),
    Implication(AKnave, Not(AKnight)),
    Or(BKnight, BKnave),
    Implication(BKnight, Not(BKnave)),
    Implication(BKnave, Not(BKnight))
    #If A is knight, then they are both the same.
    Biconditional(AKnight, Or(And(AKnight, BKnight),
                          And(AKnave, BKnave)))
    #If B is knight, then they are different
    Biconditional(BKnight, Or(And(AKnight, BKnave),
                              And(AKnave, BKnight)))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # They are either a knight or a knave but not bothOr(AKnight, AKnave),
    Or(AKnight, AKnave),
    Implication(AKnight, Not(AKnave)),
    Implication(AKnave, Not(AKnight)),
    Or(BKnight, BKnave),
    Implication(BKnight, Not(BKnave)),
    Implication(BKnave, Not(BKnight))
    #If A is a knight, he is either a knight or a knave
    Biconditional(Or(AKnight, AKnight),
              Or(AKnight, AKnave)),
    #B is a knight if and only if A is a knave.
    Biconditional(BKnight, Biconditional(AKnight, AKnave)),
    #If B is a knight, then C is a knave.
    Biconditional(BKnight, CKnave),
    #If C is a knight, then A is a knight.
    Biconditional(CKnight, AKnight)

)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
