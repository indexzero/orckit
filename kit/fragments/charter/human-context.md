# ctx/: manually adopted files

> The slot for files a human places here by hand because they belong with
> this run. Examples are loose notes, feedback, and designs. They sit
> beside the kit artifacts without being any of them. No tool writes into this slot.
> Nothing else instantiates into it. The import and cleanup diff gates
> ignore it. ctx/ is never part of an import contract.

Adopt freely. The one rule is provenance. Name the origin of the file in
the commit that adopts it (`doc(ctx) adopt <file> from <where>`). A loose
file with no origin is a mystery by the next session.
