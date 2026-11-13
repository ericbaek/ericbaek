# Eric Baek · Software Engineer

I lead **Musecat**, a community platform where players find arcade games and report broken machines. I’ve run it for **over three years**, growing the directory from **45 arcades at launch in June 2023 to 3,264**. I built both Go backends myself and co-developed the TypeScript web app with a web designer.

| Page views | Directory edits | Machine fault reports |
| --- | --- | --- |
| **1.62 million** since 28 Feb 2026 | **21,226** | **2,091** |

Figures as of 14 Nov 2026. [Explore Musecat](https://musecat.app/en) · [Follow its development from launch](https://musecat.app/en/community/updates)

### Engineering decisions from running Musecat

- **Protecting community edits.** If one player moves a cabinet listing from 1F to 2F, saving an older version could erase that correction. The API detects the stale edit and keeps a history of who changed what. [Read the Go regression test](https://github.com/ericbaek/Musecat-Backend-Core/commit/624a8b244164e358b383b48d78417488eec857b3)
- **Keeping rewards consistent.** Deleting a post should revoke its XP exactly once. If deletion fails, the XP change rolls back too. [Review the implementation and tests](https://github.com/ericbaek/Musecat-Backend-Core/pull/42)
- **Shipping changes to a live database.** Backend Core defines the API and its rules. Backend Full pins a tested Core version and owns production migrations, so I can evolve the public API and control when a change reaches existing data. [Read the architecture contract](https://github.com/ericbaek/Musecat-Backend-Core/blob/main/docs/architecture-contract.md)
