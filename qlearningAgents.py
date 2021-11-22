# qlearningAgents.py
# ------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from game import *
from learningAgents import ReinforcementAgent
from featureExtractors import *

import random,util,math

class QLearningAgent(ReinforcementAgent):
    """
      Q-Learning Agent

      Functions you should fill in:
        - computeValueFromQValues
        - computeActionFromQValues
        - getQValue
        - getAction
        - update

      Instance variables you have access to
        - self.epsilon (exploration prob)
        - self.alpha (learning rate)
        - self.discount (discount rate)

      Functions you should use
        - self.getLegalActions(state)
          which returns legal actions for a state
    """
    def __init__(self, **args):
        "You can initialize Q-values here..."
        ReinforcementAgent.__init__(self, **args)

        "*** YOUR CODE HERE ***"
        self.qValues = util.Counter()

    def getQValue(self, state, action):
        """
          Returns Q(state,action)
          Should return 0.0 if we have never seen a state
          or the Q node value otherwise
        """
        "*** YOUR CODE HERE ***"
        if (state,action) not in self.qValues:
          return 0.0
        return self.qValues[(state,action)]
        # util.raiseNotDefined()


    def computeValueFromQValues(self, state):
        """
          Returns max_action Q(state,action)
          where the max is over legal actions.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return a value of 0.0.
        """
        "*** YOUR CODE HERE ***"
        legalActions = self.getLegalActions(state)
        if legalActions is None or len(legalActions) == 0:
          return 0.0
        return max([self.getQValue(state,action) for action in legalActions])
        # util.raiseNotDefined()

    def computeActionFromQValues(self, state):
        """
          Compute the best action to take in a state.  Note that if there
          are no legal actions, which is the case at the terminal state,
          you should return None.
        """
        "*** YOUR CODE HERE ***"
        legalActions = self.getLegalActions(state)
        if legalActions is None or len(legalActions) == 0:
          return None
        maxQValue = self.computeValueFromQValues(state)
        maxActions = []
        for action in legalActions:
          if self.getQValue(state,action) == maxQValue:
            maxActions.append(action)
        return random.choice(maxActions)
        # util.raiseNotDefined()

    def getAction(self, state):
        """
          Compute the action to take in the current state.  With
          probability self.epsilon, we should take a random action and
          take the best policy action otherwise.  Note that if there are
          no legal actions, which is the case at the terminal state, you
          should choose None as the action.

          HINT: You might want to use util.flipCoin(prob)
          HINT: To pick randomly from a list, use random.choice(list)
        """
        # Pick Action
        legalActions = self.getLegalActions(state)
        action = None
        "*** YOUR CODE HERE ***"
        if util.flipCoin(self.epsilon):
          action = random.choice(legalActions)
        else:
          return self.computeActionFromQValues(state)
        # util.raiseNotDefined()

        return action

    def update(self, state, action, nextState, reward):
        """
          The parent class calls this to observe a
          state = action => nextState and reward transition.
          You should do your Q-Value update here

          NOTE: You should never call this function,
          it will be called on your behalf
        """
        "*** YOUR CODE HERE ***"
        currQValue = self.getQValue(state, action)
        newSampleEstimate = reward + self.discount * self.computeValueFromQValues(nextState)
        self.qValues[(state,action)] = (1-self.alpha)*currQValue + self.alpha*newSampleEstimate 
        # util.raiseNotDefined()

    def getPolicy(self, state):
        return self.computeActionFromQValues(state)

    def getValue(self, state):
        return self.computeValueFromQValues(state)


class PacmanQAgent(QLearningAgent):
    "Exactly the same as QLearningAgent, but with different default parameters"

    def __init__(self, epsilon=0.05,gamma=0.8,alpha=0.2, numTraining=0, **args):
        """
        These default parameters can be changed from the pacman.py command line.
        For example, to change the exploration rate, try:
            python pacman.py -p PacmanQLearningAgent -a epsilon=0.1

        alpha    - learning rate
        epsilon  - exploration rate
        gamma    - discount factor
        numTraining - number of training episodes, i.e. no learning after these many episodes
        """
        args['epsilon'] = epsilon
        args['gamma'] = gamma
        args['alpha'] = alpha
        args['numTraining'] = numTraining
        self.index = 0  # This is always Pacman
        self.isSarsaAgent = False
        QLearningAgent.__init__(self, **args)

    def getAction(self, state):
        """
        Simply calls the getAction method of QLearningAgent and then
        informs parent of action for Pacman.  Do not change or remove this
        method.
        """
        action = QLearningAgent.getAction(self,state)
        self.doAction(state,action)
        return action


class ApproximateQAgent(PacmanQAgent):
    """
       ApproximateQLearningAgent

       You should only have to overwrite getQValue
       and update.  All other QLearningAgent functions
       should work as is.
    """
    def __init__(self, extractor='IdentityExtractor', **args):
        self.featExtractor = util.lookup(extractor, globals())()
        PacmanQAgent.__init__(self, **args)
        self.weights = util.Counter()

    def getWeights(self):
        return self.weights

    def getQValue(self, state, action):
        """
          Should return Q(state,action) = w * featureVector
          where * is the dotProduct operator
        """
        "*** YOUR CODE HERE ***"
        featureVector = self.featExtractor.getFeatures(state, action)
        weightVector = self.weights
        return sum([weightVector[feature]*featureVector[feature] for feature in featureVector])
        # util.raiseNotDefined()

    def update(self, state, action, nextState, reward):
        """
           Should update your weights based on transition
        """
        "*** YOUR CODE HERE ***"
        difference = (reward + self.discount*self.computeValueFromQValues(nextState)) - self.getQValue(state, action)
        featureVector = self.featExtractor.getFeatures(state, action)
        for feature in featureVector:
          self.weights[feature] = self.weights[feature] + self.alpha*difference*featureVector[feature]
        # util.raiseNotDefined()

    def final(self, state):
        "Called at the end of each game."
        # call the super-class final method
        PacmanQAgent.final(self, state)

        # did we finish training?
        if self.episodesSoFar == self.numTraining:
            # you might want to print your weights here for debugging
            "*** YOUR CODE HERE ***"
            pass

# SARSA Logic
class ApproximateQAgentSarsa(ApproximateQAgent):
    """
       ApproximateQAgentSarsa
    """
    def __init__(self, extractor='IdentityExtractor', **args):
        ApproximateQAgent.__init__(self, extractor, **args)
        # SARSA Logic
        self.isSarsaAgent = True

    def getQValue(self, state, action):
        """
          Should return Q(state,action) = w * featureVector
          where * is the dotProduct operator
        """
        "*** YOUR CODE HERE ***"
        # Handling Q(terminalState, Action) = 0.0 for Sarsa
        if state.isWin() or state.isLose():
          return 0.0
        return ApproximateQAgent.getQValue(self, state, action)

    def observationFunction(self, state, action):
        """
            This is where we ended up after our last action.
            The simulation should somehow ensure this is called
        """
        if not self.lastState is None:
            reward = state.getScore() - self.lastState.getScore()
            self.observeTransition(self.lastState, self.lastAction, state, action, reward)
        return state

    def observeTransition(self, state,action,nextState,nextAction,deltaReward):
        """
            Called by environment to inform agent that a transition has
            been observed. This will result in a call to self.update
            on the same arguments
        """
        self.episodeRewards += deltaReward
        # SARSA Logic
        self.update(state,action,nextState,nextAction,deltaReward)

    def update(self, state, action, nextState, nextAction, reward):
        """
           Should update your weights based on transition
        """
        "*** YOUR CODE HERE ***"
        difference = (reward + self.discount*self.getQValue(nextState, nextAction)) - self.getQValue(state, action)
        featureVector = self.featExtractor.getFeatures(state, action)
        for feature in featureVector:
          self.weights[feature] = self.weights[feature] + self.alpha*difference*featureVector[feature]
        # util.raiseNotDefined()

    def getAction(self, state):
        """
        Simply calls the getAction method of QLearningAgent
        """
        action = QLearningAgent.getAction(self,state)
        return action
    
    def final(self, state):
        "Called at the end of each game."
        # call the super-class final method
        # PacmanQAgent.final(self, state)
        deltaReward = state.getScore() - self.lastState.getScore()
        self.observeTransition(self.lastState, self.lastAction, state, None, deltaReward)
        self.stopEpisode()

        # Make sure we have this var
        if not 'episodeStartTime' in self.__dict__:
            self.episodeStartTime = time.time()
        if not 'lastWindowAccumRewards' in self.__dict__:
            self.lastWindowAccumRewards = 0.0
        self.lastWindowAccumRewards += state.getScore()

        # SARSA Logic, Setting reward update frequency
        NUM_EPS_UPDATE = 100
        if self.episodesSoFar % NUM_EPS_UPDATE == 0:
            print('Reinforcement Learning Status:')
            windowAvg = self.lastWindowAccumRewards / float(NUM_EPS_UPDATE)
            if self.episodesSoFar <= self.numTraining:
                trainAvg = self.accumTrainRewards / float(self.episodesSoFar)
                print('\tCompleted %d out of %d training episodes' % (
                       self.episodesSoFar,self.numTraining))
                print('\tAverage Rewards over all training: %.2f' % (
                        trainAvg))
            else:
                testAvg = float(self.accumTestRewards) / (self.episodesSoFar - self.numTraining)
                print('\tCompleted %d test episodes' % (self.episodesSoFar - self.numTraining))
                print('\tAverage Rewards over testing: %.2f' % testAvg)
            print('\tAverage Rewards for last %d episodes: %.2f'  % (
                    NUM_EPS_UPDATE,windowAvg))
            print('\tEpisode took %.2f seconds' % (time.time() - self.episodeStartTime))
            self.lastWindowAccumRewards = 0.0
            self.episodeStartTime = time.time()

        if self.episodesSoFar == self.numTraining:
            msg = 'Training Done (turning off epsilon and alpha)'
            print('%s\n%s' % (msg,'-' * len(msg)))

        # did we finish training?
        if self.episodesSoFar == self.numTraining:
            # you might want to print your weights here for debugging
            "*** YOUR CODE HERE ***"
            pass

class EpisodicSemiGradientSarsaAgent(ApproximateQAgentSarsa):
    """
       EpisodicSemiGradientSarsaAgent

       You should only have to overwrite the update function.  All other QLearningAgent functions
       should work as is.
    """
    def __init__(self, extractor='IdentityExtractor', **args):
        ApproximateQAgentSarsa.__init__(self, extractor, **args)

    def update(self, state, action, nextState, nextAction, reward):
        """
           Should update your weights based on transition
        """
        "*** YOUR CODE HERE ***"
        difference = (reward + self.discount*self.getQValue(nextState, nextAction)) - self.getQValue(state, action)
        featureVector = self.featExtractor.getFeatures(state, action)
        for feature in featureVector:
          self.weights[feature] = self.weights[feature] + self.alpha*difference*featureVector[feature]
        # util.raiseNotDefined()

class TrueOnlineSarsaAgent(ApproximateQAgentSarsa):
    """
       TrueOnlineSarsaAgent

       You should only have to overwrite the update function.  All other QLearningAgent functions
       should work as is.
    """
    def __init__(self, extractor='IdentityExtractor', traceDecayRate=0.5, **args):
        ApproximateQAgentSarsa.__init__(self, extractor, **args)
        self.traceDecayRate = float(traceDecayRate)

    def startEpisode(self):
        """
          Called by environment when new episode is starting
        """
        ApproximateQAgentSarsa.startEpisode(self)
        # initializing Q_old and z for each episode in true online sarsa algorithm
        self.Q_old = 0.0
        self.eligiblityTrace = util.Counter()

    def update(self, state, action, nextState, nextAction, reward):
        """
           Should update your weights based on transition
        """
        "*** YOUR CODE HERE ***"
        Q_value = self.getQValue(state, action)
        Q_dash = self.getQValue(nextState, nextAction)
        delta = (reward + self.discount*Q_dash) - Q_value
        featureVector = self.featExtractor.getFeatures(state, action)
        dot_product = sum([self.eligiblityTrace[feature]*featureVector[feature] for feature in featureVector])
        
        for feature in featureVector:
          self.eligiblityTrace[feature] = (self.discount * self.traceDecayRate * self.eligiblityTrace[feature]) + \
            (1 - self.alpha*self.discount*self.traceDecayRate*dot_product)*featureVector[feature]
        
        for feature in featureVector:
          self.weights[feature] = self.weights[feature] + (self.alpha * (delta + Q_value - self.Q_old) * \
            self.eligiblityTrace[feature]) - (self.alpha * (Q_value - self.Q_old) * featureVector[feature])

          self.Q_old = Q_dash

        # util.raiseNotDefined()