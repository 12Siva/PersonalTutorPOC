# Atlas 🌎🌍🌏

### Overview
> 🚀 Everything you need to build your own AI agent for tutoring! 🚀

# 🌊 Quick Start Guide

Prerequisites:  [Python](https://www.tutorialspoint.com/python/python_quick_guide.htm) plus [Typescript](https://www.typescriptlang.org/docs/)

> Check out the package locally
```bash
gh repo clone 12Siva/PersonalTutorPOC
```

> Leverage the python virtual environment to bootstrap the dependencies [TODO](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)
```
https://packaging.python.org/en/latest/discussions/wheel-vs-egg/ 
```

# Documentaion 📚
Documentation, tutorials, challenges, and many more resources, visit: docs.atlas.io

# 🔭 Learning Atlas
📕 Read the docs: https://docs.atlas.org

📚Go through each of the dependencies for this library:

    * VirtualEnv: https://docs.python.org/3/library/venv.html
    * Django: https://docs.djangoproject.com/en/4.2/
    * AWS: https://docs.aws.amazon.com/
    * Terraform: https://terraform-docs.io/
    * Polychain: https://github.com/polynetwork/docs/blob/master/cosmos/README.md
    * ETH wrapper: https://github.com/scaffold-eth/scaffold-eth/blob/matic/README.md
    * OpenSea: https://opensea.io/


# High Level Overview

# System Design
![System Diagram](https://github.com/12Siva/PersonalTutorPOC/blob/4dc35c8ce2eee9812f649c60cba32ebdb2a88f78/System%20Design.png)

Figure A: In the above simplified system diagram we outline how a user will interact with the LLM model to create a personal tutor agent.

### Sequence Diagram
![Screenshot 2023-05-07 at 10 39 09 AM](https://user-images.githubusercontent.com/7332619/236693523-8f058215-b493-43a0-9026-fdddc532312e.png) 

_💥 Note: The above diagram is outdated as of 5/9/2023 💥_ 

# Objective 
Leverage a large language model such as ChatGPT or Google's BARD to act as a tutor.

The tutor agent will be confined to a single subject such as photography.
The tutor agent will create a set of topics for the subject.

For example, some topics for the subject of photography will be:
    
    * Composition - creative topic
    
    * Lighting - creative topic
    
    * Lenses - technical topic

The agent will then create reminders to test the knowledge of a previous topic or teach a new topic.



# UI/UX Flow

- User inputs what subject they want to learn
- AI will outline what are the main topics of the subject
- User sees main topics of the subject
    - User selects yes/no if the topics are satisfactory  

##### TODO
1. Add illustration of how the memory managment game / Flash Cards will look like

    Step 1: Learn Illustrator
        - maybe we can leverage Google Spreadsheets for this?

    Step 2: Upload screen mock-ups to github repository

    Step 3: Add them to README.md and to PressRelease.md under the 2nd pivot chapter (crypto-currency section)
    
2. Add FAQ Section to PressRelease.md to generate the PRFAQ doc



## Example Bard conversation given the prompt
![Screenshot 2023-05-03 at 3 28 04 AM](https://user-images.githubusercontent.com/7332619/235893539-a0739f5e-9157-48c3-a105-9fe1dc9065c6.png)

![Screenshot 2023-05-03 at 3 37 07 AM](https://user-images.githubusercontent.com/7332619/235893764-d467bf28-9855-4019-9420-6c916aae41c9.png)

### Development Resources

#### Implementation Details
1. Steamship-packages - https://github.com/steamship-packages - Wrapper for the LLM model workflows
    
    [Reference](https://www.youtube.com/live/vw-KWfKwvTQ?feature=share)
1. One option for LLM model API is via Google PaLM and MakerSuite [Reference](https://developers.googleblog.com/2023/03/announcing-palm-api-and-makersuite.html)

1. We are leveraging the OpenAI LLM [Reference](https://platform.openai.com/docs/api-reference?lang=python)

### Expected Questions
1. How will students discover this service?

2. Will students return to this service?
    - We plan to launch a companion app / game.
    - Similar to the kids mental math game used with flash cards. We'll reward completion of the game with minted NFTs.

3. What will the minted NFTs look like?
    - Like baseball / Pokemon trading cards
    ![Screenshot 2023-05-06 at 1 39 11 PM](https://user-images.githubusercontent.com/7332619/236645750-62c37547-ac72-49ce-af9f-dcf1a0b0d83a.png)

4. How should we charge for this service?

5. What keeps the student engaged with the service?

6. What are the foundational models this is built on top of?

7. How will we mint the NFTs?


### Future Work

1. Proof of concept for minting NFTs on OpenSea


2. Go through to learn corporate finance for Pitchbook:


![Screenshot 2023-05-10 at 8 23 12 PM](https://github.com/12Siva/PersonalTutorPOC/assets/7332619/a9ed0ff4-7bd3-4769-83e5-1fd13b508566)
