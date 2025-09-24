### **Prompt**

```
I want to create an ADK AI Agent for the customers of realtors. There are 2 key pieces of functionality I want to incorporate.
1) allow you to search for homes within a zip code and a price point
2) upload a picture and virtually stage it with furniture

Write a design document for this application using Google ADK Framework (https://github.com/google/adk-python) and VertexAI for the the image generation.
```

# 

# **Real Estate AI Agent \- Design Document**

## **1\. Introduction**

This document outlines the design for a Real Estate AI Agent built using the Google Agent Development Kit (ADK). The agent is designed to assist the customers of realtors with two primary functionalities: searching for homes and virtually staging rooms.

The agent will provide a conversational interface for users to find properties based on their criteria and to visualize the potential of a space by adding virtual furniture to uploaded images. This will be achieved by leveraging the power of Google's ADK for agent creation and Vertex AI for advanced image generation.

## **2\. System Architecture**

The system will be composed of a central ADK agent that orchestrates the different functionalities. The agent will use a set of tools to interact with external services, such as a real estate data provider and the Vertex AI API.

The architecture will consist of the following components:

* **ADK Agent:** The core of the application, responsible for understanding user requests and invoking the appropriate tools.  
* **Home Search Tool:** A custom tool that connects to a real estate API to fetch property listings.  
* **Virtual Staging Tool:** A tool that uses the Vertex AI API to generate virtually staged images.  
* **Real Estate API:** An external service that provides data on property listings (e.g., Zillow API, Realtor.com API).  
* **Vertex AI:** Google's AI platform, which will be used for the text-to-image generation required for virtual staging.

## **3\. ADK Agent Design**

The agent will be built using the Python ADK. The core logic of the agent will be defined in an agent.py file.

### **3.1. Core Agent (agent.py)**

The main agent will be configured with the following:

* **Name:** RealEstateAssistant  
* **Description:** An AI agent to help with home searching and virtual staging.  
* **Model:** A Gemini model (e.g., gemini-pro) for natural language understanding and generation.  
* **Tools:** The agent will be equipped with the HomeSearchTool and VirtualStagingTool.

### **3.2. Tools**

#### **3.2.1. Home Search Tool**

This tool will be a custom Python function that takes a user's query, extracts the relevant information (zip code and price range), and then makes a request to a real estate API.

**Function Signature:**

def search\_homes(zip\_code: str, max\_price: int) \-\> list:  
    """  
    Searches for homes in a given zip code up to a maximum price.  
    """  
    \# ... logic to call a real estate API ...  
    return properties

The tool will parse the results from the API and return a formatted list of properties to the agent, which can then be presented to the user.

#### **3.2.2. Virtual Staging Tool**

This tool will handle the image staging functionality. It will take an image file and a text prompt describing the desired style of furniture and then use Vertex AI to generate a new image.

**Function Signature:**

def stage\_image(image\_path: str, style\_prompt: str) \-\> str:  
    """  
    Virtually stages an image with furniture based on a style prompt.  
    """  
    \# ... logic to call the Vertex AI API ...  
    return generated\_image\_url

The tool will be responsible for constructing the appropriate prompt for the Vertex AI API and handling the response.

## **4\. Virtual Staging with Vertex AI**

The virtual staging feature will be powered by Vertex AI's image generation capabilities. The process will be as follows:

1. The user uploads an image of a room.  
2. The user provides a text prompt describing the desired style (e.g., "modern, minimalist furniture with a neutral color palette").  
3. The Virtual Staging Tool sends the image and prompt to the Vertex AI API.  
4. Vertex AI generates a new image with the virtual furniture and returns it to the agent.  
5. The agent presents the staged image to the user.

### **4.1. Prompt Engineering**

To ensure high-quality results, the prompts sent to Vertex AI will be carefully constructed. The agent can be trained to ask clarifying questions to help the user build a more effective prompt. For example, it might ask about preferred colors, materials, or specific pieces of furniture.

## **5\. Data Flow**

The following diagrams illustrate the data flow for the two main functionalities:

**Home Search:**

User \-\> ADK Agent \-\> Home Search Tool \-\> Real Estate API \-\> Home Search Tool \-\> ADK Agent \-\> User

**Virtual Staging:**

User \-\> ADK Agent \-\> Virtual Staging Tool \-\> Vertex AI API \-\> Virtual Staging Tool \-\> ADK Agent \-\> User  
