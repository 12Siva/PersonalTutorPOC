# Personal Tutor Agent
Proof of concept for a personal tutor agent

# Target Audience
High school / college students in developing countries. We'll start with Latin America. 

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
    - User selects yes/no if    


# System Design
![System Diagram](https://github.com/12Siva/PersonalTutorPOC/blob/4dc35c8ce2eee9812f649c60cba32ebdb2a88f78/System%20Design.png)


## Example Bard conversation given the prompt
![Screenshot 2023-05-03 at 3 28 04 AM](https://user-images.githubusercontent.com/7332619/235893539-a0739f5e-9157-48c3-a105-9fe1dc9065c6.png)

![Screenshot 2023-05-03 at 3 37 07 AM](https://user-images.githubusercontent.com/7332619/235893764-d467bf28-9855-4019-9420-6c916aae41c9.png)

### Development Resources

#### Implementation Details
* Steamship-packages - https://github.com/steamship-packages - Wrapper for the LLM model workflows
    
    [Reference](https://www.youtube.com/live/vw-KWfKwvTQ?feature=share)
* One option for LLM model API is via Google PaLM and MakerSuite 

    [Reference](https://developers.googleblog.com/2023/03/announcing-palm-api-and-makersuite.html)

### Expected Questions
1. How will students discover this service?

2. Will students return to this service?
    - We plan to launch a companion app / game.
  
