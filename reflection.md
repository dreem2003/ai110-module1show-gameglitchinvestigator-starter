# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
    - **Slow to start up, but thats streamlit.**
    - **The attempts were lower than when refreshed to start a new game**
- List at least two concrete bugs you noticed at the start
    - **Hints are backwards**
    - **session state when a game is won or lost does not refresh, so new game cannot be started**
    - **Button clicks are chunky and take time**
    - **Easy mode and hard mode give numbers out of range**


---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  - **Cursor agents**
  - **Claude code**
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  - **Fixing attempts on initial loading**
  - **Higher, lower hint switch**
  - **Test cases generated**
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  - **It got nothin gwrong surprisingly, aside from annoying inline suggestions lol**

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  - **Testing through the streamlit web app**
  - **Creating and running test cases for specific function**
- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
  - **Tested the full game mode on the web app and ran through guessing numbers using the correctly fixed hints. The games pretty easy**
- Did AI help you design or understand any tests? How?
  **- Yes it designed the tests based off the specific problems i brought up. I crosschecked it did it well.**

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
  - **Did not notice this, but I've worked with streamlit prior and know numbers that aerent specifically saved as a session stae reset whenever there is an event, like clikcing a button.**
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
    - **While you have the server active Streamlit periodically gets amnesia, unless you tattoo what you want to keep on its eyelids. When the server is shutdown however you find out that the tattoos are really the fake ones that wash out when you take a shower.**
- What change did you make that finally gave the game a stable secret number?
  - **The secret was already a designated sessionsstate**

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - **Working quickly with testing especially on nonprod environments**
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
  - **Grill the AI a bit more**
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  - **Extremely fast at testing and working through issues as well as brainstorming potential issues**
