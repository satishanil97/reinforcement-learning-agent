# reinforcement-learning-agent
CSE 571 AI Team Project Group 1 - Topic 5: Reinforcement Learning Agent

Relevant Parts of code:

pacman.py -> runGames: runs pacman world agents for specified number of runs

game.py -> run: runs each episode of pacman world agents

game.py -> run -> executeSarsaPacman: runs each episode of pacman agent

learningAgents.py -> ReinforcementAgent: base class of pacman refinforcement learning agent with default behaviour

qlearningAgents.py -> ApproximateQAgent: class of pacman agent for project 4

qlearningAgents.py -> ApproximateQAgentSarsa: class of pacman agent with sarsa flow (this class overrides all methods needed to change behaviour for sarsa flow)

qlearningAgents.py -> EpisodicSemiGradientSarsaAgent: class to implement Episodic Semi Gradient Sarsa algorithm (extends ApproximateQAgentSarsa)

qlearningAgents.py -> TrueOnlineSarsaAgent: class to implement True Online Sarsa algorithm (extends ApproximateQAgentSarsa)

To run normal qLearning agent

python pacman.py -p ApproximateQAgent -a extractor=SimpleExtractor -x 2000 -n 2000 -l smallGrid

To run EpisodicSemiGradientSarsaAgent

python pacman.py -p EpisodicSemiGradientSarsaAgent -a extractor=SimpleExtractor -x 2000 -n 2000 -l smallGrid

To run TrueOnlineSarsaAgent

with default lambda=0.5

python pacman.py -p TrueOnlineSarsaAgent -a extractor=SimpleExtractor -x 2000 -n 2000 -l smallGrid

with custom lambda

python pacman.py -p TrueOnlineSarsaAgent -a extractor=SimpleExtractor,traceDecayRate=0.9 -x 2000 -n 2000 -l smallGrid