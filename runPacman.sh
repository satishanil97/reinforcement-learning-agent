#!/bin/sh

approximateQAgentRun() {
    count=$1
    layout=$2
    outputFileName="console_${layout}_ApproximateQAgent.txt"
    echo "Count ${count}"
    echo ""
    echo "Layout ${layout}"
    echo ""
    echo "OutputFileName ${outputFileName}"
    echo ""
    for i in $(seq $count); do
        python pacman.py -p ApproximateQAgent -a extractor=SimpleExtractor -x 2000 -n 2000 -l "$layout" > "$outputFileName"
        echo "COMPLETED $i RUNS of ApproximateQAgent"
        echo ""
    done
}

episodicSemiGradientSarsaAgentRun() {
    count=$1
    layout=$2
    outputFileName="console_${layout}_EpisodicSemiGradientSarsaAgent.txt"
    echo "OutputFileName ${outputFileName}"
    for i in $(seq $count); do
        python pacman.py -p EpisodicSemiGradientSarsaAgent -a extractor=SimpleExtractor -x 2000 -n 2000 -l "$layout" > "$outputFileName"
        echo "COMPLETED $i RUNS of EpisodicSemiGradientSarsaAgent"
        echo ""
    done
}

trueOnlineSarsaAgentRun() {
    count=$1
    layout=$2
    outputFileName="console_${layout}_TrueOnlineSarsaAgent.txt"
    echo "OutputFileName ${outputFileName}"
    echo ""
    for i in $(seq $count); do
        python pacman.py -p TrueOnlineSarsaAgent -a extractor=SimpleExtractor -x 2000 -n 2000 -l "$layout" > "$outputFileName"
        echo "COMPLETED $i RUNS of TrueOnlineSarsaAgent"
        echo ""
    done
}

echo "Starting Pacman Runs"
approximateQAgentRun $1 $2 >> $3 2>&1 &
episodicSemiGradientSarsaAgentRun $1 $2 >> $3 2>&1 &
trueOnlineSarsaAgentRun $1 $2 >> $3 2>&1 &
echo "Ended Pacman Runs"