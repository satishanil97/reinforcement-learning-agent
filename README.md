# reinforcement-learning-agent
CSE 571 AI Team Project Group 1 - Topic 5: Reinforcement Learning Agent

To run normal qLearning agent:
python pacman.py -p ApproximateQAgent -a extractor=SimpleExtractor -x 2000 -n 2000 -l smallGrid

To run EpisodicSemiGradientSarsaAgent:
python pacman.py -p EpisodicSemiGradientSarsaAgent -a extractor=SimpleExtractor -x 2000 -n 2000 -l smallGrid

To run TrueOnlineSarsaAgent:
with default lambda=0.5:
python pacman.py -p TrueOnlineSarsaAgent -a extractor=SimpleExtractor -x 2000 -n 2000 -l smallGrid
with custom lambda:
python pacman.py -p TrueOnlineSarsaAgent -a extractor=SimpleExtractor,traceDecayRate=0.9 -x 2000 -n 2000 -l smallGrid