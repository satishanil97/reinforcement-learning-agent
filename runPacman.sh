count=25
for i in $(seq $count); do
    python pacman.py -p ApproximateQAgent -a extractor=SimpleExtractor -x 2000 -n 2000 -l smallClassic > console_smallClassic_ApproximateQAgent.txt
    echo "COMPLETED $i RUNS of ApproximateQAgent"
done
for i in $(seq $count); do
    python pacman.py -p EpisodicSemiGradientSarsaAgent -a extractor=SimpleExtractor -x 2000 -n 2000 -l smallClassic > console_smallClassic_EpisodicSemiGradientSarsaAgent.txt
    echo "COMPLETED $i RUNS of EpisodicSemiGradientSarsaAgent"
done
for i in $(seq $count); do
    python pacman.py -p TrueOnlineSarsaAgent -a extractor=SimpleExtractor -x 2000 -n 2000 -l smallClassic > console_smallClassic_TrueOnlineSarsaAgent.txt
    echo "COMPLETED $i RUNS of TrueOnlineSarsaAgent"
done