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

To run pacman agent n times, run: python pacman.py n <..rem args>

Below samples show command to run once

To run normal qLearning agent

python pacman.py 1 -p ApproximateQAgent -a extractor=SimpleExtractor -x 1000 -n 1000 -l originalClassic

To run EpisodicSemiGradientSarsaAgent

python pacman.py 3 -p EpisodicSemiGradientSarsaAgent -a extractor=SimpleExtractor -x 1000 -n 1000 -l smallClassic

To run TrueOnlineSarsaAgent

with default lambda=0.5

python pacman.py 3 -p TrueOnlineSarsaAgent -a extractor=SimpleExtractor -x 1000 -n 1000 -l smallClassic

with custom lambda

python pacman.py 1 -p TrueOnlineSarsaAgent -a extractor=SimpleExtractor,traceDecayRate=0.9 -x 2000 -n 2000 -l smallGrid

python pacman.py 1 -p TrueOnlineSarsaAgent -a extractor=SimpleExtractor,traceDecayRate=0.9 -x 1000 -n 1000 -l smallGrid

#### Short Testing observations of runtime ####

approx training time per 100 episodes for envs for ApproximateQAgent (on M1 macbook):

very low (< 2 sec): smallGrid, mediumGrid, smallClassic, testClassic, trappedClassic, minimaxClassic

low (< 10 sec): capsuleClassic

moderate (< 15 sec): powerClassic, contestClassic, mediumClassic

high (< 20 sec): openClassic

too high (> 20 sec): trickyClassic (29.22), originalClassic (112.97)


#### Testing Strategy ####

epsilon=0.05,gamma=0.8,alpha=0.2 (default values of project 4)

Run each layout-algo combination for 25 runs (in python 3.6 conda env of cse571)

Agents: ApproximateQAgent, EpisodicSemiGradientSarsaAgent, TrueOnlineSarsaAgent

Environments Set 1: smallGrid, smallClassic, trappedClassic, capsuleClassic, originalClassic

Environments Set 2: mediumGrid, testClassic, minimaxClassic, powerClassic, openClassic, trickyClassic, contestClassic, mediumClassic

lamda values to test: 0.2, 0.4, 0.6, 0.8, 1

lambda_map: {1:0.2, 2:0.4, 3:0.6, 4:0.8, 5:1}

2 people split testing. One person takes up <Environment Set 1>, the other takes up <Environment Set 2>

Each person does the following to run tests in background:

activate virtual environment cse571

for layout in env_set {

    # output_redirect_file format for non-lamda agents: console_<layout>_<agent>.txt

    python pacman.py 25 -p ApproximateQAgent -a extractor=SimpleExtractor -x 2000 -n 2000 -l layout > output_redirect_file 2>&1 &

    python pacman.py 25 -p EpisodicSemiGradientSarsaAgent -a extractor=SimpleExtractor -x 2000 -n 2000 -l layout > output_redirect_file 2>&1 &

    for key, lambda_value in lambda_map {

        # output_redirect_file format for true online sarsa: console_<layout>_<agent>_<key>.txt
        
        python pacman.py 25 -p TrueOnlineSarsaAgent -a extractor=SimpleExtractor,traceDecayRate=lambda_value -x 2000 -n 2000 -l layout > output_redirect_file 2>&1 &

    }
    
}

Leave programs running overnight