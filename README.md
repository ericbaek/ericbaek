# Eric Baek

For over three years, I’ve been building and running **Musecat**, a community directory for arcade players. It launched in June 2023 with 45 arcades so players could find out which venues had the games they wanted to play. Players now use it to find cabinets, correct listings, and report broken machines.

By **14 November 2026**, Musecat listed **3,264 arcades** and had recorded **21,226 edits** and **2,091 fault reports**. Its pages received **1.62 million views** between 28 February 2026, when view tracking began, and 14 November. [Explore Musecat](https://musecat.app/en) · [Read the development history](https://musecat.app/en/community/updates)

I build the Go APIs behind those edits and work on the TypeScript web app players use to submit them. One design decision came directly from running a shared directory. If someone moves a cabinet from the first floor to the second, another player saving an older listing could erase that correction. Musecat keeps the earlier revision, records who changed it, and detects the stale edit. [Read the regression test](https://github.com/ericbaek/Musecat-Backend-Core/commit/624a8b244164e358b383b48d78417488eec857b3)

Two more examples from the backend are [keeping XP consistent when a post is deleted](https://github.com/ericbaek/Musecat-Backend-Core/pull/42) and [separating the public API from production migrations](https://github.com/ericbaek/Musecat-Backend-Core/blob/main/docs/architecture-contract.md).
