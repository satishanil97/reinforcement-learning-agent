# reinforcement-learning-agent
CSE 571 AI Team Project Group 1 - Topic 5: Reinforcement Learning Agent

The main motivation of this project is to understand the differences in learning performance of three model-free RL algorithms with similar exploitation strategies but varying exploration strategies: 

+ Q-learning - an off-policy learning algorithm
+ Episodic semi-gradient SARSA - an on-policy algorithm
+ True online SARSA - an on-policy algorithm 

All the experiments are executed in the ‘Pacman domain’ where the Pacman learning agent learns to navigate a maze to obtain food pellets while avoiding deadly ghosts.

#### Team Members ####
@punarvasu510

Relevant Parts of code:

pacman.py -> runGames: runs pacman world agents for specified number of runs

game.py -> run: runs each episode of pacman world agents

game.py -> run -> executeSarsaPacman: runs each episode of pacman agent

learningAgents.py -> ReinforcementAgent: base class of pacman refinforcement learning agent with default behaviour

qlearningAgents.py -> ApproximateQAgent: class of pacman agent for project 4

qlearningAgents.py -> ApproximateQAgentSarsa: class of pacman agent with sarsa flow (this class overrides all methods needed to change behaviour for sarsa flow)

qlearningAgents.py -> EpisodicSemiGradientSarsaAgent: class to implement Episodic Semi Gradient Sarsa algorithm (extends ApproximateQAgentSarsa)

qlearningAgents.py -> TrueOnlineSarsaAgent: class to implement True Online Sarsa algorithm (extends ApproximateQAgentSarsa)


Below samples show command to run agent once

To run normal qLearning agent

python pacman.py -p ApproximateQAgent -a extractor=SimpleExtractor -x 2000 -n 2000 -l originalClassic

To run EpisodicSemiGradientSarsaAgent

python pacman.py -p EpisodicSemiGradientSarsaAgent -a extractor=SimpleExtractor -x 1000 -n 1000 -l smallClassic

To run TrueOnlineSarsaAgent

with default lambda=0.4

python pacman.py -p TrueOnlineSarsaAgent -a extractor=SimpleExtractor -x 2000 -n 2000 -l smallClassic

with custom lambda

python pacman.py -p TrueOnlineSarsaAgent -a extractor=SimpleExtractor,traceDecayRate=0.9 -x 2000 -n 2000 -l smallGrid

#### To plot graphs #### 
Change the path of input csv file in Cell 2 of PlotGraphs_v3.ipynb

Then run all the cells
