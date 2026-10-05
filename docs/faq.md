# Frequently asked questions

## Is the repository open source?

Yes. The visibility is public, and the grant is the MIT Licence in [LICENSE](../LICENSE). You may use, copy, modify, and redistribute the notebooks and the documentation, including in a course, provided the copyright notice and the permission notice travel with any substantial copy. The MIT Licence does not require you to publish your changes.

## Who holds the copyright?

Er. Rishabh Aryan, 2026, as stated in the licence file. A citation form for teaching notes is in [CITATION.cff](../CITATION.cff). Attribution beyond the licence notice is appreciated and not required.

## Which Python version do I need?

3.10 or newer. The reason, and the features that set that floor, are in [Getting started](getting-started.md).

## Do I need to install NumPy, pandas, or a requirements file?

No. There is no `requirements.txt` because the notebooks do not import third-party packages. Jupyter is a viewer, not a dependency of the code. Installing Jupyter is described in the getting-started guide.

## Why does `id()` differ from the stored output?

`id` reports an identity in the current process. The stored number was valid in the process that built the notebook. Compare types, printed values, and exception messages, not identities.

## Why is one tic-tac-toe game a loss for the human?

The sample human moves are not optimal. The engine is. The note in [the tic-tac-toe document](capstones/02-tic-tac-toe.md) separates those two facts. Optimal play by both sides from an empty board draws.

## Can I type guesses into Hangman?

Yes. Call `play_interactive("python")` in a cell or a terminal session. The published demonstration does not call it, so **Run all** does not block on `input`.

## May I assign these notebooks as coursework?

Yes. The licence allows that. Please keep the copyright and licence notice with any substantial copy you distribute to students. A link to the repository satisfies that for a digital handout if you do not redistribute modified files; a modified copy must include the notice.

## Where should a correction go?

A wrong explanation or a failing cell belongs in an issue. A proposed notebook belongs in a pull request. The procedure is in [CONTRIBUTING.md](../CONTRIBUTING.md).

## Why are the notebooks not at the repository root?

So the root can be the project description rather than a flat list of course files. The map is in [Repository layout](repository-layout.md).
