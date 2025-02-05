# Network Models -- Project Management
For this assignment, linear programming and network modelling concepts were used to create a project plan for a client interested in a consumer-focused restaurant recommendation system app.

## Setting Up the Problem
The objective is to find the minimun cost of the project. A spreadsheet containing the 16 tasks needed to be completed for the project as well as any predecessor relationships was provided. Each task represented its own decision variable with the hours as the lower bound. The problem was run a total of 3 times for each scenario (best, expected, worst). 

![](https://github.com/sallydlee/msds460-network-models/blob/main/misc/project-plan-1.PNG?raw=true)
![](https://github.com/sallydlee/msds460-network-models/blob/main/misc/project-plan-2.PNG?raw=true)

## Solving the Problem
For the best-case scenario, the linear programming model returned a total minimum cost of $188000.00. For the expected scenario, the linear programming model returned a total minimum cost of $298000.00. For the worst-case scenario, the linear programming model returned a total minimum cost of $476000.00.

## GenAI Tools
ChatGPT was utilized to estimate the duration of each task for the best-case, expected, and worst-case scenario. The entire conversation and prompts can be read in the `ChatGPT conversation.txt` file.
