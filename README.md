# Software engineer & project lead at Musecat

I’ve led development and run **Musecat** since its launch in June 2023. Players use it to find a game near them, update cabinet listings, and report faults. The directory started with **45 arcades**.

**Backend** · I designed and built both Go backends on my own. Core handles the API and edit history. Full runs the production service and migrates the live database.  
**Frontend** · A web designer and I co-developed the TypeScript web app players use.

| Arcades listed | Page views | Directory edits | Fault reports |
| ---: | ---: | ---: | ---: |
| **3,264** | **1.62M** | **21,226** | **2,091** |

As of 14 Nov 2026. Page views counted since 28 Feb 2026. [Explore Musecat](https://musecat.app/en) · [Three years of releases](https://musecat.app/en/community/updates)

### Inside the backend

- **When two players edit the same cabinet.** If one moves it from floor 1 to floor 2, the API catches a later save based on the old listing. The test checks both the conflict and the edit history. [Read the Go test](https://github.com/ericbaek/Musecat-Backend-Core/blob/624a8b244164e358b383b48d78417488eec857b3/tests/arcade/game_state_v2_test.go#L41-L105)
- **When a player deletes a post.** The backend revokes its XP exactly once. If deletion fails, the XP change rolls back with it. [See the pull request and tests](https://github.com/ericbaek/Musecat-Backend-Core/pull/42)
- **When the API changes.** The production service pins a tested Core version so I can test an API change before rolling it out to the live database. [Read the Core and Full architecture contract](https://github.com/ericbaek/Musecat-Backend-Core/blob/main/docs/architecture-contract.md)

As of 14 Nov 2026, I had authored [35 merged pull requests in Musecat Backend Core](https://github.com/ericbaek/Musecat-Backend-Core/pulls?q=is%3Apr+is%3Amerged+author%3Aericbaek+merged%3A%3C%3D2026-11-14).
